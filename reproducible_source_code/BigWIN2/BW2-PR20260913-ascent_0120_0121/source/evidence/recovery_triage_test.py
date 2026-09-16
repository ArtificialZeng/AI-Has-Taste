"""Bounded recovery triage: reproduce saved tests and extend the quotient check.

Run from the project root with python3 evidence/recovery_triage_test.py.
Only the new recovery JSON is written; prior evidence and source stay untouched.
"""
from collections import Counter
from contextlib import redirect_stdout
from pathlib import Path
from unittest.mock import patch
import hashlib
import io
import json
import runpy

JOB = "primary-20260913-ascent-0120-0121-triage-8e85505dad88"
MAX_PREFIX = 11
protected = ["source.md", "evidence/triage_test.py",
             "evidence/triage-test-results.json", "evidence/canonical_state_test.py",
             "evidence/canonical-state-results.json"]
before = {p: hashlib.sha256(Path(p).read_bytes()).hexdigest() for p in protected}
reproduction = []
canonical = None
for script, result in [(protected[1], protected[2]), (protected[3], protected[4])]:
    captured = {}
    def capture(path, data, *args, **kwargs):
        captured[str(path)] = data
        return len(data)
    with patch.object(Path, "write_text", capture), redirect_stdout(io.StringIO()):
        namespace = runpy.run_path(script)
    assert captured[result].encode() == Path(result).read_bytes()
    reproduction.append({"script": script, "result": result, "byte_identical": True})
    if "canonical" in script:
        canonical = namespace

# Exact reference remembers endpoints of all increasing subsequences of length 2.
# Its banned set is built from these pairs, without the simplified forbidden-set
# formula or any canonical-state assumption.
def exact_children(s):
    a, last, seen, pairs, banned = s
    for t in range(a + 2):
        if t in banned:
            continue
        newly_banned = {v for pair in pairs if pair[1] < t for v in pair}
        next_pairs = pairs | frozenset((u, t) for u in seen if u < t)
        yield t, (a + int(last < t), t, seen | {t}, next_pairs,
                  banned | newly_banned)

def project(s):
    a, last, seen, pairs, banned = s
    if max(seen) < 2:
        return ("binary", a, last)
    eligible = [t for t in range(a + 2) if t not in banned]
    h = tuple(i for i, t in enumerate(eligible) if t in seen)
    assert h and eligible[min(h)] == last, s
    return ("postbinary", len(eligible), h)

def proposed_children(p):
    if p[0] == "postbinary":
        return [("postbinary", k, h) for k, h in canonical["children"](p[1:])]
    _, a, last = p
    return [("binary", a + int(last < t), t) for t in (0, 1)] + [
        ("postbinary", a + 1, (t - 2,)) for t in range(2, a + 2)]

root = (0, 0, frozenset({0}), frozenset(), frozenset())
states = {root: (1, (0,))}
counts = [1, 1]
coverage = []
for n in range(1, MAX_PREFIX + 1):
    next_states = {}
    post_checks = binary_checks = boundary_edges = exact_edges = 0
    for s, (multiplicity, witness) in states.items():
        p = project(s)
        children = list(exact_children(s))
        actual = Counter(project(cs) for _, cs in children)
        proposed = Counter(proposed_children(p))
        assert actual == proposed, (n, witness, s, p, actual, proposed)
        if p[0] == "postbinary":
            post_checks += 1
            assert all(cp[1] <= p[1] for cp in actual)
        else:
            binary_checks += 1
            boundary_edges += sum(t >= 2 for t, _ in children)
        exact_edges += len(children)
        for t, cs in children:
            old_count, old_witness = next_states.get(cs, (0, witness + (t,)))
            next_states[cs] = (old_count + multiplicity, old_witness)
    coverage.append({"prefix_length": n, "exact_states": len(states),
                     "represented_prefix_words": sum(m for m, _ in states.values()),
                     "postbinary_successor_multiset_checks": post_checks,
                     "binary_successor_multiset_checks": binary_checks,
                     "binary_to_postbinary_edges": boundary_edges,
                     "exact_state_edges": exact_edges})
    states = next_states
    counts.append(sum(m for m, _ in states.values()))
assert counts == canonical["counts"][:MAX_PREFIX + 2]
after = {p: hashlib.sha256(Path(p).read_bytes()).hexdigest() for p in protected}
assert before == after
out = {"job_id": JOB, "max_prefix_length": MAX_PREFIX,
       "reference_counts_n0_to_n12": counts, "coverage": coverage,
       "all_projected_successor_multisets_match": True,
       "all_checked_postbinary_widths_nonincreasing": True,
       "reference_counts_match_saved_canonical_counts_through_n12": True,
       "saved_test_reproduction": reproduction, "protected_sha256": before,
       "protected_files_unchanged": before == after,
       "qualification": "Exact finite verification only. Every reachable exact state through prefix length 11 is checked, including binary transitions. Totals through length 12 come from the exact pair/banned recurrence. This is not a uniform quotient proof or a novelty certificate."}
Path("evidence/recovery-triage-results.json").write_text(json.dumps(out, indent=2) + "\n")
print(json.dumps(out, indent=2))
