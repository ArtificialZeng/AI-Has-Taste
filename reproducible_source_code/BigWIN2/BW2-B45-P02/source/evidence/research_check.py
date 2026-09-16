#!/usr/bin/env python3
"""Exact algebra checks for research_pass1.md; requires SymPy."""
import sympy as sp

a, r, x = sp.symbols("a r x", positive=True)

# Verify the coefficientwise form of the operator identity through a symbolic
# arbitrary-degree coefficient b_k.
k = sp.symbols("k", integer=True, nonnegative=True)
bk = sp.symbols("b_k")
lhs_term = bk * ((a + k) / a * x ** (k + 1) + k / a * x**k)
rhs_term = bk * (x * x**k + x * (x + 1) / a * sp.diff(x**k, x))
assert sp.factor(lhs_term - rhs_term) == 0

# In the frozen quadratic case, verify agreement with every displayed cubic
# coefficient in source.md after using u=s+t and v=st.
s, t = sp.symbols("s t")
f = (x + s) * (x + t)
R = sp.expand((x + r) * f + x * (x + 1) / a * sp.diff(f, x))
expected = (
    r * s * t
    + (r * (s + t) + s * t + (s + t) / a) * x
    + (r + ((a + 1) * (s + t) + 2) / a) * x**2
    + (a + 2) / a * x**3
)
assert sp.factor(R - expected) == 0

# Verify the partial-fraction identity (2) for a symbolic list of roots for
# several degrees; it is termwise, while the loop catches transcription errors.
for n in range(1, 8):
    ss = sp.symbols(f"s0:{n}")
    direct = x + r + x * (x + 1) / a * sum(1 / (x + z) for z in ss)
    partial = (
        (1 + sp.Rational(n, 1) / a) * x
        + r
        + (n - sum(ss)) / a
        - sum(z * (1 - z) / (a * (x + z)) for z in ss)
    )
    assert sp.factor(direct - partial) == 0

print("operator identity, frozen cubic, and partial fractions verified exactly")
