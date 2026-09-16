"""Compare independently produced counts and the full n=11 membership set."""
from pathlib import Path
import hashlib
import json
import triage_count as first

a = json.loads(Path('evidence/triage_counts.json').read_text())
b = json.loads(Path('evidence/insertion_counts.json').read_text())
for ra, rb in zip(a['rows'], b['rows']):
    for field in ('n', 'a_n', 'avoid312_54321', 'b_n_ending_in_1'):
        assert ra[field] == rb[field], (field, ra, rb)
members_a = sorted(p for p in first.avoid312(11, 4) if first.avoids132(first.square(p)))
members_b = [tuple(p) for p in json.loads(Path('evidence/insertion_members_n11.json').read_text())]
assert members_a == members_b
assert len(members_a) == 1265
failures = [r['n'] for r in a['rows'] if r.get('recurrence_matches') is False]
assert failures[0] == 11
out = {'counts_match_through': 11, 'full_membership_set_matches_at': 11,
       'membership_count': len(members_a), 'first_recurrence_failure': 11,
       'actual_a11': 1265, 'recurrence_rhs': 655 + 338 + 174 + 89 + 10,
       'members_sha256': hashlib.sha256(Path('evidence/insertion_members_n11.json').read_bytes()).hexdigest(),
       'scope': 'Two algorithms in one triage worker; not an independent referee'}
Path('evidence/enumeration_comparison.json').write_text(json.dumps(out, indent=2) + '\n')
print(json.dumps(out))
