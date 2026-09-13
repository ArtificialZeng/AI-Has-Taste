# Gate 5 independent referee report

Date: 2026-08-29 (Asia/Shanghai)  
Role: referee, reconstructing from definitions without trusting the builder or
counterexample search.  No proof assistant was used.

## Verdict

I independently verify a complete theorem for **real (3\times3) matrices of
rank at most two**.  If

\[
H_3(T):=20\operatorname{per}(T)^2-
\operatorname{per}\!\begin{pmatrix}T&T\\T&T\end{pmatrix},
\]

then (H_3(T)\geq0).  The proof below covers zero rows/columns,
(\operatorname{per}(T)=0), rank one, repeated projective factors, and affine
chart boundaries.  An independent exact verifier passes.

I do **not** certify the (n=4) endpoint.  The binary-quartic reduction is
valid, but a proof must still control the real-split quartic cone, its
cross-ratio parameter, and all repeated/infinite-root strata.  Numerical
search cannot close this major gap.

## 1. Source/domain audit

1. The exact displayed statement is Conjecture 10 of Adam W. Marcus,
   *A Determinantal Identity for the Permanent of a Rank 2 Matrix*,
   arXiv:2108.02528v2, page 9 (PDF text lines 667--683).  It is exactly
   \[
   \operatorname{per}\!\begin{pmatrix}T&T\\T&T\end{pmatrix}
   \leq {2n\choose n}\operatorname{per}(T)^2,
   \qquad \operatorname{rank}T\leq2.
   \]
2. The arXiv v2 article works in a real-matrix setting: the setup uses
   (M\in\mathbb R^{n\times n}), and Theorem 9 explicitly has
   (X\in\mathbb R^{n\times n}).  Conjecture 10 says "any matrix" without
   restating the field, but its order relation and surrounding convention make
   the real interpretation the defensible one.  The user's phrase "complex
   case" is **not present in the source**; the displayed (\leq) is undefined
   for a general complex permanent.  A complex absolute-value variant would be
   a different conjecture and must not be silently substituted.
3. An older author-hosted 2016 draft states the determinantal identity over a
   field (\mathbb F), but it does not contain Conjecture 10.  It therefore
   does not support extending this ordered inequality to complex matrices.
4. The paper says only that a proof is known when every entry of (T) is
   positive.  No supporting citation is attached to that sentence, so this is
   an **author report**, not a source-verified borrowed theorem for the present
   proof.
5. Publisher metadata confirms publication in *The American Mathematical
   Monthly* 129(10), 962--971 (2022), DOI
   [10.1080/00029890.2022.2115803](https://doi.org/10.1080/00029890.2022.2115803).
   The primary preprint used for the formula is
   [arXiv:2108.02528v2](https://arxiv.org/pdf/2108.02528).

## 2. Reconstruction from the permanent definition

Write (T=FG^{\mathsf T}), with row factors
(f_i=(x_i,u_i)) and column factors (g_j=(y_j,v_j)).  This covers every
real matrix of rank at most two, including rank one (one factor column may be
zero).  Define binary-form coefficient sequences

\[
A(z)=\prod_{i=1}^n(x_i+u_i z)=\sum_{k=0}^n a_kz^k,
\qquad
B(z)=\prod_{j=1}^n(y_j+v_j z)=\sum_{k=0}^n b_kz^k.
\]

Expanding the permanent and grouping terms by the number (k) of second
factor choices gives, exactly,

\[
\operatorname{per}(T)=
\sum_{k=0}^n k!(n-k)!a_kb_k. \tag{2.1}
\]

The doubled block matrix has every factor vector repeated twice.  Hence

\[
\operatorname{per}\!\begin{pmatrix}T&T\\T&T\end{pmatrix}
=\sum_{m=0}^{2n}m!(2n-m)!
[z^m]A(z)^2\,[z^m]B(z)^2. \tag{2.2}
\]

The verifier checks (2.1)--(2.2) against a completely separate permutation
enumerator for integer rank-two matrices at (n=3,4).

## 3. Normalizations and coverage

- The factorization has the gauge
  (F\mapsto FQ, G\mapsto GQ^{-\mathsf T}) for
  (Q\in\mathrm{GL}_2(\mathbb R)); it leaves (T) unchanged.
- Scaling factor row (f_i) or (g_j) scales the corresponding row or column
  of (T).  Both sides, and hence (H_n), acquire the same factor
  (\prod_i\lambda_i^2\prod_j\mu_j^2\).  Sign is preserved only for nonzero
  scales.  A zero scale is a separate zero-row/column stratum.
- If (T) has no zero row or column, a generic gauge avoids finitely many
  forbidden projective directions; subsequent nonzero row/column scales give
  the familiar chart (T_{ij}=1+r_i s_j).  Thus this chart is dense and
  sufficient for polynomial-continuity arguments, but it is not a license to
  divide by a factor coordinate or by (\operatorname{per}(T)).
- For (n=3), (\mathrm{PGL}_2(\mathbb R)) is triply transitive on distinct
  projective directions.  Three distinct row-factor lines may therefore be
  sent to factors (1,z,1+z), so (A=z+z^2).  Repeated and zero factors are
  separate strata below.
- For (n=4), three distinct row lines can be fixed but the fourth leaves a
  real cross-ratio.  In one chart
  (A=z(1+z)(1+\lambda z)); 
  (\lambda=0,1,\infty) and coincident directions are boundary strata.  The
  affine parameter is noncompact unless one retains its projective point at
  infinity.  Any (n=4) proof omitting these cases has a major gap.

## 4. Exact (n=3) proof

From (2.1)--(2.2), direct symbolic expansion gives

\[
\begin{aligned}
H_3/16={}&18a_0a_2b_0b_2-6a_0a_2b_1^2
+81a_0a_3b_0b_3-9a_0a_3b_1b_2\\
&-6a_1^2b_0b_2+2a_1^2b_1^2-9a_1a_2b_0b_3
+a_1a_2b_1b_2\\
&+18a_1a_3b_1b_3-6a_1a_3b_2^2
-6a_2^2b_1b_3+2a_2^2b_2^2. \tag{4.1}
\end{aligned}
\]

### Three distinct row directions

Put (A=z+z^2).  First suppose all three column directions are in the finite
chart, so
(B=\prod_{j=1}^3(1+r_jz)).  Write

\[
(r_1,r_2,r_3)=(t+p,t+q,t-p-q),\quad
S=p^2+pq+q^2,\quad h=pq(p+q).
\]

Substitution into (4.1) gives the exact identity

\[
\frac{H_3}{16}=E
=6St^2+6(S+3h)t+2S^2+9h+6S. \tag{4.2}
\]

As a quadratic in (t), its coefficients (A_t,B_t,C_t) satisfy

\[
4A_tC_t-B_t^2
=12\left((p-q)^2(2p+q)^2(p+2q)^2+9S^2\right), \tag{4.3}
\]

using
(4S^3-27h^2=(p-q)^2(2p+q)^2(p+2q)^2).
Thus (E>0) when (S>0), and (E=0) when (S=0), precisely when the
three column directions coincide.

The omitted affine boundary is explicit, not assumed by continuity for the
equality claim.  With exactly one infinite column direction, (4.1) reduces to

\[
2r^2-2rs+2s^2+r+s+2
=2(m+\tfrac12)^2+6d^2+\tfrac32>0,
\]

where (m=(r+s)/2,d=(r-s)/2).  With exactly two infinite directions it is
(2>0), and with three it is (0), again exactly the coincident-column
case.

### A repeated row direction

If the nonzero row directions have multiplicities (2+1), gauge them to
factors (1,1,z), so (a=(0,1,0,0)).  Then (4.1) becomes

\[
H_3=32(b_1^2-3b_0b_2). \tag{4.4}
\]

For finite column directions, nonzero scalings give (b_0=1) and

\[
b_1^2-3b_0b_2
=\tfrac12\sum_{i<j}(r_i-r_j)^2\geq0. \tag{4.5}
\]

If exactly one column is at infinity, (4.4) is strictly positive.  If at least
two are at infinity, it is zero; in the rank-two case those two column lines
are exactly the annihilator of the repeated row line.  If all row directions
coincide, (T) has rank at most one and direct evaluation gives equality.

If a factor row or column is zero, (T) has a zero row or column; both
permanents vanish.  These observations exhaust all projective multiplicity
types, proving (H_3\geq0) without any division by (\operatorname{per}(T)).

## 5. Equality iff statement for (n=3)

Equality holds exactly in the following cases:

1. (\operatorname{rank}T\leq1);
2. (T) has a zero row or a zero column; or
3. (T) has rank two and, after row and column permutations, has a (2\times2)
   zero block, equivalently it has the support form
   \[
   \begin{pmatrix}
   0&0&a\\0&0&b\\c&d&e
   \end{pmatrix}.
   \]
   (With no zero rows/columns, (a,b,c,d\ne0).)

For case 3, the first two rows can only use one column, so
(\operatorname{per}(T)=0); after doubling, four row copies can only use two
copies of that column, so the block permanent is also zero.  Conversely, the
strictness conclusions in the two projective cases above leave only this
annihilator configuration (or rank one/zero row/column).  For example,

\[
T=\begin{pmatrix}0&0&1\\0&0&1\\1&1&0\end{pmatrix}
\]

has rank two and equality with both permanents zero.  Therefore any claim
"equality iff rank at most one" or any proof dividing by
(\operatorname{per}(T)) is false.

## 6. Adversarial lemma checks

- The coefficient inequality is **not** a positive-semidefinite quadratic
  form on arbitrary coefficient vectors.  Take the split-real row cubic
  (A=(1+z)(1+2z)(1+3z)), so (a=(1,6,11,6)), but the nonsplit coefficient
  vector (b=(1,0,0,1)).  Formula (4.1) gives (H_3=-1728).  The proof must
  use that (B) is a product of real linear factors; dropping real-splitness
  is fatal.
- Row/column scaling is harmless only when the scale is nonzero.  Zero scales
  are equality strata, not a normalization.
- The RHS cannot be used to normalize (\operatorname{per}(T)=1): exact
  rank-two equality examples have (\operatorname{per}(T)=0).
- Random or adversarial (n=4) searches, including tests on
  (\operatorname{per}(T)=0), are discovery evidence only.  They do not prove
  global nonnegativity on the real-split quartic cone.

## 7. Remaining gaps and severity

| Item | Severity | Referee disposition |
|---|---:|---|
| Real (n=3) inequality | closed | Exact proof and independent verifier pass. |
| (n=3) equality classification | closed | Includes rank-two zero-permanent support cases and affine boundaries. |
| Complex formulation | fatal if claimed | Source does not state one and (\leq) is undefined over (\mathbb C). |
| Real (n=4) global proof | major/open | Cross-ratio and all split-quartic/boundary cases need an exact certificate. |
| "Positive-entry case known" as a cited theorem | local/source gap | Original paper gives only an uncited author report. |
| Full novelty through 2026-08-29 | separate Gate 1 obligation | This referee checked the primary statement and publisher record, not an exhaustive forward-citation database. |

The scientifically supportable endpoint from this audit is therefore a
**PARTIAL_THEOREM: the full real (n=3), rank-at-most-two case**, unless a
separate audited (n=4) certificate is later supplied.

## 8. Reproduction

Command:

```bash
python experiments/referee_verify_n3.py
```

Raw output from a clean invocation in the project environment:

```text
PASS: exact symbolic identities and independent direct evaluators
n=3 coefficient gap: 16*(18*a0*a2*b0*b2 - 6*a0*a2*b1**2 + 81*a0*a3*b0*b3 - 9*a0*a3*b1*b2 - 6*a1**2*b0*b2 + 2*a1**2*b1**2 - 9*a1*a2*b0*b3 + a1*a2*b1*b2 + 18*a1*a3*b1*b3 - 6*a1*a3*b2**2 - 6*a2**2*b1*b3 + 2*a2**2*b2**2)
```

The verifier uses Python integer arithmetic and SymPy polynomial identities;
no SMT solver, CAD system, or proof assistant is invoked.
