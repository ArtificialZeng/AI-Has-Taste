# bigMac-00014-p02 — Exponent-two degree laws for a sticky-refresh sequence

## Immutable source statement

Let `(pi_j)` satisfy exactly the hypotheses of Xie--Zhou's iid
range-renewal theorem, including `pi_j in RV_(-1/gamma)` with `0<gamma<1`.
Fix `rho in [0,1)`. Start `X_0~pi`; independently at each step, keep the current
symbol with probability `rho`, and with probability `1-rho` redraw a fresh
symbol from `pi`. Build the directed and undirected simple graphs from
consecutive samples, suppressing repeated edges and deleting self-loops.

Prove or disprove that all four limiting tail/local-mass asymptotics in the
source remain exactly those of the iid model for every fixed `rho<1`, including
local exponent `2` and directed-to-undirected amplitude ratio `2^gamma`.
Every order of limits and normalization must be written explicitly from the
source theorem; if a constant retains a `rho` factor, state the corrected
formula rather than weakening the claim silently.

## Primary boundary

Xie and Zhou, *Universal Exponent-Two Degree Laws in Range-Renewal Networks*,
arXiv:2609.05290v1, main theorem and the dependent-sequence open direction in
the conclusion, pp. 12--13.

Primary PDF: `batches/literature/bigMac-14/2609.05290v1.pdf`.

The source treats iid symbols. The present fixed-`rho` Markov chain is a
specific dependent model. It is not the growing-degree regime registered as
`bigMac-00011-p15`.

## Permitted contribution boundary

A complete pathwise refresh-skeleton reduction transferring all claimed
asymptotics, or the first exact normalization/constant that fails. Simulation
alone is evidence only.

