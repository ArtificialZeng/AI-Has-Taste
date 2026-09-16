# Research pass 1: saved intermediate evidence

Superseded intermediate checkpoint: the completed argument is
`hook-prefix-proof.md`, which adds degree 2b+3 and improves the final cutoff.
This file is not a submitted decisive evidence input.

Job: primary-20260914-brugidou-positivity-research-cd617853de0e.
Source hash checked unchanged. Sole handoff read and verified against recurrence.

New exact a=5,b=1 polynomial: [60,120,130,110,80,55,35,20,10,4,1].
Its sole support-overlap coefficient is 130=10*(6+6+3)-20.

Uniform bound now derived, undergoing verification:
J_m >= (m-1) J_(m-1) coefficientwise, from adjoining the largest vertex as
a leaf to a rooted tree. Put s=b+1, A=choose(a+b-1,a-2)J_(a-1),
P=choose(a+b-1,a-3)J_(a-2). Then A >= (s+1)P.
For k=s+t, 0<=t<=s, the hook recurrence twice gives
c_k = prefix_k(A) - sum_(i=0)^t (t-i+1)P_i.
Consequently c_k >= sum_(i=0)^t(s-t+i)P_i +
(s+1)sum_(i=t+1)^k P_i, positive for t<s, and for t=s when a>=5.
The small a bases are separately explicit. Thus initial coefficients
through min(degree,2b+2) are positive for all hooks. Together with the
previous tail induction this suggests the improved full-positivity region
b>=max(0,floor(choose(a-2,2)/2)-1).

Next immediate verification: independent exact specialization and rooted-tree
enumeration, endpoints of the induction, and current primary-source comparison.
No candidate acceptance or full-conjecture resolution is asserted.
