# Fresh mathematical referee report

## Frozen scope and provenance

This review concerns exactly the frozen `result-note` claim in `claim.json`:
the (d=4) Hypercube Inequality holds whenever

\[
|\operatorname{supp}(x)|\leq 5,
\]

and equality within that restricted domain occurs exactly when the support is
contained in a cube facet.  The claim explicitly does **not** cover supports of
size at least six and leaves the original universal claim (HC4) unresolved.

I reviewed snapshot
`b42d07e55381f1aed86686332fad090211b685092fa115590503ef0c9cb29a06`
under fresh referee job
`bigMac-00022-p03-referee-3fa971e80f3d`.  I recomputed all snapshot file
SHA-256 hashes; every hash agreed with `audit/snapshot.json`, including the
immutable `source.md` hash
`68215e4f5db3f2e45b59e4565f391a19bd6956fe740e2cd2400cf38fce32aeb7`.

## Reconstruction of the decisive argument

Write (T=\operatorname{supp}(x)).

1. If (|T|\leq4), every squarefree five-variable product in (P_4)
   vanishes, so (P_4=0) and the claimed inequality follows from (Q_4\geq0).
2. If (|T|=5), enumerate (T=\{v_0,\ldots,v_4\}) and put
   (y_j=x_{v_j}>0).  Exactly one term of (P_4) can survive.  Thus the gap is
   exactly
   \[
   D_T(y)=\prod_{r=1}^4\prod_{b=0}^1
      \left(\sum_{j:(v_j)_r=b}y_j\right)
      -\operatorname{Vol}(T)y_0y_1y_2y_3y_4
       (y_0+\cdots+y_4)^3.
   \]
3. If (T) is affinely dependent, its determinant volume is zero, so this is
   a product of eight nonnegative linear forms.
4. If (T) is affinely independent, each coordinate assumes both bit values
   on (T); otherwise (T) would lie in a three-dimensional cube facet.
   Hence all eight restricted facet factors are nonempty.  Coordinate
   permutations and independent coordinate complements form all 384 cube
   symmetries, preserve the eight factors up to permutation, and preserve the
   determinant absolute value.  Exact enumeration partitions all
   \(\binom{16}{5}=4368\) supports into 27 orbits.  Ten orbits (1,360
   supports) have volume zero.  For every one of the 17 independent orbits
   (3,008 supports), direct integer expansion of (D_T) has no negative
   coefficient and has at least one positive coefficient.  Consequently
   (D_T\geq0) on the nonnegative orthant and (D_T>0) when all five (y_j)
   are positive.

This proves the inequality for the entire frozen support range without a
limit, compactness, division, or positivity-extension step.

For equality in the dependent cases (including supports of size at most four),
(P_4=0), while

\[
Q_4=0
\quad\Longleftrightarrow\quad
\sum_{v\in F}x_v=0\text{ for some facet }F
\quad\Longleftrightarrow\quad
T\subseteq V_4\setminus F.
\]

The complement of a cube facet is its opposite facet.  Conversely, support in
a facet makes the opposite facet factor zero and also forces (P_4=0).
Independent five-point supports give strict inequality by the positive
coefficient argument.  This includes the zero vector, whose empty support is
contained in every facet.

## Checks actually performed

- Recomputed all six snapshot hashes and matched the recorded snapshot.
- Ran
  `python3 evidence/verify_five_supports.py --check evidence/five_support_certificate.json`.
  It regenerated the certificate byte-for-byte with SHA-256
  `33e1aad46c7d3f20c2eb24e12a5969af20935311185f49c8dd883b1ece44cb93`.
  It reported 4,368 supports, 27 orbits, 17 independent orbits, 10 dependent
  orbits, and no negative coefficients.
- Performed a separate exact computation that did not load the stored
  certificate.  It computed each volume as a (4\times4) determinant of
  difference vectors using fraction-free Bareiss elimination, rather than the
  supplied (5\times5) Leibniz routine.  It then expanded the restricted gap
  directly for every one of the 4,368 supports, not merely orbit
  representatives.  All 3,008 independent supports had a nonempty gap with
  every nonzero coefficient positive; there were no failures.  The independent
  volume census was reproduced as
  \[
  \#\{\operatorname{Vol}=0,1,2,3\}=(1360,2672,320,16).
  \]
- Independently repartitioned the five-subsets under tuple-based cube actions.
  This again gave 27 orbits, with size census
  (16^2,48^1,64^4,96^4,192^{13},384^3), split into 17 independent and 10
  dependent orbits.
- Compared every displayed orbit representative, orbit/stabilizer size,
  volume, term count, and coefficient range in `five_support_proof.md` with
  the serialized certificate; they agree.
- Exhausted the set-theoretic support cases of sizes zero through five to check
  that vanishing of a facet factor is equivalent to containment of the support
  in the opposite facet.  No exceptional boundary case was found.

The determinant convention is correct: the verifier uses the matrix whose
rows are ((v_j,1)), which is the transpose of the source's displayed matrix,
so the absolute determinant is unchanged.  The five variables are positive
precisely because they index the support; this justifies strictness in the
independent case.

## Source comparison and contribution

The frozen source comparison identifies the (d=3) theorem as the nearest
established full result and records that the cited primary source leaves
(d\geq4) open.  It found no separate primary-source resolution of this exact
five-support classification as of 2026-09-09, while explicitly disclaiming a
priority guarantee.  The present result is not being represented as a
resolution of (HC4).

Within its stated scope, this is a complete exact boundary-layer theorem, not
a sampled computation or an arbitrary numerical slice: it covers all 4,368
five-subsets, includes exact determinant normalization, supplies serialized
integer polynomial identities, and classifies equality.  Independent
five-sets genuinely span four dimensions, so their inequalities do not follow
merely by placing the support in the already proved (d=3) case.  The result
is a reproducible base case and boundary benchmark for six-support searches or
any later compression argument.  This meets the frozen source's stated
meaningful local-exit criterion.  The bounded literature comparison supports
the note's conservative wording but is not a claim of novelty or priority.

## Limits and verdict

Nothing reviewed supplies a bridge from five-point supports to supports of
size six or larger.  The original universal (d=4) inequality therefore
remains unresolved, and any manuscript must preserve that limitation.  The
literature screen is bounded and cannot guarantee priority.

**Verdict: ACCEPT the exact frozen scope as a `result-note`; retain original
status `unresolved`.**  Scope match, mathematical correctness, exact evidence,
equality classification, and subsidiary contribution all pass.
