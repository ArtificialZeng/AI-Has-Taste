# Precise problem and candidate enumeration scope

Job: primary-20260913-ascent-0120-0121-research-3f4c053fe3cf; 2026-09-13.
The verbatim original is `source.md`, which is immutable. Its SHA256 is
c3511d885d5d487049ba8d52247444c1e27c6005f320a593c5aa5ffbb7bfd48b.

For a finite integer word w=w_1...w_m, set
asc(w)=|{j: 1<=j<m and w_j<w_(j+1)}|, with asc(empty)=0.
For every n>=1, let A_n consist of the nonnegative integer words x of length n
such that x_1=0, x_i<=1+asc(x_1...x_(i-1)) for 2<=i<=n, and

    there do not exist i<j<k<l with x_i<x_j<x_k and x_l in {x_i,x_j}.

The last condition is exactly simultaneous classical subsequence avoidance
of 0120 and 0121, with equality preserved under reduction. Positions need
not be adjacent. Let A_0={empty}, a_n=|A_n| and F(z)=sum_{n>=0}a_n z^n.
Non-RGF ascent sequences and sequences containing 0132 or 021 remain in
scope; no extra pattern restriction has been introduced.

The frozen target is all-length enumeration, either a proved explicit
ordinary generating function or a comparably informative uniform structural
enumeration beyond exhaustive word generation. It assumes no rationality,
algebraicity, convergence, or particular scalar formula. Finite initial data
alone do not solve it.

## Primary comparison and limits

Liu, Kitaev and Zhang, Simultaneous avoidance of length-4 patterns in ascent
sequences, arXiv:2604.06735v1, Section 1/Table 1 and Section 6, expressly leave
this exact pair unenumerated. The definitions and the pair row were inspected
live again on 2026-09-13. Local source:
`literature/liu-kitaev-zhang-2604.06735v1.html`; the complete identical copy
bound for review is `evidence/external/liu-kitaev-zhang-2604.06735v1.html`.
Primary URL: https://arxiv.org/html/2604.06735v1 . Lemma 2.2's RGF hypothesis
prevents applying its shorter-pattern reductions to the whole present class.

The accessible primary preprint arXiv:2507.17947v1 by Mansour and Shattuck
was newly inspected for its definitions, scope, Table 1 and RGF comparison:
it enumerates classes with 021 additionally forbidden. Its checked class
containing the pair {021,0120} has 89 words of length 6; our class has 90.
The July 2026 Mansour paper on 0132 avoidance was not obtained in full.
Indexed excerpts and metadata are only leads, not checked theorems or a
complete overlap exclusion. See `literature/research-scope-screen.md` for
exact inspection coverage, failed retrievals and search limits. No worldwide
priority or exhaustive current-open-status claim is made.

The existing 659-record registry screen was read and remains evidence of a
bounded duplicate check; it was not rerun unchanged. It identifies this same
project and an unrelated lexical hit, not a second admitted copy.

## Proposed all-length theorem

For every K>=2 define

    D_K={(k,H): 2<=k<=K, empty!=H subset {0,...,k-2}}.

For s=(k,H), put m=min(H). For each rank t=0,...,k-1 define f(s,t) by

    t<=m: (k,H union {t});
    t>m:  r=|{h in H:h<t}|,
           (k+1-r, {h-r:h in H,h>=t} union {t-r}).

Let T_K(s,u)=|{t:f(s,t)=u}|, preserving repeated successors. Let b_K be the
row with entries 1 at (K,{h}), 0<=h<=K-2, and 0 elsewhere; let 1 be the
all-ones column. The proposed exact formal generating function is

    F(z)=(1-z)/(1-2z)
          +sum_{K>=2}(z/(1-z))^(2K-1) b_K(I-zT_K)^(-1)1.

Equivalently a_0=1 and, for all n>=1,

    a_n=2^(n-1)+sum_{K=2}^{floor((n+1)/2)}
                     sum_{d=0}^{n-2K+1}
                       binom(n-d-1,2K-2) b_K T_K^d 1.

Every matrix is explicitly defined without generating avoiding words. It
has 2^K-K-1 states, is independent of suffix length, and is closed because
eligible width cannot increase after the first nonbinary letter. Each
summand begins at degree 2K-1, so the infinite series is locally finite.
At fixed exit width the arbitrary-length continuation series is rational.
A proved coefficient algorithm uses O(N L 2^L+N^3) integer additions for all
lengths through N, where L=floor((N+1)/2), rather than enumerating all words.
This is an arithmetic-operation bound, not a unit-bit-cost claim.

The intended resolution scope is the original uniform structural enumeration
alternative, with the displayed generating series as an additional exact
expression. It does not assert a simpler scalar closed form or an analytic
classification. Whether this meets the original informative-enumeration
standard and has a publishable contribution is explicitly submitted to a
fresh referee; no acceptance is asserted here.

## Proof and exact verification

`evidence/quotient-enumeration-proof.md` supplies the complete induction.
For a postbinary prefix w, its exact banned set is {0} together with the
positive values having a larger value later. The last letter is the least
seen eligible letter. Also max(w)<=asc(w), so the top eligible letter is
unseen. The append rule deletes precisely the seen lower eligible ranks;
an ascent adds one new unseen largest value. This proves the quotient Q
uniformly and sharpens its domain by excluding a seen top rank. The binary
boundary is (a+1,{v-2}) for a prefix with a ascents and first nonbinary letter
2<=v<=a+1. Alternating-run decomposition gives binary-prefix weight
z^(2a)/(1-z)^(2a+1), proving the series and coefficient formula.

The new exact test compares the quotient with increasing-pair/banned-letter
states through prefix length 15, including all binary transitions, and
confirms totals through length 16. At length 15 it checks 16575 exact states
representing 2359338 words. A separate binomial/matrix assembly agrees with
the mixed quotient DP through length 28. Structured initialization checks
reach width 32; 40 deterministic-seed stress walks have 160 steps each;
small rational continuation systems are checked symbolically for K=2,3,4.
Code and results: `evidence/quotient_enumeration_test.py` and
`evidence/quotient-enumeration-results.json`. These computations support,
but do not replace, the all-length proof.

Counts a_0,...,a_16 are
1,1,2,5,13,34,90,244,683,1980,5945,18470,59306,196547,671306,2359338,8519890.
The raw exact-state reference confirms the full displayed range. Previously
only the proposed automaton supplied the values at lengths 13--16.

## Obstacles and next test

No mathematical gap in the displayed enumeration is presently identified
by the proposer. Independent proof review has not occurred. Full-text overlap
with the later 0132 paper and changes in the journal version of the 021 paper
remain unverified; priority language must stay bounded. The earlier literal
append-choice collision only rejects reconstruction from five elementary
statistics, and is not used as an unlabeled-tree obstruction.

One next test: a fresh referee audit of the exact matrix enumeration, checking
the quotient induction, binary weights and original-scope sufficiency, with
an explicit decision on the remaining later-literature comparison limit.
