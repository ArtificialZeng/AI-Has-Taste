# Factor-two improvement of the universal projection-constant stability bound

## Immutable source statement

For positive integers `n>=r`, let `lambda(r,n)` be the maximal relative projection constant of an `r`-dimensional subspace of `ell_infinity^n`, and let `lambda(r)` be the maximal absolute projection constant, exactly as in equation (1.1) of the primary source.

Prove or disprove:

> For every integer `r>=1` and every integer
> `n >= 2^(r-1) binom(r+1,2)`, one has `lambda(r,n)=lambda(r)`.

## Quantifiers and scope

- This is a uniform theorem for every real dimension `r`, not a finite check for selected dimensions.
- The ambient scalar field and all definitions are the real ones used by the source.
- A proof must preserve every feasibility and maximizing-pair condition in Theorem 2.1 and Claims 2.1--2.5; counting sign cells alone is insufficient.
- A counterexample must refute the displayed universal threshold, not merely show that it is not the least possible threshold.

## Primary source and nearest result

- Hitesh Kumar, Bojan Mohar, Seyed Ahmad Mojallal, and Shivaramakrishna Pragada, *Stability of maximal relative projection constants*, arXiv:2609.03200v1 (2026), https://arxiv.org/abs/2609.03200.
- Local PDF: `batches/inbox/bigWin-56-materials/2609.03200.pdf`.
- SHA-256: `59a16bdd68bf224d429f4b22e3f91ecf6a3c1875cf7537cf632770b5d5112ef8`.
- Locators: Problem 1.2 and Theorem 1.3, PDF pp.3--4; maximizing-pair reduction and Cloning Claim 2.4, pp.6--8; Stability Claim 2.5, pp.9--10.
- Nearest theorem: Theorem 1.3 proves the same conclusion under `n >= 2^r binom(r+1,2)`. The source says only that minor improvements may be possible and does not state the displayed factor-two threshold.

## Proposed contribution boundary

The candidate proof normalizes each row `x_i` of a maximizing matrix by replacing it with `-x_i` whenever its first coordinate is negative. This preserves `U^T U`, weights, and every absolute inner product while leaving only `2^(r-1)` sign orthants. The research task must fully audit zero coordinates, the signed graph used in the proof, repeated cloning, deletion of zero rows, and the final passage from finite `n` to `lambda(r)`. If the statement is already a direct published consequence or the source's phrase “minor improvements” conceals this exact bound elsewhere, record it as known rather than new.

## Cheapest decisive test and certificates

Write the row-sign normalization as multiplication by a diagonal matrix `D` with entries `+/-1`, verify each optimization constraint symbolically, and then re-run every line of Claims 2.4--2.5 with only the half-orthant partition. A finite numerical experiment is diagnostic only. The decisive artifact is a complete proof or an exact obstruction to one of these preservation steps.

## Provenance

Prepared on 2026-09-07 from the primary PDF during the authorized fallback after the exact Chrome target could not be attached. This statement is immutable; any further strengthening must be frozen separately.
