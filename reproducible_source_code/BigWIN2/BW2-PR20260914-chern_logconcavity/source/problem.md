# Precise problem and triage scope

The immutable statement is `source.md`, copied from Bérczi–Fehér,
[arXiv:2605.25271v1](https://arxiv.org/html/2605.25271v1), Section 3,
Definition 3.1 and Conjecture 3.3. Its SHA256 is recorded in
`evidence/source-sha256.txt`. No correction to that file is proposed.

For every integer d >= 0, let

\[
 c_k(2,d)=[z^k]\prod_{i=0}^{d}(1+z(i x_1+(d-i)x_2)).
\]

For every integer k >= 0 and every integer 0 <= j <= floor(k/2), define
A_{k,j}(d) by the unique expansion

\[
c_k(2,d)=\sum_{j=0}^{\lfloor k/2\rfloor}A_{k,j}(d)s_{(k-j,j)}(x_1,x_2),
\qquad
s_{(k-j,j)}=\sum_{m=j}^{k-j}x_1^{k-m}x_2^m.
\]

The dependence on d is a rational polynomial, determined by all its
nonnegative integer values. Define its unique Newton coefficients by

\[
A_{k,j}(d)=\sum_{r\ge0}B_{k,j,r}\binom dr,\qquad
B_{k,j,r}=\Delta^r A_{k,j}(0)
=\sum_{q=0}^r(-1)^{r-q}\binom rq A_{k,j}(q),
\quad \Delta f(d)=f(d+1)-f(d).
\]

Here binom(d,r) is the falling-factorial polynomial divided by r!,
including binom(d,0)=1. The coefficients B are integers. Extend them by
zero for negative r and beyond their finite support.

**Frozen assertion.** For every admissible pair (k,j), the support
{r >= 0 : B_{k,j,r} != 0} is an interval of integers, and for every r >= 0,

\[
B_{k,j,r}^{2}-B_{k,j,r-1}B_{k,j,r+1}\ge0.
\]

The no-internal-zero requirement follows the source's Definition 3.1;
it does not mean compressing a sequence after deleting internal zeros.
Nonnegativity of B is the separate Conjecture 3.2 and is not silently
added to Conjecture 3.3. It is useful ancillary evidence and a potential
input to a proof. Ordinary log-concavity of A_{k,j}(d) in d is a weaker,
different assertion; log-concavity in j or k is also outside this target.

Boundary conventions: c_0=1, A_{0,0}=1, B_{0,0,0}=1. For k>d+1 the
value c_k(2,d) is zero; this does not restrict the quantifier over k or
change the polynomial A_{k,j}. At d=0 the total product equals 1.
All polynomial degrees are at most 2k: the m-th Chern-root power sum
has degree at most m+1 in d, and Newton's identities express c_k in
products whose indices sum to k. Consequently forward differences
through order 2k recover every B for each fixed (k,j).

## Prior results and proposed contribution

The primary text proves log-concavity for j=0 (Theorem 3.7) and j=1
(Theorem 5.4), and positivity through j=2 (Theorems 3.6 and 5.2).
Section 1.2 explicitly leaves higher log-concavity modes open. The
primary Figure 1 labels the last log-concavity result as j=2, in conflict
with the formal theorem and proof, which both use j=1. This discrepancy
must remain visible in any later priority check.

The supplied MathDB capture contains Shivam Patel's claimed all-j
positivity proof by recurrence and support induction. That is prior work,
not a proposed new result here; it does not prove log-concavity.

Nearest prior result: the j=1 log-concavity certificate in Theorem 5.4.
The original proposed research target was all-k>=4 log-concavity for j=2.
That target remains unresolved. Both the direct common-defect k-2 and
k-3 trace/Abel certificates fail. The latter has 348 negative active
prefixes for 5<=k<=32; an exact negative trace occurs at k=8,r=10 while
the actual B minor is positive (`evidence/j2-defect-kminus3.json`).

The research-pass candidate is a strictly identified auxiliary theorem.
For k>=4 set

\[
\begin{aligned}
R_k(x)={}&(x-k+2)A_{k-1,1}(x)
+\tfrac12(x-k+3)(x-k+2)A_{k-2,0}(x)\\
&+(x+1)(x-k+3)A_{k-2,1}(x)
+\tfrac12(x+1)(x-k+4)(x-k+3)A_{k-3,0}(x).
\end{aligned}
\]

Write R_k(x)=sum_r rho_{k,r} binom(x,r), with zero extension. The proposed
result is that rho_{k,r}>0 exactly for k-2<=r<=2k-1 and
rho_{k,r}^2>=rho_{k,r-1}rho_{k,r+1} for every k>=4,r>=0.
These are the four lower-mode forcing terms in source equation (5.2):
Delta A_{k,2}=(x+1)A_{k-1,2}+R_k. Their positivity and the recurrence are
prior results; log-concavity of their sum is the proposed increment.

The proof uses 41 exact support-variable prefix polynomials with 1,506
positive coefficients and no negative coefficients. An independent
standard-library implementation verifies the identities using a degree
bound and exact polynomial interpolation. The complete argument and
remaining mixed inequality are in `evidence/auxiliary-proof.md`.
This candidate neither proves j=2 log-concavity nor the full original.
Fresh mathematical and contribution review has not yet occurred.

Source status: open-supported by v1 for the higher modes, with the
figure discrepancy and current literature/registry limits recorded in
`evidence/literature-triage.md` and `evidence/research-literature.md`.
The primary text is copied byte-for-byte to
`evidence/external/2605.25271v1.html` for the candidate's review.
