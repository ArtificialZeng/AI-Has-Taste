# Exact exclusion of the ordered `star2` chamber

## Statement covered

Let (a_0\ge a_1\ge a_2\ge a_3\ge a_4>0), and let
(T=(a_0+\cdots+a_4)/2).  This report treats the closure of the sign chamber

\[
a_0+a_1\ge T,\qquad a_0+a_2\ge T,
\]

with every other pair sum at most (T).  Thus its high-pair graph is the
two-edge star \(\{01,02\}\).  The result is

\[
\boxed{\text{this ordered full-support chamber closure contains no critical direction.}}
\]

Pair-sum walls and coordinate-equality walls are included.  Zero-coordinate
strata are not included here and are handled by support reduction.

## Exact chamber coordinates

Use homogeneity to put (a_4=1), and write the ordered gaps as

\[
\begin{aligned}
a_3&=1+w,& a_2&=1+w+z,\\
a_1&=1+w+z+y,&a_0&=1+w+z+y+x,
\end{aligned}
\qquad x,y,z,w\ge0.
\]

The only nonredundant pair-sign inequalities are

\[
x+z-1\ge0,\qquad 1+z-x\ge0,\qquad 1+x-z\ge0.
\]

Indeed these are respectively the margins for high pair (02), low pair
(03), and low pair (12); ordering supplies all remaining signs.  The exact
substitution

\[
x=u+v,\qquad z=u+1-v
\]

therefore identifies the whole closure with

\[
u,y,w\ge0,\qquad 0\le v\le1.
\]

The three margins become (2u,2(1-v),2v).

## Critical numerators

For this chamber reconstruct the paired truncated-power polynomial

\[
P=T^4-\sum_i(T-a_i)^4+\sum_{i<j}(T-a_i-a_j)^4
  -2\!\sum_{ij\in\{01,02\}}(T-a_i-a_j)^4.
\]

On the chart (a_4=1), apart from the positive constant (1/24), the volume is

\[
F=\frac{\sqrt S\,P}{D},\qquad
S=\sum_i a_i^2,\quad D=a_0a_1a_2a_3.
\]

For each gap coordinate (q\in\{x,y,z,w\}), define the integer-polynomial
critical numerator

\[
H_q=S_qPD+2SP_qD-2SPD_q=2SPD\,\partial_q\log F.
\]

Full support gives (S,D>0), and the section-density interpretation gives
(P>0).  The certificate also proves (P>0) directly by the same Bernstein
method below.  Consequently every critical point must satisfy all four
(H_q=0).

## Strict Bernstein certificate

Set

\[
H=-2H_x+2H_y-2H_z+H_w
\]

and substitute (x=u+v, z=u+1-v).  Exact conversion from the power basis to
the degree-eight Bernstein basis gives

\[
H(u,v,y,w)=\sum_{k=0}^{8} B_k(u,y,w)
  {8\choose k}v^k(1-v)^{8-k}.
\]

The serialized sparse table contains all nine (B_k).  Each (B_k) has 125
monomials in (u,y,w), and **every one of the 1125 rational coefficients is
strictly positive** (the minimum is (32)); each constant coefficient is also
strictly positive.  Hence (B_k>0) for (u,y,w\ge0), and the nonnegative
Bernstein basis sums to one on (0\le v\le1).  Therefore

\[
H>0
\]

on the entire chamber closure.  This contradicts (H_x=H_y=H_z=H_w=0).

For completeness, the same certificate expands (P) in the degree-four
Bernstein basis.  Its five coefficient polynomials each have 14 monomials and
all 70 coefficients are strictly positive (minimum (16)), independently
certifying (P>0) on the closure.

## Certificate and independent verification

- Serialized coefficient certificate:
  `results/star2_bernstein_no_go_certificate.json`
- Certificate constructor: `src/build_star2_bernstein_certificate.py`
- Fail-closed verifier: `src/verify_star2_bernstein.py`
- Mutation tests: `tests/test_star2_bernstein_verifier.py`

The verifier imports no discovery or project formula module.  It reads the
high-pair graph and chart from the JSON, independently reconstructs the
box-spline polynomial, (S,D,H_q), both Bernstein identities, all rational
coefficient tables, and their canonical SHA-256 digest.  It rejects an altered
graph, claim, critical-numerator definition, derivative combination, domain,
degree, coefficient, or chamber-margin identity.

Reproduction:

```bash
python src/build_star2_bernstein_certificate.py \
  --output results/star2_bernstein_no_go_certificate.json
python src/verify_star2_bernstein.py \
  results/star2_bernstein_no_go_certificate.json
python tests/test_star2_bernstein_verifier.py
```

Observed result:

```text
PASS: star2 Bernstein positivity certificate verified
PASS: valid certificate accepted; 8 corruptions rejected
```

SHA-256 of the serialized certificate:
`fd591e360a57668ad818ba8adb8e48d5670a211da3f43528c7f3f68517310a80`.

No Lean, Coq, Isabelle, or other proof assistant was used.  Exact polynomial
arithmetic was performed by SymPy over the rationals.
