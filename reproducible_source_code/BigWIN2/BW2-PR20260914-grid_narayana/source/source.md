# Narayana factorization for a truncated two-row grid preorder

For each integer n>=1, let P_n be the coordinatewise ordered set
({1,...,n} x {1,2}) minus its unique maximum (n,2).
For every lower ideal I of P_n impose sum_(v in I) x_v <= |I|, together
with x_v>=0, and call the resulting polytope Q_n. Let
H_n(t)=sum_(x in Q_n intersect Z^(2n-1)) t^(number of nonzero coordinates of x).

Define
A_r(t)=sum_(j=0)^r binom(r,j)binom(r+1,j)t^j/(j+1)
and B_r(t)=sum_(j=0)^r binom(r,j)^2 t^j.

Prove or disprove the identity H_n(t)=A_(n-1)(t) B_n(t) for every integer n>=1.
The empty ideal is allowed and imposes no additional restriction.

Primary source: Athanasiadis–Chapoton, Polytopes and posets associated to preorders,
arXiv:2605.26916v1, Section9.3, final unnumbered proposed identity.
https://arxiv.org/html/2605.26916
This is a precise transcription of that proposed identity, not the distinct
Ehrhart h-star polynomial or an all-preorder real-rootedness claim.
