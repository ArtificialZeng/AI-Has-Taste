# Proof candidate: the Ehrhart–word identity for every arbor

2026-09-14. Proposer job:
`primary-20260914-arbor-ehrhart-words-research-9e9070b093b6`.
This is a complete proposed argument for a fresh referee, not an acceptance
report or publication manuscript. It checks and completes the derivation in
`evidence/triage-transform.md`.

## Exact statement

Let n>=1. Let the vertices of a finite rooted tree be the nonempty blocks
B_v of any partition of [n]. For each vertex v let D_v be the union of all
blocks in its descendant subtree, including B_v, and put N_v=|D_v|,
b_v=|B_v|. Define
\[
 Q_\tau=\{x\in\mathbb R_{\ge0}^n:
                 \sum_{i\in D_v}x_i\le N_v\text{ for every }v\}.
\]
Let W_tau be the length-n words on [n] such that at least N_v letters,
counting occurrences, belong to D_v for every v. For
\(d(w)=|\{j:1\le j<n,\ w_j\le w_{j+1}\}|\), the claim is
\[
 \sum_{m\ge0}|mQ_\tau\cap\mathbb Z^n|t^m
       =\frac{\sum_{w\in W_\tau}t^{d(w)}}{(1-t)^{n+1}}. \tag{T}
\]
Since d(w)=n-1-des(w), this is precisely the immutable source statement,
with no restrictions on labels, block sizes, height, or branching.

All generating-series calculations below are formal. All binomial upper
arguments in the enumeration are nonnegative integers, and binomial
coefficients outside their usual range are zero.

## A local polynomial identity

For b>=1 and K>=0, let T_{>=b} delete terms of degree below b. Then
\[
 y^b\sum_{q=0}^{K}\binom{q+b-1}{b-1}(1+y)^{K-q}
             =T_{\ge b}(1+y)^{K+b}. \tag{L}
\]
Both sides have zero coefficients below b and above K+b. At degree b+j,
0<=j<=K, the left coefficient is
\[
 \sum_{q=0}^{K-j}\binom{q+b-1}{b-1}\binom{K-q}{j}
 = [z^{K-j}](1-z)^{-b}(1-z)^{-j-1}
 = \binom{K+b}{b+j}.
\]
For the first equality to the coefficient expression, write
K-q=j+(K-j-q) and use the binomial series for each factor. This proves
(L), including K=0, when both sides are y^b. No limiting argument is used.

Here is the exact operator form needed for the induction. Fix m>=0 and
N>=b>=1, and let R(x)=sum_s r_s x^s be any polynomial of degree at most
m(N-b); its coefficients need not be positive. Define
\[
 H(x)=T_{\le mN}\bigl((1-x)^{-b}R(x)\bigr).
\]
Then
\[
 y^N(1+y)^{mN}H((1+y)^{-1})
 =T_{\ge N}\left(y^{N-b}(1+y)^{mN+b}R((1+y)^{-1})\right). \tag{O}
\]
Indeed, for each s in R, put K=mN-s. The degree hypothesis gives
K>=mb>=0. Its contribution to the left side is
\[
 r_s y^N\sum_{q=0}^{K}\binom{q+b-1}{b-1}(1+y)^{K-q}
 =r_s y^{N-b}T_{\ge b}(1+y)^{K+b}
\]
by (L). Sum over s and use the polynomial identity
\(y^{N-b}T_{\ge b}P=T_{\ge N}(y^{N-b}P)\).
Every expression being truncated is an ordinary polynomial: in particular,
K+b>=b. This establishes (O) without commuting an invalid rational
truncation or substituting into an untruncated infinite series.

## Subtree enumeration and induction

Fix any integer m>=0. For each vertex v, let F_v(x) enumerate vectors
\(z\in\mathbb Z_{\ge0}^{D_v}\), weighted by \(x^{\sum_i z_i}\),
that satisfy
\(\sum_{i\in D_u}z_i\le mN_u\) for every descendant u of v,
including v. These are finite sets, and deg F_v<=mN_v. If C(v) is the
set of children of v, independence on the disjoint sets
\(B_v\) and \(D_c\), c in C(v), gives
\[
 F_v(x)=T_{\le mN_v}\left((1-x)^{-b_v}
                              \prod_{c\in C(v)}F_c(x)\right). \tag{F}
\]
The factor (1-x)^(-b_v) counts unrestricted nonnegative vectors on the
block B_v; its coefficient of x^q is binom(q+b_v-1,b_v-1).
The truncation imposes exactly the additional inequality at v. At the
root r, \(F_r(1)=|mQ_\tau\cap\mathbb Z^n|\), including m=0.

Independently, let G_v(y) enumerate vectors
\(a\in\{0,\ldots,m+1\}^{D_v}\), weighted by
\(y^{\sum_i a_i}\prod_{i\in D_v}\binom{m+1}{a_i}\),
that satisfy \(\sum_{i\in D_u}a_i\ge N_u\) at every descendant u of v.
The binomial theorem and the same disjoint decomposition give
\[
 G_v(y)=T_{\ge N_v}\left((1+y)^{(m+1)b_v}
                              \prod_{c\in C(v)}G_c(y)\right). \tag{G}
\]
This definition does not use F_v or any preorder-duality theorem.

We claim, for every vertex v,
\[
 G_v(y)=y^{N_v}(1+y)^{mN_v}F_v((1+y)^{-1}). \tag{I}
\]
Induct from the leaves toward the root. Write N=N_v, b=b_v, and
R(x)=product_c F_c(x). For a leaf the product is 1. In all cases
\(\sum_cN_c=N-b\) and \(\deg R\le m(N-b)\).
Using the child identities (an empty family for a leaf) gives
\[
 (1+y)^{(m+1)b}\prod_cG_c(y)
    =y^{N-b}(1+y)^{mN+b}R((1+y)^{-1}).
\]
Apply T_{>=N} and then (O). The result is (I), because (F) is the
polynomial H in (O). This is a genuine subtree induction: the only
instances assumed are those at proper child subtrees.

Let
\[
 A_\tau=\{a\in\mathbb Z_{\ge0}^n:|a|=n,
                        \sum_{i\in D_v}a_i\ge N_v\text{ for every }v\}.
\]
Taking the coefficient of y^n in (I) at the root gives
\[
 |mQ_\tau\cap\mathbb Z^n|=F_r(1)=[y^n]G_r(y)
                 =\sum_{a\in A_\tau}\prod_{i=1}^n\binom{m+1}{a_i}.
                                                               \tag{B}
\]
The coefficient after removing y^n on the right of (I) is its constant
term, obtained by setting y=0 in the polynomial factor; it is F_r(1).
Terms with a_i>m+1 have zero weight, which justifies extending the sum
from the defining finite box of G_r to all of A_tau.

## Explicit word bijection

Fix a in A_tau and m>=0. For each i in [n], choose a subset S_i of the
m+1 ordered boxes {0,...,m} of cardinality a_i. In box k place the letters
i such that k belongs to S_i, in strictly decreasing numerical order.
Separate consecutive boxes by one bar and read the resulting sequence.
Empty boxes are retained: they correspond to initial, final, or adjacent
bars. There are n letters and exactly m bars.

This construction is a bijection between the subset choices and barred
words of content a in which each box is strictly decreasing. Its inverse
splits at the bars, indexes the resulting m+1 boxes from 0, and records
the box indices containing each letter. Strict decrease ensures that a
letter occurs at most once in each box, so the inverse yields subsets.

For an unbarred word w of content a, a bar is required in precisely each
internal gap j for which w_j<=w_{j+1}. A barred word has decreasing boxes
if and only if every such gap has at least one bar. Necessity is immediate;
for sufficiency, every adjacent pair within a box is strictly decreasing,
which forces the entire box to be strictly decreasing and repetition-free.
There are d(w) required gaps. Removing one bar from each of them leaves
m-d(w) indistinguishable bars distributed freely over all n+1 gaps,
including both ends. Hence the number of barred words above w is zero
for m<d(w), and otherwise is
\[
                         \binom{m-d(w)+n}{n}. \tag{W}
\]
Thus the product in (B) is the sum of (W) over words of content a.
Moreover
\[
 \sum_{m\ge d(w)}\binom{m-d(w)+n}{n}t^m
                  =\frac{t^{d(w)}}{(1-t)^{n+1}}.
\]
Summing over the finite set A_tau proves (T), since its words are exactly
W_tau by the definitions. This completes the proposed proof of the full
original claim.

## Boundary and dependency audit

- n=1: Q=[0,1], L(m)=m+1, and W contains the single word 1.
- m=0: F_v=1 and G_v=y^{N_v}; on the word side only the unique fully
  decreasing word n,...,1 contributes at degree zero. Its content is all
  ones, so it satisfies every subtree lower bound.
- A leaf may have b_v>1; (L) applies with N=b_v and K=mb_v. No
  singleton-leaf assumption occurs.
- Arbitrary many children are allowed; no order of the children or of the
  blocks is used. Actual numerical letter order enters only when reading
  boxes, so arbitrary interleaved labels are covered.
- Equal letters force a separating bar. Leading/trailing and multiple
  adjacent bars are included in the n+1 gaps in (W).
- The polytope contains [0,1]^n and is full dimensional. The proof directly
  establishes its displayed counting series; it does not require a
  triangulation, a cited h-star formula, or integrality as an unproved step.
  Its known lattice-polytope status is also proved in Chapoton, Lemma 1.2.
- Essential structural hypothesis: proper child descendant sets are
  disjoint and partition D_v minus B_v. Arbitrary preorders do not have
  this decomposition. This proof makes no all-preorder claim.
- Dependencies: elementary binomial-series identities, disjoint product
  enumeration, finite rooted-tree induction, and the explicitly invertible
  box/word construction. No computer computation is a logical dependency.

Known mathematical gap list: empty after the proposer's symbolic check.
Fresh referee verification of (L), (O), (I), the bijection, and full scope
is still required. Literature novelty is bounded to the sources and searches
recorded in `literature/research-verification.md`.
