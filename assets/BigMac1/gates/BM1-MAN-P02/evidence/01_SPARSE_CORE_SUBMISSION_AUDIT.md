# Final submission audit: sparse nonsingular cores at adjacency rank ten

Date: 2026-08-27  
Verdict: **PASS**  
Fatal / major / minor findings: **0 / 0 / 0**

## Audited claim

The manuscript proves a sharp conditional theorem: a reduced simple graph of
real adjacency rank ten has at most 62 vertices whenever it contains a
connected nonsingular induced ten-vertex subgraph with at most eleven edges.
The condition is equivalent to the full-rank core being a tree, unicyclic
graph, or bicyclic graph.  Exact 62-vertex witnesses attain the bound in all
three families.

The audit confirms that the paper does **not** claim the unrestricted
rank-ten conjecture.  Connected nonsingular ten-vertex cores with at least
twelve edges remain outside the theorem.

## Mathematical gates

- Complete domains: 106 tree, 657 unicyclic and 2678 bicyclic isomorphism
  classes.
- Nonsingular cores: 15, 136 and 719, respectively.
- Exact target-53 clique exclusions: complete for every nonsingular instance.
- Independent no-import searches: PASS, with 760,220; 11,600,208; and
  41,704,342 recursive calls.
- Bicyclic discovery search: 48,967,729 integer branch nodes.
- Arithmetic: integer determinants, cofactor adjugates, bilinear profile
  tests and exact branch-and-bound only; no floating-point rank, eigenvalue,
  optimization or numerical stopping rule enters the proof.
- Sharpness: the 62-vertex certificate has exact rank 10, is reduced, and
  contains a connected nonsingular bicyclic ten-vertex core with 11 edges and
  determinant -1.
- Five fail-closed attacks are rejected.  The theorem-document audit is
  PASS with 0/0/0 findings.
- Milestone manifest: all bound file hashes match.

The machine-readable audit `audit/SPARSE_CORE_SUBMISSION_AUDIT.json` reports
PASS on 48 checks.

## Bibliography and build gates

- Nine cited keys, nine BibTeX entries and nine generated auxiliary entries.
- Missing entries: 0.  Unused entries: 0.  Unresolved citations: 0.
- The serial primary-source audit is recorded in
  `literature/sparse_core_bib_audit.md`.
- `latexmk -pdf -interaction=nonstopmode -halt-on-error main.tex` converges.
- The final log has no overfull/underfull box, undefined citation, undefined
  reference, BibTeX warning, LaTeX error, or fatal stop.

## PDF presentation gate

The seven pages were rendered to PNG and inspected individually.  The title,
theorem, equations, tables, certificate digest, bibliography and address
blocks are legible and remain inside the page bounds.  No clipping, overlap,
blank page, missing glyph or malformed link was observed.  Yonghua Xiong is
marked with an asterisk and the first-page note reads “Corresponding Author.”

This is a submission audit of the stated partial theorem, not an assertion
that the unrestricted rank-ten conjecture has been proved or disproved.
