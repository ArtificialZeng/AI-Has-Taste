# Support-counting compositional inverse for comb preorder polytopes

Source: Athanasiadis and Chapoton, Polytopes and posets associated to preorders,
arXiv:2605.26916v1, Section9.6 final unnumbered proposal.
https://arxiv.org/html/2605.26916#S9.SS6
This is a precise mathematical transcription of the source's proposal, not
claimed to be a verbatim quotation or a numbered conjecture.

Define tau_0 to be the empty poset. Recursively obtain tau_(n+1) from tau_n
by taking its disjoint union with one new singleton, then adjoining one new
minimum below every existing element. Thus tau_n has 2n elements.

For every n>=0 define
Q_n={x in R_(>=0)^(2n): sum_(v in I) x_v <= |I| for EVERY lower ideal I of tau_n},
and h_n(t)=sum_(x in Q_n intersect Z^(2n)) t^(#{v:x_v>0}), with h_0(t)=1.
This is raw lattice-point support enumeration, not the Ehrhart h-star polynomial.

Work in Q(t)[[x]], with t an indeterminate, and set
F(t,x)=sum_(n>=0) t^(-n) h_n(t) x^(n+1),
R(t,x)=sum_(m>=1) (-1)^(m-1)
 [1+(1+t)^m t^(1-m) sum_(j=0)^(m-2) t^j] x^m.
The inner sum is empty and equals0 when m=1.

Prove or disprove the all-n/formal-series identity
R(t,F(t,x))=x, equivalently F(t,R(t,x))=x.
The source separately suggests the unweighted sequence A034015; the selected
target is the full support-refined compositional inverse, not just t=1.
