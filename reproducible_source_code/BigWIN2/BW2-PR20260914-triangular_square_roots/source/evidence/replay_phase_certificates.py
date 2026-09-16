"""Standard-library-only replay of phase_checks.json; no floating arithmetic.

Rebuilds D by its three-term coefficient recurrence and each requested D^2
row by ordinary matrix multiplication, rather than the four-term G recurrence
used to generate the large rows in phase_checks.py. This is a separate code
check in the same research context, not an independent mathematical referee.
"""
from pathlib import Path
from fractions import Fraction
import hashlib
import json

ROOT = Path(__file__).resolve().parents[1]
path = ROOT/"evidence/phase_checks.json"
data = json.loads(path.read_text())
assert hashlib.sha256((ROOT/"source.md").read_bytes()).hexdigest() == data["source_sha256"]
certs = data["exact_sign_certificates"]
N = max(cert["n"] for cert in certs)
D = [[1]]
for n in range(1,N+1):
    get = lambda row,k: row[k] if 0 <= k < len(row) else 0
    D.append([get(D[n-1],k)+get(D[n-1],k-1)
              +(get(D[n-2],k-1) if n>=2 else 0) for k in range(n+1)])

total = 0
for cert in certs:
    n = cert["n"]
    row = [sum(D[n][i]*D[i][k] for i in range(k,n+1)) for k in range(n+1)]
    assert row == cert["coefficients_ascending"]
    assert len(row) == n+1 and row[-1] == 1
    den = int(cert["denominator"])
    assert den > 0
    ps = [int(p) for p in cert["numerators_in_decreasing_order"]]
    assert len(ps) == n+1 and all(ps[j]>ps[j+1] for j in range(n))
    for j,p in enumerate(ps):
        q = Fraction(p,den)
        assert q+4 >= 0 or (q+4)**2 < 18
        assert q+3 <= 0 or (q+3)**2 < 8
        # Evaluate using rational Horner directly. Fraction automatically
        # reduces denominators; this differs from homogeneous integer Horner.
        value = Fraction(0)
        for coefficient in reversed(row):
            value = value*q+coefficient
        sign = (value>0)-(value<0)
        assert sign == cert["exact_signs"][j] == (-1)**j
        total += 1

result = {"job_id":data["job_id"],"certificate_sha256":hashlib.sha256(path.read_bytes()).hexdigest(),
          "degrees":[cert["n"] for cert in certs],"exact_signs_replayed":total,
          "matrix_square_rows_rebuilt":True,"arithmetic":"Python int and Fraction only",
          "scope":"Finite certificate replay in proposer context; not a fresh referee or all-n proof."}
target=ROOT/"evidence/phase_replay.json"
temporary=target.with_suffix(".json.tmp")
temporary.write_text(json.dumps(result,indent=2)+"\n")
temporary.replace(target)
print(json.dumps(result))
