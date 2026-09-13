# Fresh mathematical referee report

## Frozen scope and provenance

This review concerns the exact `resolution-paper` claim frozen in snapshot
`59e03e68ab8779d31d40334c841de1fae8b4fd0f247cdcff6f179d4f3391dfc4`:
for every positive-integer pair `(u,v)`, the entropy of
`1+B_1+uB_2+vB_3` is concave on the whole interval `[0,1]`.  I reviewed the
immutable source statement, its precise interpretation, the claim, and every
file enumerated by that snapshot.  I independently recomputed all eight file
hashes and the canonical snapshot digest; they agree with `audit/snapshot.json`.

## Reconstruction of the proof

Write `q=1-p`, `R=pq`, and

\[
b(p)=-p\log p-q\log q.
\]

The eight bit vectors have probabilities `A=p^3`, three copies of
`B=p^2q`, three copies of `C=pq^2`, and `D=q^3` before equal support points
are merged.

The collision classification is exhaustive.  If two subset sums of
`{1,u,v}` agree, cancel their common summands.  The two remaining subsets are
disjoint and nonempty.  With only three positive weights, the resulting
equality is either one weight against one weight or one weight against the
other two.  Therefore the only possible relations are

\[
u=1,\quad v=1,\quad u=v,\quad v=u+1,\quad u=v+1;
\]

the sixth formal relation `1=u+v` is impossible for positive integers.
Resolving intersections of these relations gives exactly five cases:

| parameters | merged atom multiset | entropy profile |
|---|---|---|
| `(1,1)` | `A,3B,3C,D` | `3b-3R log 3` |
| `(1,2)` or `(2,1)` | `A,2B,R,2C,D` | `3b-Rb-2R log 2` |
| `u=1,v>=3`; `v=1,u>=3`; or `u=v>=2` | `A,B,2B,C,2C,D` | `3b-2R log 2` |
| consecutive `u,v>=2` | `A,B,B,R,C,C,D` | `3b-Rb` |
| all remaining pairs | `A,B,B,B,C,C,C,D` | `3b` |

I checked the intersections explicitly: the exceptional overlap of an equal
weight relation with a sum relation is precisely `(1,2)` or `(2,1)`, while
`(1,1)` is the triple-equal case.  Thus no positive-integer pair is omitted
or counted under an incorrect generic profile.

The entropy identities follow directly from merging.  The unmerged entropy
is `3b`; merging `k` equal atoms of mass `a` lowers entropy by
`ka log k`.  In the only mixed merge, `B=pR`, `C=qR`, and `B+C=R`, so

\[
(-B\log B-C\log C)-(-R\log R)=Rb.
\]

This yields the displayed profiles without approximation.

All five profiles have the common form

\[
F_{\delta,c}=3b-\delta Rb-cR,
\]

with `(delta,c)` equal respectively to
`(0,3 log 3)`, `(1,2 log 2)`, `(0,2 log 2)`, `(1,0)`, and `(0,0)`.
For `0<p<1`, direct differentiation gives

\[
b''=-1/R,\qquad
(Rb)''=-2b+2(1-2p)\log(q/p)-1.
\]

If `delta=0`, then `F''=-3/R+2c`.  Since `R<=1/4`, this is strictly
negative in cases 1, 3, and 5 (using `log 3<2` and `log 2<1`).  If
`delta=1`, then

\[
F''=-3/R+2b-2(1-2p)\log(q/p)+1+2c.
\]

Here `b<=log 2`, and `(1-2p) log(q/p)>=0` because its two factors have the
same sign.  Consequently

\[
F''\le -11+2\log2+2c,
\]

which is less than `-9` for case 4 and less than `-5` for case 2.  Hence
every profile is strictly concave on `(0,1)`.

The formulas only divide by `R` on the open interval, where `R>0`.
Every atom entropy has the continuous convention `0 log 0=0`, so each profile
extends continuously to both endpoints.  Applying the interior concavity
inequality to inward approximations of any endpoint arguments and taking
limits proves concavity on `[0,1]`.  No differentiation or division at an
endpoint is being assumed.

## Independent checks and attempted failure modes

I reran both frozen programs using the required research interpreter.  The
symbolic verifier returned exact zero for all five atom/profile identities,
for both derivative identities, and for every displayed second derivative.
The partition verifier matched each representative and all 10,000 pairs with
`1<=u,v<=100`; this finite computation is corroboration only, not the reason
the universal quantifier holds.  The disjoint-subset argument above supplies
that reason.

I specifically checked the universal parameter quantifiers, multiple-relation
intersections, possible collisions involving the unique minimum and maximum
support points, the mixed `B+C` merge, the signs in differentiating `Rb`, the
equality case `p=1/2`, division by zero, and passage to `p=0,1`.  None produces
a gap.  The proof uses no compactness, uniform limiting exchange, numerical
sign inference, or external theorem whose hypotheses remain unchecked.

## Source comparison and contribution

Relative to the frozen source boundary in `source.md` and `problem.md`, the
candidate settles the complete `n=3` statement, not a sampled parameter
family: the previously untreated collision profiles are cases 2--4, and the
classification also incorporates the binomial and collision-free profiles.
That is a substantive full-scope resolution of the submitted original claim
and makes no assertion for `n>3`.

The cited primary PDF was not enumerated in this snapshot, and the job's
evidence restriction therefore did not permit an independent bibliographic or
priority check against its full text.  This does not create a mathematical or
scope gap here: the immutable original statement itself is frozen, and the
contribution expressly makes no priority claim beyond the documented source
comparison.  Any broader novelty attribution should remain bounded or be
checked in the later citation review.

## Verdict

**Accept.**  The frozen argument proves the exact universal claim, handles all
positive-integer collision types and both endpoints, and supports the declared
`resolution-paper` scope.  I found no material mathematical revision needed.
