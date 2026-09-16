"""Independent inverse-map check. Run: python3 evidence/recovery_check.py."""
from itertools import combinations, permutations
from pathlib import Path
import hashlib
import json

ROOT = Path(__file__).resolve().parents[1]
JOB = "newwin-00001-p07-triage-47782f07ff79"


def has_pattern(p, pattern):
    for values in combinations(p, len(pattern)):
        ranks = {v: i + 1 for i, v in enumerate(sorted(values))}
        if tuple(ranks[v] for v in values) == pattern:
            return True
    return False


def decode(p):
    parts = []
    while p:
        d = p.index(1) + 1
        assert p[:d] == tuple(range(2, d + 1)) + (1,)
        parts.append(d)
        p = tuple(v - d for v in p[d:])
        assert set(p) == set(range(1, len(p) + 1))
    return tuple(parts)


def encode(parts):
    p = []
    offset = 0
    for d in parts:
        p.extend(offset + ((i + 1) % d) + 1 for i in range(d))
        offset += d
    return tuple(p)


def main():
    source_hash = hashlib.sha256((ROOT / "source.md").read_bytes()).hexdigest()
    assert source_hash == "f55a25a1a14dbeef692d590d1d55513ad3e234065d61da1ae130416417c7a59e"
    old = json.loads((ROOT / "evidence/triage_check.json").read_text())
    assert old["source_sha256"] == source_hash
    assert old["script_sha256"] == hashlib.sha256(
        (ROOT / "evidence/triage_check.py").read_bytes()).hexdigest()
    assert sum(r["compositions_checked"] for r in old["rows"]) == 4096
    assert sum(r.get("all_permutations_checked", 0) for r in old["rows"]) == 46234
    rows = []
    for n in range(9):
        tested = base = accepted = 0
        decoded = set()
        for p in permutations(range(1, n + 1)):
            tested += 1
            if has_pattern(p, (3, 1, 2)) or has_pattern(p, (3, 2, 1)):
                continue
            base += 1
            parts = decode(p)
            assert parts not in decoded
            decoded.add(parts)
            assert encode(parts) == p
            # Repeated application, without using a block-power formula.
            q = tuple(range(1, n + 1))
            for _ in range(3):
                q = tuple(p[v - 1] for v in q)
            avoids = not has_pattern(q, (2, 1, 4, 3))
            assert avoids == (sum(d not in (1, 3) for d in parts) <= 1)
            accepted += avoids
        assert len(decoded) == (1 if n == 0 else 2 ** (n - 1))
        assert accepted == old["rows"][n]["cube_avoiders"]
        rows.append({"n": n, "permutations_checked": tested,
                     "inverse_round_trips": base, "cube_avoiders": accepted})
    result = {
        "job_id": JOB,
        "kind": "exact_finite_observation",
        "source_sha256": source_hash,
        "script_sha256": hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
        "prior_artifact_integrity": "hashes and coverage totals match; prior script not rerun",
        "rows": rows,
        "total_permutations_checked": sum(r["permutations_checked"] for r in rows),
        "total_inverse_round_trips": sum(r["inverse_round_trips"] for r in rows),
        "counterexamples_found": 0,
        "limitations": "Finite inverse-map validation only; not an all-n proof, novelty finding, or independent referee."
    }
    out = ROOT / "evidence/recovery_check.json"
    temporary = out.with_suffix(".json.tmp")
    temporary.write_text(json.dumps(result, indent=2) + "\n")
    temporary.replace(out)
    print(json.dumps(result, indent=2))


if __name__ == "__main__":
    main()
