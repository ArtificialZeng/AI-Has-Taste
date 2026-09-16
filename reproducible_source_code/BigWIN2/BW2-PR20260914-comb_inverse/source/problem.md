# Precise problem

Frozen original: `source.md`, SHA-256
`43669ff2a9b8b7c472001ccd2e726fe69f54a96d58bb34957d636160c09bcfce`.
This is the supplied transcription of the final unnumbered proposal in
[Athanasiadis--Chapoton, Section 9.6](https://arxiv.org/html/2605.26916v1#S9.SS6).
Live text and version history inspected 2026-09-14 Asia/Shanghai.

For each integer n>=0, let tau_0 be empty and let tau_(n+1) be formed by
adjoining a disjoint singleton to tau_n, then a new element smaller than all
existing elements. Equivalently, tau_n has distinct vertices
r_1,...,r_n,s_1,...,s_n with covering relations r_i<r_(i+1) for i<n and
r_i<s_i for i<=n. These generate all comparabilities by transitivity;
the spine is indexed from its minimum.

A lower ideal I is a subset such that v in I and u<=v imply u in I.
For every n define

    Q_n = {a in R_(>=0)^(2n): sum_(v in I) a_v <= |I|
           for every lower ideal I of tau_n},
    h_n(t) = sum_(a in Q_n intersect Z^(2n)) t^|{v:a_v>0}|.

The empty-dimensional polytope has one lattice point, so h_0(t)=1.
The whole ground set is an ideal, hence all coordinates sum to at most 2n
and the enumeration is finite. This is the raw support polynomial, distinct
from the Ehrhart h-star polynomial.

Let t be an indeterminate and work in Q(t)[[x]]. Define

    F(t,x) = sum_(n>=0) t^(-n) h_n(t) x^(n+1),
    R(t,x) = sum_(m>=1) (-1)^(m-1)
      [1+(1+t)^m t^(1-m) sum_(j=0)^(m-2) t^j] x^m.

The inner sum for m=1 is empty, equal to zero. The selected assertion is
R(t,F(t,x))=x as an identity of formal series (every coefficient, for all n),
equivalently F(t,R(t,x))=x. Both series have zero constant term and linear
coefficient one, so formal inversion exists uniquely. Negative powers of t
do not request evaluation at t=0. The unweighted t=1 sequence is only a
specialization, not a replacement target. No correction of the source is proposed.

Source status: the primary paper explicitly proposes this identity. Research
pass 1 supplies a **full-scope proof candidate**, pending fresh mathematical
review. No equivalent resolution was found in the primary passages inspected
on this date; this does not certify global openness or priority. The decisive
primary text is archived as `evidence/external/2605.26916.html`, and its
Sections 1, 5, and 9.6 were compared with the live version. See
`literature/research-screen.md` for current coverage and its limits.

Nearest prior results X: Chapoton's arbor support/height recursion,
Propositions 2.8 and 2.9 of arXiv:2503.04247v2, and the classical weighted-tree
equation T=z W(T). The latter is exemplified by Banderier--Flajolet (2002),
Example 3, p. 52; all the elementary tree facts actually used are proved in
the dossier, without importing finite-step analytic hypotheses.

Research correction to the triage literature comparison: Wang--Hou--Thawinrak--
Liu--Dai, arXiv:2608.16037v1, Theorem 1.3, states general support duality and
explicitly identifies its preorder application as resolving the source's
Conjecture 5.4. Thus support duality should no longer be described as an
unsupplied theorem. This known result does not state the explicit comb
inverse in the passages inspected. The present proof uses the original
minimum-rooted inequalities directly, with no duality theorem as a dependency.

Proposed delta Y: a support-preserving reduction of ALL comb ideal inequalities
to weighted prefix sequences and an exact forest interpretation, proving the
source's full support-refined inverse. The contribution is this particular
resolution; the general tree method and support-duality theorem are prior art.

Verification Z: `evidence/research-proof.md` proves both directions of the
forest bijection, including the uniquely specified first leaf's factor
z(1+t), and derives

    H(z)=T/[z(1+t)(1-T)],    T=z W(t,T),
    R(t,y)=y/[(1+y)(1+(1+t)y)(1+(1+t)y/t)],
    R(t,F(t,x))=x=F(t,R(t,x)).

Its formal rearrangements are coefficientwise finite and include n=0.
No mathematical gap is currently identified by the proposer; this is not an
independent acceptance. `evidence/research-forest-check.py` additionally
checks all 82499 ordered forests with 1,...,11 vertices against all 250953
ambient cost words in the corresponding ranges, repeats the original ideal
comparison on 198627 lattice vectors for n=0,...,5 using the recursive poset,
and verifies the relevant cleared-denominator polynomial identities exactly.
Its cubic-equation coefficients agree with the earlier prefix recurrence for
n=0,...,12. Finite checks are supplementary to the all-n proof.

Research decision: submit a **resolution-paper candidate**, with proposed
original_status=proved, for a fresh referee to audit the precise original,
all-ideal equivalence, canonical-first-leaf bijection, formal elimination,
and bounded prior-result comparison. No manuscript or acceptance is created
by this research role.
