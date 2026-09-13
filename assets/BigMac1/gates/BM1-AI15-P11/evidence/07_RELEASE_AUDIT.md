# Release audit

Date: 2026-08-29 (Asia/Shanghai)

Status: **PASS**.

## Released artifacts

- PDF: `output/pdf/tree_independence_unimodality_order31.pdf`
  - SHA-256: `22426d70897c55f8acac4e315ba7d132194ef55aa97027a7b195b92150786f7b`
- source/certificate archive:
  `output/source/tree_independence_unimodality_order31_source.zip`
  - SHA-256: `56e19265911e2c9ca236d2ed628b2ca9dc52e4832b4f5bf1413a859516189c26`
- archive manifest: `MANIFEST.sha256.json`
  - SHA-256: `cbe3029175e04560e78f8dfc2447699e16223d695dc109f9bce2ec7be5a8e3aa`
  - recorded files: 559

The manifest binds the LaTeX source, formal bibliography, generated `.bbl`,
zero-warning clean-build logs, final PDF, 240 completed sweep files, both
aggregators, isolated-rebuild verifier, four-corruption negative-control
driver and result, preflight, nauty archive, and mathematical audits.  The
external release audit itself is intentionally not placed inside the ZIP, so
that it can record the ZIP hash without a circular self-reference.

## Clean manuscript build

The final manuscript was built in the fresh directory
`tmp/pdfs/clean-build-terminal-v3.mxMjvR`.  Two earlier fresh builds were
rejected: the raw DOI export's `#P4.03` caused a TeX fatal error, and its bare
`July` value caused a BibTeX warning.  The metadata-preserving normalizations
are recorded in `audit/CITATION_AUDIT.md`.  The accepted build has 9/9
citation closure, zero warning/error, five Letter pages, and a five-page
individual visual inspection recorded in `audit/PDF_AUDIT.md`.

## Fresh-root verification

The final ZIP was extracted to
`tmp/release-root-audit-terminal-revision.ztBUrs/order31_tree_unimodality`.  The following
checks were run from that extracted root with fail-fast shell semantics:

1. The skill manifest verifier checked all 559 recorded files.
2. An independent set comparison proved that the archive contains exactly
   those 559 non-manifest files, with neither omissions nor additions.
3. `audit/order31_independent_aggregate.py`, with project imports disabled by
   construction, returned PASS with exactly 40,330,829,030 trees,
   `nonunimodal=0`, `nonlogconcave=159`, and rebuilt all 159 serialized
   exceptional polynomials.
4. `audit/fail_closed_rejection_tests.py` recreated all four corruptions from
   the ZIP root; every case returned exit code 1 with its expected reason.
5. The README contains `cd paper` before the LaTeX/BibTeX commands.  A fresh
   build from ZIP sources had 9/9 citation closure and zero warning/error.
6. `pdftotext -layout` from the ZIP-built PDF was byte-identical to the
   released PDF, and the PDF embedded in the ZIP is byte-identical to it.
7. The 559 manifest entries were verified again after all checks.

Final output: `RELEASE_ROOT_AUDIT PASS`.

No proof assistant or theorem prover was used.
