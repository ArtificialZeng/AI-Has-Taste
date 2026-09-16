# Two-factor reduction and a negative-difference witness

Provenance: `primary-20260914-q-product-unimodality-triage-b5b9ae83cac9`, 2026-09-14. These are mathematical triage arguments, without independent referee acceptance or a novelty claim. The full original conjecture is not resolved here.

Let \(1\le a\le c\), \(r\ge2\), \(b\ge1\), and
\(P=[a]_q[c]_q[b]_{q^r}=\sum p_nq^n\), with \(p_n=0\) outside \([0,D]\) and \(D=a+c-2+r(b-1)\). Define
\[
N_{r,b}(L,U)=\max\{0,\min(b-1,\lfloor U/r\rfloor)-\max(0,\lceil L/r\rceil)+1\}.
\]
It counts integers \(j\in[0,b-1]\) with \(L\le rj\le U\). Directly,
\[
(1-q)[a]_q[c]_q=(1+\cdots+q^{a-1})-q^c(1+\cdots+q^{a-1}),
\]
so
\[
p_n-p_{n-1}=N_{r,b}(n-a+1,n)-N_{r,b}(n-a-c+1,n-c). \tag{1}
\]
This is the same interval-count mechanism used for stretch 2 in source Proposition 4.5, now written for arbitrary stretch.

## Uniform necessity witness for two nondivisible factors

Write \(a=rA+s\), \(c=rC+t\), where \(A,C\ge0\) and \(1\le s,t\le r-1\). Put \(M=A+C\), \(u=\max(s,t)\). If \(b\ge M+2\), take
\[
n_* = rM+u.
\]
For the positive count in (1), its lower endpoint is \(rC+u-s+1\), lying strictly between \(rC\) and \(r(C+1)\), and its upper endpoint is \(rM+u\). Thus the admissible integers are \(j=C+1,\ldots,M\): exactly \(A\) of them, with the empty case interpreted as zero.

For the negative count, the lower endpoint is \(u-s-t+1=1-\min(s,t)\le0\), and the upper endpoint is \(rA+u-t\), with \(0\le u-t<r\). Thus \(j=0,\ldots,A\): exactly \(A+1\) of them. Since \(b-1\ge M+1\), the upper clipping removes none of these integers. Hence
\[
p_{n_*}-p_{n_*-1}=-1.
\]
Moreover,
\[
D-2n_*=r(b-1-M)-|s-t|-2\ge r-(r-2)-2=0.
\]
Thus \(1\le n_*\le\lfloor D/2\rfloor\), proving nonunimodality in this parameter range. This verifies the necessity implication for \(k=2\); it supports the original conjecture and is not a counterexample to it. No assertion about novelty of this elementary lemma is made.

## One remaining test: a uniform sufficient inequality

Assume \(b\le M+1\). When \(n<c\), the negative count in (1) vanishes. For \(c\le n\le\lfloor D/2\rfloor\), one has \(n<a+c-1\), and (1) reduces the sufficient direction to
\[
\min\{b-1,\lfloor n/r\rfloor\}\ \ge
\lfloor(n-a)/r\rfloor+\lfloor(n-c)/r\rfloor+1. \tag{2}
\]
Indeed the negative count has lower clipping at zero and its upper endpoint lies below \(r(b-1)\); the positive count is
\(\max(0,\min(b-1,\lfloor n/r\rfloor)-\lfloor(n-a)/r\rfloor)\).
The next research test is to prove or falsify (2) uniformly, splitting \(n=rh+v\), \(0\le v<r\), at \(v=s,t\) and retaining the midpoint constraint. This identifies a finite list of residue-order cases with unbounded quotient variables, not a request to extend a finite table.

## Exact calibration

`triage_boundary.py` constructs coefficients by ordinary integer convolution and compares every difference, including the outside endpoint, with (1). Its fixed boundary-adapted range is recorded in `triage-boundary.json`: 10,802 parameter tuples, 578,721 difference identities, 6,050 sufficient-regime tests, and 4,752 negative-witness tests, all passing. The range covers r=2..12, both quotients 0..2, all nonzero residues, and five specified distinct b choices. These are finite observations only.

Example: r=5, a=7, c=9, b=4 has D=29, n*=14, p13=13 and p14=12. It violates the proposed sufficient condition and fails unimodality, as predicted. This is calibration, not an original-conjecture counterexample.
