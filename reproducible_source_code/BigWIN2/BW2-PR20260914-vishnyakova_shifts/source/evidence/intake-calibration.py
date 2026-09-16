"""Bounded exact intake calibration; no conjecture or novelty certification."""
import json
import platform
import time
from datetime import datetime
import sympy as s

started = time.monotonic()
z, t, a = s.symbols('z t a')

def transform(n, shift, parameter=s.S.One):
    return s.Poly(s.expand(sum(
        s.rf(parameter, k) / s.factorial(k) * z**k * sum(
            (-1)**j * s.binomial(k, j) * (k-j+shift)**n
            for j in range(k+1)) for k in range(n+1))), z)

def interval_roots(p):
    # Square-free Sturm counts with multiplicities reinstated, endpoints included.
    return sum(int(m) * int(f.count_roots(-1, 0)) for f, m in p.sqf_list()[1])

q2 = transform(2, t)
assert s.expand(q2.as_expr() - (t*t+(2*t+1)*z+2*z*z)) == 0
disc2 = s.factor(s.discriminant(q2.as_expr(), z))
assert disc2 == -4*t*t+4*t+1
boundary = (1-s.sqrt(2))/2
assert s.simplify(disc2.subs(t, boundary)) == 0
assert s.simplify(disc2.subs(t, 1-boundary)) == 0

rows = []
failures = []
for n in range(1, 7):
    accepted = []
    for numerator in range(-20, 41):
        shift = s.Rational(numerator, 20)
        p = transform(n, shift)
        count = interval_roots(p)
        ok = count == n
        if ok:
            accepted.append(str(shift))
        if n % 2 and ok != (0 <= shift <= 1):
            failures.append({'n': n, 't': str(shift), 'test': 'known odd interval'})
        if n == 2 and ok != (disc2.subs(t, shift) >= 0):
            failures.append({'n': n, 't': str(shift), 'test': 'known degree two'})
        mirror = transform(n, 1-shift)
        if s.expand(mirror.as_expr() - (-1)**n * p.as_expr().subs(z, -1-z)) != 0:
            failures.append({'n': n, 't': str(shift), 'test': 'reflection'})
    rows.append({'n': n, 'accepted_grid_points': accepted})

# Auxiliary warning about the DIFFERENT all-a conjecture, not the a=1 target.
aux = transform(2, s.Rational(-3,100), s.Rational(1,100))
aux_scaled = s.Poly(aux.as_expr()*10000, z)
assert aux_scaled.as_expr() == 101*z*z+94*z+9
assert interval_roots(aux_scaled) == 2
assert s.Rational(-3,100) < -2*s.Rational(1,100)
assert not failures, failures
print(json.dumps({
    'observed_at': datetime.now().astimezone().isoformat(),
    'python': platform.python_version(), 'sympy': s.__version__,
    'arithmetic': 'exact rationals, symbolic identities, square-free Sturm counts',
    'randomness': False, 'seed': None,
    'range': {'n': [1,6], 't': 'j/20, -20<=j<=40'},
    'grid_tests': 366, 'symmetry_identity_tests': 366,
    'degree_two_polynomial': str(q2.as_expr()), 'degree_two_discriminant': str(disc2),
    'degree_two_boundary': '(1-sqrt(2))/2 and (1+sqrt(2))/2; known calibration',
    'rows': rows, 'failures': failures,
    'auxiliary_generalized_bound': {
        'target': '2608.03723v1 Conjecture6.5 bound c2(a)<2a, not selected Conjecture5.8',
        'a': '1/100', 't': '-3/100', 'scaled_transform': str(aux_scaled.as_expr()),
        'discriminant': int(s.discriminant(aux_scaled.as_expr(),z)),
        'roots_in_closed_interval_minus_one_zero': interval_roots(aux_scaled),
        'scope': 'Elementary auxiliary counterexample; no novelty/review/publication claim.'
    },
    'wall_seconds': time.monotonic()-started,
    'uniform_even_conjecture_proved': False,
    'interpretation': 'Finite selection/calibration data, not independent holdout or uniform proof.'
}, ensure_ascii=False, indent=2))
