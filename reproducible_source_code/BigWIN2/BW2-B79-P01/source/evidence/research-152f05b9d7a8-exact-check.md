# Exact Gram and relation check

Research job: `win-00079-p01-research-152f05b9d7a8`.

The following SymPy calculation was run with exact rationals after the proof
statement was fixed.  It checks the full forced Gram matrix and verifies that
the three pair-sum relations span its kernel.

```python
import sympy as s

G = s.zeros(8)
for a in range(8):
    G[a, a] = 1
for i in range(4):
    G[2*i, 2*i+1] = G[2*i+1, 2*i] = s.Rational(-5, 3)
for i in range(4):
    for j in range(i+1, 4):
        for a in (2*i, 2*i+1):
            for b in (2*j, 2*j+1):
                G[a, b] = G[b, a] = s.Rational(-1, 3)

relations = []
for i in range(1, 4):
    v = s.zeros(8, 1)
    v[2*i] = v[2*i+1] = 1
    v[0] = v[1] = -1
    relations.append(v)

assert G.rank() == 5
assert G.eigenvals() == {
    s.Rational(8, 3): 4,
    s.Rational(-8, 3): 1,
    s.Integer(0): 3,
}
assert all(G*v == s.zeros(8, 1) for v in relations)
assert s.Matrix.hstack(*relations).rank() == 3
```

Output:

```
rank 5
spectrum [('-8/3', 1), ('0', 3), ('8/3', 4)]
three_sum_relations_span_kernel True
exact_check PASS
```

This deterministic check corroborates the matrix arithmetic only.  The null
vertex-ray argument, time orientation, and oriented-halfspace conclusion are
proved separately in `evidence/research-152f05b9d7a8-proof.md`.
