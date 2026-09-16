Mathematical referee report — verdict: **accept**.

Job: `primary-20260912-ray-west-j-referee-84360b7c5281`.
Snapshot: `35ef4ddb8305673591e7206c8fd904dc2c3189210aaafe52b3b7feed0ff83af1`.
Frozen kind: `result-note`. Frozen original status: `unresolved`.

The exact submitted scope passes mathematical and contribution review. For
arbitrary nonempty permutations alpha and beta, the accepted theorem is

    j(alpha ⊕ beta) = j(alpha) + j(beta) + T(alpha) H(beta),

where T and H test whether the incident last and first sum-indecomposable
components are decreasing, and singleton components qualify. Acceptance also
covers the stronger internal-good-gap restriction statement and join criterion,
the complemented skew-sum law, the stated maximal-tree statistic for every
separable permutation, and both equality classifications on the full sum- and
skew-decomposable domains. No hypothesis on the summands being separable has
been added. The original all-permutation statistics problem remains unresolved;
no formula or equality classification on permutations indecomposable in both
senses is accepted here. This is acceptance of the frozen scope, without a
substantive revision or downgrade.

All 23 entries in the frozen file mapping match their SHA-256 hashes. Its
canonical sorted compact JSON hash also matches the snapshot digest. In
particular, `source.md` retains hash
`92f387c6551ae42e866ea2561665abf78b80baa018f1808f81a0d899ea4b7bf2`.
See `audit/referee-integrity.json`. The owner checkpoint, state, earlier job
transcripts and earlier verdicts were not consulted. The mathematical review
uses the submitted proof, the listed source and computational evidence, and
the actual primary sources discussed below. Hashing the other frozen files
does not imply that every large census was independently reproduced.

The decisive proof is `evidence/sum-restriction-proof.md`. Its argument was
reconstructed as follows.

1. **Meaning of j and the good-gap count.** An insertion produces one ambient
   permutation, and synonymity means equality of those actual permutations.
   Ray–West's active-site definition uses the two original columns adjacent
   to a grid site; activity applies to the left triple only. Their Corollary
   8.6 and Theorem 8.7 identify the residual j with the number of distinct
   active left triples in the two strict pattern-(C) orientations, with at
   most one per adjacent gap. Thus neither occurrences nor choices of the
   right triple are being overcounted. For positive orientation, the source
   equations are i=c2, r1=p(i+1), and p(c1)=r2+1; the adjacent points belong
   to different tracks. Reflecting original position q to m+1-q and grid
   column c to m+2-c gives i=c1-2 for negative orientation. The repeated
   positive sign in the second case of the printed corollary is indeed
   present in the PDF. The explicit reflection in the candidate handles it
   correctly.

2. **The support and monotonicity hypotheses really apply.** The definition
   of insertion in the source gives original-point shifts
   q -> q + number of column sites at most q, and the corresponding formula
   for values. Under strict separated row multisets, their difference is
   positive precisely for values in [r1,s2-1]. The column difference is
   positive on [c1,d2-1] in the positive orientation, and negative on
   [d1,c2-1] in the reflected orientation. For an original point, one shift
   difference vanishes if and only if the other does: otherwise the two
   embeddings would give two different points of the same ambient
   permutation with an identical row or column. Consequently every row and
   column of the asserted support rectangle has its permutation point
   inside it. Following equality between the two original embeddings gives
   the tracks of Theorem 6.4; their values increase, with positions
   increasing or decreasing according to orientation. Proposition 8.5
   supplies two nonempty tracks for an active pattern-(C) pair. No
   additional assumption of right-triple activity, canonicity, or track
   primeness is needed. This also independently explains why a support
   rectangle cannot conceal points outside the two tracks used at the cut.

3. **Positive prefix restriction preserves the insertion identity.** Put
   p=alpha ⊕ beta and k=|alpha|. If the left source row and column multisets
   lie at most k, its common ambient value is tau_A ⊕ beta, with |tau_A|=k+2.
   The first k original points in the right-hand embedding have both
   coordinates at most k+2, and so form an occurrence of alpha in tau_A.
   Its two complementary points are the required new inserted pair.
   For q<=k, min(d,k+1)<=q is equivalent to d<=q; the identical fact for
   rows proves exactly the claimed clipped site multisets. The actual two
   complementary points determine their relative permutation. There is no
   reason it must equal the old right permutation, and the proof correctly
   does not impose that condition. Since max R and max C are at most k,
   clipping a strictly larger coordinate to k+1 preserves strict
   separation. Repeated coordinates are permitted throughout. The left
   triple and gap index stay fixed, and deleting the suffix cannot create
   a new obstructing adjacent entry. This is a complete restriction
   argument, not an appeal to the computational examples.

4. **All internal gaps restrict in the claimed orientation.** In a positive
   gap i<k, the source equations force c2=i<=k-1 and r2=p(c1)-1<=k-1,
   placing the sources within the range of the preceding argument. In a
   positive gap i>k, r1=p(i+1)>k and p(c1)=r2+1>k force c1>k; strict
   separation puts all four multisets at least k+1. Subtracting k then
   gives the suffix witness. In negative orientation, a track cannot
   cross a direct-sum cut, since positions and values have opposite
   orders along it. If the adjacent gap points lie in one summand, both
   tracks do, hence so does the complete support. All sites are on that
   summand's grid, including its boundary. Restricting the equality of
   insertions therefore gives the asserted internal witness.

5. **Lifting and the cut boundary have been checked.** A prefix witness
   uses sites at most k+1, so both inserted rows and columns stay within
   the augmented prefix. The strict row inequality makes its source
   rows at most k; the first new suffix entry has value greater than k
   and cannot invalidate activity at grid column k+1. For a suffix
   witness translated by k, source rows exceed k and the preceding
   prefix entry cannot invalidate activity. Thus internal restriction
   is an equivalence, including witnesses touching the boundary.

6. **Necessity of the join condition is not limited to special summands.**
   The join is an ascent. Its negative-orientation tracks cannot cross
   the direct-sum cut and contain one incident point each, so exactly
   one track lies in each summand. Complete support implies that the
   prefix-side part occupies columns d1,...,k and values r1,...,k.
   Counting gives d1=r1. Since it is a single decreasing track, these
   entries must be k,k-1,...,d1. Likewise the suffix-side part is a
   decreasing initial interval with the consecutive smallest values
   of that summand. The complementary entries lie entirely below or
   above these intervals respectively. These are therefore direct-sum
   components, and their decreasing form makes them indecomposable.
   They are exactly the incident components tested by T and H.

7. **Sufficiency and degeneracies.** For delta_a ⊕ delta_b with a,b>=1,
   the submitted sites R=(1,a), C=(a+2,a+b+1), S=(a+2,a+b+1), D=(1,a),
   with both inserted permutations increasing, give exactly the
   displayed common ambient permutation. At source (1,a+2), adjacent
   entries exceed 1; at (a,a+b+1), the only adjacent value is a+1.
   Hence activity and both strict inequalities hold. Empty displayed
   decreasing ranges cause no exception when a=1 or b=1; for a=b=1
   the ambient permutation is 3412. Lifting into surrounding direct
   summands is covered by the preceding boundary argument. Together
   with steps 4–6, counting the internal gaps and the single join
   proves the composition law for all nonempty summands.

8. **All stated consequences follow without circularity.** Complementing
   values gives a bijection of ambient containing permutations, so it
   preserves j and converts skew sums to direct sums. The incident
   component tests become increasing skew components. Iteration over
   maximal components gives the adjacent-child formula; recursion
   terminates at singleton leaves, where j=B(1)-6=0. This proves the
   entire separable-tree statistic. For maximal sum components p1,...,pt
   with t>=2, write the deficit as

       |p|-1-j(p) = sum_h (|ph|-1-j(ph))
                    + sum_(h=1)^(t-1) (1-I_h),

   where I_h tests two adjacent decreasing components. Every term is
   nonnegative by the established Ray–West bound. Equality forces all
   I_h=1, and thus every child decreasing. Conversely, decreasing
   children attain their bounds by the skew rule on singletons, so
   every layered sum-decomposable permutation has equality. Complement
   gives the full stated colayered classification. No assumption of
   the unproved all-permutation equality conjecture or deletion
   inequality enters this argument.

The independent computational checks are corroboration, not the proof of
these universally quantified statements. `audit/referee_exact.py` imports
none of the submitted modules. It enumerates every ambient permutation of
lengths 3 through 8 and derives each pattern occurrence and insertion triple
from actual two-position deletions. It then follows the two occurrences
inside that ambient permutation to recover tracks. This checks the insertion
conventions and their connection to g2 by a route different from the
submitted insertion-triple generator.

The completed output `audit/referee-exact.json` records 46,230 ambient
permutations, 1,246,962 deletion occurrences, and all 873 patterns of lengths
1 through 6. Their independently computed g2 values agree with the frozen
census. The 3,120 active-left pattern-(C) pairs include 792 with inactive
right triples. All support, monotonicity, source-equation, distinct-gap, and
j-count checks passed. There are 2,231 pair/cut cases, including 659 positive
prefix restrictions, of which 134 change the right permutation. All 465
direct-sum cut identities and exact gap-set identities passed. The separate
tree implementation agrees on all 515 separable patterns in this range;
the decomposable equality tests also pass. This finite range is not called
a blind sample: the candidate already had data there, but the verifier and
its reconstruction from deletion occurrences were independently authored.

`audit/referee_witnesses.py` separately checks all eight serialized clipping
counterexamples from the submitted verification JSON, including the repaired
and unrepaired ambient values. It decodes the written parametric join
permutation by deletion for every 1<=a,b<=50 (2,500 cases). All passed,
including a=1, b=1, and repeated sites; see `audit/referee-witnesses.json`.
These checks do not certify the submission's entire length-7-to-9 census or
its larger structured sample, which were not needed to validate the proof.
Reproduction commands are `python3 audit/referee_exact.py` and
`python3 audit/referee_witnesses.py` from the project root.

The nearest mathematical source is [Ray and West, *Posets of Matrices and
Permutations with Forbidden Subsequences* (2003)](https://eprints.maths.manchester.ac.uk/609/1/lume2wjganftta0j.pdf).
The frozen primary PDF and extracted text were inspected at the active-site
and synonymity definitions (printed pp. 64, 67), track results (pp. 72–74),
and pattern-(C) analysis (pp. 80–83). Rendered printed pp. 81–82 were also
viewed; the images are `audit/referee-ray-west-28.png` and
`audit/referee-ray-west-29.png`. The source supplies the track count and
extremal bound, not the submitted endpoint-indicator composition formula
in these passages. Whole-text searches for direct sum, separable, layered,
component, and composition terminology found no equivalent statement.

[Shar's 2016 thesis](https://sites.math.rutgers.edu/~zeilberg/Theses/NathanielSharThesis.pdf)
was checked live on 2026-09-12: Theorem 1.3 (printed p. 19), the repeated-sum
definition and Corollary 4.21, and Theorem 4.25 with examples (pp. 62–64).
It proves eventual polynomiality for repeated copies of a fixed pattern and
compares their leading coefficients. Its displayed codimension-two examples
already predict j=n-1 for repeated 21,132,321 and j=2n/3 for repeated 231,
with a stated unproved stabilization threshold. Those predictions are prior
work. The candidate's exact formula handles arbitrary unequal summands and
does not require a stabilization threshold. No equivalent law was found in
the inspected thesis passages.

[Vatter's live v2 paper](https://arxiv.org/html/2602.16355v2), Section 3,
was checked on 2026-09-12 and still states Problem 3.7. Its surrounding
discussion identifies structural necessary conditions for Wilf-equivalence
as a use of g2 information. That supports the relevance of an intrinsic
formula on separable permutations while leaving the universal task open
in the inspected sources. This is not a claim about an uninspected later
version or every current publication.

Additional live searches combined the exact Ray–West title or author names
with “direct sum”, “separable”, “statistics”, “codimension 2”, and
“direct-sum”. The relevant primary hits were consistent with the comparison
above; unrelated results were not used as evidence. The search did not
audit a complete citation chain, every thesis, or unpublished work. The
appropriate novelty statement is only that no equivalent composition law
was found in these bounded source checks on this date.

The contribution is a nontrivial structural refinement of the established
track formula. The source count does not immediately identify how witnesses
cross a sum cut: even the natural coordinate-only restriction fails at 213.
The submitted occurrence-based restriction and complete-support join
argument resolve that issue and yield a binary endpoint correction for
arbitrary summands. The separable statistic provides direct evaluation of
j, hence g2, from a natural decomposition of an entire established
permutation class. The decomposable equality classification is a further
coherent consequence. These belong together in one result note; they are
neither a renaming of the residual definition nor an arbitrary toy
specialization. No journal acceptance or exhaustive priority claim follows
from this review.

No unresolved mathematical gap was found in the exact frozen candidate.
The unresolved original problem and the out-of-scope deletion and general
equality conjectures remain explicitly unresolved. The next workflow step
is the runner's `check-math` integrity/provenance gate, followed by writing
only the accepted result-note scope. No manuscript or publication was
created by this referee job.
