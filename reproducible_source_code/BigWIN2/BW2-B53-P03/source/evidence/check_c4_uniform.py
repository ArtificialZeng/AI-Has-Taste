#!/usr/bin/env python3
"""Exact instance checker for every step in c4_uniform_proof.md.

The universal force comes from the algebra in the Markdown proof.  This script
guards against sign, residue, AP, boundary, and mirror mistakes by instantiating
both schemas.  A flood step is accepted only when its recorded seed and target
are in the same g-class and both reflections stay inside the block.
"""

from __future__ import annotations

import argparse
import hashlib
import json


def check_M(M: int):
    assert M >= 20 and M % 8 == 4
    lo, hi = M + 1, 2 * M
    b = lambda j: M + j
    t = lambda i: 2 * M - i
    m = 3 * M // 2
    known = set()
    trace = []

    def inside(*xs):
        assert all(lo <= x <= hi for x in xs), (M, xs)

    def put(u, v, why):
        inside(u, v)
        assert u != v and (v, u) not in known, (M, u, v, why)
        known.add((u, v))
        trace.append((u, v, why))

    def trans(u, v, w, why, conflict=False):
        assert (u, v) in known and (v, w) in known
        if conflict:
            assert (w, u) in known
            trace.append((u, w, why + " [contradiction]"))
        else:
            put(u, w, why)

    def ap_rule(source, target, triple, why):
        a, mid, c = triple
        inside(a, mid, c)
        assert a < mid < c and a + c == 2 * mid
        permitted = {
            (a, mid): (c, mid), (c, mid): (a, mid),
            (mid, c): (mid, a), (mid, a): (mid, c),
        }
        assert source in known and permitted[source] == target
        put(*target, why)

    def flood(seed, target, center, g, why, conflict=False):
        assert g % 2 == 0 and seed in known
        su, sv = seed
        tu, tv = target
        if su == center:
            assert tu == center
            member, wanted = sv, tv
        else:
            assert sv == center and tv == center
            member, wanted = su, tu
        inside(center, member, wanted, 2 * center - member,
               2 * center - wanted)
        assert member % g == wanted % g
        assert center % g == (member + g // 2) % g
        if conflict:
            assert (target[1], target[0]) in known
            trace.append((target[0], target[1], why + " [contradiction]"))
        else:
            put(*target, why)

    # Lemma 1, contradiction branch S: b3 < b5.  The odd leaders are 3 mod 4.
    def lemma1_case(case):
        known.clear(); trace.clear()
        cs, css = m - 1, m + 1
        assert m % 4 == 2 and cs % 4 == 1 and css % 4 == 3
        assert 2 * m - t(5) == b(5)
        assert 2 * cs - b(3) == t(5)
        assert 2 * cs - t(10) == b(8)
        assert 2 * css - t(11) == b(13)
        assert 2 * css - b(2) == t(0)
        put(b(3), b(5), "S")
        put(t(11), b(2), "Q")
        put(t(10), b(3), "A3")
        # Needed adjacent leader edges, consequences of zigzag from S.
        for x in (cs - 2, cs + 2): put(x, cs, "zigzag-S")
        for x in (css - 2, css + 2): put(css, x, "zigzag-S")
        if case == 1:
            put(t(5), m, "case-I")
            flood((t(5), m), (cs, m), m, 2, "polar-in")
            flood((cs - 2, cs), (b(3), cs), cs, 4, "G4-in")
            flood((cs, m), (cs, t(10)), cs, 2, "P2-out")
            assert (b(3), cs) in known and (cs, t(10)) in known
            assert (t(10), b(3)) in known
        else:
            put(m, t(5), "case-II")
            flood((m, t(5)), (m, css), m, 2, "polar-out")
            flood((css, css + 2), (css, t(11)), css, 4, "G4-out")
            flood((m, css), (b(2), css), css, 2, "P2-in")
            assert (css, t(11)) in known and (t(11), b(2)) in known
            assert (b(2), css) in known

    lemma1_case(1)
    lemma1_case(2)

    # Lemma 2.  Reset to its hypotheses and add adjacent odd-leader seeds as
    # needed.  All centers used below are in the leader class 1 mod 4.
    known.clear(); trace.clear()
    put(b(5), b(3), "L")
    put(t(13), b(1), "P")
    put(t(5), b(5), "A1")

    def leader_center_to(center, target, why):
        # target and its reflection are in the trailer class; center's local
        # relation to either neighbor is supplied by the zigzag phase L.
        assert center % 4 == 1 and target % 4 == 3
        neighbor = center + 2
        if neighbor > hi:
            neighbor = center - 2
        put(center, neighbor, "zigzag-L")
        flood((center, neighbor), (center, target), center, 4, why)

    if M % 16 == 4:
        c, d = m - 5, m - 1
        assert m % 8 == 6 and c % 8 == 1 and d % 8 == 5
        assert 2 * c - t(13) == b(3)
        assert 2 * c - b(1) == t(11)
        assert 2 * c - d == m - 9
        assert 2 * d - t(5) == b(3)
        assert 2 * d - b(5) == t(7)
        assert 2 * d - c == m + 3
        leader_center_to(c, t(13), "c<t13, mirror b3")
        trans(c, t(13), b(1), "P-chain")
        flood((c, b(1)), (c, d), c, 8, "8-flood c<d")
        leader_center_to(d, t(5), "d<t5, mirror b3")
        if M == 20:  # here b5=c, so the A1 chain itself closes the cycle
            assert b(5) == c
            trans(d, t(5), b(5), "A1-chain", conflict=True)
        else:
            trans(d, t(5), b(5), "A1-chain")
            flood((d, b(5)), (d, c), d, 8, "8-flood d<c", conflict=True)
        assert (c, d) in known
    else:
        assert M % 16 == 12
        c, d = m - 1, m - 5
        assert m % 8 == 2 and c % 8 == 1 and d % 8 == 5
        assert 2 * c - t(13) == b(11)
        assert 2 * c - b(1) == t(3)
        assert 2 * c - d == m + 3
        assert 2 * d - t(13) == b(3)
        assert b(1) + t(11) == 2 * d
        assert 2 * t(11) - t(5) == t(17)
        assert 2 * d - b(5) == t(15)
        assert 2 * d - c == m - 9
        leader_center_to(c, t(13), "c<t13, mirror b11")
        trans(c, t(13), b(1), "P-chain-c")
        flood((c, b(1)), (c, d), c, 8, "8-flood c<d")
        leader_center_to(d, t(13), "d<t13, mirror b3")
        trans(d, t(13), b(1), "P-chain-d")
        ap_rule((d, b(1)), (d, t(11)), (b(1), d, t(11)),
                "AP b1,d,t11")
        leader_center_to(t(11), t(5), "t11<t5, mirror t17")
        trans(d, t(11), t(5), "to-t5")
        trans(d, t(5), b(5), "A1-chain")
        flood((d, b(5)), (d, c), d, 8, "8-flood d<c", conflict=True)
        assert (c, d) in known

    return {"M": M, "subclass": M % 16, "lemma1_cases": 2,
            "lemma2_trace_steps": len(trace)}


def main():
    p = argparse.ArgumentParser()
    p.add_argument("--max-M", type=int, default=4092)
    args = p.parse_args()
    records = [check_M(M) for M in range(20, args.max_M + 1, 8)]
    payload = json.dumps(records, sort_keys=True, separators=(",", ":"))
    print(json.dumps({"status": "PASS", "checked": len(records),
                      "first_M": records[0]["M"], "last_M": records[-1]["M"],
                      "subclasses": sorted(set(x["subclass"] for x in records)),
                      "records_sha256": hashlib.sha256(payload.encode()).hexdigest()},
                     sort_keys=True))


if __name__ == "__main__":
    main()
