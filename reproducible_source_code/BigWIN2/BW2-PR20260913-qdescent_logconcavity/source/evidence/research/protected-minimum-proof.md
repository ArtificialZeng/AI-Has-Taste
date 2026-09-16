# Proposed resolution: a transfer preserving the minimum

Job: primary-20260913-qdescent-logconcavity-research-8293ab93d85b.
Research evidence, 2026-09-13. This is a proof candidate for a fresh referee,
not an acceptance, manuscript, or priority certificate.

## Exact scope

Retain every definition and quantifier of source.md and problem.md. In
particular, the literal original requires i<j. The following argument claims
that all a_k(S;q), 1<=k<=m=max S, are nonzero and that

    a_i(S;q)a_j(S;q) - a_(i-1)(S;q)a_(j+1)(S;q) >=_q 0

for every finite nonempty S subset of the positive integers and every
1<=i<=j<=m, with a_0=a_(m+1)=0. The diagonal i=j conclusion is an explicitly
additional strengthening, not a correction to the frozen original.

In fact we prove the directed strengthening of frozen Target K:

    K(m;i,r)K(m;j,s) - K(m;i-1,r)K(m;j+1,s) >=_q 0

for all m>=1, 1<=i<=j<=m, and independently 1<=r,s<=m. Here

    K(m;k,r) = q^(k^2)([m choose k]_q - [m-r choose k]_q)

for 1<=k<=m and K(m;0,r)=K(m;m+1,r)=0. This directed statement implies
both the single and the symmetrized mixed expressions of frozen Target K.

## 1. Subsets and reversed kernels

For a k-element subset U of [m]={1,...,m}, put

    w_k(U) = sum(U) - k(k+1)/2.

This is a nonnegative integer. Let P_k(m;r) consist of the k-element
subsets U with min U<=r, for 1<=k<=m. Set P_0(m;r)=P_(m+1)(m;r)=empty.
Define H(m;k,r) as the sum of q^w_k(U) over P_k(m;r), with those zero
boundary conventions. The usual subset definition of Gaussian coefficients
immediately gives, for 1<=k<=m,

    H(m;k,r) = [m choose k]_q - q^(kr)[m-r choose k]_q.          (1)

Indeed the excluded subsets are precisely r+V for k-subsets V of [m-r];
translation adds kr to the weight. Replacing each u in a k-subset of [n]
by n+1-u proves Gaussian reciprocity

    [n choose k]_(q^-1) = q^(-k(n-k))[n choose k]_q.

Use the zero convention when k>n. Equation (1) consequently gives

    q^(mk) H(m;k,r)(q^-1) = K(m;k,r).                         (2)

This reversal has no negative powers: w_k(U)<=k(m-k)<=mk. Also H has
constant coefficient 1, from U=[k]. Thus K has degree mk and a nonzero
coefficient at q^(mk), for every 1<=k,r<=m.

## 2. The transfer lemma, including its inverse

Fix m and 1<=i<=j<m and let delta=j-i+1>=1. Given any A subset [m]
of size i-1 and B subset [m] of size j+1, we construct (C,D), of sizes
i and j, satisfying

    sum(C)+sum(D) = sum(A)+sum(B)-delta,                      (3)
    min D = min B,
    min C <= min A when A is nonempty.                       (4)

The construction is injective. For i=1 the lemma still makes sense with
A empty, although the kernel application at that boundary is already trivial.

Protect b=min B: set B0=B without b, and A_delta={a+delta:a in A}.
For integers delta<=t<=m+delta define

    f(t)=#{a in A_delta:a<=t}-#{b' in B0:b'<=t}.

All elements of A_delta exceed delta, while B0 contains no 1. Therefore

    f(delta)=-#(B0 intersect [delta]) >= 1-delta.

At t=m+delta we have f(t)=(i-1)-j=-delta. More generally f(t)<=-delta
for t>=m, since B0 is already fully counted. Thus, if M=max f and L
is the largest integer with f(L)=M, then M>=1-delta>-delta and L<m.
Put e=L+1. By the choice of L, f(e)<f(L), and a one-step increment
of f belongs to {-1,0,1}. It follows that

    delta<e<=m,    e in B0,    e not in A_delta,    f(e)=M-1.

Consequently

    C=A union {e-delta},      D=B without e                   (5)

are subsets of [m] of the required sizes. The element added to A is new;
the protected minimum of B is not removed. This proves (3) and (4).

For injectivity, the following recovers e from any output in the image.
Compute b=min D, C_delta={c+delta:c in C}, D0=D without b, and

    g(t)=#{c in C_delta:c<=t}-#{d in D0:d<=t}

on the same integer interval [delta,m+delta]. Equation (5) gives

    g(t)=f(t)+2*1_(t>=e).

For t<e, g(t)<=M. For t>=e, the last-maximum definition of L gives
f(t)<=M-1, hence g(t)<=M+1; at t=e equality holds. Therefore e is
exactly the FIRST integer at which g attains its maximum. Recover

    A=C without {e-delta},    B=D union {e}.

This is a deterministic left inverse, proving injectivity. The use of the
last maximum in the forward map and first maximum in the inverse is essential.

## 3. Directed coefficientwise inequalities

Take 2<=i<=j<m, and arbitrary 1<=r,s<=m. Apply the transfer to

    A in P_(i-1)(m;r),    B in P_(j+1)(m;s).

By (4), C belongs to P_i(m;r) and D belongs to P_j(m;s). Thus the
same map restricts to an injection between these two products of families;
no ordering of r and s is needed. The normalization constants obey

    (i-1)i/2 + (j+1)(j+2)/2
      - i(i+1)/2 - j(j+1)/2 = delta.

Together with (3) this gives

    w_i(C)+w_j(D)=w_(i-1)(A)+w_(j+1)(B).

The injection preserves the exponent of q exactly. Its complement in the
target product therefore enumerates the nonnegative coefficients of

    H(m;i,r)H(m;j,s) - H(m;i-1,r)H(m;j+1,s).                 (6)

If i=1 or j=m, the right-hand product is zero by convention, so (6) is
also nonnegative. This includes all cases, including m=1 and diagonals.
Applying coefficient reversal q^(m(i+j)) times substitution q -> q^-1
to (6), and using (2), proves the directed K statement. Both terms have
reversal bound m(i+j), so reversal merely reindexes nonnegative coefficients.

## 4. Direct reduction from the original permutation definition

This verifies the intake reduction without requiring its imported script
or the source's a-to-b transformation as a mathematical dependency.

Fix S, m=max S, and T=S without m. For 1<=r<=m let

    x_r(q)=sum q^inv(sigma),

over sigma in Sym(m) with Des(sigma)=T and sigma_m=r. For a permutation
pi counted by a_k(S;q), all descents after position m are absent; hence
its final k entries are a k-element subset U of [m], in increasing order.
Its first m entries are ([m] without U) union {m+1,...,m+k}; standardizing
them yields exactly one sigma counted by x_r, for some r.

Write U={u_1<...<u_k}. Exactly u_1-1 prefix values are smaller than u_1.
The required descent at m is therefore equivalent to r>=u_1, or min U<=r.
Conversely, any such pair (sigma,U) reconstructs a unique pi, with precisely
the specified descent set and all large values in its first m entries.

Prefix inversions contribute inv(sigma), suffix inversions contribute zero.
For the suffix entry u_t, the number of larger prefix values is

    (m+k-u_t) - (k-t) = m-u_t+t.

Thus the number of cross inversions is

    km-sum(U)+k(k+1)/2 = km-w_k(U).

Summing gives, directly from the frozen original definition,

    a_k(S;q)=sum_(r=1)^m x_r(q) q^(mk)H(m;k,r)(q^-1)
            =sum_(r=1)^m K(m;k,r)x_r(q).                    (7)

Consequently, for 1<=i<=j<=m,

    a_i a_j-a_(i-1)a_(j+1)
      =sum_(r,s=1)^m x_r x_s
          (K(m;i,r)K(m;j,s)-K(m;i-1,r)K(m;j+1,s)) >=_q 0.

Every summand is nonnegative by Section 3 and x_r in Z_>=0[q]. For support,
every T subset [m-1] is realized by a permutation: split the positions into
blocks joined by exactly the edges in T, assign successive intervals of
integers to successive blocks, and reverse the entries within each block.
This has descents exactly T. Thus some x_r is nonzero. For that r, the
subset U=[k] is allowed for every 1<=k<=m, so (7) shows every a_k is
nonzero. Both the literal original and the disclosed diagonal strengthening
follow.

## Dependencies, provenance, and gap list

The proof is self-contained after the original definitions. The Gaussian
identity is established by subsets and reciprocity, and the reduction is
proved directly. Gaetz--Gao v2, Sections 1.2 and 2, identifies the original
problem; the immutable local primary HTML is included in the candidate scope.

The transfer adapts the shifted-set last-maximum construction in Christian
Krattenthaler, *On the q-log-concavity of Gaussian binomial coefficients*,
Monatshefte fuer Mathematik 107 (1989), 333--339, Section 2. The added step
is to protect min B before forming the prefix-difference function. The
unmodified construction need not preserve the cutoffs; for m=4, i=j=2,
A={2}, B={2,3,4}, it produces C={1,2}, D={3,4}, which loses min D<=2.
The protected construction instead produces C={2,3}, D={2,3}.
The classical method is prior work; no claim is made to invent it.

Known mathematical gaps in the proposed proof: none identified by this
research pass. This is a request for fresh scrutiny, not an independent audit.
In particular the referee should check the strict inequality at f(delta),
the position of the last maximum, the inverse, reversal bounds, and direct
permutation reconstruction. Computation checks finite instances only.
Literature coverage and access gaps are separate from the mathematical proof;
see literature/research-pass-1-screen.md. No global priority/current-open
assertion is part of the mathematical claim.
