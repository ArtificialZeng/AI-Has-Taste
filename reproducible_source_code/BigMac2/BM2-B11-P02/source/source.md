# bigMac-00011-p02 — Polyregular classification of small additive level sorts

## Immutable source statement

For the additive-level sort on Dyck step words defined in
arXiv:2609.05005v1, let the up- and down-step weights `(u,d)` range over
coprime integers with `|u|,|d|<=2`, and treat separately each of the source's
two fixed tie orders.  Modulo simultaneous multiplication of the weights by
`-1` and the evident word-reversal symmetry, classify every resulting word
map as polyregular or non-polyregular.  For each positive case give an
explicit polyregular transducer; for each negative case give a rigorous
semilinearity or pumping obstruction.

## Primary boundary

Zeng and Kim, *A Computational Obstruction to Swapping Area and Dinv: An
Automata-Theoretic View of the q,t-Catalan Symmetry*, arXiv:2609.05005v1,
Section 11, Open Problem (4).  The source observes that `(u,d)=(1,1)` makes
the level equal to position and the map the identity, and develops a
non-polyregular mechanism for mixed-sign sweep maps, but does not give this
finite weight classification.

Primary PDF: `batches/literature/bigMac-11/2609.05005v1.pdf`  
PDF SHA-256: `b55c4a261469e318c2058e0461ef2440a012243800b16ac07077e420c1067a66`

## Permitted contribution boundary

A complete symmetry-reduced table for both tie orders, with replayable
transducers or exact obstruction languages for every entry.  Testing finitely
many words or showing that one natural transducer fails is not a classification.

