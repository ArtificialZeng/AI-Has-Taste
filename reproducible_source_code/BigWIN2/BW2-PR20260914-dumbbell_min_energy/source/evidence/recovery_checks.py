"""Replay preserved mathematical assertions without overwriting prior evidence.

Run from PROJECT_DIR: python3 evidence/recovery_checks.py
The prior verifier's registry scan is intentionally excluded in this recovery.
"""
from pathlib import Path
import hashlib
import json

job = 'primary-20260914-dumbbell-min-energy-triage-cf68286d5ba6'
prior = Path('evidence/triage_checks.py').read_text()
prefix, separator, _ = prior.partition("\nregistry=Path(")
assert separator, 'Expected boundary after all mathematical checks'
prefix = prefix.replace('primary-20260914-dumbbell-min-energy-triage-f6149d7dafbe', job)
prefix = prefix.replace("Path('evidence/triage-checks.json')", "Path('evidence/recovery-checks.json')")
namespace = {'__name__': '__main__'}
exec(compile(prefix, 'evidence/triage_checks.py[mathematical replay]', 'exec'), namespace)

# Supplement the preserved algebra with the exact kernel comparison used in
# the written global-minimum argument. These identities do not replace its
# real-root sign counts and monotonicity proof.
S = namespace['S']
a, b, t = (namespace[k] for k in ('a', 'b', 't'))
Z, X, W = (namespace[k] for k in ('Z', 'X', 'W'))
K = (Z-a*b*W)**2 + X**2*(a+b)**2
same_product_diagonal = (Z-a*b*W)**2 + 4*a*b*X**2
assert S.expand(K-same_product_diagonal-X**2*(a-b)**2) == 0
assert S.expand(Z*W-X**2-4*t**8*(1+t**2)**2) == 0
assert S.expand(K-Z**2-(X**2*(a*a+b*b)-2*a*b*(Z*W-X**2)+a*a*b*b*W**2)) == 0
p, x = namespace['p'], namespace['x']
c = S.symbols('c', real=True)
diagonal = p.subs({a:c, b:c})
zero_root_slope = -S.diff(diagonal,c).subs({x:0,c:S.Rational(1,2)}) / S.diff(diagonal,x).subs({x:0,c:S.Rational(1,2)})
assert zero_root_slope == -S.Rational(2,3)

outpath = Path('evidence/recovery-checks.json')
out = json.loads(outpath.read_text())
out.update({
    'replayed_verifier_sha256': hashlib.sha256(Path('evidence/triage_checks.py').read_bytes()).hexdigest(),
    'replay_scope': 'All preserved mathematical assertions; no registry rescan; only output path and job provenance changed.',
    'supplemental_kernel_identities_passed': True,
    'simple_zero_root_diagonal_slope': str(zero_root_slope),
    'independent_referee': False,
})
outpath.write_text(json.dumps(out, indent=2)+'\n')
print('Recovery supplemental identities passed; prior artifacts preserved.')
