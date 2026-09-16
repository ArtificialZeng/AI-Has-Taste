# Exact transfer formulation for the next research test

Job: primary-20260914-grid-narayana-triage-7308d1927a46.
This is an elementary reformulation and finite calibration, not an accepted
new theorem or a proof of the proposed Narayana factorization.

Write a_i=x_(i,1), b_j=x_(j,2), U_i=i-sum_(k<=i)a_k and
V_j=j-sum_(k<=j)b_k, with U_0=V_0=0. Every ideal is uniquely a pair of
prefixes (i,j), 0<=i<=n and 0<=j<=min(i,n-1). Its inequality is
U_i+V_j>=0. Conversely every such pair is an ideal, since an included upper
element forces its lower counterpart and both rows must be prefixes.

After i complete columns, put M_i=min(V_0,...,V_i),
z=U_i+M_i and s=V_i-M_i. Both z,s are nonnegative for a legal prefix.
Appending a=a_(i+1) and b=b_(i+1) introduces exactly the inequalities
U_(i+1)+V_j>=0 for 0<=j<=i+1. Those involving old j give
0<=a<=z+1. The last inequality gives 0<=b<=z+s+2-a.
Writing delta=max(0,b-s-1), the new state is

    (z',s')=(z+1-a-delta, max(0,s+1-b)).

Indeed M_(i+1)=M_i-delta, which proves the update by substitution.
All earlier inequalities remain intact. The allowed values and new state
depend only on z,s, so merging histories with these states loses no future
feasibility information. The support weight is t^([a>0]+[b>0]).

Start at (0,0) with weight 1; perform n-1 complete-column transitions.
The last coordinate is a_n alone, with 0<=a_n<=z+1. Therefore its weight
multiplier is 1+(z+1)t. This describes H_n exactly for every n>=1 and
does not evaluate the transfer sum in closed form.

Executable: `python3 -B evidence/triage-transfer.py`.
The output file records exact integer comparisons with the proposed formula
through n=10 and direct complete ambient enumeration through n=6, including
generic order-ideal masks through n=4. The direct enumerator is the supplied
intake code, inspected and rerun locally; this is not a fresh-context referee.

Next test: derive a functional equation for the weighted generating series
of this two-variable transfer and determine whether its terminal functional
equals A_(n-1)(t)B_n(t) for all n. A proof needs an exact solution or a
weight-preserving bijection with an explicit inverse; more matching terms
alone cannot settle the identity.
