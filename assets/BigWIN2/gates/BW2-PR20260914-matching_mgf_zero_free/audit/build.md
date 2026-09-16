# Fresh build audit

Verdict: accept. Release job: `primary-20260914-matching-mgf-zero-free-release-1689b9e708f3`. Reviewed at 2026-09-14T12:37:53.067693+00:00 UTC.

Ran `python3 manuscript/build.py`. The inspected script creates an empty project-local
temporary build directory, runs pdfLaTeX, BibTeX, then two final pdfLaTeX passes, and
retains the resulting logs and PDF. BibTeX uses the canonical references.bib through
BIBINPUTS. This release performed the complete clean build after the markup repair.
The source-date epoch is fixed by the existing build program; its PDF timestamp is
12:00 UTC on 14 September 2026 and is not presented as the audit time.

Read the real final compiler log, BibTeX log, generated BBL and recorder. The final
logs have no warnings, undefined citations/references, missing or repeated entries,
fatal errors, or overfull/underfull boxes. Initial-pass unresolved-reference messages
in the complete transcript are resolved by the final passes. A routine font-info
message substitutes the available Latin Modern typewriter bold face for the bx face;
the actual listing was visually inspected and is legible.

The bibliography checker reports 5 cited keys, 5 bibliography entries and 5 AUX
labels, with zero missing, unused or mismatched keys. The BBL agrees with the
canonical bibliography. `audit/bib-key-check.txt` retains its output.

The recorder confirms main.tex and its generated BBL/aux/out are the only local
TeX inputs; the other inputs are installed system styles, fonts and configuration.
Matrices and the printed program are literal in main.tex; the accompanying exact
programs and build program remain in publication.json. No authored dependency is
missing from the six-file source list.

pdfinfo confirms seven unencrypted letter-size pages, correct title and author,
no PDF JavaScript, and PDF 1.5. Text extraction is nonempty and resolves all
references. Font output is retained in audit/pdf-fonts.txt. All seven rendered
pages were independently inspected in this release context; see audit/visual.md.

Final log: manuscript/build/main.log
Final log SHA-256: e80c4a4bfa34f5a8a232119b65f4ed6cb060324841979d0dc92ac22508d04646
Manuscript digest: b275a1fd9f3375267cea0a0051d8326af9a76fa27d32a0c76c53567cb28dceac
PDF digest: 83adefea005610b44c10437b6dea087ed709d691063f234d1ce0bb930ac9b389
Supporting checks: audit/build-validation.json, audit/pdfinfo.txt,
manuscript/build/build-transcript.txt. No frozen mathematical input was modified.
