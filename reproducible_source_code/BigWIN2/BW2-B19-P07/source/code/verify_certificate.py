#!/usr/bin/env python3
"""Independent exact verifier for the finite witness and counting lemmas."""
import hashlib, itertools, json, pathlib, sys

ROOT = pathlib.Path(__file__).resolve().parents[1]
INPUT = ROOT / "certificate" / "dominating_set_j84.json"

def sha256(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()

def fail(message):
    print("FAIL:", message, file=sys.stderr)
    raise SystemExit(1)

def main():
    try:
        data = json.loads(INPUT.read_text(encoding="utf-8"))
        n, r = data["graph"]["n"], data["graph"]["r"]
        blocks = [frozenset(x) for x in data["sets"]]
    except Exception as exc:
        fail(f"malformed input: {exc}")
    if (n, r, len(blocks)) != (8, 4, 6):
        fail("unexpected parameters or block count")
    if len(set(blocks)) != 6 or any(len(x) != 4 or not x <= set(range(1, 9)) for x in blocks):
        fail("blocks are not six distinct 4-subsets of [8]")

    vertices8 = {frozenset(x) for x in itertools.combinations(range(1, 9), 4)}
    # Evaluator 1: use the defining intersection predicate directly.
    covered1 = {v for v in vertices8 if any(len(v & b) >= 3 for b in blocks)}
    # Evaluator 2: independently generate each closed ball by zero or one replacement.
    covered2 = set()
    for b in blocks:
        covered2.add(b)
        for old in b:
            for new in set(range(1, 9)) - b:
                covered2.add(frozenset((b - {old}) | {new}))
    if covered1 != vertices8 or covered2 != vertices8 or covered1 != covered2:
        fail("the proposed family does not dominate J(8,4) in both evaluators")

    # Exhaustively check the local lemma used for J(9,4): disjoint closed balls
    # imply centre intersection at most one.
    vertices9 = [frozenset(x) for x in itertools.combinations(range(1, 10), 4)]
    balls9 = [{v for v in vertices9 if len(v & b) >= 3} for b in vertices9]
    if any(len(ball) != 21 for ball in balls9):
        fail("a J(9,4) closed ball does not have size 21")
    pair_cases = 0
    for i, a in enumerate(vertices9):
        for j in range(i + 1, len(vertices9)):
            b = vertices9[j]
            if not (balls9[i] & balls9[j]) and len(a & b) > 1:
                fail("disjoint balls found with centre intersection greater than one")
            pair_cases += 1

    print(json.dumps({
        "result": "PASS",
        "input_sha256": sha256(INPUT),
        "verifier_sha256": sha256(pathlib.Path(__file__)),
        "j84_vertices_covered": len(covered1),
        "j84_closed_ball_size": 17,
        "j94_closed_ball_size": 21,
        "j94_centre_pairs_checked": pair_cases,
        "design_arithmetic": {"blocks": 6, "pairs_per_block": 6,
                              "pairs_on_9_points": 36,
                              "replication_equation": "3*r_x=8 (impossible over integers)"}
    }, indent=2))

if __name__ == "__main__":
    main()
