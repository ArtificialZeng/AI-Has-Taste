# Citation audit

Audit date: 2026-08-30 (Asia/Shanghai).

Scope: every citation-bearing sentence in paper/main.tex and every BibTeX
entry in paper/references.bib. The automated LaTeX audit reports
cited=9, bib=9, missing=0, unused=0.

## Claim-by-claim verification

| Paper claim | Citation key | Source checked | Support and boundary | Result |
|---|---|---|---|---|
| The finite-integer equal-length problem arose in uniformly repetitive semigroups. | PirilloVarricchio1994 | [DOI 10.1007/BF02573477](https://doi.org/10.1007/BF02573477), Crossref and EuDML metadata | The 1994 paper is the printed semigroup formulation. The manuscript does not make an unsupported earliest-priority claim. | verified |
| Recent primary sources continue to state the integer problem as open. | PopoliShallitStipulanti2024 | [DOI 10.4230/LIPIcs.FSTTCS.2024.32](https://doi.org/10.4230/LIPIcs.FSTTCS.2024.32), publisher PDF | The introduction distinguishes the open integer problem from automatic-sequence complexity results. | verified |
| Same open-status sentence. | AndradeMol2025 | [DOI 10.1007/978-3-031-97548-6_3](https://doi.org/10.1007/978-3-031-97548-6_3), arXiv:2408.15390v2, DBLP | The opening discussion treats additive-square avoidance over finite integer alphabets as open. The citation uses the WORDS 2025 version of record. | verified |
| Same open-status sentence. | Vukusic2026 | [DOI 10.1080/00029890.2025.2545706](https://doi.org/10.1080/00029890.2025.2545706), arXiv:2506.21200v1, publisher/Crossref | The article presents a continuous analogue and reports the discrete integer problem as open. The manuscript uses the Monthly version of record. | verified |
| Brown proves bounded-error approximations, not exact equality. | Brown2012 | [DOI 10.1515/integers-2012-0006](https://doi.org/10.1515/integers-2012-0006), full Integers article | Theorem 2.1 gives adjacent equal-length blocks with bounded difference of sums. The manuscript preserves the approximation qualifier. | verified |
| Rao--Rosenfeld construct an infinite ASF morphic word over \(\mathbb Z^2\), not \(\mathbb Z\). | RaoRosenfeld2018 | [DOI 10.1137/17M1149377](https://doi.org/10.1137/17M1149377), arXiv:1511.05875v2 and ancillary C++ | The theorem and weights are genuinely two-dimensional. The manuscript explicitly avoids calling this a scalar solution. | verified |
| Freedman--Brown give exact balanced-family values and \(\min g(A)=50\) over four-element real sets. | FreedmanBrown2016 | [journal PDF](https://math.colgate.edu/~integers/q33/q33.pdf), Theorem 1 and table | Their theorem assumes \(a+d=b+c\) for the upper-bound family, and the global minimum statement is over four-element real sets. Both quantifiers are retained. | verified |
| The public exact baseline is \(g(\{0,1,2,4\})=62\). | TheoremDB2026 | [TheoremDB R28](https://theoremdb.org/records/asq-claim-alphabet-0124-maximum-62/) and its Python/C++ artifacts | The record reports 19,097,778 nodes, 5,350,440 leaves, maximum 62, and two maximizers. The local exact reproduction matches all four invariants. | verified |
| Keränen constructed an infinite abelian-square-free word on four symbols. | Keranen1992 | [DOI 10.1007/3-540-55719-9_62](https://doi.org/10.1007/3-540-55719-9_62), ICALP bibliographic record | The cited theorem is abelian-square avoidance on four letters. The base-\(N\) scalar consequence in the manuscript is then proved directly, rather than attributed to the source alone. | verified |
| The unbounded four-letter lower-bound observation is also present in Freedman--Brown. | FreedmanBrown2016 | same journal PDF, introduction | The paper explicitly observes arbitrarily long sequences on suitable four-number sets via abelian-square-free words. | verified |

## Bibliographic metadata verification

- Andrade--Mol: authors, title, LNCS 15729, pages 24--36, year 2025, and DOI
  agree with Springer/DBLP.
- Brown: author, title, Integers 12(5), pages 805--809, year 2012, and DOI
  agree with the version of record.
- Freedman--Brown: authors, title, Integers 16, article A33, 10 pages, and
  year 2016 agree with the journal PDF.
- Keränen: author, title, LNCS 623, pages 41--52, year 1992, and DOI agree
  with Springer.
- Pirillo--Varricchio: authors, title, Semigroup Forum 49(1), pages 125--129,
  year 1994, and DOI agree with Crossref/version-of-record metadata.
- Popoli--Shallit--Stipulanti: authors, title, LIPIcs 323, article
  32:1--32:18, year 2024, and DOI agree with Dagstuhl.
- Rao--Rosenfeld: authors, title, SIAM J. Discrete Math. 32(4), pages
  2381--2397, year 2018, and DOI agree with SIAM/arXiv.
- TheoremDB: record label, snapshot date, access date, and URL agree with the
  dated public packet. It is cited as a web record, not a journal article.
- Vukusic: author, title, American Mathematical Monthly 133(4), pages
  371--375, year 2026, and DOI agree with publisher/Crossref metadata.

## Novelty-language audit

Pass 2 searched the two exact values, tree sizes, witness prefixes, and the
four-state 2-uniform statement. No match was located in the recorded search
corpus. Because Semantic Scholar returned HTTP 429 and free-text OpenAlex
search was noisy, the paper uses only the bounded wording “not located in our
dated result-specific literature search” and explicitly says this is not a
priority claim.

Disposition: PASS. Every citation exists, its metadata was checked, and the
cited source supports the nearby claim with the stated quantifiers.
