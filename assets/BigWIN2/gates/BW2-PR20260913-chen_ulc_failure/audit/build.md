# Build audit

PASS. Job primary-20260913-chen-ulc-failure-release-6faab700d5ab; checked 2026-09-12T22:57:21.251568+00:00.

The prescribed bash manuscript/build.sh first cleaned the manuscript auxiliaries and PDF, then ran pdfLaTeX/BibTeX/latexmk to convergence, exit 0. The complete stdout/stderr is audit/release-6faab700d5ab/clean-build.log. Only the final converged log is bound as build_log; transient first-pass reference messages in a clean build are not final failures. The final TeX and BibTeX logs were freshly copied and scanned: no undefined citations/references, missing database entry, duplicate entry, fatal error, overfull box or underfull box. The mechanical BibTeX check reports six cited keys, six entries and six matching .aux keys, with no missing, unused or extra keys.

The complete five authored publication source files were read: main.tex, references.bib, README.md, build.sh and verification.py. There are no nested authored TeX inputs or custom citation macros. Packages are installed system dependencies; the portable verifier has only standard-library imports and optional SymPy. The current source hashes match the writer's frozen source hashes. Fresh exact and symbolic execution reproduced the stated finite counts and boundary controls. The separate seven library-source rational comparisons also passed.

pdfinfo reports five letter-sized pages, the correct title, Xiaojian Zeng as author, the versioned conjecture subject, no encryption and no JavaScript. All 19 listed fonts are embedded Type 1 fonts with Unicode maps. The extracted text has resolved citation labels and equations (1)–(21). All five rendered pages were inspected separately in this release context; see visual.md.

Mathematical snapshot: 4556257bb02194676513831cafeed05699982a8fd956a67820a92eda025f8ae5.
Manuscript digest: 3ceea70d8cc6150305a1e7803d7c68e99dca884218ce450049e222720edc65fc.
PDF digest: 5a8c9b3de7676d91dac6e3836d8d4b43d2fe8301c99567a45480fbc9af995028.
Final TeX log digest: 023ad8d21b7f4a7a617ca8c494fc8640446ef08d184354f8717bfd1257fbabca.
