# Total positivity of shifted even-power sequences

Primary source: Anna Vishnyakova, Polynomials interpolated totally positive
sequences, arXiv:2607.06207v1 (2026-07-07), Example 5.7 and Conjecture 5.8.
https://arxiv.org/html/2607.06207v1
Selected 2026-09-14 Asia/Shanghai using authorized primary-literature fallback.
Not a ChatGPT-generated batch; no 大WIN batch number is consumed.

For n>=1 and real t, put P_(n,t)(x)=(x+t)^n. A sequence (a_j)_(j>=0)
is TP in the source's terminology when EVERY finite minor of the infinite
Toeplitz matrix (a_(j-i))_(i,j>=0) is nonnegative, with a_l=0 for l<0.
Thus TP means total nonnegativity, not strict positivity of every minor.
Define M_n={t in R : ((k+t)^n)_(k>=0) is TP}.

Original Conjecture 5.8, mathematical notation transcribed:
For all k in N,
M_(2k)=[-c_(2k),1+c_(2k)], 0<c_(2k)<2,
and c_2<=c_4<=c_6<=... .

The frozen target is the conjunction of these assertions for all positive
integers k, including the closed interval endpoints. Equivalently, do such
constants c_(2k) exist with these equalities, bounds, and monotonicity?
The source separately asks for their possible limit; that extra question is
context, not an additional requirement silently added to this target.

For exact verification, let L send binom(x,j) to z^j. Then
Q_(n,t)(z)=L(P_(n,t))(z)=sum_(j=0)^n z^j sum_(l=0)^j
(-1)^l binom(j,l)(j-l+t)^n.
The source's generating-function characterization makes t in M_n equivalent
to all n roots of Q_(n,t), counted with multiplicity, lying in [-1,0].
The known odd-degree result M_(2k+1)=[0,1] is not the research target.
Any finite-degree classification, stricter sufficient interval, or subsidiary
counterexample is only partial unless it proves/disproves this frozen conjunction.

Do not conflate this a=1 question with the all-a Pochhammer Conjecture 6.5
in arXiv:2608.03723v1, or with its multiplication-closure Open Problem 1.9.
