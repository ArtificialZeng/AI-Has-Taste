# Build audit

Verdict: **accept**. Job: primary-20260914-lorentzian-cliques-release-1bb091df0970. Generated: 2026-09-13T23:58:16.133131+00:00.

A fresh clean rebuild ran from manuscript/ with `latexmk -C main.tex`, followed by `latexmk -pdf -interaction=nonstopmode -halt-on-error -file-line-error main.tex`. Both exited zero. No TeX or BibTeX source edit was needed. Actual command transcripts are audit/recovery-clean.log and audit/recovery-build-transcript.log. The final TeX and BibTeX logs, audit/recovery-main.log and audit/recovery-main.blg, were read completely and inspected for errors, unresolved citations/cross-references, missing/duplicate bibliography entries and layout warnings. There are none. Transient first-pass references in the build transcript resolved normally.

The installed check_bib_keys.py ran against the canonical TeX and final aux; all seven keys agree, with no missing, unused or extra key. Its output is audit/recovery-bib-key-check.txt. The generated bibliography is preserved as audit/recovery-main.bbl. The actual recorder and source review establish the complete authored dependency inventory: manuscript/main.tex and manuscript/references.bib. Other local inputs are generated aux/out/bbl files, and the remaining styles, fonts and configuration are installed TeX dependencies. There are no authored external imports or figures.

The final PDF has six pages, correct title and author metadata, nonempty text extraction, no encryption or JavaScript, and all 23 listed font instances embedded with Unicode mappings. The extracted layout text is byte-identical to the writer's accepted manuscript text. Evidence is in audit/recovery-build-checks.json, audit/recovery-pdfinfo.txt, audit/recovery-fonts.txt and audit/recovery-pdf.txt. The official freeze-manuscript command ran after this build. All six images subsequently inspected came from this exact PDF.

Evidence digest: 433d775ecce23495c57cb0b57f8bf311721ff57d30a9c8a2b19e2d8bf4270d2d.
Manuscript digest: 5520840a8b7f7353be231676b0d5f9e3faeee90c4ea30ea71662c211cbda9974.
PDF digest: bd3460c9c0fda440e051949450b2933709fa2bf8d6d15fa80178d98be4490f65.
Build log SHA256: b775c71ac930b7b354b7196bef79219d7e25087f88b93479cdeb5eacda13b525.

A clean build establishes document consistency, not mathematical truth.
