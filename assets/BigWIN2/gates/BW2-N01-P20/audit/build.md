# Final build audit

Accepted by release job `newwin-00001-p20-release-3992adf5ac58` at 2026-09-12T12:32:05.700710+00:00. From `manuscript`, the declared clean command `latexmk -pdf -gg -interaction=nonstopmode -halt-on-error -file-line-error -outdir=build main.tex` exited 0 after all final edits. The complete unedited build transcript is `manuscript/build/clean-build.txt`. Bootstrap undefined references occur before BibTeX and reruns; the final converged `main.log` and `main.blg` contain no warnings, undefined references/citations, overfull/underfull boxes, duplicate/missing entries or errors. The final engine log is the gate-bound convergence record.

The skill key checker reports six cited keys, six bibliography keys and six auxiliary keys; missing/extra/unused counts are all zero (`audit/bib-key-check.txt`). The canonical references.bib supplies the whole bibliography. The `.bbl` was regenerated and inspected.

The PDF has six A4 pages, valid extractable text, correct title and author metadata, no encryption or JavaScript, and all listed fonts embedded with Unicode mapping (`audit/release-pages/pdfinfo.txt`, `fonts.txt`). All final pages were separately inspected; the visual report records that review.

The portable supplementary checker was actually rerun, producing JSON identical to the supplied output, including precision and the exact finite counts (`audit/release-supplement-replay.json`). Its scientific scope is finite and floating special-function values are not interval certificates.

Only source formatting and one redundant word changed: direct library cite; literal floor delimiters; standard url; optional microtype removed; continuous equation numbering; MSC metadata via standard thanks; PDF title/author supplied. The one minor overflow after removing microtype was corrected and the final clean build has none. No mathematical input or accepted claim changed.

Mathematical snapshot `cf7630d6bb75637ad046c973a80a87165a82712e35b2590de9570c5fd83fbf73`; manuscript `7b93959746febc59f27108bef0e6f383afed252661f643a166d5d32589bd16ce`; PDF `4ca5de43598fb74ebcc0a8c28110cf8ac5b7bc1c4cfe184f991656f46160a160`.
