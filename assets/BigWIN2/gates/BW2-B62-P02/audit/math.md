# Fresh mathematical referee report

## Frozen scope and source comparison

I reviewed the exact `resolution-paper` claim in `claim.json`, bound to snapshot
`a90af197f42fc4801e2afb8c2dfb203a086f7a60ecb71e0770308a198ede60c4`.
All snapshot hashes recomputed to the listed values. In particular, the frozen
source and the local arXiv PDF retain SHA-256 digests
`38652f72dbb487f434a6e4e82daf843f197dc158c56204ae1d2f4a9ce62d55c4`
and `1707cb5423c732793ebc688f84b5663dee15ad7ae330ccb6b10cdd210a76bfd2`.

The PDF's Sections 1.1--1.2 define strict votes, give indifferent agents no
vote, and define a popular-winning set using each agent's best match in the
set. Table 1 and Theorem 3.3 give only the general range 2--3 for unweighted
marriage instances with ties; they do not determine the fixed complete
three-by-three census. Thus the submitted statement has exactly the scope of
the frozen problem and does not silently substitute a subsidiary claim. It
makes no claim of priority beyond resolving this frozen question.

## Reconstruction of the exhaustive upper bound

The decisive unreduced verifier has the following complete quantifier chain.

1. A normalized rank triple is retained exactly when its used ranks are
   `{0,...,max(r)}`. These are precisely the total preorders on three labelled
   alternatives, and the generator returns 13 of them.
2. Every sextuple of such orders is visited once by decoding each integer from
   0 through `13^6-1` in base 13. Hence the program covers all 4,826,809
   labelled profiles, without a symmetry assumption.
3. Matchings are independently generated as partial injective functions from
   the three men to the three women. The generator asserts 34 distinct partner
   vectors and sets the reverse partner for every woman, so it includes every
   matching of sizes 0, 1, 2, and 3, including the empty matching.
4. For every matching and every agent, an acceptable partner has the rank from
   that agent's row and an unmatched agent has rank 3. Since every acceptable
   rank is at most 2, this implements the required unmatched convention.
5. A candidate singleton uses its matching's six ranks; a candidate pair uses
   the componentwise minima, exactly the six agents' best-partner ranks across
   the set. For each of all 34 alternatives, the code adds one for a strict
   vote for the candidate, subtracts one for a strict vote for the alternative,
   and adds zero for a tie. It accepts precisely when every resulting integer
   margin is nonnegative.
6. The loops test all 34 singletons and, when none wins, all 561 unordered
   pairs with distinct indices. They therefore implement the full existential
   search required for dimension at most 2.

The unreduced program performs no orbit reduction, Burnside computation, or
popularity-vector cache. Its terminal assertions establish that all profiles
were classified and none remained at dimension 3. I reran the frozen-hash
script in this referee job with one Numba thread under Python 3.10.12, NumPy
2.2.6, and Numba 0.67.0; it exited successfully and reproduced exactly
`d1=4,826,131`, `d2=678`, `d3=0`.

As a separate consistency check, I reconstructed the primary orbit program's
predicate and coverage. It uses the 72 side-preserving or side-exchanging
automorphisms, marks the images of each least unvisited base-13 profile, and
gets 67,815 orbits covering all 4,826,809 labelled profiles. Its independently
computed Burnside fixed-point sum is 4,882,680, also giving 67,815 orbits. I
reran this frozen-hash program with one thread; it reproduced 67,797
dimension-one orbits, 18 dimension-two orbits, no dimension-three orbit, and
the same labelled counts as the unreduced verifier. The universal conclusion
does not depend on the symmetry code because the unreduced pass quantifies
over every labelled profile directly.

## Reconstruction of the lower bound

For the displayed profile, the proposed pair

`{m2-w0}` and `{m0-w0,m1-w1,m2-w2}`

has best-rank vector `(0,1,0,0,2,0)` in agent order
`(m0,m1,m2,w0,w1,w2)`. The pure-standard-library verifier enumerates the 34
matchings independently. It supplies a strictly defeating alternative for
each of the 34 possible singleton candidates. It then checks the pair against
every alternative and obtains margins

`6,4,3,5,4,4,5,5,4,5,2,1,3,3,2,3,2,2,3,4,2,3,2,3,3,4,3,3,1,1,0,1,1,2`.

All are nonnegative, including the one equality case. I reran this verifier;
all 34 singleton defeats and all 34 pair checks reproduced and the script
exited successfully. Consequently this profile has dimension exactly 2.

## Adversarial checks and verdict

The quantified domains are nonempty and exact; there is no division by zero,
floating-point comparison, limiting argument, compactness claim, or appeal to
an unchecked mathematical lemma. Partial and empty alternatives are present.
Ties are handled by zero contribution, and pairs contain distinct matchings.
The lower-bound witness establishes that the maximum is not 1, while the
unreduced census establishes that it is at most 2. Together they prove the
frozen statement in full.

I found no unresolved mathematical or scope gap. **Verdict: accept.**
