# Quantitative partition-jump theorem: proof dossier

Proposer: `primary-20260914-partition-jumps-research-abca685cda7d`.
Date: 2026-09-14. This is a research argument submitted for fresh review,
not an accepted manuscript. Definitions and the immutable original are in
`problem.md` and `source.md`.

## Exact proposed scope

For the simple unit-transfer partition graph and the invariants specified in
`problem.md`, the following statements hold.

1. For every integer n >= 2,

       D_delta(n) = 0  if n is 2 or 3;
                    1  if 4 <= n <= 10 or n is 12 or 13;
                    2  if n = 11 or n >= 14.

2. Put T_s=s(s+1)/2 and s=max{t:T_t<=n}. For every n>=10,

       4s-8 <= D_d(n) <= 4s+2.

   In particular, D_d(n)=4 sqrt(2n)+O(1) as n tends to infinity, with an
   absolute implied constant and a lower-bound witness for every n>=10.

3. The proof also characterizes edges with dimension jump two by the local
   support and multiplicity conditions in Section 3 below. This is a local
   characterization, not a statement about concentration in global geometric
   regions or distance from layer boundaries.

The two quantitative growth questions are answered by these conclusions.
The separate qualitative localization question in source Problem 8.2 is
not claimed resolved. Accordingly this is proposed conservatively as one
`result-note`, with workflow `original_status=unresolved`.

## 1. Prior inputs and a three-case reformulation

Write the support as s_1>...>s_r>0, with multiplicities m_i, and s_{r+1}=0.
Set a_i=1[m_i=1] and b_i=1[s_i-s_{i+1}=1], with a_{r+1}=b_0=0. We use
the established formulas

    d = r(r-1)+A+B,
    A = #{i:s_i-s_{i+1}>1},  B = #{i:m_i>1},                 (1)
    delta = max({r+1-a_i-b_i:1<=i<=r}
                union {r-a_j-b_{j-1}:1<=j<=r+1}).           (2)

Formula (1) is Theorem 2.2 of Lyudogovskiy's *Degree theory*,
https://arxiv.org/html/2603.27248v1. Formula (2) is Theorem 7.1 of
*Local Morphology*, https://arxiv.org/html/2603.18696v1, and is reproduced
with these exact conventions in Background Proposition 3.1 of
https://arxiv.org/html/2606.20773v1. Full primary HTML copies of the
degree paper, synthesis, and original questions are in `evidence/external/`.
These formulas and the following elementary reformulation are prior input
or immediate consequences, not the claimed new contribution.

Call a partition H if some positive size x>=2 occurs at least twice while
x-1 is absent. This is precisely the condition that some i has a_i=b_i=0:
the next smaller size is then at most x-2, including the terminal zero.
Let S_r=(r,r-1,...,1), and put epsilon=delta-r. Equation (2) gives

    epsilon = -1  for S_r;
               1  for an H partition;
               0  otherwise.                              (3)

Indeed, row capacities lie between r-1 and r+1, and column capacities
are at most r. A row has capacity r+1 exactly in case H. If H fails,
all rows have capacity at most r; they are all r-1 exactly when all
a_i=b_i=1, which is exactly S_r. For S_r the first and last columns
have capacity r-1 and every other column has capacity r-2. In the remaining
case some row has capacity r. This proves (3), including r=1.

## 2. Two restrictions on support changes

For a legal move p -> p-1, q -> q+1, write U and V for the old and new
positive supports. Only p,q can disappear and only p-1,q+1 can appear;
zero is omitted. Therefore ||V|-|U||<=2. This recovers the support bound
already stated in the original source, Proposition 3.1.

**Lemma 1.** Every neighbor of S_r has strictly smaller support.

Proof. The case r=1 has no edge and is outside n>=2. In S_r all rows
are singletons, so p=q>0 is impossible. The case p=q+1 is an identity
and is excluded. If q=0, then p>=2; size p disappears and both outputs
p-1 and 1 were already in the support. If q>0, the distinct sizes p,q
both disappear: neither can be an output, since that would require the
excluded equality p=q+1. The only possible new size is r+1, from q=r.
At least two sizes are lost and at most one is gained. In both cases
the support strictly decreases. Coincident outputs p-1=q+1 can only
reduce the number of births. QED.

**Lemma 2.** If a move increases support by two, its starting partition is H.

Proof. The number of births is at most two, so a net increase of two
requires two distinct positive births and no death. In particular p>1,
p-1 was absent, and size p survives. Since the move removes a row of
size p and neither newborn size was previously present, an additional
row of size p existed. Thus m_p>=2 and p-1 was absent, proving H. If
p=q, two rows are removed and survival actually requires m_p>=3; the
same conclusion follows. If q=0, the birth q+1=1 is handled in exactly
the same argument. The cases p=1 and p-1=q+1 cannot have two distinct
positive births and hence cannot occur here. QED.

## 3. Universal dimension bound and equality edges

Orient an arbitrary edge lambda -> mu with r(mu)>=r(lambda), and let
k=r(mu)-r(lambda), so k is 0, 1, or 2. Write r=r(lambda), e=epsilon(lambda),
and f=epsilon(mu). The signed dimension difference is

    delta(mu)-delta(lambda) = k+f-e.                         (4)

If k=0, Lemma 1 excludes staircases at either endpoint, so e,f belong to
{0,1} and the difference has absolute value at most one.

If k=1, Lemma 1 excludes a staircase at the starting endpoint. Therefore
e belongs to {0,1} and f to {-1,0,1}; expression (4) lies in [-1,2].

If k=2, Lemma 2 gives e=1. Expression (4) is 1+f, which lies in [0,2].

Thus every edge has absolute dimension jump at most two. The same cases
give a necessary and sufficient condition for equality: with this support
orientation, either

    k=1, lambda is neither a staircase nor H, and mu is H;
or
    k=2, and both lambda and mu are H.                       (5)

There are no negative jumps of magnitude two under this orientation.
Thus maximal dimension jumps require a support increase, and (5) identifies
their endpoints solely from finite support and multiplicity data.

## 4. Sharpness and the finite exceptions

For n=11, the move 3 -> 2, 0 -> 1 gives

    (4,4,3) ~ (4,4,2,1),  with dimensions 2 and 4.

For n=14, the move 4 -> 3, 0 -> 1 gives

    (5,5,4) ~ (5,5,3,1),  with dimensions 2 and 4.

For every n>=15 put k=n-11>=4 and sort the two displayed multisets:

    (k,4,4,3) ~ (k,4,4,2,1).                               (6)

The same split of 3 gives a legal edge and preserves total n. If k=4,
the left endpoint has support {4,3}, is not H, and is not a staircase;
the right endpoint has support {4,2,1} and is H at size 4. Their dimensions
are 2 and 4. If k>=5, the supports have sizes 3 and 4; the left endpoint
is not H, since its only repeated size is 4 with predecessor 3 present,
while the right endpoint is H at 4. Their dimensions are 3 and 5. This
includes k=5, where the top gap is one, and every arbitrarily large k.

For every n>=4, the edge (n)~(n-1,1) has dimensions 1 and 2, giving the
lower bound one wherever the upper bound is not attained. The graphs at
n=2 and n=3 have, respectively, one edge and a three-vertex path, so all
local dimensions are one and both maxima are zero.

For the remaining finite upper bounds the following exact enumeration is
part of the evidence, not an extrapolation:

| n | number of vertices | number of edges | D_delta |
|---|---:|---:|---:|
| 2 | 2 | 1 | 0 |
| 3 | 3 | 2 | 0 |
| 4 | 5 | 5 | 1 |
| 5 | 7 | 9 | 1 |
| 6 | 11 | 17 | 1 |
| 7 | 15 | 28 | 1 |
| 8 | 22 | 47 | 1 |
| 9 | 30 | 73 | 1 |
| 10 | 42 | 114 | 1 |
| 11 | 56 | 170 | 2 |
| 12 | 77 | 253 | 1 |
| 13 | 101 | 365 | 1 |

`evidence/research_check.py` generates every partition in this range and
computes all edges by the padded row-coordinate criterion

    lambda~mu  iff  sum_i |lambda_i-mu_i|=2.                 (7)

To justify (7), a unit transfer changes an unsorted row list by L1 distance
two, and sorting cannot increase the minimal L1 matching distance. This
last assertion follows by repeatedly uncrossing a matching, using
|a-c|+|b-d| <= |a-d|+|b-c| for a<=b and c<=d. Two distinct integer vectors
of equal sum have L1 distance at least two. Conversely, distance two
between the sorted padded lists means one entry decreased by one and a
different entry increased by one, which is precisely a legal row transfer;
an increased zero entry is the allowed new row.

The script independently generates the same edges by multiplicity moves
and asserts equality with (7). For every vertex it then checks all subsets
of its neighborhood in descending size until finding a clique. Every
larger subset has therefore been tested and rejected. This determines the
actual local dimension without using (2). Partition generation recursively
chooses the next part no smaller than the previous one until the remaining
sum is zero; every nondecreasing positive partition occurs once. No symmetry
quotient or unexamined partition class is used. The serialized output
`evidence/research_check.json` includes all 371 vertices in this finite
range, their degrees, exact dimensions and clique witnesses. These finite
checks and (6) finish the exact formula for D_delta.

## 5. Degree estimate

Regard A as a function of the finite support, including its bottom gap to
zero. Inserting a new size x strictly between consecutive a>b>=0 replaces
the contribution 1[a-b>1] by

    1[a-x>1]+1[x-b>1].

Since a-x and x-b are positive integers and a-b>=2, the change is in
{-1,0,1}. Inserting above the maximum adds just 1[x-a>1], which is zero
or one. For an empty support insertion adds 1[x>1], also zero or one.
Deletion is the reverse operation. Thus inserting or deleting one support
size changes A by at most one, including both endpoints.

A transfer changes membership at at most four positive sizes, so
|A(mu)-A(lambda)|<=4, by inserting the new sizes and then deleting the
lost ones. The function B=sum_{x>=1}1[m_x>=2] also changes at at most
four sizes, and each indicator changes by at most one even when two rows
of the same size are affected. Hence |B(mu)-B(lambda)|<=4. Equation (1)
therefore yields the uniform edge estimate

    |d(mu)-d(lambda)
      - (r(mu)(r(mu)-1)-r(lambda)(r(lambda)-1))| <= 8.        (8)

In particular, support-neutral edges have degree jump at most eight.
Every partition of n has r<=s, since its distinct positive sizes alone
sum to at least T_r. For s>=4 and positive supports differing by at most
two, the greatest difference of r(r-1) is

    s(s-1)-(s-2)(s-3)=4s-6.

Combining this with (8) proves D_d(n)<=4s+2 for n>=10.

For the matching lower bound, write n=T_s+q, 0<=q<=s, and take

    mu     = (s+q,s-1,s-2,...,3,2,1),
    lambda = (s+q,s-1,s-2,...,4,3,3).                       (9)

The range s-1,...,4 is empty at s=4. Both partitions sum to n. Moving
the unit row of mu into its row of size 2 gives lambda, so they are
adjacent. At mu the support is s, B=0, and A=1[q>0]. At lambda the
support is s-2, the only repeated size is 3, and its bottom gap is 3;
therefore B=1 and A=1+1[q>0]. The degree difference is exactly

    s(s-1)-(s-2)(s-3)-2 = 4s-8.

This proves the two-sided bound for every n>=10. Finally s=sqrt(2n)+O(1)
follows directly from T_s<=n<T_{s+1}, proving the stated leading term.

## 6. Verification scope and gaps

The infinite bounds and witness families above have symbolic proofs.
Only the finitely many small dimension exceptions use exhaustive graph
computation. The additional range and structured tests in
`research_check.json` are adversarial regression evidence, not a replacement
for these proofs. They include equal donor/recipient sizes, vanished unit
donors, creation of new rows, coincident outputs, both triangular endpoints
of each sampled degree family, and large part sizes in (6).

Known mathematical gaps in the stated quantitative theorem: none identified
by this proposing pass. Fresh referee review is still required. Global
localization, sharp additive constants for degree growth, and a full exact
formula for D_d are not asserted. The three-case reformulation and all
imported vertex formulas must retain attribution. Current bounded literature
comparison and source-access limits are recorded in
`literature/research-screen.md`; absence of an equivalent search result does
not establish worldwide priority.
