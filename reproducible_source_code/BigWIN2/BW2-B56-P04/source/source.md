# Repair or refute the key lemma in the claimed Daykin--Frankl proof

## Immutable source statement

Let `R` be any finite poset and let `P` be a convex subset of `R x Q_1`, where `Q_1={0,1}`. Write

`P=P_0 x {0} union P_1 x {1}`

with `P_0,P_1 subseteq R`. Prove or disprove the inequality

`w(P) >= ( w(P_0 x Q_1)+w(P_1 x Q_1) )/2`.

If it is true, supply a complete proof with every auxiliary set defined and both constructed antichains checked in all comparability directions; then independently verify that the backward induction in the source yields, for all `n,k>=0` and every convex `P subseteq Q_n`,

`w(P x Q_k) >= w(Q_(n+k)) |P| 2^(-n)`.

If it is false, give an exact smallest or near-smallest finite counterexample and identify which asserted antichain step fails.

## Quantifiers and scope

- `R` ranges over all finite posets; no lattice or ranked assumption may be introduced silently.
- Convexity is order convexity exactly as defined by the source.
- The two-layer order is the product order.
- Exhaustive verification up to a finite size is evidence only unless accompanied by a complete certificate for an explicit counterexample.
- Repairing the lemma validates the displayed proof route; it does not by itself establish priority or novelty of the overall Daykin--Frankl theorem.

## Primary source and nearest result

- Kada Kálmán Williams, *Confirmation of the Daykin-Frankl Conjecture*, arXiv:2609.03087v1 (2026), https://arxiv.org/abs/2609.03087.
- Local PDF: `batches/inbox/bigWin-56-materials/2609.03087.pdf`.
- SHA-256: `d5cb26a66fb4e4ffb03eebd1a6a584b806c89c9dda04adafe2e0054467133549`.
- Locators: definitions and conjecture, PDF p.1; Theorem 1, Lemma 2, and induction, p.2; proof of Lemma 2, p.3.
- Audit trigger: the p.3 proof uses a set `C` several times without defining it and dismisses the second antichain by “hourglass symmetry.” The natural inferred repair `C=(P_0 union P_1) setminus (P_0 intersect P_1)` is a hypothesis to audit, not part of the frozen lemma.

## Proposed contribution boundary

A publishable-scale outcome can be a concise rigorous repair of a gap in a newly claimed proof of a longstanding conjecture, provided a fresh referee verifies every direction and literature review confirms the gap is not already corrected. If the inferred definition makes the existing prose immediately complete, report this honestly as an audit note rather than inflating it.

## Cheapest decisive test and certificates

Enumerate all finite posets through at least five elements (and six if feasible), all convex subsets of their products with `Q_1`, and exact widths to search symmetrically for counterexamples. In parallel, formalize the set-sorting construction with the inferred `C` and check both antichains direction by direction. Preserve canonical Hasse diagrams and maximum-antichain witnesses for any failure.

## Provenance

Prepared on 2026-09-07 from the primary PDF during the authorized fallback after the exact Chrome target could not be attached. This statement freezes the lemma and downstream implication; it does not presume the claimed proof is valid.
