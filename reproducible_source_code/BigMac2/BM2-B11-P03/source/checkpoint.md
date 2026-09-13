# Checkpoint

## Accepted mathematical scope

The fresh audit in `audit/math.md` accepts the frozen `resolution-paper` claim
at snapshot digest
`34fc7c533f472c12c11c2e62b9890097b62bc171f4bd1d4168075cea194b9ae6`.
The writing-phase `check-math` gate passed. The immutable `source.md` still has
SHA-256
`c1b138ca46b1461350f7d08629d515228c1181f53fc0c7a54349d60ef6bb06a5`.

For the explicitly independent-row subgroup

\[
H=\langle(12),(34)\rangle\cong C_2^2,
\]

the accepted identity is

\[
K_{(2,2)}\times K_{(2,2)}\cong
2K_{(2,2)}\mathbin{\sqcup}K_{(1,1,1,1)}.
\]

Thus the coefficient vector in partition order
`(4),(3,1),(2,2),(2,1,1),(1,1,1,1)` is `(0,0,2,0,1)`.
The five species and, separately, their five cycle indices have no nonzero
integral relations.

## Decisive evidence

- `evidence/proof.md` proves that the order-eight normalizer of (H) consists
  of two size-four double cosets and that the remaining size-sixteen double
  coset has trivial intersection stabilizer. Hence the three stabilizers are
  (H,1,H).
- `evidence/s4_certificate.py` and `evidence/s4_certificate.json` give a
  byte-reproducible exact enumeration of all 24 permutations, together with
  exact mark and cycle-index checks.
- `audit/math.md` independently reconstructed both the group-theoretic proof
  and an exact orbit enumeration and found no gap.

## Release audit outcome

The three-page article was rebuilt from a `latexmk -C` state and refrozen
without changing its sources or accepted mathematical scope. The current
manuscript digest is
`208748d8901627eba5664e66bd2e3b56bc024719049f758394b3b169b4b1d5f4`; the
current PDF SHA-256 is
`474f76ce0f5c756936656289753da6304b59e3704ca685da7457b553f1b96fde`.
The final compiler log SHA-256 is
`920c0666b7f91f318bca177a2e39c28a715e6187b3dabd50645e5c9b561ceb30`.

Fresh release reports in `audit/citations.md`, `audit/build.md`, and
`audit/visual.md` bind those digests and job
`bigMac-00011-p03-release-af4aac704f2b`. The citation-check-skill two-pass
audit verified both citations against primary arXiv text and the official ECA
listing, found no unsupported strengthening, and confirmed the complete source
dependency list. The clean build has no unresolved citation/reference or
layout diagnostic. All rendered pages `[1,2,3]` were visually inspected and
have no clipping, overlap, or illegibility. A fresh
`release_gate.py check` returned `ok:true`.

The required `literature/user_bibliography_check.md` remains absent. Both
included papers are genuinely relevant and their metadata and cited passages
are verified, but their provenance from the user's cited Excel list cannot be
reconfirmed. `audit/citations.json` therefore records
`accept_with_citation_limitations`; this is a source-provenance access limit,
not a mathematical, citation-support, build, or visual defect.

## Obstacles

No mathematical, citation-support, build, visual, or gate obstacle remains.
Only the disclosed missing-Excel-list provenance limitation remains. The
article correctly retains the explicit independent-row hypothesis because the
two cited papers use different repeated-part conventions.

## Next test

The supervisor should run `release_gate.py publish` on this unchanged project
and verify that `release/manifest.json` records PDF digest
`474f76ce0f5c756936656289753da6304b59e3704ca685da7457b553f1b96fde`.
