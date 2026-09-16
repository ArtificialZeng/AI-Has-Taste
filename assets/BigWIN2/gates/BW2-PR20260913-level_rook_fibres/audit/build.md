# Build audit

**Accept.** Job `primary-20260913-level-rook-fibres-release-8051a1494029`,
2026-09-12 UTC. Bindings are recorded in `audit/build.json`.

Ran `sh manuscript/build.sh`, which cleans the output directory and invokes
`latexmk -pdf -bibtex -outdir=build -interaction=nonstopmode -halt-on-error
-file-line-error main.tex`. The final run exited successfully and produced
`manuscript/build/main.pdf`, seven pages. BibTeX and subsequent TeX passes
converged. `audit/release-build-full.log` preserves the whole clean build;
`audit/release-build.log` combines the final TeX and BibTeX logs. The latter is
the digest-bound clean final log, avoiding transient first-pass cross-reference
warnings from an intentionally empty auxiliary directory.

The final logs contain no undefined citations/references, missing bibliography
entries, duplicate keys, control-sequence errors, fatal errors, TeX/BibTeX
warnings, or overfull/underfull horizontal boxes. A broad preliminary scanner
matched the infwarerr package description and BibTeX's zero-count `warning$`
statistic; neither is a diagnostic. The final diagnostic-pattern scan distinguishes
these metadata lines from actual warnings.

Ran the requested `bib-reference-audit/scripts/check_bib_keys.py` with the
canonical main file and built aux file: 12 cited keys, 12 bibliography keys,
12 aux keys, no missing or extra key. The canonical references.bib is the sole
bibliography. No source key was renamed.

The PDF title, subject and author match the paper. `pdfinfo` reports seven
unencrypted letter-size pages and no PDF JavaScript. `pdffonts` reports all
17 font resources embedded, with Unicode mappings. The PDF contains selectable
text. Metadata and font-tool outputs are saved in `audit/pdfinfo.txt` and
`audit/pdffonts.txt`.

After the installed citation parser rejected two custom notation macros,
floor/ceiling invocations were expanded literally. The regenerated PDF's
normalized extracted text is identical to the immediately preceding draft.
All citation sentences and mathematical statements keep their meaning.
The final sources/PDF were refrozen with the supplied release_gate.py
freeze-manuscript command; the claim ledger digest matches that snapshot.

The packaged exact verifier was also rerun with
`python3 -B manuscript/supplement/verify.py > audit/release-verification.json`.
Its output equals `manuscript/supplement/verification.json` as a JSON object.
The counter and verifier have no external package/network requirement. This
replay checks the published finite table; it does not substitute for its proof.

All accepted mathematical input hashes, the immutable original source and the
checkpoint were checked again without modification. The final release check
is separate from this factual build report.
