# Precise problem: antiprism h-vector transformation

Frozen source: `source.md`, SHA-256
`9e95e6241ffc8f233a1c0b4bf2ac35126b98ace72434474ca22006c35c7f9615`.
The original wording is retained there without alteration. This file fixes its
mathematical reading; no correction or restriction of the target is proposed.

For integers a,b, write C(a,b)=0 unless 0<=b<=a; otherwise C(a,b)
is the usual binomial coefficient. Let S(a,b) be the Stirling number of the
second kind, with S(0,0)=1, S(a,0)=0 for a>0, and S(a,b)=0 unless
0<=b<=a. All invalid summands below are zero.

For every integer d>=1, define the integer matrix H_d, indexed by
0<=i,j<=d, by

```
H_d(i,j) = sum_{r=0}^d sum_{s=0}^i
  C(j,s) C(d-j,d-r-s) C(r,i-s)
  sum_{ell=0}^d (ell!)^2 S(i-s,ell) S(r-i+s,ell).
```

The inner cutoff d is equivalent to the source's ell>=0. The target assertion
is: for every d>=1, every 1<=k<=d+1, and every pair of increasing lists
I=(i_1<...<i_k), J=(j_1<...<j_k) from {0,...,d},
`det(H_d[I,J]) >= 0`, with precisely these row and column orders.
This property is called total nonnegativity (TN) here. The cited papers use
"total positivity" for this same weak inequality. Strict positivity is not
intended: the top and bottom rows have boundary zeros.

## Geometric interpretation and independent normalization

A finite simplicial complex Delta is a collection of finite vertex sets closed
under taking subsets, including the empty set. Dimension d-1 means the largest
face has d vertices. Set f_{k-1}=#{F in Delta: |F|=k}, including f_{-1}=1.
Define h by
`sum_{i=0}^d h_i t^i = sum_{k=0}^d f_{k-1} t^k(1-t)^(d-k)`.
Vectors are columns.

The antiprism subdivision is the clique complex on pointed faces (F,v), v in F.
Distinct pointed faces (F,v),(G,w) are adjacent if F=G, or if F is a proper
subset of G and w is in G\F, or if G is a proper subset of F and v is in F\G.
This is Definition 4.1 of Athanasiadis--Brunink--Juhnke-Kubitzke.

That paper's equation (20) identifies H_d(i,j)=p_A(d,j,i). Proposition 5.12
and Proposition 5.7(b) give the displayed formula above by substitution,
including the empty local h-polynomial value ell_A(0,0)=1.
For an independent computational construction set

```
Q_d(i,k) = C(k,i) sum_{ell=0}^i ell! S(i,ell) ell^(k-i)  (i<=k),
Q_d(i,k) = 0                                         (i>k),
B_d(i,k) = (-1)^(i-k) C(d-k,d-i)                      (k<=i),
B_d(i,k) = 0                                         (k>i).
```

Use 0^0=1, so Q_d(0,0)=1. Equation (19) and Proposition 5.11 yield
`f(sd_A Delta)=Q_d f(Delta)` and hence `H_d=B_d Q_d B_d^{-1}`.
Here `B_d^{-1}(k,j)=C(d-j,d-k)` for j<=k and is zero otherwise.
The alternating signs in B_d mean this conjugation alone does not establish TN.

## Status, nearest results, and proposed contribution

Status on 2026-09-14: open-supported within the inspected primary sources and
bounded searches; no assertion of exhaustive worldwide priority. Liu--Mao,
[arXiv:2607.01577v1](https://arxiv.org/html/2607.01577v1), PDF Remark 5.8,
printed p.19 (HTML Remark 5.20), presents this matrix and proposes investigating
its total positivity. Their established results concern barycentric and interval
subdivision; their interlacing criterion guarantees only order 2.
Mu--Welker, [arXiv:2404.03500v2](https://arxiv.org/html/2404.03500v2), Section 2
after the geometric-conditions question, already reports positive antiprism
experiments in small dimensions, without a specified range in that passage.
The independent formulas are in
[arXiv:2006.10789v2](https://arxiv.org/pdf/2006.10789v2), Section 5.3,
printed pp.21--23, and Proposition 5.7, printed p.19.

Nearest prior result X: the exact antiprism transformation and finite positive
evidence, plus uniform TN proofs for other subdivision families.
Proposed delta Y: an exact negative minor, or a uniform nonnegative elementary
bidiagonal/planar-network factorization of H_d. Verification route Z: construct
the matrices by two independent formulas, verify any negative determinant in
integer arithmetic, or prove a proposed factor identity and factor signs for
every dimension. A new positive finite table alone is not a contribution.

The all-order, all-dimension matrix question is the whole selected target.
Interlacing, simplex real-rootedness, and finite-order statements are separate
subsidiary claims and cannot substitute for its resolution. In particular this
family is not the infinite Eulerian triangle or a TP4 truncation of it.

## Research pass 1: local progress, unchanged target

`evidence/research-pivots.md` derives a generating identity directly from the
frozen formula and proves positivity of all two-column minors in rows {1,2}
(and their reflections) for d>=3. It also gives an exact algebraic certificate
for positivity of the consecutive three-row flags
`det H_d[{1,2,3},{j-2,j-1,j}]`, d>=4, 3<=j<=d. The latter does not include
the triple {0,1,2} or arbitrary order-three minors. These are initial Neville
stages, not a proof of all-order TN, and no publishable candidate is claimed.
The original target, conventions, and quantifiers above remain unchanged.

## Research pass 2: further flags and an algebraic kernel

`evidence/research-pass2.md` proves strict positivity of the flags in rows
{1,...,k} and consecutive columns {j-k+1,...,j} for k=4,5,6 and every
d>=j>=k, using complete rational polynomial certificates. The fourth-order
certificate and both higher-order identities have separate arithmetic
verifiers in the same research context. No fresh referee is claimed.

For arbitrary k, set a=j-k, n=d-j and replace the exponential bases by
`b_l=l^k(z_1+...+z_l)`. The resulting determinant polynomial R_k has
explicit nonnegative product formulas at total (a,n)-degrees zero and
k(k+1)/2, proved in that dossier. Coefficient nonnegativity at all degrees
was a stronger working hypothesis, frozen before the order-six attack in
`evidence/flag-coefficient-hypothesis.md`. It would settle these first-stage
flags, but no equivalence with the original matrix question has been proved.
The original target and its quantifiers are unchanged.

## Research pass 3: the coefficient hypothesis is false

`evidence/research-pass3.md` gives a complete subsidiary proof and exact
certificates, proposed for a fresh result-note review. With the **same**
R_k and K=k(k+1)/2, define
`lambda_k=(prod_(r=1)^k r!)/(prod_(l=1)^k l^l)>0`. For every k>=5,

```
[a^(K-1) n^0 z_1^5 z_6...z_k]R_k
 = -lambda_k*(125k^4-9555k^3+17736k^2-346478k+858264)/20736.
```

This coefficient is negative for every integer k>=76. There is also an
exact negative coefficient at order 22:

```
[a^252 n^0 z_1^9 z_10...z_22]R_22
 = -lambda_22*4429926944297146258237/14051921264640000000.
```

The general degree-K-1 expression is derived in the dossier. The smaller
witness is recomputed directly from the defining determinant by a separate
integer Bareiss calculation; the uniform quartic formula is checked as a
complete polynomial identity. Both verifications are in this research
context, not a fresh referee. Files: `evidence/research_next_degree.py`
and `.json`, and `evidence/verify_next_degree.py` and `.json`.

Thus the all-k coefficient assertion from pass 2 is refuted; the prior
fixed-order identities remain compatible with this result. This is a
specific obstruction to that certificate strategy. A negative formal
coefficient does not give a negative minor at the actual a,n,z
specialization. The original TN question, its interpretation above, and
all its quantifiers are unchanged and unresolved.
