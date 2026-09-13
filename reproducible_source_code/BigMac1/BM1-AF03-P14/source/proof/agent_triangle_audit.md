# Independent exact audit: triangle high-pair chamber

## Audited endpoint

There is no real full-support critical point of the (Q_5) central-section
volume in the ordered closure of the triangle high-pair chamber

\[
a_0\ge a_1\ge a_2\ge a_3\ge a_4>0,
\qquad
E_{\rm high}=\{01,02,12\}.
\]

After dividing by (a_4), the audit uses (a_4=1).  “Closure” means that the
three high-pair inequalities are weakly high, the complementary seven pair
inequalities are weakly low, and the polygon/singleton inequality is weak.  The
exact certificate is
`results/triangle_highpair_no_go_certificate.json`.

This is a chamber no-go, not a classification of (Q_5).  It says nothing by
itself about zero-coordinate strata or sign chambers not incident to this
closure.

## Independent reconstruction

I used `src/root_exact_systems.py` only to identify the intended source recipe,
then reconstructed the equations in a no-import verifier.  No numerical root,
cached basis, discovery JSON, or conclusion file is read by that verifier.

Let

\[
T=\frac{a_0+a_1+a_2+a_3+1}{2},\qquad
S=a_0^2+a_1^2+a_2^2+a_3^2+1.
\]

For the high-pair triangle (H=\{01,02,12\}), define

\[
P=T^4-\sum_{i=0}^4(T-a_i)^4
  +\sum_{0\le i<j\le4}(T-a_i-a_j)^4
  -2\sum_{ij\in H}(T-a_i-a_j)^4,
\]

where (a_4=1).  The sign convention follows from pairing each pair subset
with its complementary triple: the pair contributes (+L^4) on the low side
(L=T-a_i-a_j>0) and (-L^4) on the high side (L<0).

For (i=0,1,2,3), the scale-invariant critical equations are

\[
g_i=a_iS\frac{\partial P}{\partial a_i}+(a_i^2-S)P=0.
\]

The verifier recomputes over (\mathbb Q)

\[
J=\operatorname{Sat}
 \left(\langle g_0,g_1,g_2,g_3\rangle,
 a_0a_1a_2a_3PS\right).
\]

The saturation is legitimate at every physical point covered here:
(a_i>0), (S>0), and (P>0) because the section volume is positive and its
remaining factors are positive.  The saturation deliberately does not cover a
zero-coordinate support boundary.

## Recomputed saturated basis

Singular, degree-reverse-lexicographic order in
((a_0,a_1,a_2,a_3)), independently returns

\[
\dim J=1,\qquad \operatorname{vdim}J=-1,
\qquad |G|=6.
\]

Thus this is a positive-dimensional algebraic system, not a finite-root
enumeration.  The full six-polynomial basis is serialized in the certificate.
The first three elements are

\[
\begin{aligned}
b_0={}&4a_1^2-3a_0a_2-9a_1a_2+6a_2^2+2a_3^2+2,\\
b_1={}&6a_0a_1-9a_0a_2-9a_1a_2+10a_2^2+2a_3^2+2,\\
b_2={}&4a_0^2-9a_0a_2-3a_1a_2+6a_2^2+2a_3^2+2.
\end{aligned}
\]

The last one is

\[
\begin{aligned}
b_5
&=a_2^4-5a_2^2a_3^2+4a_3^4-5a_2^2+8a_3^2+4\\
&=\boxed{(a_2^2-a_3^2-1)(a_2^2-4a_3^2-4)}.
\end{aligned}
\]

The verifier does not merely compare printed text.  It reconstructs and
saturates the original ideal, forms the serialized candidate basis, and checks
mutual ideal containment by exact normal-form reduction.  It then checks the
factorization and every identity below as polynomial identities.

## Exact ordered-cone contradiction

Write

\[
F_1=a_2^2-a_3^2-1,qquad
F_2=a_2^2-4a_3^2-4.
\]

Any point of the saturated variety obeys (F_1F_2=0).  First, subtract the
first basis element from the third:

\[
b_2-b_0
=2(a_0-a_1)(2a_0+2a_1-3a_2).
\]

The second factor is strictly positive in the ordered cone, since

\[
2a_0+2a_1-3a_2
=2(a_0-a_2)+2(a_1-a_2)+a_2>0.
\]

Therefore (a_0=a_1).  Let
(c_i=b_i|_{a_1=a_0}) for (i=0,1).  Direct subtraction gives

\[
c_1-c_0=2(a_0-a_2)(a_0-2a_2).
\]

Hence (a_0=a_2) or (a_0=2a_2).  In either case, substitution into (c_0=0)
gives

\[
F_1=a_2^2-a_3^2-1=0. \tag{1}
\]

This already separates the two factors exactly.

### Branch (F_2=0)

Ordering and the basis force (1).  If (F_2=0) as well, then

\[
F_2-F_1=-3(a_3^2+1)=0,
\]

which has no real solution.  Thus the second algebraic component never enters
the ordered cone.

### Branch (F_1=0)

The closure of the high edge (12) says

\[
a_1+a_2\ge a_0+a_3+1.
\]

Since (a_0=a_1), this becomes (a_2\ge a_3+1).  But (F_1=0) gives

\[
(a_3+1)^2-a_2^2=-F_1+2a_3=2a_3>0,
\]

so (a_2<a_3+1), a contradiction.  Notice that weak high-pair inequality is
enough; no strict chamber margin was used.

Both components are therefore excluded.  In fact, the proof uses only order,
positivity, and the closure inequality for edge (12); the other chamber
inequalities are not needed for the contradiction.

## Wall and closure coverage

The exact conclusion covers more than the open chamber:

- coordinate-equality faces of the ordered chamber are included because all
  order inequalities were used weakly;
- any one or several pair subset-sum walls in the closure are included;
- the singleton/polygon wall (T-a_0=0) is included;
- intersections of these full-support walls are included.

For (Q_5), each truncated-power term is (x_+^4), which is (C^3).  Across a
pair wall the two adjacent polynomial recipes differ by (2L^4); their values
and first derivatives agree at (L=0).  Hence every full-support local extremum
on one of these walls is a critical point of the same differentiable function,
and the reconstructed critical equations from the triangle side remain
necessary.  The same observation applies to the singleton wall.  This justifies
using the closed sign cone rather than only its interior.

Not covered:

- (a_4=0) or any lower-support stratum, because (a_4=1) dehomogenization and
  saturation are invalid there;
- subset-sum walls that are not in the closure of this triangle sign cone;
- interiors of the other five high-pair graph chambers;
- algebraic (P=0) components (which are nonphysical for a full-support central
  section but are intentionally removed by saturation).

Thus the audit is a certified chamber-and-closure no-go, not a proof of the
global (Q_5) conjecture.

## Certificate, verifier, and mutation tests

Files:

- `results/triangle_highpair_no_go_certificate.json`
- `src/verify_triangle_highpair_no_go.py`
- `tests/test_triangle_highpair_verifier.py`

Reproduction:

```bash
python src/verify_triangle_highpair_no_go.py \
  results/triangle_highpair_no_go_certificate.json
python tests/test_triangle_highpair_verifier.py
```

Observed output:

```text
PASS: exact saturated ideal, factorization, and proof identities verified
PASS: valid certificate accepted; 6 corruptions rejected
```

The mutation suite rejects a missing high edge, a changed basis coefficient, a
dropped saturation factor, a strict/closed-endpoint substitution, a truncated
proof identity set, and an expression-injection attempt.  The verifier rejects
unknown/missing fields, missing Singular, CAS errors, timeouts, failed normal
forms, and absent/duplicate success sentinels.

SHA-256 at this audit milestone:

```text
5e0bab27d028cdfc65027c3c346d3f0397dd13a623b1bf7782616823019278a1  results/triangle_highpair_no_go_certificate.json
e559f4be5737fb743c75028a729fe5a883e1039049b64b2d45eea3c1e4387077  src/verify_triangle_highpair_no_go.py
5360d2db876a62362a020019405edfe5c22bb0466457a5ad23d0361ff9e74b97  tests/test_triangle_highpair_verifier.py
```

No Lean, Coq, Isabelle, or other proof assistant was used.  Exact polynomial
reconstruction, saturation, Gröbner reduction, and identity checking were done
with Singular; the semialgebraic contradiction above is human-readable and
uses only the serialized exact identities and order inequalities.

