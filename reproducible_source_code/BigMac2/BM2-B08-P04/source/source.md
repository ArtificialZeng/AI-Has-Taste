# bigMac-00008-p04 — 三变量 v-number 反例的次数最小性

## Immutable source statement

Let `I` range over all `m=(x,y,z)`-primary monomial ideals in `K[x,y,z]` whose
minimal monomial generating set has at most four members, each of total degree
at most four.  Using the v-number and integral closure conventions of
arXiv:2609.05044v1, prove or disprove

`v(overline(I)) <= v(I)`

for every such `I`.

The field and any characteristic dependence must be stated.  The degree bound
is on every minimal generator, not on an arbitrary redundant presentation.

## Primary boundary

*A comparison of the v-number of a monomial ideal and its integral closure*,
arXiv:2609.05044v1, Theorem 3.2 and Example 3.3.  Positive results include all
two-variable monomial ideals and three-variable equigenerated monomial ideals.
Example 3.3 gives the four-generator degree-five counterexample
`(x^2,y^2,z^5,xyz)`.  The bounded degree-four minimality statement above is a
newly proposed finite boundary, not an openness assertion by the authors.

Primary PDF: `batches/literature/bigMac-08/2609.05044v1.pdf`  
PDF SHA-256: `e8ba90b5273578389918379df6e5b66fc899825ddb3b66dcb0f866f04e1561ab`

## Permitted contribution boundary

Either one strictly smaller exact counterexample, or a canonical exhaustive
proof covering every admissible exponent antichain, with independent checks of
integral closure and both v-numbers.  A search log without a completeness
argument is only an observation.
