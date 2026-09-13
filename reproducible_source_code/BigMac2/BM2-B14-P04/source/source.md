# bigMac-00014-p04 — Exact relative dimension of `B_3`

## Immutable source statement

Let `B_3=(2^{[3]}, subseteq)`. Use the definitions of partial linear extension,
local realizer, relative frequency, and relative dimension in Dürrschnabel et
al. Prove or disprove

`rdim(B_3)=2`.

A proof of equality must provide both:

1. a valid local realizer of total element-occurrence cost `16`; and
2. an independently checkable lower certificate excluding every local realizer
   of total cost at most `15`.

The lower certificate may be a rational covering dual or a proof-checked
SAT/UNSAT artifact, but a solver status line alone is not sufficient.

## Primary boundary

Dürrschnabel, Hodor, Micek, Stumme and Trotter, *Relative Dimension of Posets*,
arXiv:2609.05166v1, definitions pp. 2--3 and Figure 1 / proof of Theorem 5,
p. 8.

Primary PDF: `batches/literature/bigMac-14/2609.05166v1.pdf`.

The source explicitly exhibits `rdim(B_3)<=2` but does not give the matching
lower bound in the checked text. A fresh novelty search is required. The prior
registry item `bigMac-00008-p15` asks for the different value `rdim(B_4)`.

## Permitted contribution boundary

The exact value with both certificates, or a valid lower-cost realizer that
disproves it. A finite optimization result without a replayable certificate is
not sufficient.

