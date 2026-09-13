# Exact cut-LP solution on the branch \(\ell=1\)

## Theorem

For every integer \(m\ge2\), the complete cut LP `(P)` of `problem.md` satisfies
\[
 \operatorname{OPT}_{m,1}
 =\max\left\{2m+2,\frac{5m}{2}\right\}
 =\begin{cases}
 2m+2,&m=2,3,\\
 5m/2,&m\ge4.
 \end{cases}
\]
Consequently, \(J_{m,1}\) is fractionally Hamiltonian if and only if
\(2\le m\le4\). In particular,
\[
 \operatorname{OPT}_{5,1}=25/2>12,
 \qquad
 \operatorname{OPT}_{6,1}=15>14.
\]
Thus \(J_{5,1}\) is an exact counterexample to the natural proposed sharpness
of the previously known sufficient non-fractional-Hamiltonicity boundary
\(m\ge2\ell+4\): here \(m=2\ell+3\).

## Universal lower bound

For any graph of order \(n\), summing the \(n\) singleton-cut constraints gives
\(2\sum_e x_e\ge2n\), hence `(P)` has value at least \(n\). Here this gives
\(\operatorname{OPT}_{m,1}\ge2m+2\).

The dual of `(P)` assigns nonnegative weights \(y_S\) to distinct nontrivial
cuts and is
\[
 \max 2\sum_S y_S
 \quad\text{subject to}\quad
 \sum_{S:e\in\delta(S)}y_S\le1\quad(e\in E).
\]
For every \(m\), put, for each \(i\),
\[
 y_{\{b_i\}}=\frac14,
 \qquad y_{\{x_i\}}=\frac34,
 \qquad y_{\{b_i,x_i\}}=\frac14,
\]
and set every other dual variable to zero. The dual load is \(1\) on each
edge \(b_i b_j\), \(a x_i\), \(b_i x_i\), and \(u x_i\); it is \(1/2\) on
each \(u b_i\), and \(0\) on \(ua\). Hence this is dual feasible, with value
\(2m(1/4+3/4+1/4)=5m/2\). Therefore
\[
 \operatorname{OPT}_{m,1}\ge\max\{2m+2,5m/2\}.
\]

## Matching upper bound for \(m\ge4\)

Let \(u\) be the unique vertex of the joined \(K_1\). Assign the following
primal weights:
\[
 x_{b_i b_j}=\frac1{m-1},\qquad
 x_{a x_i}=x_{u x_i}=\frac12,\qquad
 x_{b_i x_i}=1,
\]
and assign zero to \(ua\) and every \(u b_i\). Their total is
\[
 \binom m2\frac1{m-1}+m\left(\frac12+1+\frac12\right)
 =\frac{5m}{2}.
\]

It remains to check every cut. For a shore \(S\), write
\(A,U,B_i,X_i\in\{0,1\}\) for membership of
\(a,u,b_i,x_i\), respectively, and put \(k=\sum_i B_i\). Its exact weight is
\[
 C(S)=\frac{k(m-k)}{m-1}
 +\sum_i|B_i-X_i|
 +\frac12\sum_i|X_i-A|
 +\frac12\sum_i|X_i-U|. \tag{1}
\]
If \(A\ne U\), the last two summands contribute exactly \(m/2\), so
\(C(S)\ge m/2\ge2\).

If \(A=U\), complement the shore if necessary and assume \(A=U=0\). When
\(k=0\), nontriviality forces some \(X_i=1\), and that index contributes
\(2\) to (1). When \(k\ge1\), every index with \(B_i=1\) contributes exactly
\(1\) to the last three sums, so
\[
 C(S)\ge k+\frac{k(m-k)}{m-1}\ge2;
\]
the last inequality is immediate for \(k\ge2\), while equality holds for
\(k=1\). Thus all nontrivial cuts are feasible, proving the upper bound for
every \(m\ge4\).

## The two remaining values

For \(m=2\), the graph contains the Hamiltonian cycle
\[
 a,x_1,b_1,b_2,u,x_2,a.
\]
For \(m=3\), it contains the Hamiltonian cycle
\[
 a,x_2,b_2,u,x_1,b_1,b_3,x_3,a.
\]
The incidence vector of a Hamiltonian cycle is feasible for `(P)` and has
weight equal to the order. Together with the singleton lower bound, these
cycles prove the values \(6\) and \(8\), respectively.

Combining the cases proves the theorem. Since the order is \(2m+2\), the LP
equality criterion in `problem.md` yields fractional Hamiltonicity exactly for
\(m\le4\).

## Exact computational audit of the requested boundary cases

`evidence/cut_lp_certify.py` independently expands orbit-constant rational
certificates, uses `fractions.Fraction`, enumerates every nonempty shore not
containing `a` (exactly one shore from each complementary pair), and checks
every primal cut and every dual edge constraint. The machine-readable inputs
are in `evidence/J_m_1_certificates.json`, and the captured output is
`evidence/J_m_1_verification.json`.

In particular, it checks all \(2^{11}-1=2047\) distinct cuts for \(J_{5,1}\)
and all \(2^{13}-1=8191\) distinct cuts for \(J_{6,1}\). Both have minimum
certified cut weight \(2\), and the matching exact primal/dual objectives are
\(25/2\) and \(15\), respectively. These computations audit the explicit
certificates; the all-\(m\) conclusion above follows from the symbolic cut
argument, not from finite extrapolation.
