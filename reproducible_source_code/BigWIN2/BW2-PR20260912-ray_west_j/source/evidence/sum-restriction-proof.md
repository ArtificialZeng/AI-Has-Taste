# A direct-sum formula for the Ray--West correction

Research proof submitted for scrutiny, 2026-09-12.
Proposer job: primary-20260912-ray-west-j-research-db44e3159ae7.
No independent mathematical acceptance is asserted.

## Statement and scope

For a nonempty permutation p of length m, let g2(p) count the distinct
permutations of length m+2 containing p, and set

    j(p) = (m^4+2m^3+m^2+4m+4)/2 - g2(p).

Write p uniquely as a direct sum of sum-indecomposable components. Let
H(p), respectively T(p), equal 1 when its first, respectively last,
component is decreasing, and 0 otherwise. Singletons are decreasing.

**Theorem.** For every pair of nonempty permutations a,b,

    j(a direct-sum b) = j(a)+j(b)+T(a)H(b).                 (S)

More precisely, every Ray--West good gap internal to either summand is
good exactly when it is good in that summand. The join is good exactly
when T(a)H(b)=1.

This is a subsidiary structural theorem. It does not give an intrinsic
formula for j on all permutations and does not settle original Problem 3.7.
The consequences below give such a statistic on separable permutations
and classify equality among all sum- or skew-decomposable permutations.

## Insertion conventions and primary-source dependencies

All coordinates are one-based original-grid coordinates. A 2-triple is
t=(rho; R,C), with R=(r1,r2), C=(c1,c2) weakly increasing in [1,m+1].
Insertion places the new entries in positions c1,c2+1 and gives them
values r1,r2+1 in relative order rho. An original point (q,p(q)) goes to

    (q + #{c in C:c<=q}, p(q) + #{r in R:r<=p(q)}).        (1)

A site (r,c) is active when neither original column c-1 nor c contains
value r, omitting nonexistent columns. A triple is active when both its
sites are active. A synonymity is an equality of two insertion results.
Only the left triple is required to be active; the right triple need not
be active or canonical.

We use the following established facts from Ray and West (2003), copied
in evidence/external/ray-west-2003.pdf and its full extracted text.

1. Corollary 8.6 and Theorem 8.7, printed pp. 82--83: j counts distinct
   active left triples t having a synonymous right triple u=(sigma;S,D)
   of pattern (C), in either of the following orientations:

       r1<=r2<s1<=s2, c1<=c2<d1<=d2             (+)
       r1<=r2<s1<=s2, d1<=d2<c1<=c2             (-).

   There is at most one counted left triple per adjacent gap. A gap
   between positions i and i+1 is called good when it receives one.
   Multiple choices of u for the same t are counted only once.

2. Theorem 6.4, Proposition 6.3 and the discussion before Proposition
   8.5, printed pp. 72--73, 80: the original points involved in (C) form
   two nonempty tracks, covering a contiguous permutation submatrix.
   Its row interval is [r1,s2-1], and its column interval is [c1,d2-1]
   in (+), or [d1,c2-1] in (-). Every row and column of this rectangle
   contains its unique permutation point there. Along each track values
   strictly increase; positions strictly increase in (+) and strictly
   decrease in (-). Every original point of the rectangle belongs to
   one track. Here a track includes its original permutation points;
   its inserted source and target are sites, not extra original points.

3. The proof of Corollary 8.6, using Proposition 8.5: in (+) the assigned
   gap is a descent, and its index and source coordinates satisfy

       i=c2, r1=p(i+1), p(c1)=r2+1.                       (2)

   The original points at i and i+1 lie on different tracks. In (-) the
   gap is an ascent, i=c1-2, and again the two adjacent original points
   lie on different tracks. The latter facts follow by horizontal
   reflection of the former. The printed second signed case in the
   corollary repeats a sign; we use the explicit reflection, not that
   repeated sign. Original position q reflects to m+1-q and a grid
   column c reflects to m+2-c, giving i=c1-2 as stated.

These are prior track facts, not claimed contributions. The proof below
does not use the source's separate notion of a prime track matrix.

## Lemma 1: restriction with re-pairing

Let p=a direct-sum b with |a|=k. Suppose an active synonymity t~u is
of orientation (+), and max R,max C<=k. Put

    S'=(min(s1,k+1),min(s2,k+1)),
    D'=(min(d1,k+1),min(d2,k+1)).

There exists sigma' in S2 such that t~(sigma';S',D') is an active
orientation-(+) synonymity for a, assigned to the same gap. It is not
in general valid to insist that sigma'=sigma.

**Proof.** Inserting t gives tau=tau_A direct-sum b, where
tau_A=Ins(t;a) has length k+2. Consider the original copy of p furnished
by u in tau. Its first k points, which form a, have positions

    x(q)=q+#{d in D:d<=q}, 1<=q<=k,

and values v+#{s in S:s<=v} for 1<=v<=k, by (1). Both coordinates
are at most k+2. Thus these points are an occurrence of a entirely in
tau_A. The two complementary points of tau_A define sigma', S',D'.

To verify the displayed multisets, for every q<=k and every d,

    min(d,k+1)<=q  iff  d<=q.

Consequently inserting at D' gives exactly the same positions x(q) for
the retained k points. These positions uniquely determine the two
missing positions and hence their original-grid insertion multiset.
The same argument on values gives S'. Pair each missing position with
its actual value in tau_A to obtain sigma'. This proves the insertion
identity, including repeated sites or clips of one or both coordinates.

The left triple remains active on deleting b: no new adjacent entry
equal to either source row can be introduced, and its insertion result
is tau_A. For strict separation, s1>r2 and k+1>r2 imply
min(s1,k+1)>r2; similarly min(d1,k+1)>c2. Hence both strict (C)
inequalities survive, including clipping exactly to k+1 and repeated
clipped coordinates. The left triple and c2 are unchanged, so the
assigned gap is unchanged. This proves the lemma.

The elementary counterexample p=213, k=2 in
sum-restriction-pass2.md explains why the re-pairing step is necessary.

## Lemma 2: internal gaps restrict and lift

Let p=a direct-sum b, |a|=k. Every good gap within a restricts to the
same good gap of a; every good gap within b restricts to the translated
good gap of b. Conversely all good gaps of a or b lift to p.

**Proof of restriction in (+).** Write i for the gap index in p. If
i<k, then c1<=c2=i<=k-1. Since p(c1)<=k, equation (2) gives
r2=p(c1)-1<=k-1. Thus R,C are within the prefix grid and Lemma 1
applies. This covers all right-site configurations, including ones
straddling the cut and ones lying entirely beyond it.

If i>k, then r1=p(i+1)>k, so r2>=r1>k. Equation (2) now gives
p(c1)=r2+1>k, whence c1>k. Thus every coordinate in R,C,S,D is
at least k+1, because S lies strictly after R and D after C. Subtract
k from all coordinates and restrict to b. Both insertion results have
the same unchanged prefix a, so their suffixes agree. Activity and
strict separations survive translation. The new gap is i-k.

**Proof of restriction in (-).** An increasing-value, decreasing-position
track cannot contain points on both sides of a direct-sum cut: any
point of a is both smaller in value and earlier in position than every
point of b, which is incompatible with either order along that track.
The points at i and i+1 belong to different tracks. If both are in a,
each of the two tracks lies entirely in a. They cover the whole support
rectangle, so all its row and column indices are at most k. All four
site multisets therefore lie in [1,k+1]. If both adjacent points are
in b, the same argument puts every support row and column above k,
and every site coordinate is at least k+1. In either case restricting
the two equal insertions to the appropriate summand, translating in
the suffix case, gives a synonymity with the same strict inequalities
and gap. Activity survives restriction. No clipping is needed here.

**Proof of lifting.** A witnessing pair on a lifts by leaving every
coordinate unchanged; each common insertion is the old common result
direct-sum b. A witnessing pair on b lifts by adding k to every
coordinate; each common result is a direct-sum the old result. The
strict inequalities survive. For the prefix lift, r2<s1<=k+1 implies
every active source row is at most k, so an added adjacent entry from b
cannot invalidate activity even at grid column k+1. For the suffix
lift, every source row is greater than k, so an adjacent entry of a
cannot invalidate activity at the first suffix grid column. This
also checks boundary sites. The gap assignments are unchanged or
translated by k, respectively.

## Lemma 3: the join criterion

The gap at the join of p=a direct-sum b is good if and only if the last
sum-indecomposable component of a and the first component of b are both
decreasing.

**Necessity.** The join is an ascent, so a witness has orientation (-).
The two tracks respectively contain p(k) and p(k+1). By the monotonicity
argument in Lemma 2, the first lies wholly in a and the second wholly in
b. Write the support rectangle as rows [r1,s2-1], columns [d1,c2-1].
It crosses the cut. Its a part uses exactly columns d1,...,k and
exactly values r1,...,k. These sets have the same cardinality because
every support row and column is occupied, so d1=r1. All these points
are on a single decreasing track. Hence the suffix p(d1),...,p(k) is
precisely k,k-1,...,d1. Similarly the b part is a decreasing prefix
whose values are k+1,...,c2-1, with s2=c2. The prefix and suffix just
found are direct-sum components: their preceding/following points use
exactly the complementary smaller/larger values. A decreasing
permutation is sum-indecomposable, including a singleton. Thus these
are exactly the two incident indecomposable components.

**Sufficiency.** It suffices to give a witness on delta_a direct-sum
delta_b for arbitrary positive integers a,b, because their union is
an interval and the surrounding direct summands can be left unchanged.
Put m=a+b and use rho=sigma=12 and

    R=(1,a), C=(a+2,m+1), S=(a+2,m+1), D=(1,a).

Both insertions equal the permutation

    (a+2, a,a-1,...,2, m+2, 1, m+1,m,...,a+3, a+1),

with empty ranges omitted. This follows directly from (1). The left
source (1,a+2) has neither adjacent entry equal to 1; if b=1 the only
adjacent entry is a+1. At (a,m+1), the only adjacent entry is a+1,
different from a. The left triple is active. Both strict inequalities
hold because max R=max D=a<a+2=min S=min C. The assigned gap is
c1-2=a. This verifies all cases a=1, b=1, including a=b=1.

## Proof of (S) and intrinsic consequences

Lemma 2 identifies all internal good gaps exactly, and Lemma 3 identifies
the only remaining gap. Counting gaps via Corollary 8.6 proves (S).

Let c(p) be value complementation. It bijects containing permutations
of p with those of c(p), so j(c(p))=j(p). Since

    c(a skew-sum b)=c(a) direct-sum c(b),

(S) gives the analogous skew-sum rule, with the indicators now testing
whether the incident first/last skew-indecomposable components are
increasing. This conclusion uses the containment bijection, without
assuming that the active-gap labels themselves are preserved by
complementation.

For a maximal direct-sum decomposition p=p1 direct-sum ... direct-sum pt,
iterating (S) gives

    j(p)=sum_h j(ph)
         +sum_(h=1)^(t-1) 1{ph and p_(h+1) are decreasing}.    (3)

The corresponding maximal skew decomposition uses increasing children.
A separable permutation is, by definition here, one obtained recursively
from singletons using these two operations. Its decomposition tree gives
an intrinsic statistic: at each maximal sum node count adjacent children
that are both decreasing; at each maximal skew node count adjacent
children that are both increasing; sum these counts over all nodes.
Singleton leaves contribute zero. Formula (3) and its skew analogue
prove that this statistic equals j. No insertion search or superpattern
count is needed to evaluate it from that tree.

Finally, for any sum-decomposable p, using the known bound
j(ph)<=|ph|-1 in (3) gives j(p)<=|p|-1. Equality requires every one of
the t-1 displayed indicators to be 1. As t>=2, every child must therefore
be decreasing, so p is layered. Conversely every decreasing child has
j=|ph|-1 (by the skew rule applied to its singleton components), and
(3) then gives equality for every layered p. Complementation proves
that a skew-decomposable p has equality if and only if it is colayered.
Every separable permutation of size at least 2 has one of these two
decompositions, so its equality cases are exactly the layered and
colayered permutations. At size 1, j=0 directly and both descriptions
apply. No assertion about permutations indecomposable in both senses
is needed or made here.

## Evidence, limitations, and gap list

The new verifier enumerates all insertion triples, with no activity
requirement on right triples. It checks all 873 permutations through
length 6 and 15 larger structured permutations of lengths 10--12. It
reconstructs the two tracks from the two original embeddings, checks
their complete rectangular support and the local source equations,
and checks the clipping/re-pairing, localization, and join steps.
It tests 3,110 pair/cut cases; 1,219 use positive-prefix restriction,
and 188 require changing the right inserted pattern. There are 849
pattern-(C) pairs with inactive right triples in the tested data, so
requiring an active right triple would be an unnecessary restriction.
All checks pass. Exact files: verify_sum_restriction.py and
sum-restriction-verification.json. These computations are finite
corroboration of the proof above, not a proof of the universal theorem.

The earlier census tests (S) on 132,849 cuts through total length 9;
its stronger gap test covers 2,673 cuts through length 7. They informed
the statement and are exploratory evidence. No new blind-test claim
is made for those inherited data.

The executable tree statistic in separable_statistic.py agrees with all
52,465 separable permutations in that inherited census through length 9;
see separable-statistic-verification.json. This checks the stated
consequence and its implementation against separately obtained g2 data.
It is a regression check on already-seen data, not a blind experiment.

Known mathematical gap list for (S) and the stated consequences: empty
at submission. The proof relies explicitly on the cited Ray--West track
facts; those dependencies and the boundary arguments require a fresh
referee. No independent review has yet occurred. The all-permutation
statistic, the deletion inequality (D), and the equality conjecture for
permutations indecomposable in both senses remain unresolved here.
