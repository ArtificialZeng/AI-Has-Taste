# Checkpoint

- Release job: `bigMac-00029-p13-release-2f9da8670649`.
- Candidate remains the accepted `result-note`: (n_*=24) and
  \(\mathcal G_{24}=\{\{2\}\cup T:T\subseteq\{8,14,20\}\}\). The original
  asymptotic question remains unresolved, with no claim above level 24 and no
  broad publication-priority claim.
- The frozen mathematical evidence and acceptance remain current at snapshot
  `e72a058f7568b7218d0ac764304fe9fe521908ccb6e06489b6f4241cbc08f2f0`.
  Immutable `source.md` still has SHA-256
  `a4e8a9bb1fdaa7a9e9b0266a518a1ee0d134f343adf5c7f056e20034d68aa67e`.
- The citation-check skill was applied in fixed extraction and verification
  passes. The primary arXiv v1 full text verifies the Raso--Venturi metadata,
  Definitions 28--29, Theorem 30, Corollary 33, Remark 34, and Proposition 36.
  The Zeng DOI endpoint did not refresh; its metadata is preserved from the
  user-designated workbook (`metadata_basis=user_designated_workbook`, external
  refresh unavailable). Nearby manuscript prose was narrowed to the supported
  title-level methodological comparison; no proof uses that work.
- A full `latexmk -C` cleanup and declared pdfLaTeX/BibTeX build succeeded.
  The final `manuscript/main.log` has no compilation, citation, cross-reference,
  box, or rerun warning. BibTeX's separate one-line `empty journal` metadata
  warning is disclosed and nonblocking because the exact authoritative record
  intentionally has no journal field. All PDF fonts are embedded and text
  extraction is nonempty.
- The final five-page PDF has complete title/author metadata and was freshly
  rendered at 144 dpi. Pages 1--5 were opened at original image resolution and
  inspected: equations, both tables, citations, bibliography, margins, and page
  numbers are legible, with no clipping, overlap, malformed glyph, or blank page.
- Current manuscript digest:
  `ed2c8fdb091943df4adaee0a686a42d053978294e12cf60fcc12d94fe4650763`.
  Current PDF digest:
  `8fc3fde82341463d4b92ad7bdfa4bda4096c83e66be521b2d56fc958d80a853f`.
  Fresh citation, build, and visual audits are bound to those digests and this
  release job.
- `release_gate.py check` succeeds for the current project state. Remaining
  obstacle: none.
- Next test: the supervisor should run `release_gate.py publish` and verify the
  resulting `release/manifest.json` and `release/main.pdf` digests match the
  checked state.
