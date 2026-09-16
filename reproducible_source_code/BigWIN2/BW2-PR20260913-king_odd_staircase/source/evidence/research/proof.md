# Uniform mex-transfer proof submitted for review

Proposer: primary-20260913-king-odd-staircase-research-fd17b876b830.
This is a mathematical evidence dossier, not an accepted manuscript. The
argument below proposes a proof of the exact frozen original claim. No fresh
referee has checked it. Mathematical gap list: **none known**. Current
openness and priority remain unverified because the later SSRN full text has
not been compared.

## Statement and dependencies

Fix a positive odd integer r. Write
D_k=((kr)^r,((k-1)r)^r,...,r^r), for every positive integer k, where
exponents mean repetition. A King option of a nonempty partition lambda is
lambda[0,1], lambda[1,0], or lambda[1,1], provided the destination is
nonempty. G is the normal-play mex value, with mex(empty set)=0.

We prove the following stronger boundary assertion. Put

    p=r+2,  t=1+((k-1) mod p),  h=floor((k-1)/p) mod 2,
    L=p-t,  x=L mod 2=(t+1) mod 2,  y=1-x=t mod 2,
    a=3-h,  b=2+h.

For 0<=j<r, define W_k(j) by

    W_k(0)=2 if L=0;
    W_k(j)=x (j even), a (j odd), if j<L;
    W_k(j)=b (j even), y (j odd), if j>=L,

where the first rule has priority. Then G(D_k[0,j])=W_k(j).
At j=0 this is precisely Conjecture 5.1 in source.md: if
q=k mod(r+2), the root value is 2 for q=0, 0 for odd q,
and 1 for positive even q. No parameter restrictions beyond the original
ones have been added.

Dependencies are the elementary mex recurrence, composition of partition
deletions, and the rectangle base calculation proved below. The local primary
source evidence/external/gkm-2501.14640v1.html identifies the original
conjecture and the known special cases; no assertion about a later version
is used in the mathematical proof. Computation is corroboration only.

## 1. A symmetric grid satisfying the mex recurrence

For any integer L>=0 and either (a,b)=(3,2) or (2,3), let
x=L mod 2 and y=1-x. For nonnegative integers i,j set
m=min(i,j), n=max(i,j), and define F(i,j) by the following three tables.
Rows are the parity of m (even, odd); columns are the parity of n
(even, odd). Override all tables with F(L,L)=2.

| Region | table |
|---|---|
| n<L | P = [[x,a],[b,y]] |
| m<=L<=n | C = [[b,y],[x,a]] |
| L<m | T = [[y,b],[a,x]] |

These regions partition the domain apart from the explicitly overridden
point. We claim, for every i,j>=0,

    F(i,j)=mex{F(i+1,j),F(i,j+1),F(i+1,j+1)}.       (1)

This is an identity of an explicitly defined infinite array, not an induction
on an infinite game. We prove it by the following exhaustive local cases.
Symmetry permits i<=j. Write the ordered successor triple as (down,right,
diagonal); duplicate values have no effect on mex.

In a P region where all four cells use P, the off-diagonal cases are

| i parity | j parity | value | successor triple |
|---|---|---|---|
| even | even | x | (b,a,y) |
| even | odd | a | (y,x,b) |
| odd | even | b | (x,y,a) |
| odd | odd | y | (a,b,x) |

For i=j even the value/triple are x/(a,a,y); for i=j odd they
are y/(b,b,x). These identities follow because {x,y}={0,1} and
{a,b}={2,3}. The same verification applies to T after exchanging
x with y and a with b. In a C region where all four cells use C,
the 2-by-2 pattern contains all four values 0,1,2,3, so the other
three values have mex equal to the current value.

Here are all remaining off-diagonal cases. A displayed case is used only
when its coordinate inequalities are feasible.

| Location | L parity | other parity | value | successor triple |
|---|---|---|---|---|
| j=L-1, i<j | even | i even | a | (1,b,0) |
| j=L-1, i<j | even | i odd | 1 | (a,0,b) |
| j=L-1, i<j | odd | i even | 1 | (b,0,a) |
| j=L-1, i<j | odd | i odd | b | (1,a,0) |
| i=L-1, j=L | even | — | 0 | (2,a,1) |
| i=L-1, j=L | odd | — | 0 | (2,b,1) |
| i=L, j>L | even | j odd | 1 | (0,b,a) |
| i=L, j>L | even | j even | b | (a,1,0) |
| i=L, j>L | odd | j even | 1 | (0,a,b) |
| i=L, j>L | odd | j odd | a | (b,1,0) |

The two remaining diagonal cases are

| Location | value | successor triple |
|---|---|---|
| i=j=L-1 (L>=1) | 1 | (0,0,2) |
| i=j=L | 2 | (1,1,0) |

Every row gives the asserted mex for both choices of (a,b). For completeness,
if i<j and j<=L-2 all four cells use P. If j=L-1 use the first
four exceptional rows. If j=L and i<=L-2 all four cells use C;
the one remaining case is (L-1,L). If j>L, then i<L gives four C
cells, i=L is the horizontal seam, and i>L gives four T cells.
For i=j, only L-1 and L depart from the ordinary P or T diagonal.
This covers L=0 and L=1 as well, simply omitting impossible cases.
Thus (1) holds with no bound on L,i,j.

## 2. Exact square transfer

D_k is self-conjugate. Exchanging rows and columns preserves the King
moves, hence preserves G. Write B_k(j)=G(D_k[0,j]) for 0<=j<r.
Deleting complete blocks gives

    D_k[r,0]=D_k[0,r]=D_(k-1)  (k>=2),
    D_k[r,r]=D_(k-2)            (k>=3).

These are identities of shapes, not assertions that a block deletion is a
single legal move. At k=2 the second destination is empty. Composition of
deletions and conjugate invariance therefore give the south and east edges
of the first square:

    A_k(r,j)=A_k(j,r)=B_(k-1)(j),   0<=j<r,
    A_k(r,r)=B_(k-2)(0)            if k>=3.

The corner is absent for k=2. Every cell A_k(i,j) with 0<=i,j<r
exists, and its legal successors are its right, down, and diagonal neighbors
in this square with these edges, omitting the absent corner. Backward
induction on i+j uniquely determines the square from the edges. Consequently
any proposed values with the correct edges and the correct mex at every
interior cell are the actual SG values. No zero value is assigned to an
empty board.

## 3. Base case k=1

For a rectangle with positive side lengths u,v the mex recurrence gives

    R(u,v)=0 if both sides are odd;
           2 if both are even;
           1 if the parities differ and min(u,v) is odd;
           3 if the parities differ and min(u,v) is even.

Here is an elementary verification (the source also states this as Theorem
3.8). A side of length 1 gives the alternating path values 0,1. For both
sides at least 2 use induction on u+v and assume u>=v by symmetry.
If u>v and both are odd the option set is {1,2,3}; if both are even
it is {0,1,3}. For odd u and even v it is {0,1,2}; for even u
and odd v it is {0,2,3}. For u=v odd the option set is {2,3},
and for u=v even it is {0,1}. Each mex is the displayed value.

Now D_1[0,j] is the r-by-(r-j) rectangle. For even j its value is
0. For odd j its smaller side is even, so its value is 3. This is
W_1 because L=r+1, x=0, a=3. This base uses the rectangle calculation;
the grid F is not asserted to describe the interior at k=1.

## 4. Induction and the missing corner

Suppose k>=2 and all preceding boundary assertions hold. Use the parameters
t,h,L,x,y,a,b for k, and the array F from Section 1. We show that F
gives every interior cell A_k(i,j), 0<=i,j<r.

First let 2<=t<=p. The preceding phase has t'=t-1 with the same h,
threshold L+1, and reversed x,y. Its root is not the special t'=p
case. Since r is odd, substitution into F gives, for 0<=s<r,

    F(r,s)=F(s,r)= y if s<=L and s even,
                        a if s<=L and s odd,
                        b if s>L and s even,
                        x if s>L and s odd.

This is exactly W_(k-1)(s), since s<=L means s<L+1. If t>=3,
then L<r and F(r,r)=x, from T's odd-odd entry. The parameter of
k-2 is t-2>=1, so W_(k-2)(0)=(t-1) mod 2=x, as required.
If t=2 then L=r and F(r,r)=2. When k>2, the parameter for k-2
is p, so the actual corner also has value 2. In all these cases the
whole prescribed boundary agrees with F, and (1) proves the induction step.

At k=2, t=2 and L=r, the actual corner is absent. Only the interior
cell (r-1,r-1) has this corner as an option. Its two other options
both have value W_1(r-1)=0, because r-1 is even. Its proposed value
is x=1. Omitting the fictitious value 2 changes the option set from
{0,2} to {0}; both have mex 1. All other interior identities remain
unchanged. Thus the actual absent corner is handled, including r=1.

## 5. Both phase wraparounds

It remains to consider t=1 with k>1. Then k=ell*p+1 for ell>=1,
L=r+1 is even, x=0,y=1, and h=ell mod 2. Every point in
[0,r]^2 uses P. The preceding boundary is at t'=p with phase
1-h; its tail high value is a. Therefore its entries with s>0 are
a for even s and 1 for odd s. These agree with F(r,s). At s=0
the actual preceding root is always 2, while F(r,0)=F(0,r)=a.
Also F(r,r)=1, which matches the preceding-previous root: its parameter
is p-1, a positive even integer.

For h=1, a=2, so the entire prescribed boundary already agrees with F.
For h=0, a=3 and b=2. Replace the two boundary entries (r,0)
and (0,r) by 2. When r>=3, these changes affect only the respective
interior cells (r-1,0) and (0,r-1). At (0,r-1), F is 0 and
the three successor values after replacement are 2,2,1. Their mex
remains 0; symmetry gives the other cell. When r=1 the two affected
interior cells coincide at (0,0); its options are 2,2,1 again, with
mex 0. Thus the wraparound step works for both phases and all odd r.

## 6. Conclusion and scope

Backward uniqueness in the square transfer now proves

    G(D_k[i,j])=F(i,j) for every k>=2 and 0<=i,j<r.

At i=0, the three region rules and the override F(L,L)=2 give
exactly W_k(j). Together with k=1, this completes induction on all
positive k. Taking j=0 proves the exact universal formula frozen in
source.md for every positive odd r.

The extra full-square formula is useful proof structure, not a separate
publication target. Its boundary agrees with the formula frozen in triage;
no observed counterexample was removed by narrowing the original claim.
The old period-r+2 assertion for the entire boundary remains false.

The proof has no computational premise: the finite tests in verify.py
check transcription, the exhaustive seam table, both wraparounds, the r=1
degeneracy, and the k=2 omission. They do not replace the exhaustive argument
in Section 1 or the induction. This is a proposer-side proof candidate;
fresh mathematical review and a satisfactory bounded literature assessment
are still required before any publication decision.
