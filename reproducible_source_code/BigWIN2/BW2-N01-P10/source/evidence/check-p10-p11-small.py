"""Exact bounded intake calibration; no all-N injectivity or coverage assertion."""
from collections import Counter
from datetime import datetime, timezone
from hashlib import sha256
from itertools import combinations
from math import prod
from pathlib import Path
import json
import platform
import time


def partitions(n, top=None):
    if n == 0:
        yield ()
        return
    for a in range(min(n, top if top is not None else n), 0, -1):
        for rest in partitions(n-a, a):
            yield (a,) + rest


def elementary_values(p, k):
    return Counter(prod(c) for c in combinations(p, k))


def schur22_monomials(p):
    out = Counter()
    for x, y in combinations(p, 2):
        out[x*x*y*y] += 1
    for x, y, z in combinations(p, 3):
        xyz = x*y*z
        out[xyz*x] += 1
        out[xyz*y] += 1
        out[xyz*z] += 1
    for x, y, z, w in combinations(p, 4):
        out[x*y*z*w] += 2
    return out


def schur22_tableaux(p):
    # Rows weakly increasing; columns strictly increasing by VARIABLE INDEX.
    out, l = Counter(), len(p)
    for a in range(l):
        for b in range(a, l):
            for c in range(a+1, l):
                for d in range(max(c, b+1), l):
                    out[p[a]*p[b]*p[c]*p[d]] += 1
    return out


def schur22_jacobi_trudi(p):
    e2, out = elementary_values(p, 2), Counter()
    for a, na in e2.items():
        for b, nb in e2.items():
            out[a*b] += na*nb
    for a, na in Counter(p).items():
        for b, nb in elementary_values(p, 3).items():
            out[a*b] -= na*nb
    assert all(v >= 0 for v in out.values())
    return +out


def main():
    started = time.monotonic()
    rows, tested, triple_checked = [], 0, 0
    for n in range(2, 25):
        seen, collisions, count = {}, [], 0
        for p in partitions(n):
            if len(p) < 2:
                continue
            count += 1
            tested += 1
            values = schur22_monomials(p)
            assert values == schur22_jacobi_trudi(p), p
            if len(p) <= 6:
                assert values == schur22_tableaux(p), p
                triple_checked += 1
            l = len(p)
            assert sum(values.values()) == l*l*(l*l-1)//12
            key = tuple(sorted(values.items()))
            if key in seen:
                collisions.append([list(seen[key]), list(p)])
            else:
                seen[key] = p
        rows.append(dict(N=n, partitions_checked=count, collisions=collisions))
    a, b = (40,16,16,16,5,5), (32,32,10,10,10,4)
    assert sum(a) == sum(b) == 98
    assert elementary_values(a,3) == elementary_values(b,3)
    assert elementary_values(a+(1,),3) != elementary_values(b+(1,),3)
    out = dict(schema=1, observed_at_utc=datetime.now(timezone.utc).isoformat(),
               python=platform.python_version(), arithmetic="exact integers", seed="none; deterministic exhaustive enumeration",
               p10_domain="Every positive integer partition of each N=2..24 with length >=2; repeated parts retained",
               p10_algorithms=["monomial expansion m22+m211+2*m1111", "dual Jacobi-Trudi e2^2-e1*e3", "independent semistandard tableaux when length<=6"],
               p10_partitions_checked=tested, p10_three_method_checks=triple_checked,
               p10_results=rows,
               p11_known_source_example=dict(source="Thomas-Tung arXiv:2606.19796v1 Example 3.1, not a new discovery", a=a,b=b,N=98,
                                             common_E3=dict(sorted(elementary_values(a,3).items())),
                                             appending_one_preserves_collision=False),
               limitations="Finite observations do not prove p10 for arbitrary N. Known p11 scaling examples do not prove eventual coverage, and padding both partitions by 1 breaks this particular collision.",
               script_sha256=sha256(Path(__file__).read_bytes()).hexdigest(), elapsed_seconds=time.monotonic()-started)
    target = Path(__file__).with_name("p10-p11-intake-check.json")
    target.write_text(json.dumps(out, indent=2)+"\n", encoding="utf-8")
    print(json.dumps({"output":str(target), "tested":tested, "triple_checked":triple_checked,
                      "collisions":[r for r in rows if r["collisions"]],
                      "known_p11_example_reproduced":True, "p11_padding_by_one_fails":True,
                      "elapsed_seconds":out["elapsed_seconds"]}, indent=2))


if __name__ == "__main__":
    main()
