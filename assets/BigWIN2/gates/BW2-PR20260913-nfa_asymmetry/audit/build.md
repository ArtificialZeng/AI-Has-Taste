# Fresh clean build audit

Verdict: accept. Job: primary-20260913-nfa-asymmetry-release-a0b9dbc9657e. Checked UTC: 2026-09-12T19:48:38.214933+00:00.

The final source was compiled from a clean output directory using
`bash manuscript/build.sh`: pdfLaTeX, BibTeX, then two pdfLaTeX passes.
All prior main.aux, main.bbl, main.blg, main.fls, main.log, main.out and
main.pdf build outputs were removed immediately before this build.
The final command exited 0. No source or mathematical evidence was generated
by the build beyond the declared manuscript build outputs.

The full multi-pass transcript is audit/release-build.stdout.log; expected
first-pass unresolved references disappear on convergence. The audit-bound
final LaTeX log is audit/release-build.log, byte-identical to
manuscript/build/main.log; the final BibTeX log is audit/release-build.blg.
Both final logs were scanned: no undefined citation or cross-reference,
BibTeX missing/duplicate key, warning, error, overfull or underfull box remains.

The installed bib-reference-audit checker was actually run as:

    python3 /home/ailab/.codex/skills/bib-reference-audit/scripts/check_bib_keys.py manuscript/main.tex --aux manuscript/build/main.aux

Its final output in audit/release-bib-keys.txt has seven cited keys, seven
bibliography entries, seven resolved aux entries, zero missing and zero extra.
Only canonical manuscript/references.bib is used. All listed publication
source files were read: the main article, bibliography, build script,
supplement README, verifier, witness inputs and saved results. The TeX
packages and bibliography style are installed toolchain inputs; no undeclared
project source, figure or bibliography dependency was found.

PDF metadata from pdfinfo identifies the correct title, Xiaojian Zeng,
six A4 pages, no encryption and no JavaScript. Every font reported by pdffonts
is embedded, subset and has a Unicode map. Text extraction is nonempty.
The PDF was refrozen after the final typography changes; no subsequent source
or PDF edit occurred. Exact digests are held in audit/manuscript-snapshot.json
and audit/build.json rather than manuscript prose.

Supplement replay is separate evidence: byte-identical code and input copies
under audit/supplement-replay completed with zero failed assertions and all
six semantic fields matching the published output. This tests finite claims,
not the infinite theorem. The frozen mathematical files were not rerun in a
way that could overwrite their evidence.
