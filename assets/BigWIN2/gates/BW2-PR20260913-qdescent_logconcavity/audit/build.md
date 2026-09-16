# Clean build audit

Verdict: accept. Release job: primary-20260913-qdescent-logconcavity-release-2bbc928589b7. Generated: 2026-09-13T16:45:11.353922+00:00.

The final source was built from clean generated outputs using `python3 manuscript/build.py`: pdfLaTeX, BibTeX, pdfLaTeX, pdfLaTeX. The driver removes generated main.* files first and stops on a nonzero process result. The complete final four-pass output is audit/release-build-transcript.log; the converged final compiler log is audit/release-final-pass.log. Initial unresolved references in the first pass are ordinary intermediates; the final compiler and BibTeX logs have none.

The final engine and BibTeX logs were inspected for fatal errors, unresolved citations/references, undefined commands, duplicate bibliography entries, and overfull/underfull boxes. No such diagnostics or final LaTeX warning occurred. The skill checker `python3 /home/ailab/.codex/skills/bib-reference-audit/scripts/check_bib_keys.py manuscript/main.tex --aux manuscript/build/main.aux` reports seven cited, bibliography and aux keys, with zero missing/unused/extra keys.

The installed citation parser initially rejected the custom genfrac macro. The scope-preserving correction is documented in audit/tex-compatibility-revision.json. Reversing the notation substitution reconstructs the exact original TeX; no mathematical statement, number, prose argument or key changed. After correction the selection validator passed, the manuscript was rebuilt, refrozen and every page reinspected.

The final PDF is a valid six-page A4 PDF 1.5 with nonempty text. All listed fonts are embedded and have Unicode mappings. It has no encryption or JavaScript. Descriptive metadata fields are empty rather than incorrect; Creator/Producer identify LaTeX/hyperref and pdfTeX. Creation/modification time is the build driver's documented fixed timestamp, not the verification date. The intended author/title appear correctly on the first page. Metadata and font evidence are audit/pdfinfo.txt and audit/pdffonts.txt.

The exact-check executable was read and rerun with output audit/release-recomputed.json. Its transfer/kernel/original-definition/failure objects match both the accepted referee results and manuscript/verification-results.json exactly. This reproduction checks all table counts, not the uniform theorem by extrapolation. Publication source dependencies were completely inspected and no source outside the declared list is required except standard installed Python/TeX libraries.

Research digest: 9ae9add72fc8f4054cff292c5f61239af227e330f2412ceb2363069cdd3253eb.
Manuscript digest: 9c91cab3e0c3ea4b65affa78e4ea90b8c6db452b0b757bf346dc16e0d4556447.
PDF digest: b9524c5edb91d5c6eae42f0da65169a7ed18e8978128c2da1d71c68dba5e192f.
Build log digest: 03d3c00e002ca9ef9fdd7fb4a05af653ff73334c780cb2a05fc7a2d94500a56e.
