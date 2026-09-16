# Root delivery audit

Audit date: 2026-08-31 (Asia/Shanghai)

## Mathematical replay

The root monitor independently reran `computation/verifiers/exact_cover_verify.py` under Python 3.10.12. The run exited successfully after 179.619 seconds and reproduced all frozen statistics:

- 1,203 collision hyperedges;
- a 31-element witness with 465 distinct strict-pair products;
- rejection of vertex-cover budget 30;
- 4,684,599 recursive states;
- 4,578,740 memoized infeasible states.

The result is therefore restricted to the finite strict-pair equality `F(62)=31`; it does not resolve any asymptotic or higher-product part of Erdős problem 425.

## Citation audit

All three cited records were checked individually against primary or authoritative records. No citation key or manuscript bibliography entry required replacement.

| Key | Record checked | Result |
|---|---|---|
| `Erdos1938` | Rényi Institute Erdős archive and original scan | Title, author, journal, volume, year, pages 74--82, and the different-members problem all verified. |
| `Erdos1969` | Springer/DOI record, Crossref export, and Rényi scan | Title, chapter, year, pages 77--82, DOI, and the graph-theoretic account all verified. |
| `LiuPach2019` | Elsevier/DOI record and arXiv 1808.06182 | Title, authors, journal, volume 165, year 2019, pages 152--175, DOI, and the cited asymptotic background all verified. |

The earlier referee note giving pages 237--252 for Liu--Pach was corrected to 152--175. The submission bibliography itself already had the correct pages.

Mechanical bibliography checks report three cited keys, three defined entries, no missing entries, no unused entries, and no auxiliary-file inconsistency. A converged `latexmk` build has no undefined citation, missing database entry, duplicate-entry, or fatal LaTeX warning.

## PDF and source-package audit

The final PDF has three letter-size pages. Its metadata title is *The Strict-Pair Product Extremal Value at 62 Is 31* and its author is Zijian Zeng. All pages were rendered at 160 dpi and inspected. Typography, equations, theorem statements, bibliography, affiliation, both email addresses, headers, page numbers, and whitespace are legible and free of clipping, overlap, missing glyphs, or black boxes.

Extracted PDF text and the packaged LaTeX sources were scanned for model/vendor names, prompting or agent terminology, proof-assistant traces, and digest-like workflow markers; none were present.

The LaTeX ZIP contains `main.tex` and `references.bib`. It was extracted into a new directory and rebuilt successfully with `latexmk`. The rebuilt document has the same title, author, page count, page size, and extracted text as the delivered PDF.

Verdict: PASS for delivery as a submission-ready certified finite-result manuscript and LaTeX source package, without any claim of journal acceptance or priority.
