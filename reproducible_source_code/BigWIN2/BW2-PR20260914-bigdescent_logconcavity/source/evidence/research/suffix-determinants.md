# Determinant recurrences for the attempted suffix induction

Use T(A,B,C)=(A+tB+tC,A,tB+C), zero-extended coefficient sequences,
L_k(P)=p_k^2-p_{k-1}p_{k+1}, and
M_k(P,Q)=2p_kq_k-p_{k-1}q_{k+1}-p_{k+1}q_{k-1}.
Let U=M(A,B), V=M(A,C), W=M(B,C), H=M(A,tB),
I=M(A,tC), J=M(C,tB), and K(P)=M(P,tP).
A superscript minus below means replace k by k-1; prime means apply T.
Bilinearity of M and L(P+Q)=L(P)+L(Q)+M(P,Q) give the exact identities

    L(A)' = L(A)+L(B)^-+L(C)^-+H+I+W^-,
    L(B)' = L(A),
    L(C)' = L(B)^-+L(C)+J,
    U' = 2 L(A)+H+I,
    V' = H+V+2 L(B)^-+J+W^-+K(C),
    W' = H+V,
    H' = K(A)+U^-+V^-,
    I' = M(A,t^2 B)+I+K(B)^-+W^-+J^-+2 L(C)^-,
    J' = U^-+M(C,tA).

For nonnegative LC coefficient sequences with interval support,
K_k(P)=p_k p_{k-1}-p_{k+1}p_{k-2}>=0, by multiplying consecutive
ratio inequalities (with zero boundaries handled directly).
Thus only the last two displayed identities introduce mixed terms
outside the nine proposed nonnegative invariants. This is a diagnosis
of this particular induction, not a proof that I,J are the only possible
difficulties in every approach. Their finite tests are in
suffix_diagnostics.json, with exact recurrence checks and two witnesses.

The negative terms cannot simply be assumed nonnegative. In particular,
the scaled reachable seed (1+5t,1,1) satisfies the proposed nine inequalities,
but its first update has J_1=-3 and its second has C=1+2t+5t^2.
The formal scaling obstruction and its precise scope are proved in
scale-obstruction.md.
