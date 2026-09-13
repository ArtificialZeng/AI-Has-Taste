# General cyclic-prefix derivation for research verification

Status: unaudited mathematical derivation found during triage, not an
accepted resolution. It is stronger evidence for admission than a numerical
fit. Scope: exactly the polynomial bases and full Boolean domain in problem.md.

First, G(1_C)=0 whenever |C|<n. If at most n-2 matrix entries are nonzero,
rank(P)<=n-2 and adj(P)=0. Otherwise |C|<n forces u=0. Consequently all
ANF coefficients of size < n vanish. This reproduces Theorem 17's argument.
For any A of size n, all proper subsets vanish, so c_A=G(1_A).

Choose i=1. There exists r != i with (J(e_i))_r=1. Indeed alpha is neither
zero nor one, and alpha^{-1}=alpha would imply alpha^2=1 and alpha=1
in characteristic two. Thus J(e_1) cannot be e_1 or zero and has an
off-diagonal nonzero coordinate. There is also a modulus-independent choice:
for n>=3 choose r=n-1, since irreducibility gives p(0)=1 and

alpha^{-1} = alpha^{n-1} + a_{n-1}alpha^{n-2} + ... + a_2 alpha + a_1

when p(t)=t^n+a_{n-1}t^{n-1}+...+a_1 t+1.
For n=2 the sole irreducible polynomial is t^2+t+1, and r=0 works.

For each k=0,...,n-1 let sigma_k(h)=(h+k) mod n, c_k=sigma_k(r),
j_k=sigma_k(i), and define the n-element set

A_k = {p_{h,sigma_k(h)} : h != r} union {u_{j_k}}.

At its indicator assignment, P is a partial permutation matrix with its
rth row and c_kth column zero. All other rows and columns are matched.
Thus adj(P)=e_{c_k} e_r^T: deleting row r and column c_k leaves a
permutation matrix of determinant one over F_2; every other relevant minor
retains a zero row or column. Also Pu=e_i. Therefore

c_{A_k} = G(1_{A_k}) = e_{c_k}(J(e_i))_r = e_{c_k} != 0.

The n sets A_k are pairwise disjoint. Their union is exactly all n(n-1)
matrix variables outside row r, together with all n operand variables.
Putting these supported monomials first introduces n variables each time.
Only the n entries of row r remain unseen. Appending every remaining support
in any order introduces at most n new variables at every later step.
This would establish L(G)<=n; together with the verified prior lower bound,
it would establish the frozen equality for every n and every allowed p.

The key distinction from an unnecessarily stronger search target: degree-n
supports need not cover every variable. It suffices to leave at most n.
No enumeration of the complete ANF for large n is required by this argument.

Next proof test: check the adjugate orientation and exact coefficient identity
c_{A_k}=e_{(r+k) mod n}, then verify the cyclic cover and the n=2 boundary
from the frozen definitions. Any failure here invalidates this proposed proof.
