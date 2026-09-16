# Fresh clean-build review

Release job: `primary-20260913-ascent-0120-0121-release-fadb0e167fc3`. Reviewed at 2026-09-13T14:05:45.025420+00:00. Verdict: accept.

Both commands were actually executed from manuscript/ and returned zero:

```sh
latexmk -C -outdir=build main.tex
latexmk -pdf -interaction=nonstopmode -halt-on-error -outdir=build main.tex
```

Commands, timestamps and exit codes are in audit/release-recovery-build-commands.json;
the complete transcript is audit/release-recovery-build-console.log. The final
compiler log was copied byte-for-byte to audit/release-recovery-build.log; the BibTeX log is
audit/release-recovery-bibtex.log. Final diagnostics contain no undefined citations
or cross-references, missing bibliography entries, duplicate entries, fatal errors,
LaTeX/package warnings, or overfull/underfull boxes. The literal warning/layout
scan supplements the diagnostic expressions in audit/release-recovery-build-checks.json.

The skill's check_bib_keys.py was run with manuscript/build/main.aux: nine cited
keys, nine bibliography keys, and nine resolved aux keys, with zero missing,
unused or extra entries. The generated bibliography was read in PDF text and
visually on pages 6–7. The recorder and BibTeX log show only main.tex,
references.bib, generated aux/bbl/out files, and system dependencies. The README
and supplementary coefficients.py are also explicitly covered by publication.json.

pdfinfo reports seven unencrypted US-letter pages, PDF 1.5, with the correct title
and Xiaojian Zeng author metadata. All 20 listed fonts are embedded, with Unicode
maps; no Type 3 font was reported. pdftotext extraction is nonempty and matches
the source content. Exact table values and the degree-28 publication-code result
were checked against accepted records. Metadata/text/font outputs and checks are
saved under audit/release-recovery-*.

After rebuilding, the official freeze-manuscript command succeeded. Source digest
70eefb4deff8b4596f3bff22f2c5c9c168caa6c13744cbd542c0a5fd6789d707 was unchanged; current PDF SHA-256 is b826f7c4131f1e021d364c9a841d5e4e5fb82e26f5c66580c38550b425e194ad.
All audit bindings refer to that snapshot. No manuscript source or mathematical
input was edited. The fresh page renders and native view_image inspections are
reported separately in audit/visual.md.
