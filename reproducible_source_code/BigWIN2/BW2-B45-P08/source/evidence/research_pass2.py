#!/usr/bin/env python3
"""Exact five-voter 3:2 census for the supplied 254-tournament RDS.

The RDS parser deliberately supports only the simple serialization actually
used here: a version-3 XDR VECSXP of 254 REALSXP 9x9 matrices with a dim
attribute.  It rejects every unexpected byte.  Z3 is used only to find SAT
profiles; each returned profile is recounted by plain Python before output.
"""

import argparse
import base64
import gzip
import hashlib
import itertools
import json
import struct
import time

import z3


N = 9
COUNT = 254
PAIRS = list(itertools.combinations(range(N), 2))


class Reader:
    def __init__(self, data):
        self.data = data
        self.at = 0

    def take(self, n):
        if self.at + n > len(self.data):
            raise ValueError("truncated R serialization")
        ans = self.data[self.at:self.at + n]
        self.at += n
        return ans

    def u32(self):
        return struct.unpack(">I", self.take(4))[0]


def parse_rds(path):
    stored = open(path, "rb").read()
    compressed = base64.b64decode(stored, validate=False) if path.endswith(".base64") else stored
    raw = gzip.decompress(compressed)
    r = Reader(raw)
    if r.take(2) != b"X\n":
        raise ValueError("not an XDR R serialization")
    version, writer_version, min_reader_version = r.u32(), r.u32(), r.u32()
    if version != 3:
        raise ValueError(f"unsupported serialization version {version}")
    enc = r.take(r.u32())
    if r.u32() != 19 or r.u32() != COUNT:  # VECSXP, length 254
        raise ValueError("expected a VECSXP of length 254")

    matrices = []
    for index in range(COUNT):
        if r.u32() != 0x20E or r.u32() != N * N:  # REALSXP + attributes
            raise ValueError(f"matrix {index}: unexpected REALSXP header")
        vals = [struct.unpack(">d", r.take(8))[0] for _ in range(N * N)]

        # Attribute pairlist: dim=c(9L,9L).  The first occurrence serializes
        # the symbol; later occurrences use the R reference table.
        if r.u32() != 0x402:
            raise ValueError(f"matrix {index}: missing tagged attribute")
        if index == 0:
            if (r.u32(), r.u32(), r.u32(), r.take(3)) != (1, 0x40009, 3, b"dim"):
                raise ValueError("unexpected first dim symbol encoding")
        elif r.u32() != 0x1FF:
            raise ValueError(f"matrix {index}: unexpected dim symbol reference")
        if (r.u32(), r.u32(), r.u32(), r.u32(), r.u32()) != (13, 2, N, N, 254):
            raise ValueError(f"matrix {index}: expected dim=c(9L,9L) then NIL")

        # R matrices are serialized column-major.
        matrix = [[vals[row + N * col] for col in range(N)] for row in range(N)]
        matrices.append(matrix)

    if r.at != len(raw):
        raise ValueError(f"unparsed suffix of {len(raw) - r.at} bytes")
    meta = {
        "compressed_bytes": len(compressed),
        "stored_as": "base64 text" if path.endswith(".base64") else "binary RDS",
        "uncompressed_bytes": len(raw),
        "sha256": hashlib.sha256(compressed).hexdigest(),
        "git_blob_sha1": hashlib.sha1(
            b"blob " + str(len(compressed)).encode() + b"\0" + compressed
        ).hexdigest(),
        "serialization_version": version,
        "writer_version_hex": f"0x{writer_version:08x}",
        "minimum_reader_version_hex": f"0x{min_reader_version:08x}",
        "encoding": enc.decode("ascii"),
    }
    return matrices, meta


def validate_and_bits(matrix):
    for row in matrix:
        if len(row) != N or any(x not in (0.0, 1.0) for x in row):
            raise ValueError("adjacency entry is not exactly 0 or 1")
    for i in range(N):
        if matrix[i][i] != 0.0:
            raise ValueError("nonzero diagonal")
        for j in range(i + 1, N):
            if matrix[i][j] + matrix[j][i] != 1.0:
                raise ValueError("not a tournament")
    return tuple(bool(matrix[i][j]) for i, j in PAIRS)


def lex_le(xs, ys):
    """Boolean-vector lexicographic xs <= ys, with False < True."""
    prefix = z3.BoolVal(True)
    clauses = []
    for x, y in zip(xs, ys):
        clauses.append(z3.Implies(prefix, z3.Or(z3.Not(x), y)))
        prefix = z3.And(prefix, x == y)
    return z3.And(clauses)


def solve_five(bits, timeout_ms):
    x = [[z3.Bool(f"x_{p}_{i}_{j}") for i, j in PAIRS] for p in range(5)]
    pidx = {pair: k for k, pair in enumerate(PAIRS)}
    solver = z3.Solver()

    # A tournament is transitive iff it has no directed triangle.
    for p in range(5):
        for a, b, c in itertools.combinations(range(N), 3):
            ab, ac, bc = x[p][pidx[a, b]], x[p][pidx[a, c]], x[p][pidx[b, c]]
            solver.add(z3.Or(z3.Not(ab), z3.Not(bc), ac))
            solver.add(z3.Or(ab, bc, z3.Not(ac)))

    # Voters are interchangeable, so sort their comparison bit vectors.
    for p in range(4):
        solver.add(lex_le(x[p], x[p + 1]))

    for k, bit in enumerate(bits):
        supporters = [x[p][k] if bit else z3.Not(x[p][k]) for p in range(5)]
        solver.add(z3.PbEq([(lit, 1) for lit in supporters], 3))

    solver.set(timeout=timeout_ms, random_seed=0)
    started = time.perf_counter()
    status = solver.check()
    elapsed = time.perf_counter() - started
    if status != z3.sat:
        return str(status), None, elapsed

    model = solver.model()
    orders = []
    for p in range(5):
        wins = [0] * N
        for k, (i, j) in enumerate(PAIRS):
            if z3.is_true(model.eval(x[p][k], model_completion=True)):
                wins[i] += 1
            else:
                wins[j] += 1
        order = sorted(range(N), key=lambda v: -wins[v])
        if sorted(wins) != list(range(N)):
            raise AssertionError("model voter is not a transitive tournament")
        orders.append(order)
    return "sat", orders, elapsed


def recount(bits, orders):
    if len(orders) != 5:
        return False, []
    positions = []
    for order in orders:
        if sorted(order) != list(range(N)):
            return False, []
        positions.append({v: k for k, v in enumerate(order)})
    counts = []
    for bit, (i, j) in zip(bits, PAIRS):
        ij = sum(pos[i] < pos[j] for pos in positions)
        counts.append(ij if bit else 5 - ij)
    return all(c == 3 for c in counts), counts


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("input")
    ap.add_argument("--output", default="evidence/research_pass2_results.json")
    ap.add_argument("--timeout-ms", type=int, default=120000)
    args = ap.parse_args()

    started = time.perf_counter()
    matrices, input_meta = parse_rds(args.input)
    bitsets = [validate_and_bits(m) for m in matrices]
    if len(set(bitsets)) != COUNT:
        raise ValueError("duplicate labelled adjacency matrices")

    records = []
    tallies = {"sat": 0, "unsat": 0, "unknown": 0}
    for index, bits in enumerate(bitsets, 1):
        status, orders, elapsed = solve_five(bits, args.timeout_ms)
        if status == "sat":
            ok, counts = recount(bits, orders)
            if not ok or set(counts) != {3}:
                raise AssertionError(f"independent recount failed at {index}")
            tallies["sat"] += 1
        elif status == "unsat":
            tallies["unsat"] += 1
        else:
            tallies["unknown"] += 1
        bitstring = "".join("1" if b else "0" for b in bits)
        records.append({
            "index": index,
            "upper_triangle_order": [[i, j] for i, j in PAIRS],
            "upper_triangle_bits": bitstring,
            "sha256_bitstring": hashlib.sha256(bitstring.encode()).hexdigest(),
            "solver_status": status,
            "solver_seconds": elapsed,
            "five_orders_zero_based": orders,
        })
        print(index, status, f"{elapsed:.3f}s", flush=True)

    result = {
        "job_id": "win-00045-p08-research-734b9cd9143a",
        "scope": "all 254 matrices serialized in the supplied pinned official RDS",
        "input": input_meta,
        "n": N,
        "matrix_count": len(matrices),
        "distinct_labelled_bitstrings": len(set(bitsets)),
        "matrix_validation": "all exact 0/1; zero diagonal; A[i,j]+A[j,i]=1",
        "encoding": "five strict total orders; exactly three supporters per target arc",
        "solver": f"Z3 {z3.get_version_string()}",
        "per_instance_timeout_ms": args.timeout_ms,
        "tallies": tallies,
        "elapsed_seconds": time.perf_counter() - started,
        "records": records,
        "epistemic_scope": [
            "SAT profiles are exact finite certificates and were recounted without Z3.",
            "A Z3 UNSAT status alone would not be treated as a counterexample.",
            "The RDS parser validates its full byte stream but does not prove the repository's 254-class census.",
        ],
    }
    with open(args.output, "w", encoding="utf-8") as f:
        json.dump(result, f, indent=2)
        f.write("\n")
    print(json.dumps({"tallies": tallies, "elapsed_seconds": result["elapsed_seconds"]}))


if __name__ == "__main__":
    main()
