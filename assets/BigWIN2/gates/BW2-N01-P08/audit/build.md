# Build audit

Verdict: accept. Job newwin-00001-p08-release-467bc3c43b74. Reviewed 2026-09-12T09:48:39.283125+00:00.

The final canonical sources were rebuilt with `python3 manuscript/build.py`.
The script removed its generated outputs and ran pdfLaTeX with halt-on-error
and recorder mode, BibTeX, and two final pdfLaTeX passes. It completed with
exit code zero. No package installation or background worker was used.

The final LaTeX log is manuscript/build/main.log; the complete build command
transcript is manuscript/build/build.log; the BibTeX log is manuscript/build/main.blg.
Final logs contain no undefined citation/reference, missing or repeated BibTeX
entry, fatal error, or overfull/underfull box. The key checker
`python3 /home/ailab/.codex/skills/bib-reference-audit/scripts/check_bib_keys.py manuscript/main.tex --aux manuscript/build/main.aux`
reports nine citations, nine BibTeX entries and nine aux entries, and zero missing
or unused keys; its output is audit/bib-keys.log.

The PDF has six nonempty letter-size pages, author Xiaojian Zeng, the correct
title and subject, no encryption and no JavaScript. All twenty reported fonts
are embedded Type 1 subsets with Unicode mappings. See audit/release-fonts.txt.
Text extraction is supplementary to the separate all-page visual inspection.

Scope-preserving release corrections: xurl became standard url; the unsupported
allcolors option became explicit blue link/citation/URL colors; two Bézout
spellings use literal UTF-8 to allow exact active-text citation binding; the
independently corroborated DOI was restored to the selected bibliography entry.
No mathematical formula, assertion, citation key or parameter range changed.
After the final correction the PDF was rebuilt, refrozen and all pages rendered
and viewed again.

The compiler-local inputs are main.tex and generated aux/bbl/out. The canonical
references.bib is the BibTeX input. All source and supplement dependencies are
listed in publication.json. The verifier was also rerun: 303 polynomials at 49
pairs and eleven identities passed and match the earlier exact rows. This is
reproduction, not an additional mathematical referee acceptance.

Snapshot 4c76e5c2d8e61b75a85b57cf165889afc1b82282f4c36bfce8d9575114e62dd6; PDF 9e7ebe7f07e45ddd1ff6e9e524e8cd63ce4060627680c871a96a8815807e76ff.
