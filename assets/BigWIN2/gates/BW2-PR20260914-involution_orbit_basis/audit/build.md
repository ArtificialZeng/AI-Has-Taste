# Build audit

Verdict: **accept**.
Release job: `primary-20260914-involution-orbit-basis-release-0d8839b8ec7d`.
Audit time (UTC): 2026-09-14T11:39:34.022643+00:00.

The current source was built from clean generated products using `bash manuscript/build.sh`: three successful pdfLaTeX passes with an intervening BibTeX pass. The script removed only the named generated build/main products. No package installation or source-generation worker was used. The final build finished with exit code 0.

The inspected final `build/main.log`, `build/main.blg` and BibTeX stdout contain no undefined citations or references, missing database entries, repeated entries, LaTeX warnings, overfull/underfull boxes, fatal errors, runaway arguments or emergency stops. The read-only bibliography checker was run before and after compilation; all seven cited keys exist and all seven auxiliary entries match.

The PDF has a valid PDF header, seven A4 pages, nonempty searchable text, no encryption or JavaScript, and embedded Type-1 fonts with Unicode maps. Metadata identifies Xiaojian Zeng and the actual manuscript title. The publication repairs preserve the accepted theorem and only repair DOI encoding, direct citation syntax, equivalent partition notation and spacing.

The recorder file identifies the only authored TeX input as manuscript/main.tex; the local auxiliary, bibliography output and hyperlink output are generated. BibTeX reads manuscript/references.bib, the sole bibliography. The complete publication source list is therefore correct. Build and reproduction scripts are not imported source dependencies.

The manuscript snapshot was regenerated after the clean build. No source, PDF or build log was changed after the freeze; current hashes are bound in `audit/build.json`. Seven rendered pages were inspected separately and documented in `audit/visual.md`.
