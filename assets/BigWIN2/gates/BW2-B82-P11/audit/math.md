# Fresh mathematical referee report

Job: `win-00082-p11-referee-e35f12b35489`

Snapshot: `278b3d2ca7edc578e39d19c763b48bb9e2c0962bad99075e3f38f8750f03904a`

## Frozen scope reviewed

The candidate is a `resolution-paper`.  Its primary assertion is the full
universal statement in `source.md`: every strictly increasing real
five-letter alphabet whose mass-at-most-three relation span has rank one and
whose primitive generator has mass three has an exact-profile increasing
integer model of diameter at most 33.  I also reviewed, rather than silently
downgrading, the stronger assertion that the exact maximum is 33 and that,
up to the generator's sign, the only directions attaining it are

\[
(1,-3,0,0,2)\quad\text{and}\quad(2,0,0,-3,1).
\]

All hashes listed in `audit/snapshot.json` were recomputed and matched.  I
also recomputed the canonical SHA-256 of its `files` mapping; it equals the
snapshot digest above.

## Reconstruction of the decisive argument

Let \(\delta\) be the primitive balanced generator.  Primitivity makes
\(\mathbb Q\delta\cap\mathbb Z^5=\mathbb Z\delta\): a rational multiple of
a primitive integral vector which is integral has an integral multiplier.
Every nonzero member of \(Z_3(T)\) is therefore \(k\delta\) for an integer
\(k\).  Since mass is homogeneous and \(m(\delta)=3\), the mass cutoff forces
\(|k|=1\).  Conversely, the nonzero profile spans the line, so the same
argument shows that one of its members is \(\pm\delta\).  Hence

\[
Z_3(T)=\{0,\delta,-\delta\}.
\]

Put \(g_j=t_j-t_{j-1}>0\) and
\(A_j=\sum_{i=j}^4\delta_i\).  Balance gives the exact identity

\[
\delta\mathbin\cdot T=\sum_{j=1}^4 A_jg_j.
\]

For nonzero \(\delta\), a positive gap vector annihilates this expression
if and only if the four tail sums contain both signs.  Necessity follows
from positivity of every gap.  For sufficiency, assigning to every positive
tail the total absolute negative tail sum, to every negative tail the total
positive tail sum, and assigning 1 at zero tails gives a positive exact
solution.  Thus this is an exact order-cone criterion, including directions
having zero tail sums.

A balanced row of mass three has every coordinate in \([-3,3]\).  Exhausting
that finite box, fixing sign by requiring the first nonzero coordinate to be
positive, and imposing coordinate gcd one is therefore complete.  It gives
160 primitive mass-three directions modulo sign; the mixed-tail criterion
leaves 65.  There is no sampling or unexamined real parameter at this point:
every qualifying real alphabet has one of these directions.

For an integer model, translation gives
\(S=(0<s_1<s_2<s_3<s_4=D)\).  Every balanced relation of mass at most three
is the difference of two unordered three-letter multisets after padding both
sides to length three.  Accordingly, the complete short zero profile can be
recovered exactly from collisions among the 35 unordered three-term sums of
the five letters.  The tuples through diameter 33 are exactly

\[
\sum_{D=4}^{33}\binom{D-1}{3}=\binom{33}{4}=40{,}920.
\]

The frozen census tests every such tuple and retains a tuple only when its
entire canonical zero-row set is the singleton \(\{\delta\}\).  All 65
feasible directions occur.  Since diameter is traversed in increasing order
and five distinct integers require diameter at least 4, the first occurrence
is the exact value of \(M_3\), not merely an upper-bound witness.  The largest
first occurrence is 33, and its complete extremal list is precisely the two
directions displayed above.  Translation ensures that no possible smaller
integer model is omitted.  This proves both the frozen universal bound and
the stronger direction classification.

## Independent exact checks

I ran the supplied checker without writing to the frozen evidence.  It
independently regenerated short rows from differences of unordered
multisets, regenerated mass-three directions from disjoint weak
compositions, and repeated all 40,920 alphabet checks.  It returned success
with 235 nonzero short rows modulo sign, 160 primitive mass-three directions,
65 feasible and covered directions, maximum minimum 33, and exactly the two
claimed extremal directions.

I then performed a separate fresh census which did not import either frozen
program.  It generated primitive directions directly from the coefficient
box, formed the 35 unordered triple sums for each integer alphabet, grouped
them by exact integer value, and reconstructed the profile from all
within-group differences.  It independently obtained 65 feasible
directions, 40,920 alphabets, identical minimum model and occurrence count
for every certificate entry, maximum 33, and the same two extremals.  All
arithmetic in both checks was integral and exact.

For the sharp cluster direction, the relation in a translated model is
\(-3s_1+2s_4=0\), so integrality forces

\[
S=(0,2c,2c+a,2c+b,3c),\qquad 0<a<b<c.
\]

Writing \(U=(0,a,b,c)\), relations avoiding the first zero are exactly the
relations on \(U\).  For a reduced relation of mass \(p\leq3\) using \(z\geq
1\) copies of the first zero on one side, equality would require
\(3c(p-z)\geq2cp\).  Thus \(p=3,z=1\), and equality throughout forces the
sole cluster relation \(0+2(3c)=3(2c)\).  Consequently the five-letter
profile is exactly the cluster profile if and only if \(U\) is relation-free
through mass three.

Such a four-letter core is relation-free exactly when its 20 unordered
three-term sums are distinct.  The exhaustive core domain through \(c=11\)
has
\(\sum_{c=3}^{11}\binom{c-1}{2}=165\) elements.  My fresh collision check
found none for \(c\leq10\), and at \(c=11\) found exactly

\[
(0,1,7,11),\ (0,1,8,11),\ (0,3,10,11),\ (0,4,10,11).
\]

Thus \(c\geq11\), giving diameter \(3c\geq33\); the first core yields
\((0,22,23,29,33)\).  This independently verifies sharpness and addresses
the separate lower-bound obligation in the frozen source.

## Source comparison and limitations

I inspected the cited passages in the frozen Zhang PDF.  Definition 2.1
uses equality in both directions, exactly as modeled here.  Proposition 6.5
gives only \(\mu q(q+1)=36\) at \((q,\mu)=(3,3)\); Corollary 9.2 supplies
the cluster value 33; Remark 10.1 expressly excludes this higher-mass layer;
and Question 12.3 asks for the per-mass rank-one maximum.  The result
therefore closes the exact frozen 36-to-33 gap rather than proving a toy
restriction or a subsidiary statement.

The supplied literature search is explicitly bounded and does not establish
global priority.  The candidate makes no stronger priority claim, and its
mathematical proof does not depend on that limitation.  A current literature
refresh remains appropriate before publication, but it is not a gap in the
frozen theorem or classification.

## Verdict

**Accept.**  The quantifiers, strict-order feasibility, lattice primitivity,
shorter relations, normalization of all integer models, exact minima,
sharpness, and the stronger equality-direction classification all pass.  I
found no unresolved mathematical or scope gap in the frozen candidate.
