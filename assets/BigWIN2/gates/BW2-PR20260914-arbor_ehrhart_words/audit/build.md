# Clean build audit

Verdict: ACCEPT. Job: primary-20260914-arbor-ehrhart-words-release-df3b6d5a637c. Date: 2026-09-14 UTC.

An initially empty audit/release-clean-build output directory was used for an
independent latexmk build of the initial source. Its extracted text and generated
bbl exactly matched the then-frozen PDF and bibliography. After removing only
the redundant final bibliography group wrappers, the canonical build was cleaned
and compiled from manuscript/ with:

```sh
latexmk -C -outdir=build main.tex > build/release-clean.log 2>&1
latexmk -pdf -interaction=nonstopmode -halt-on-error -file-line-error -outdir=build main.tex > build/release-latexmk.log 2>&1
```

Both latexmk stages completed successfully. The final manuscript/build/main.log
and main.blg were read and scanned. There are no undefined citations/references,
missing entries, duplicates, fatal errors, overfull/underfull boxes or relevant
warnings. The BibTeX warning count is zero and six entries are used. The generic
infwarerr package description is not a compiler diagnostic. Initial-pass messages
in the cumulative latexmk log are resolved in the final log and PDF.

The built PDF has six letter-size pages, a valid PDF header, selectable text,
correct title and Xiaojian Zeng author metadata. The complete final extracted text
matches the independent initial clean build. All six final page render hashes
match the previously inspected images after the layout-preserving wrapper edit.
The final bbl is generated from the unchanged canonical references.bib. The
bib-reference checker finds exactly six cited, stored and resolved keys with no
extras or omissions. The recorder has no omitted authored source dependency.

freeze-manuscript succeeded after this build. The audit binds manuscript digest
86d46d2a9bca82f4a491660782aab2fd6bab55254b9b392ef32d82dc8330d322, PDF digest a0966dd2d7f0ae4465313fac6828dcc584637c136f7f96f29a054eb42a3c2b93, and final compiler-log digest
1e915733ad2cca27970c7ce948cd44d50589a9287c1085de7089164bb1f52cc0. The extra audit/release-clean-build PDF is verification output only;
it is not a released manuscript or an alternate deliverable.
