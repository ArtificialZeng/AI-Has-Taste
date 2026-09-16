# Fresh clean-build audit

Verdict: accept. Job `primary-20260914-comb-inverse-release-63c10542e86d`; generated 2026-09-13T21:13:24.450260+00:00.

The final sources were cleaned and rebuilt sequentially from manuscript/ using:

    latexmk -C -outdir=build main.tex
    latexmk -pdf -interaction=nonstopmode -halt-on-error -file-line-error -outdir=build main.tex

Both commands returned zero. The complete transcript is audit/release-build-transcript.txt. The final compiler log is manuscript/build/main.log; the BibTeX log is manuscript/build/main.blg. The final logs contain no fatal diagnostic, undefined citation/reference, duplicate or missing bibliography entry, BibTeX warning, or overfull/underfull box. A preliminary cleanup invoked from the project root could not find main.tex; the successful final clean build used the correct manuscript directory and is the one audited here.

The bibliography helper reports exactly five cited keys, five bibliography keys and five aux bibcite keys, with no missing or unused keys. pdfinfo confirms the correct title and author, five A4 pages, no encryption or JavaScript. pdffonts confirms every font is embedded. pdftotext produces nonempty text with resolved references and mathematical cross-references.

The TeX recorder's authored input is main.tex; generated main.aux, main.out and main.bbl are build products. BibTeX reads references.bib. The remaining three publication source_files are supplementary code, data and README. No figure or local custom style is missing from the dependency declaration. Details: audit/release-dependencies.json and audit/bib-key-check.txt.

The supplementary functions were freshly executed without rewriting the source output. They reproduce every JSON-normalized value, including 198627 ambient lattice vectors, 6917 forests, 17577 cost words and compositions through degree 13. The original raw-Python equality check encountered tuple/list and integer-key/string-key serialization differences; normalization removed precisely those representation differences, with no numerical discrepancy. These are finite checks, not an all-degree proof.

Bindings: mathematical snapshot fac6a5d3e0cc11fe8e7a02ae312a3c4409afeaca9b3251dfc764c6d793a56ea2; manuscript 863b4513670a4d8e25144e3f958007d18a47406d9eabbd1dfa952134d7d93f35; PDF 7804aae2fb6f4f09261ece569ad0b9487ff4b7e349367a9cbcecae67856667ff.
