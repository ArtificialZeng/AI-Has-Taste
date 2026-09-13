# Builder record

Role completed: 2026-08-30T04:42Z.

## Objective

Construct exact, reproducible evidence that extends the published finite
baseline while keeping the infinite existence question explicitly outside the
claim.

## Construction

1. Preserved the source prompt verbatim and wrote a quantified formal
   statement, including the positive half-length condition, empty-word
   convention, affine invariance, reflection, and the fixed-alphabet
   compactness implication.
2. Reproduced the published baseline
   \(g(\{0,1,2,4\})=62\) by complete exact prefix-tree traversal.
3. Enumerated the primitive normalized four-letter alphabets
   \(\{0<a<b<c\}\) with \(c\leq5\), modulo \(A\mapsto c-A\), obtaining seven
   classes.
4. Closed all seven exact ASF prefix trees. The new height-five entries are
   \(g(\{0,1,2,5\})=86\) and \(g(\{0,1,3,5\})=88\).
5. Enumerated all \(4^7=16{,}384\) four-symbol 2-uniform endomorphisms
   prolongable on a relabeled symbol 0 and found an abelian square ending by
   position 19 in every fixed point.
6. Screened scalar projections of the cited Rao--Rosenfeld
   \(\mathbb Z^2\)-weighted fixed point as a bounded positive-route
   diagnostic; all 12,176 primitive directions of height at most 100 were
   killed in the first 30,000 symbols.

## Builder outputs

- certificates/census_max5.json
- certificates/uniform2_no_go.json
- results/CENSUS_MAX5.md
- results/UNIFORM2_NO_GO.md
- results/H6_PROJECTION_DIAGNOSTIC.md
- paper/main.tex

All discovery computations used exact signed integers and deterministic
enumeration. No floating-point or probabilistic output was promoted to a
claim. The Builder makes no correctness determination; that is reserved for
the subsequent roles.
