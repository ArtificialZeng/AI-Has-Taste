# Build audit

Verdict: accept. Job `newwin-00001-p19-release-825c1e67cb4c`, 2026-09-12 UTC.

Ran `latexmk -C -outdir=build main.tex` in `manuscript/`, then the declared `bash manuscript/build.sh`; both returned zero. This removed previous build products before compiling. The final build contains six A4 pages. The completed `main.log` and `main.blg` are collected without modification in `audit/build.log`; the full clean/build execution is in `audit/release-build-transcript.log` and `audit/release-build-execution.json`.

No undefined citations/references, missing bibliography entries, repeated entries, TeX errors, fatal errors, overfull boxes or underfull boxes remain in the final logs (`audit/build-diagnostics.json`). The citation skill's key checker found three cited keys, three bibliography keys and three auxiliary bibliography entries, with no missing or extra key (`audit/bib-key-check.txt`).

Read all four publication source files and checked the TeX recorder. The main source directly uses canonical `references.bib`, with no additional authored TeX or figure inputs. The accompanying certificate imports only the Python standard library. The build script invokes installed TeX Live tools. These dependencies are recorded in `audit/publication-dependencies.json`.

The title and author metadata match the manuscript. All listed fonts are embedded; the PDF has six extractable, unencrypted pages and no JavaScript (`audit/pdfinfo.txt`, `audit/pdffonts.txt`). Ran `python3 manuscript/certificate.py --full` successfully. All 26 table values and all exact coefficients/periods/gaps match accepted evidence; the decimal lower inequality and negative coarse gap at 202 were checked without rounding. These arithmetic tests supplement the accepted proof and do not replace its universal arguments.

Snapshot and PDF digests are copied from `audit/manuscript-snapshot.json` into `audit/build.json`. The full source digest is 4c489d65f1189161766c2f6e9fe675a23006759b4dfe905baef9862b73262627; PDF digest 65180f3d38bed38a49108150ab3c8efe277ebc78f4ec7d5b1ffbe5c901766bb3.
