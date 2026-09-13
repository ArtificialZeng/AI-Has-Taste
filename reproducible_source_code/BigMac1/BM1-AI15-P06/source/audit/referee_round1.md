# Referee round 1: structural proof and certificate audit

Date: 2026-08-29  
Role: independent referee, reconstructing from the definitions rather than
polishing the intended proof  
Scope: `problem/formal_statement.md`, `proof/structural_reduction.md`,
`proof/builder_notes.md`, and the finite-arithmetic verifier supporting the
sparse-gap theorem

## Bottom-line verdict

**The exact partial theorem survives this audit, and the current builder note
contains a valid strengthening:** every eleven-point equilateral configuration
in \(\ell_1^5\), if one exists, has at least fifteen positive consecutive
coordinate gaps, equivalently at least twenty total coordinate levels.  The
shorter structural note proves the intermediate bound twelve.  The five-path/
cut equivalence, real-feasible implies rational-feasible reduction,
double-centering Parseval identity, the exclusions of total gap counts ten and
eleven, the Naimark chain-length lemma, and the spectral-deficit exclusions of
gap counts twelve through fourteen are mathematically valid, including ties,
repeated cuts, complementary cuts, constant coordinates, and zero Naimark
rows.

This is **not** a proof that \(e(\ell_1^5)=10\).  No argument audited here
excludes configurations with fifteen or more positive gaps.  That is the fatal
gap for the original decision problem, although it is not a gap in the stated
sparse-stratum partial theorem.

The original verifier implementation used Python `assert` for decisive checks;
under `python -O` those checks disappeared while a `PASS` could still be
printed.  That was a **major certificate-semantics defect**.  It is resolved in
the versions audited below: the three target programs contain zero AST
`Assert` nodes and a 48-process normal/`-O`/`-I`/`-O -I` tamper matrix passed.
The sparse-gap script nevertheless certifies only the finite cut arithmetic;
the Parseval/rank-one/Naimark implications remain a human proof.

## Snapshot audited

The verdict above binds to the following SHA-256 hashes:

| File | SHA-256 |
|---|---|
| `problem/formal_statement.md` | `18235128b4f9aa47b968fcca27fc0e5d6f1ee763b23806b86b414878ba6d4d6a` |
| `proof/structural_reduction.md` | `cb65a4e438c85e1fc018a48086f90b97daf043c85c9801c6927f90b7939cd5e9` |
| `proof/builder_notes.md` | `b643104ca7b102dfee5c8312e370bb850fa9a49d7194ded3d7d474a1c5b1a4dc` |
| `certificate/verify_sparse_gap.py` | `6bbe60889ba2d5d8fc2ab9f62255237cf8f77b874f62f0efd446f7a4cf823ae5` |
| `certificate/sparse_gap_claim.json` | `00713a6115905a8fb56b2c4fc4c67654aacdace17236eb4cb4ee35ad469c37a6` |
| `certificate/verify_equilateral_witnesses.py` | `c05022faa74457ac3b57dfa53c6d2e5fa5c564a0745b02b48fd76412c3b8dc96` |
| `experiments/proof_cut_frame_audit.py` | `eb1c5627359cee682693ae904b249c16c42f01324790ca2be94d4dd7b3e0789a` |
| `audit/run_fail_closed_matrix.py` | `772a51b17f9c88fb391fa494433a913f0fdfba22415d8a16459ded175cbe9a54` |

Any subsequent mathematical or verifier edit requires a new audit or an
explicit diff review.

## Reconstruction from the definitions

### 1. Normalization, compactness, and five paths/cuts: PASS

Translation and positive scaling send the common distance to one and one
point to zero.  Then every remaining coordinate lies in \([-1,1]\), so the
normalized realization set is a closed subset of a finite cube.  No limiting
or tie stratum is lost.

For a weakly sorted coordinate, with a total-order refinement \(\pi\),
successive gaps \(g_t\ge0\), and prefixes
\(C_t=\{\pi(1),\ldots,\pi(t)\}\), direct telescoping gives

\[
 |x_r-x_s|=\sum_t g_t\,\delta_{C_t}(r,s).
\]

If values tie, the intervening gaps are zero.  Conversely, cumulative sums of
arbitrary nonnegative gaps reconstruct an ordered coordinate.  Thus the
formulation covers tied blocks of every size, a completely constant
coordinate, and every nonnegative boundary face.  A positive gap always
corresponds to a nonempty proper prefix.  Duplicate cut metrics in different
coordinates are retained as separate columns; replacing a cut by its
complement changes the centered vector's sign but not the cut metric.

The branch polytope is rational.  A feasible point with inclusion-minimal
positive support has linearly independent supported columns: a supported null
direction must have both signs because every cut column is nonzero and
nonnegative, and moving in one of the two directions until a coordinate first
vanishes contradicts minimality.  Solving the resulting full-rank rational
subsystem gives rational gaps.  Hence real feasibility is equivalent to
rational feasibility; no integrality claim is made.

### 2. Double centering and Parseval: PASS

With \(z_C=\mathbf 1_C\),
\(H=I-m^{-1}J\), and \(v_C=Hz_C\), the cut-distance matrix is

\[
 \Delta_C=z_C\mathbf1^T+\mathbf1z_C^T-2z_Cz_C^T,
 \qquad H\Delta_CH=-2v_Cv_C^T.
\]

The equilateral distance matrix is \(J-I\), and
\(H(J-I)H=-H\).  Therefore

\[
 \sum_a g_a v_{C_a}v_{C_a}^T=\tfrac12H.
\]

On \(\mathbf1^\perp\), the columns
\(a_a=\sqrt{2g_a}\,v_{C_a}\) consequently satisfy
\(AA^T=I_{m-1}\).  Rank gives at least \(m-1\) positive gaps.  This derivation
does not assume distinct cuts, generic coordinates, or nonzero zero-gap
columns; zero gaps are removed only after their contribution is known to be
zero.

### 3. Eleven labels, total gap count ten: PASS

For nonempty proper \(C,D\subset[11]\),

\[
 \langle v_C,v_D\rangle
 =|C\cap D|-\frac{|C||D|}{11}.
\]

It cannot vanish: otherwise the prime 11 divides \(|C||D|\), while both
factors lie in \(\{1,\ldots,10\}\).  This includes repeated cuts
(positive squared norm) and complementary cuts
(negative squared norm).  If exactly ten positive columns existed, the
\(10\times10\) Parseval matrix would be orthogonal, forcing every two distinct
columns to be orthogonal, a contradiction.

### 4. Eleven labels, total gap count eleven: PASS

For a \(10\times11\) Parseval matrix, \(P=A^TA\) is a rank-ten orthogonal
projection, so \(P=I-bb^T\) for a unit kernel vector \(b\).  Every off-diagonal
entry of \(P\) is nonzero by the preceding cut calculation, hence every
\(b_i\ne0\).  For any three distinct columns,

\[
 P_{ij}P_{ik}P_{jk}=-b_i^2b_j^2b_k^2<0.
\]

Three positive gaps in one coordinate give three strictly nested prefixes.
For \(S\subset T\),
\(\langle v_S,v_T\rangle=|S|(11-|T|)/11>0\), so the associated triple product
would be positive.  Thus a coordinate contains at most two positive gaps.
Five coordinates then contain at most ten, contradicting the assumed total
eleven.  Therefore the target dimension-five configuration, if it exists,
has at least twelve positive gaps.

The sharpness example is also correct: eleven selected vertices of the
\(\ell_1^6\) cross polytope have all 55 distances equal to two and exactly
eleven positive consecutive gaps.  This confirms that the conclusion
"total eleven forces ambient dimension at least six" is the correct endpoint.

### 5. Naimark chain-length lemma: PASS; zero-row repair verified

For \(t\) positive gaps and frame dimension \(m-1\), the complementary
projection \(Q=I-A^TA\) has rank \(r=t-(m-1)\).  Write
\(Q_{ij}=\langle y_i,y_j\rangle\) in \(\mathbb R^r\).  Two distinct positive
gaps in one coordinate have nested cuts, so
\(\langle y_i,y_j\rangle=-P_{ij}<0\).

If a coordinate supplies \(h\ge2\) gaps, none of its \(y_i\) can be zero.
For nonzero vectors with all pairwise products negative, a dependence cannot
have mixed signs: the inner product of the two positive combinations obtained
by moving negative terms across would be both a squared norm and strictly
negative.  Two independent one-signed dependences can be combined to make a
mixed-sign dependence, so the dependence space has dimension at most one.
Thus \(h-1\le r\), or \(h\le r+1\).  If \(h=1\), the bound is immediate; if
\(r=0\), two gaps are already impossible from \(Q_{ij}=0=-P_{ij}<0\).

This treats the requested zero-complement-row edge case.  Both current proof
notes now split off the one-gap case and explain why a zero complement row
cannot share a coordinate with another gap.  The earlier local wording gap is
resolved.

For \(m=11,t=12\), \(r=2\), so each of five coordinates has at most three
positive gaps.  The three listed partitions of 12 with five nonnegative parts
bounded by 3 are exhaustive:
\((3,3,2,2,2)\), \((3,3,3,2,1)\), and \((3,3,3,3,0)\).

### 6. Private rational direction at \(t=12\): PASS, with one local omitted sentence

For three gaps from one coordinate, the three rank-two Naimark vectors are
pairwise obtuse and span \(\mathbb R^2\); three nonzero collinear vectors
cannot have all three pairwise products negative.  Their dependence is
one-dimensional and one-signed.  To justify the builder's word "positive"
rather than merely "nonnegative", add: if a dependence coefficient vanished,
taking the inner product with the omitted vector would make zero equal a
strictly negative sum.  Thus all three coefficients are strictly positive.

Vectors in \(V\) orthogonal to the other nine frame columns correspond via
the injective map \(u\mapsto A^Tu\) to vectors supported on the chosen three
indices in \(\ker Q=\operatorname{range}(A^T)\).  The supported kernel is the
one-dimensional Naimark dependence.  Hence the other nine rational centered
cut vectors have rank nine and their orthogonal complement is a rational
line.  Applying the frame identity to a primitive integral representative
of that line gives four strictly decreasing block values and

\[
 g_i=\frac{c_i-c_{i+1}}{2\sum_{s\in S_i}u_s}.
\]

The denominator is positive because it is the corresponding positive frame
inner product.  The zero-prefix-sum and private-direction orthogonality
claims follow by successive differences.  The displayed contingency matrix
has total 11, positive row and column sums, and the two stated null vectors;
it is correctly presented only as a counterexample to an insufficient
rank-only obstruction, not as an equilateral witness.

### 7. Spectral-deficit strengthening to total gap count fifteen: PASS

This section occurs in the current `proof/builder_notes.md` but not yet in the
shorter `proof/structural_reduction.md`.  It is a genuine strengthening of the
intermediate twelve-gap theorem.

For the columns from coordinate \(j\), let \(G_j=A_j^TA_j\) and
\(B_j=A_jA_j^T\).  A strict prefix chain gives linearly independent centered
cut vectors.  Since \(\sum_jB_j=I\), each \(0\le B_j\le I\), so every nonzero
eigenvalue of \(G_j\) lies in \((0,1]\).  Thus
\(\varepsilon_j=\ell_j-\operatorname{tr}G_j\ge0\), and tracing the Parseval
identity gives exactly

\[
 \sum_{j=1}^5\varepsilon_j=t-10.
\]

For one chain, normalize its columns and let \(R\) be their correlation
matrix.  Its entries have the Markov product form
\(R_{ab}=r_a\cdots r_{b-1}\).  If
\(G=DRD\le I\) and \(x_i=D_{ii}^2\), testing on \(D\mathbf1\) gives
\(x^TRx\le\mathbf1^Tx\).  Cauchy--Schwarz in the positive-definite
\(R\)-inner product then yields
\(\operatorname{tr}G=\mathbf1^Tx\le\mathbf1^TR^{-1}\mathbf1\).  Expanding
the exact Markov precision form

\[
 y^TR^{-1}y=y_1^2+\sum_i\frac{(y_{i+1}-r_i y_i)^2}{1-r_i^2}
\]

at \(y=\mathbf1\) gives the weight-free bound

\[
 \varepsilon_j\ge\sum_i\frac{2r_i}{1+r_i}.
\]

The adjacent-correlation product is the endpoint correlation and is at least
\(1/10\).  The function
\(s\mapsto2e^s/(1+e^s)\) is increasing and strictly convex for \(s<0\), so
Jensen gives

\[
 \varepsilon_j\ge
 \frac{2(\ell_j-1)}{10^{1/(\ell_j-1)}+1}\qquad(\ell_j\ge2).
\]

The rational lower bounds
\(c_0=c_1=0,c_2=2/11,c_3=24/25,c_4=19/10,c_5=23/8\) are valid.  I checked
the three radical comparisons by the stated exact powered inequalities, and
their successive increments
\(0,2/11,214/275,47/50,39/40\) are increasing.  Hence the one-unit exchange
argument makes the balanced length distribution minimize the sum of these
bounds.  For \(t=12,13,14\), the respective lower sums are

\[
 \frac{678}{275}>2,\qquad
 \frac{892}{275}>3,\qquad
 \frac{1106}{275}>4,
\]

contradicting \(\sum_j\varepsilon_j=t-10\).  The earlier argument excludes
\(t\le11\), so \(t\ge15\), equivalently \(\sum_jq_j\ge20\).  At \(t=15\)
the balanced pattern \((3,3,3,3,3)\) is not excluded; the stopping point is
therefore explicit.

The final builder version further adds
\(c_6=193/50<10/(10^{1/5}+1)\), certified by
\(307^5>10\cdot193^5\).  I independently enumerated all 32 sorted partitions
of 15 into five parts between 0 and 6 using exact `Fraction` arithmetic.  The
only patterns whose rational deficit sum is at most 5 are

\[
 (3,3,3,3,3)\quad\text{and}\quad(4,3,3,3,2),
\]

with costs \(24/5\) and \(2729/550\).  The next cheapest pattern is
\((4,4,3,2,2)\), with cost \(1409/275=2818/550>5\).  Thus the claimed
two-pattern reduction of the first surviving stratum is exact; neither
pattern is claimed feasible.

No endpoint, zero-chain, or equality case is hidden here: \(\ell=0,1\) use
deficit zero; strict positive gaps make \(R\) positive definite; and the
Naimark bound limits the only needed chain lengths to 3, 4, and 5 for
\(t=12,13,14\), respectively.

### 8. Centrally symmetric subclass: PASS; center-point repair verified

The current proof now first excludes the center itself: if a nontrivial
centrally symmetric equilateral set contained 0 and \(v\), it would also
contain \(-v\), but the two distances \(\|v\|\) and \(2\|v\|\) could not
share a positive common value.  Equality in both
\(\|v_i-v_j\|_1=\|v_i\|_1+\|v_j\|_1\) and
\(\|v_i+v_j\|_1=\|v_i\|_1+\|v_j\|_1\) forces every coordinate product
\(v_{i,k}v_{j,k}\) to be both nonpositive and nonnegative, hence zero.
Supports are disjoint and \(s\le d\); equality gives the cross polytope.
The fixed cross-polytope nonextension calculation is also exact.

### 9. At most two levels per coordinate: PASS

For level difference \(w_k\ge0\) and signs \(\varepsilon_{r,k}\), the map
\(u_{r,k}=\sqrt{w_k}\varepsilon_{r,k}\) satisfies, pair by pair,

\[
 \|u_r-u_s\|_2^2=4\sum_{k:\varepsilon_{r,k}\ne\varepsilon_{s,k}}w_k
 =4\|x_r-x_s\|_1.
\]

Coordinates with one level have \(w_k=0\) and cause no problem.  A Euclidean
equilateral set in dimension at most \(d\) has at most \(d+1\) points, so this
subclass cannot contain eleven points in dimension five.

## Independent exact checks

I did not import or call the existing proof audit as a library.  A separate
standard-library `Fraction` program checked:

- all 55 pairs in a deliberately unsorted, tie-rich eleven-value path and its
  cumulative reverse reconstruction;
- all 320 feasible \((|C|,|D|,|C\cap D|)\) types for nonorthogonality;
- the integer-scaled identity
  \((11I-J)\Delta_C(11I-J)=-2ww^T\) for a nontrivial four-element cut;
- the exact singleton-cut Parseval decomposition and all 165 rank-plus-one
  triple products;
- the exact Markov-correlation inverse on rational parameters, all 45 endpoint
  correlation bounds, the three powered radical comparisons, the discrete
  convexity increments, and the three spectral-deficit budgets excluding
  \(t=12,13,14\);
- 496 pairs of five-coordinate Boolean rows with rational level weights,
  including a zero weight;
- 96 small integer central-symmetry equality pairs in three coordinates;
- all 55 distances and the eleven positive gaps in the serialized
  \(\ell_1^6\) sharpness witness.

The corrected run printed:

```text
INDEPENDENT_REFEREE_CHECK_OK
tie_rich_path_pairs=55 cut_intersection_types=320
double_centering_scaled_integer=PASS
singleton_rank_plus_one_triples=165
two_level_pairs=496 central_integer_pairs=96
d6_witness_positive_gaps=11
```

The first attempt incorrectly guessed a JSON key and failed with
`KeyError: 'l1_6_eleven_points'`; after reading the actual schema and selecting
the record named `sharp_q11_example_in_l1_6`, the run above passed.  This failed
attempt is recorded to avoid presenting only a sanitized transcript.

The core check is reproducible with this compact command:

```bash
python3 - <<'PY'
from fractions import Fraction as F
from itertools import combinations, product
import json
m=11; L=range(m)
def de(C,r,s): return int((r in C)!=(s in C))
def ip(C,D): return F(len(C&D))-F(len(C)*len(D),m)
v=list(map(F,(2,-1,-1,4,0,2,7,4,0,0,7)))
o=sorted(L,key=lambda i:(v[i],i)); g=[v[o[i+1]]-v[o[i]] for i in range(10)]
C=[set(o[:i+1]) for i in range(10)]
for r,s in combinations(L,2):
    assert abs(v[r]-v[s])==sum((g[i]*de(C[i],r,s) for i in range(10)),F(0))
types=0
for a in range(1,m):
 for b in range(1,m):
  for u in range(max(0,a+b-m),min(a,b)+1): assert m*u-a*b; types+=1
C0={0,2,5,7}; B=[[m*int(i==j)-1 for j in L] for i in L]
D=[[de(C0,i,j) for j in L] for i in L]
w=[m*int(i in C0)-len(C0) for i in L]
assert [[sum(B[i][r]*D[r][s]*B[s][j] for r in L for s in L) for j in L] for i in L] == [[-2*w[i]*w[j] for j in L] for i in L]
for r in L:
 for s in L: assert sum((m*int(r==i)-1)*(m*int(s==i)-1) for i in L)==m*(m*int(r==s)-1)
W=[F(0),F(1,3),F(2),F(5,7),F(11,4)]; R=list(product((-1,1),repeat=5))
for a,b in combinations(R,2): assert sum(W[k]*(a[k]-b[k])**2 for k in range(5))==4*sum(W[k] for k in range(5) if a[k]!=b[k])
data=json.load(open('certificate/equilateral_witnesses.json'))
X=next(x['points'] for x in data['witnesses'] if x['name']=='sharp_q11_example_in_l1_6')
for a,b in combinations(X,2): assert sum(abs(x-y) for x,y in zip(a,b))==2
q=sum(sum(y[i+1]>y[i] for i in range(10)) for k in range(6) for y in [sorted(x[k] for x in X)])
assert q==11
print('INDEPENDENT_REFEREE_CHECK_OK', types, q)
PY
```

The inline diagnostic uses `assert`, so it is intentionally **not** the
fail-closed release verifier and must not be run with `-O`.  Its role is only
an independent derivation/evaluator cross-check.

## Fail-closed certificate audit

Historical verdict: **MAJOR, RESOLVED.**  The earlier versions of
`certificate/verify_sparse_gap.py`,
`certificate/verify_equilateral_witnesses.py`, and
`experiments/proof_cut_frame_audit.py` placed decisive predicates in Python
`assert` statements.  Optimization mode could erase those predicates and
still reach a `PASS` print.  Outputs from those old script versions are not
valid release evidence.

Current verdict: **PASS for the stated finite-arithmetic scope.**  The current
scripts use explicit `require`/exception/nonzero-exit logic.  The command

```bash
python3 audit/run_fail_closed_matrix.py
```

completed with status `PASS`, zero AST assert nodes in all three target
programs, 12 cases, 4 interpreter modes, and 48 processes.  Valid sparse,
witness, and frame inputs passed under normal, `-O`, `-I`, and `-O -I`.
Tampered inputs (missing/changed \(m\), changed \(d\), changed gap-count list,
missing witness points, changed witness dimension/distance/coordinate, and
frame audit changed to \(m=12\)) all exited nonzero, printed `FAIL`, and never
printed `PASS` in all four modes.  Runner SHA-256:

```text
772a51b17f9c88fb391fa494433a913f0fdfba22415d8a16459ded175cbe9a54
```

Direct positive runs of `certificate/verify_sparse_gap.py` under all four
modes also passed with 320 intersection types and 55 nested types.  Its output
correctly says:

```text
scope: finite arithmetic core; human Parseval/Naimark implication not machine-checked
```

Accordingly, the script does **not** independently reconstruct a putative
equilateral configuration, nor does it machine-prove the Parseval projection
argument.  The theorem is supported by the human proof plus a finite-arithmetic
cross-check, not by a complete SAT/SMT/proof-assistant certificate.  The label
`certified_minimum_positive_gaps` in its JSON output must always be read with
that scope line; describing this script alone as certifying the whole theorem
would exceed the artifact.

## Issue ledger

| ID | Severity | Location | Verdict and required action |
|---|---|---|---|
| R1-FULL | fatal for the original problem | after the spectral-deficit theorem | No exclusion of total gap count \(\ge15\), and no exact 11-point witness.  Therefore neither `PROVED` nor `DISPROVED` is justified.  Keep the terminal claim partial/open unless later exact work closes this. |
| R1-CERT-HIST | major, resolved | old versions of the three audit/verifier scripts | Python `assert` was optimization-removable.  Never cite outputs from the old hashes.  The current explicit checks and 48/48 matrix repair this. |
| R1-CERT-SCOPE | major claim guard, currently respected | `certificate/verify_sparse_gap.py` and `experiments/proof_cut_frame_audit.py` | The first checks finite cut arithmetic for the twelve-gap intermediate result; the second also checks finite spectral arithmetic.  Human linear algebra supplies the Parseval/rank-one/Naimark/spectral implications.  Do not call either script a full proof certificate. |
| R1-CS-CENTER | local, resolved | `proof/structural_reduction.md` centrally symmetric subsection | The current note now excludes the center point before writing \(S=\{\pm v_i\}\). |
| R1-NAI-ZERO | local, resolved | `proof/builder_notes.md` chain-length lemma | The current note splits off \(h=1\) and shows \(h\ge2\) forces every complement row nonzero. |
| R1-PRIVATE-POS | local | `proof/builder_notes.md` private-direction lemma, near line 292 | Add the inner-product argument excluding a zero coefficient in the one-signed dependence before saying all coefficients are positive. |
| R1-FORMAL-TYPO | expository | `problem/formal_statement.md` line 25 | Replace `\forall,1\le r<s\le11` by a grammatically quantified statement such as `\forall\,1\le r<s\le11`. |
| R1-MAX | expository | `problem/formal_statement.md` lines 14--34 | The text notes but does not cite/prove boundedness before using `max`.  This does not affect the 11-point decision problem; add the standard finite-dimensional finiteness fact if the global definition is retained. |
| R1-SYNC-15 | local consistency | `proof/structural_reduction.md`, `proof/proof_dag.md`, `TASK_STATUS.json` | These artifacts still report the older bound twelve while the current builder note proves fifteen.  This is conservative rather than an overclaim, but synchronize them before releasing the stronger result. |

There are no other fatal or major mathematical defects in the audited partial
theorem.  In particular, ties, repeated cuts, complementary cuts, constant
coordinates, the total-gap \(10/11\) boundary cases, and zero complement rows
do not produce an omitted branch.

## Claim-versus-evidence audit

Claims supported by the audited proof:

1. exact five-order/fifty-gap LP equivalence, including zero gaps;
2. real feasibility if and only if rational feasibility;
3. the exact Parseval cut-frame identity;
4. at least fifteen positive gaps, hence at least twenty total coordinate
   levels, for any putative eleven-point \(\ell_1^5\) equilateral set;
5. the general chain-length-versus-frame-excess bound;
6. the centrally symmetric \(2d\) bound and the two-level \(d+1\) bound;
7. the conditional private-direction conclusions inside the \(t=12\) stratum;
8. the spectral-deficit inequality and the exact exclusion of
   \(t=12,13,14\).

Claims not supported by these artifacts:

1. \(e(\ell_1^5)=10\);
2. existence of an eleven-point counterexample;
3. infeasibility of the first surviving fifteen-gap distribution;
4. exhaustive coverage of the five-chain order types;
5. a complete machine-checked proof of the sparse-gap theorem;
6. novelty or publication readiness of the partial theorem.

`TASK_STATUS.json` and the limitations in both proof notes correctly keep the
full problem open.  The placeholder `paper/main.tex` contains no mathematical
claim and therefore does not overstate the certificate, but it is not a
manuscript and should not be released as one.

## Proof-assistant disclosure

No proof assistant was used.  This audit used exact rational/integer
calculations and independent human linear-algebra reconstruction.
