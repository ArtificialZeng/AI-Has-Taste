# Proof audit

Full-original-problem status: **OPEN AFTER SEARCH**.

Finite mathematical status: **PASS** for
\(\mathbf C_{P_{11}}=10/11\); this theorem and its certificate are unchanged.

## Statement

- The source and locked formal operator agree: centered closed graph balls,
  absolute values inside averages, one count per undirected edge.
- Quantifiers include every real-valued input on exactly 11 vertices.
- Constant/zero-variation inputs are handled separately.
- The full all-\(n\) conjecture is not claimed.

## Reductions

- Absolute-value reduction checked in both supremum directions.
- Translation quotient checked in both directions by shifting arbitrary
  anchored data upward.
- Scaling and compactness checked in edge-difference coordinates.
- Output sign formula and telescoping coefficient signs checked.
- Active-radius ties are covered by enumerating all positive radii.
- Negative mixtures use the correct reversed inequality direction.

## Exact certificate

- Upper target is the rational number \(10/11\).
- Canonical enumeration: 5,874,849 chambers.
- Serialized pure-radius slots: 45,011,088.
- Exact rational-mixture exceptions: 10; all weights are positive and have
  the required total mass.
- Independent verifier imports no generator/discovery module, uses standard
  library `Fraction`, regenerates chambers by a distinct mask/odometer method,
  reconstructs vertex measures, and checks cumulative edge flux.
- Full verifier result: VERIFIED.
- Five fail-closed corruption classes were deliberately tested and rejected.

## Sharpness and equality

- Endpoint point mass has input variation 1 and output variation \(10/11\).
- Thus the bound is sharp and attained on \(P_{11}\).
- No exhaustive classification of all equality cases is claimed.

## Adversarial check

An independent direct evaluator checked 227,429 nonconstant ternary,
structured, and seeded rational inputs. Its maximum was exactly \(10/11\);
no strict over-target candidate was retained. This diagnostic is not used in
the proof.

## Reproduction status

- Clean temporary-directory verifier rerun: PASS. The fresh directory
  contained only the independent verifier and the three certificate files;
  it reproduced all chamber, slot, exception, mass, and flux counts.
- Final release manifest: generated after the manuscript/code/artifact freeze
  and independently rechecked against every listed file.
- LaTeX/citation/PDF/ZIP audits: PASS.
- Proof assistant: none used.

## Arbitrary-n follow-up

- **PASS (partial theorem):** for every \(n\), the desired bound holds when
  the signs of the nonzero output differences have at most one change.  The
  peak and trough proofs give explicit edge-flux certificates and include
  clipped boundary balls and zero differences.
- **PASS (input corollary):** monotone \(|f|\) gives monotone maximal output,
  hence the sharp endpoint estimate; equality in the nonconstant
  nondecreasing cone is also checked.
- **PASS (structural reduction):** the convex hull of centered-ball measures
  at a vertex is exactly the set of fixed-mass radial nonincreasing shell
  densities.  Its minimax dual is the existing chamber problem, so no full
  theorem is inferred from the reformulation.
- **PASS (exact obstruction):** an independent `Fraction` checker verifies
  the \(P_6\) local-rule flux \(13/15>5/6\) and the nonlocal repair
  \(23/30<5/6\).  This refutes only the proposed local rule, not the
  conjecture.
- **PASS (symmetric diagnostic):** 517,609 exact nonconstant inputs over
  eleven dimensions were searched, and a separate literal-average program
  replayed all retained maxima.  No violation was found; the finite negative
  result is explicitly excluded from the proof.
- **OPEN (fatal for full claim):** no global selection theorem coordinates
  the negative radial densities for output sign patterns with two or more
  turns, and no exact counterexample family was found.

The full problem is assessed at 30% solved.  Confidence in the retained exact
partial results is 0.99; confidence that continued work along the exhausted
project routes closes the full problem is 0.42.  These workflow figures do
not occur in the manuscript or PDF.
