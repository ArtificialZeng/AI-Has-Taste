# Clean build audit

Verdict: **accept**. Job: primary-20260914-triangular-square-roots-release-774ca875bd99. Reviewed at 2026-09-14T13:18:27.105865+00:00.

The actual final PDF has six letter-size pages, nonempty text extraction and the correct title and author metadata. All fonts listed by pdffonts are embedded. No system software was installed.

From manuscript/, the build was cleaned with `latexmk -C -outdir=../build main.tex`. This retains main.bbl by default; that generated file was explicitly removed. The empty pre-compilation generated-file set is recorded in audit/release-clean.json. The exact final build command was:

```sh
latexmk -pdf -interaction=nonstopmode -halt-on-error -file-line-error -outdir=../build main.tex
```

The command exited zero, regenerated the bibliography with BibTeX, and converged in three pdfLaTeX passes. Its full transcript is audit/release-build-transcript.log. Expected first-pass missing references are not final diagnostics. The final compiler log is build/main.log, SHA-256 c5c106b70ae77383bb7eb0f9471a81a4b5dbec52c80a77639899320004e4fdd5; audit/release-final-compiler.log is a byte-identical review copy. The final compiler/BibTeX logs contain no undefined citations or cross-references, missing or duplicate entries, errors, overfull/underfull boxes or layout warnings. Bibliography statistics report zero warnings.

The final check_bib_keys.py invocation against manuscript/main.tex and build/main.aux exited zero: six cited keys, six database keys and six auxiliary citation keys, with no missing or unused entry. Canonical references.bib is resolved from manuscript/. The compiler recorder contains main.tex plus generated .aux/.out/.bbl files inside the project; all other loaded files are system TeX dependencies. The BibTeX log identifies the declared references.bib. No undeclared authored source is required.

The title is “Simple negative roots for the rows of the Delannoy matrix square”, and the author is Xiaojian Zeng. PDF metadata, text and font reports are audit/release-pdfinfo.txt, audit/release-pdf-text.txt and audit/release-pdffonts.txt. No PDF source/metadata edit occurred after the final manuscript freeze.

Bindings: mathematical snapshot afcfb64162aef0f427a3122f208edb356ac2e15cb197a2f8cd8e56b437beea5b; manuscript ba5f0bdbee3199a8021a97558ebbd7dd0fa427069cf5e43f11f8d4d5c713600f; PDF 4b58859471d0b70afb4a7aa89c3b74b16890f30608fb017b26e3585cc3f33c5e. This report establishes build consistency only.
