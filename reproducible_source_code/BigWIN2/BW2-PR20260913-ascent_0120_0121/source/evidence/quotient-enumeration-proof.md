# A finite-width enumeration of simultaneous 0120/0121 avoidance

Proposer job: primary-20260913-ascent-0120-0121-research-3f4c053fe3cf.
Date: 2026-09-13. Research proof dossier; no independent acceptance is asserted.
The object and all-length target are exactly those in `../source.md` and
`../problem.md`. All generating functions below are formal power series.

## Statement

Let A_n be the ascent sequences avoiding both classical patterns 0120 and 0121,
including A_0={empty}, and let F(z)=sum_{n>=0}|A_n|z^n. Define

    D_K = {(k,H): 2<=k<=K, empty != H subset {0,...,k-2}}

for every K>=2. Its size is 2^K-K-1. For s=(k,H), put m=min(H) and define one
successor f(s,t) for each integer t with 0<=t<k as follows:

    t<=m: f(s,t) = (k, H union {t});
    t>m:  r=|H intersect {0,...,t-1}|,
           f(s,t) = (k+1-r, {h-r: h in H, h>=t} union {t-r}).

Let T_K be the integer matrix indexed by D_K whose (s,u) entry is the number
of t giving f(s,t)=u. Thus repeated successors have their full multiplicity.
Let 1 denote the all-ones column and let b_K be the row with value 1 on
(K,{h}), 0<=h<=K-2, and 0 elsewhere. Then

    F(z) = (1-z)/(1-2z)
           + sum_{K>=2} (z/(1-z))^(2K-1) b_K (I-z T_K)^(-1) 1.       (1)

Every matrix and every entry in (1) is given explicitly by finite integer
operations on K. The summand for K has order at least 2K-1. Consequently (1)
is well-defined in Z[[z]], and K<=floor((N+1)/2) suffices to recover all
coefficients through z^N. This is an all-length structural enumeration, not a
claim that F is rational or algebraic or converges at a nonzero complex z.

## Exact append criterion

For a nonempty avoiding prefix w, write a=asc(w), l=last(w), S=the set of
its letters, and

    B(w) = union of {w_i,w_j} over i<j<k with w_i<w_j<w_k.

Appending v creates a forbidden pattern precisely when an increasing triple
already in w has v as one of its two lower values. Hence wv is an avoiding
ascent sequence if and only if 0<=v<=a+1 and v not in B(w). Put

    E(w)={0,...,a+1} minus B(w).

Two elementary ascent-sequence facts will be used. First, max(w)<=asc(w).
This holds for w=0. Inductively, if the next entry v<=a it stays true, and
if v=a+1, then v exceeds the previous maximum, makes an ascent and equals
the new ascent count. Second, before the first letter >=2, a 1 has already
occurred: the first nonzero letter must be 1 because a prefix of zeros has
ascent count zero. These observations do not require pattern avoidance.

## Banned letters and the last letter

For every ascent sequence w containing a letter >=2, one has

    B(w) = {0} union {u>0: some occurrence of u has a larger letter later}. (2)

Indeed, the first letter >=2 has earlier letters 0 and 1, so an increasing
triple bans 0. Any positive u in the right-hand side occurs in a triple
(0,u,v), since the initial 0 lies before that positive occurrence. Conversely,
each positive endpoint of an increasing triple has a larger letter later.
This proves both inclusions of (2). If w is binary, B(w) is empty instead.

For an avoiding w, its final value l cannot belong to B(w): a triple banning
l has third value larger than l, and therefore ends strictly before the last
position, which would complete a forbidden pattern. If w is postbinary,
l>0 by (2). Every previously seen value u<l belongs to B(w), by (2) for
u>0 and directly for u=0. Therefore

    l = min(S intersect E(w)).                                          (3)

In particular this intersection is nonempty. Since max(w)<=a, the largest
eligible letter a+1 is unseen. Thus if E(w) is increasingly ranked starting
at zero, its size k is at least 2 and its seen-rank set H is a nonempty
subset of {0,...,k-2}. Equation (3) says that the rank of the final value is
min(H). This also explains the smaller state domain used in the statement.

## Proof of the quotient and its closure

Let w be a postbinary avoiding prefix and append its eligible letter of rank
t, with numerical value v. By (2),

    B(wv)=B(w) union {u in S: u<v}.                                    (4)

The possible u=0 in this display is already banned, so it introduces no
exception. The new entry v itself is not in B(wv). Previously unseen
values are not banned by this append.

If t<=min(H), then v<=l and there is no new ascent. No previously seen
eligible value is below v, so (4) does not change E. The child label is
(k,H union {t}), as asserted. Its smallest seen rank is t, the final rank.

If t>min(H), then v>l, so the ascent count increases by one. Exactly the r
seen eligible values of ranks below t are removed from E. In addition, the
new upper bound a+2 supplies one new, unseen eligible value, larger than
every old eligible value. Hence the child width is k+1-r. Every surviving
old rank h>=t shifts down by r; the appended letter has rank t-r. This gives
exactly the second rule. Its smallest seen rank is again the appended rank.
Here r>=1, so width cannot increase.

The stated domain is closed under these rules, even for labels considered
abstractly. In the second branch r<=t<=k-1, so k+1-r>=2. Every retained
seen rank is below the new largest rank k-r, since an old seen h<=k-2
and t<=k-1. In the first branch t<=min(H)<=k-2, so closure is immediate.
Thus f(s,t) lies in D_K whenever s lies in D_K.

Each rank t corresponds to exactly one eligible numerical letter of w.
The preceding calculation proves agreement of successor multisets, not just
sets. Induction on suffix length therefore proves that the number of legal
suffixes of length d depends only on (k,H) and equals

    c_s(d)=(T_K^d 1)_s,  whenever s in D_K.                            (5)

For d=0 both sides equal one. The induction step sums over all k append
choices. This also proves that enlarging K does not change a continuation
series of a previously included state: widths cannot increase.

The proof uses the actual numerical ascent bound throughout, so it includes
non-RGF sequences and sequences containing 0132. No shorter-pattern or
restricted-growth reduction is used.

## Binary boundary and assembly

Every word has a unique maximal initial binary prefix. If the whole word is
binary, it avoids the two patterns and is automatically an ascent sequence
when it starts with 0. There are 2^(n-1) such words of length n>=1. With the
empty word, their generating function is (1-z)/(1-2z).

Now let a binary prefix p have exactly a>=1 ascents, and append the first
nonbinary value v, where 2<=v<=a+1. The append is legal, adds one ascent,
and bans precisely 0 and 1. Its eligible set is {2,...,a+2}; only v has
been seen in that set. Thus its label is

    (a+1,{v-2}).                                                       (6)

Putting K=a+1, every singleton (K,{h}) with 0<=h<=K-2 occurs exactly once
among the nonbinary choices for this fixed prefix. There is no exit when
a=0.

To count binary prefixes with a>=1 ascents, decompose into constant runs.
Those ending in 1 have exactly 2a nonempty alternating runs starting in 0;
those ending in 0 have exactly 2a+1. For q=z/(1-z), their combined series is

    B_a(z)=q^(2a)+q^(2a+1)=z^(2a)/(1-z)^(2a+1).                        (7)

The extra nonbinary entry contributes z. Its continuation series, including
the empty suffix, is (I-z T_K)^(-1)1 by (5). Multiplying (7) by z and summing
over the K-1 possible singleton labels gives the summand of (1), since
z B_(K-1)(z)=q^(2K-1). The maximal binary prefix and its first nonbinary
letter are unique, so there is neither overlap nor omission. This proves (1).

The inverse in (1) exists formally because I-zT_K has identity constant term.
It has rational-function entries over Q. The minimum binary-prefix length
with K-1 ascents is 2K-2, attained by (01)^(K-1); the exit costs one more
letter. This proves the claimed local finiteness and coefficient cutoff.

Equivalently, for every n>=1, (1) gives the entirely finite coefficient formula

    |A_n| = 2^(n-1)
      + sum_{K=2}^{floor((n+1)/2)} sum_{d=0}^{n-2K+1}
          binom(n-d-1,2K-2) b_K T_K^d 1,                             (8)

with |A_0|=1. Indeed, the coefficient of z^(n-d) in
(z/(1-z))^(2K-1) is exactly binom(n-d-1,2K-2) in this range.

## Concrete enumerative value

For K=2, D_2 contains only (2,{0}), with two self transitions, so

    b_2(I-zT_2)^(-1)1 = 1/(1-2z).

For K=3, write c_0,c_1,c_01 for continuations from (3,{0}), (3,{1}),
(3,{0,1}), and c_2=1/(1-2z). The full finite system is

    c_0 = 1+z(2c_0+c_1),
    c_1 = 1+z(2c_1+c_01),
    c_01= 1+z(c_01+c_0+c_2).

These equations illustrate both multiplicities and transitions to smaller
width. In particular they give the exact rational function

    b_3(I-zT_3)^(-1)1
      = (2-8z+12z^2-7z^3)/((1-2z)(1-5z+8z^2-5z^3)).

Further blocks are specified without generating any avoiding words. Formula
(1) begins with the coefficients for n=0,...,16

    1,1,2,5,13,34,90,244,683,1980,5945,18470,59306,
    196547,671306,2359338,8519890.

These coefficients were also obtained from an exact recurrence retaining all
increasing pairs, independent of the simplified banned-set identity. The
coefficient and symbolic checks are in `quotient-enumeration-results.json`.

For all coefficients through degree N let L=floor((N+1)/2). Only 2^L-L-1
postbinary labels are ever needed. Precompute their at-most-L outgoing edges,
then use the successor recurrence together with the binary states (a,last)
at each length. There are O(N) binary states at a given level; their exits
are given by (6). At most O(N L 2^L + N^3) integer additions suffice, with
O(2^L+N) live counting values after the edge list has been constructed.
This is an arithmetic-operation bound, not a bit-complexity bound; it does
not assume that the integers counted have bounded size. The finite matrices
also provide rational continuation series for suffixes of arbitrary length
at every fixed exit width. These are substantive advantages over generating
all avoiding words or retaining their sets of increasing pairs.

Every label (K,H) in the top block is actually realizable: use the binary
prefix (01)^(K-1), exit with value max(H)+2, and append the other desired
eligible ranks in decreasing order. These nonascending appends do not alter
the eligible set. This verifies that the set-state domain has a structural
interpretation; no claim of minimality under unlabeled tree equivalence is
made.

## Dependencies and gap list

The mathematical argument depends only on the definitions frozen in
`source.md` and `problem.md`, elementary finite-word reasoning, and the
formal identity (I-zT)^(-1)=sum_{d>=0}z^d T^d. There is no external theorem
used to infer the enumeration. The local primary source supplies the problem
and the April 2026 open-status comparison, not any step of this proof.

Known mathematical gaps in (1) and the quotient proof: none identified by
the proposer. This is not a fresh referee's conclusion. Numerical test
coverage, literature overlap limits, and the eventual proposed scope are
recorded separately. In particular no assertion about a simpler scalar
closed form, analytic growth, rationality or algebraicity of F is made.
