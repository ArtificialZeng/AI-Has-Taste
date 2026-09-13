# Referee round 1 diff audit: root synchronization edits

Date: 2026-08-29  
Role: independent narrow diff referee  
Baseline: the file versions bound in `audit/referee_round1.md`  
Scope: only the root-agent synchronization edits requested after round 1

## Verdict

**PASS.**  The synchronization edits correctly repair every targeted local
issue and propagate the already-audited spectral-deficit result without
strengthening it beyond the evidence.  I found no fatal, major, or local
mathematical error in the changed passages.

Specifically:

1. `problem/formal_statement.md` now proves that the maximum defining
   \(e(\ell_1^n)\) is finite and fixes the malformed quantifier in (T).
2. `proof/builder_notes.md` now excludes zero coefficients before concluding
   that the private-direction Naimark dependence is strictly positive.
3. `proof/structural_reduction.md` accurately summarizes the already-audited
   \(q\ge15\) theorem and the two surviving \(q=15\) gap-count patterns.
4. `proof/proof_dag.md`, `proof/gap_ledger.md`, and `TASK_STATUS.json` are
   mutually consistent: the full problem remains open, all counts
   \(q\le14\) are excluded, and at \(q=15\) only
   \((3,3,3,3,3)\) and \((4,3,3,3,2)\) survive the proved reduction.

This diff audit did not inspect, execute, or modify any verifier, frame audit,
runner, log, or newly generated \(q=15\) artifact.  It modifies only this
report.

## Hash binding

“Old” means the prior SHA-256 explicitly bound in
`audit/referee_round1.md`.  That report did not bind pre-synchronization hashes
for `proof/proof_dag.md`, `proof/gap_ledger.md`, or `TASK_STATUS.json`; those
entries are therefore marked **not recorded**, rather than reconstructed or
guessed.

| File | Prior referee-bound SHA-256 | Current SHA-256 | Verdict |
|---|---|---|---|
| `problem/formal_statement.md` | `18235128b4f9aa47b968fcca27fc0e5d6f1ee763b23806b86b414878ba6d4d6a` | `13db7a6d4548c38d1e6c96667aeb3182553e7be99bf11529d28aa716ba52b855` | PASS |
| `proof/structural_reduction.md` | `cb65a4e438c85e1fc018a48086f90b97daf043c85c9801c6927f90b7939cd5e9` | `2d667b17226caff40981668115f8ac58104c09957ca7c7ce9408345b5d7b935d` | PASS |
| `proof/builder_notes.md` | `b643104ca7b102dfee5c8312e370bb850fa9a49d7194ded3d7d474a1c5b1a4dc` | `bedfa516717519377349b92d5b96ab6a40c8c5d7d0594e4f4875afe9b1d44ac0` | PASS |
| `proof/proof_dag.md` | not recorded | `853fb6eed641860dd664758dff8010353ad5fbe92c7af6922cc70d9d80405031` | PASS |
| `proof/gap_ledger.md` | not recorded | `76fd90304da89eb8048d98820b760c5ef9842491a8e90c53ae6b8c04255c04ee` | PASS |
| `TASK_STATUS.json` | not recorded | `fbe0051f49488fada1aaad01d0cfe97e329c4c7b733bedb3106231c8e562df69` | PASS |

The baseline referee report itself has SHA-256
`a36d91629434fc21ff48ca4d17a5fd27e159937f9fbe3b1f0bdeadca69186a6d`.

## Itemized reconstruction

### 1. Finiteness of the maximum and target quantifier: PASS

After normalizing the common distance to one and translating one member of an
equilateral set to the origin, every point lies in the closed unit ball of the
norm: the translated origin has norm zero and every other point has norm one.
Open norm balls of radius \(1/2\) around distinct points are disjoint, since a
point in two of them would make the two centers have distance strictly less
than one.  Their union lies in the open ball of radius \(3/2\).  Lebesgue
volume is translation invariant and scales by the \(n\)-th power of the
radius, hence

\[
 |S|\operatorname{vol}(\tfrac12B)
 \le \operatorname{vol}(\tfrac32B),
 \qquad |S|\le3^n.
\]

Thus the possible positive integer cardinalities are bounded, so the maximum
is well defined.  No compactness, boundary, or strict/open-ball issue is
hidden in the packing argument.  The corrected notation
`\forall\,1\le r<s\le11` now has the intended quantifier scope.  Together
with the ten-point cross polytope, the stated equivalence of (T) and
\(e(\ell_1^5)=10\) is valid.

### 2. Strict positivity in the private-direction lemma: PASS

The earlier argument already showed that the one-dimensional dependence of
the three pairwise obtuse Naimark vectors can be oriented with all coefficients
nonnegative.  The inserted sentence correctly excludes a zero coefficient.
If, say, \(\alpha_k=0\), taking the inner product of
\(\sum_i\alpha_i y_i=0\) with the omitted nonzero vector \(y_k\) gives

\[
 0=\sum_{i\ne k}\alpha_i\langle y_i,y_k\rangle<0,
\]

because the dependence is nonzero, at least one remaining coefficient is
positive, and all cross inner products are strictly negative.  Hence all
three coefficients are strictly positive, exactly as used later in the block
monotonicity and positive-denominator argument.

### 3. Structural synchronization of the spectral theorem: PASS

The new structural section is a faithful summary, not a new proof endpoint.
It states the exact deficit budget
\(\sum_j\varepsilon_j=q-10\), the Markov/Jensen chain bound, the rational
budgets excluding \(q=12,13,14\), and therefore \(q\ge15\) and at least twenty
total coordinate levels.  It also states exactly the two patterns surviving
at \(q=15\):

\[
 (3,3,3,3,3),\qquad(4,3,3,3,2).
\]

These are the endpoints independently reconstructed in round 1.  The summary
properly routes the full Markov inverse and radical comparisons to
`proof/builder_notes.md`, identifies the finite audit as checking only
integer/rational arithmetic, and explicitly says that the linear-algebraic
implications remain a human proof.  Its limitation section correctly leaves
all surviving and denser strata open.

### 4. Dependency graph: PASS with scope qualification intact

The dependency graph now contains the complete implication chain from the
five-path reduction through \(q\ge15\) and the two-pattern reduction.  It does
not confuse the intermediate \(q\ge12\) theorem with the stronger endpoint.
Its closing sentence preserves the trust boundary: independently checked
finite arithmetic does not turn the frame implications into a machine proof.

The phrase “finite arithmetic in steps 4, 5, 7, 10, and 11” should be read
literally as the finite arithmetic portions of those steps.  The general
rank-one projection, Markov inverse, Cauchy--Schwarz, Jensen, and frame
implications remain the human arguments already audited; the following line
states this explicitly.  Therefore the wording does not overclaim complete
machine verification.

### 5. Gap ledger: PASS

The ledger retains the global fatal gap G01 and the open exhaustive-enumeration
gap G03.  It marks the historical verifier-semantic issue resolved, adds the
spectral strengthening as resolved G06, and records the two surviving
\(q=15\) patterns as fatal open gap G07.  G01 and G07 overlap intentionally:
G01 is the global target, while G07 names its first exact unresolved stratum.
No resolved item is being used to claim the full conjecture.

### 6. `TASK_STATUS.json`: PASS

The JSON parses successfully.  Its state remains `running`,
`original_prompt_complete` remains `false`, and the summary/evidence accurately
report:

- the problem remains open;
- every putative counterexample needs at least fifteen positive gaps and
  twenty coordinate levels;
- only two patterns survive at the first boundary stratum;
- verifier outputs certify only their recorded finite scopes;
- the integer-box result is a separate finite theorem, not an unrestricted
  real theorem.

The reported `solution_percent` is not being substituted for a proof, and the
mathematical claims supporting the increased `confidence_percent` are listed
in the evidence array.  No terminal state, unrestricted counterexample, or
complete proof is asserted.

## Remaining limitations unaffected by this diff

- Neither surviving \(q=15\) pattern has been excluded or realized.
- No branch-complete SAT/LP/Farkas enumeration exists for the unrestricted
  real problem.
- The exact audit programs do not constitute a complete proof-assistant
  formalization of the spectral theorem.
- No proof assistant was used.

These are pre-existing research limitations, not defects introduced by the
synchronization diff.
