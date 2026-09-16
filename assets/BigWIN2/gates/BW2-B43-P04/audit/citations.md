# Citation and bibliography audit

Verdict: **accept**.

Audit date: 2026-09-06. Method: two-pass search verification under
`citation-check-skill`, followed by the BibTeX mechanical checker. The explicit
job constraint prohibited subagents, so all seven keys were checked serially.
Pass 1 is frozen in `audit/citation-claim-ledger.json`; this report and
`audit/citation-verification.json` are the independent Pass 2.

## Claim-to-source verification

| Key | Primary record and exact location | Nearby claim | Result |
|---|---|---|---|
| `HuKongWang2026` | Official arXiv record `https://arxiv.org/abs/2609.02845`; supplied v1 PDF: abstract, Theorem 2.8 (PDF pp. 6--7), and Problem 4.1 (PDF p. 15). | Definitions, `q_B<=10`, lower example, and the 9-versus-10 open problem. | Verified exact. Authors, title, version, statement, hypotheses, and locator match. |
| `Zeng2026Tuza` | Official Preprints.org v1 record `https://www.preprints.org/manuscript/202608.1304/v1`, abstract and Introduction/Theorem 1. | Methodological comparison: 44,702 canonical records with explicit packing/covering witnesses and independent verification. | Verified exact. The manuscript labels the paper a non-peer-reviewed methodological comparison and asserts no implication. |
| `ReadWilson1998` | Official Oxford Academic book record `https://academic.oup.com/book/54439`. | Source of the Graph Atlas. | Verified. Authors, 1998 date, publisher, ISBN, DOI, and atlas scope match. |
| `HagbergSchultSwart2008` | Proceedings page `https://conference.scipy.org/proceedings/SciPy2008/paper_2/`; author citation record; official NetworkX `graph_atlas_g` documentation. | NetworkX interface and its all-isomorphism-classes-through-seven coverage. | Verified exact. The software paper metadata match; the exact API behavior is confirmed by the primary project documentation (1,253 graphs, all orders 0--7). |
| `IgnatievMorgadoMarquesSilva2018` | DOI `10.1007/978-3-319-94144-8_26`, official project citation and author preprint, pp. 428--437. | PySAT provides Python access to SAT oracles used for the CNF instances. | Verified exact. |
| `AudemardSimon2009` | Original IJCAI PDF `https://www.ijcai.org/Proceedings/09/Papers/074.pdf`, pp. 399--404, especially abstract and Sections 1--4. | Glucose is in the Audemard--Simon CDCL solver family. | Verified paraphrase; official competition record also lists Glucose 1.0 by the same authors. |
| `Brelaz1979` | ACM DOI `10.1145/359094.359101`, original paper pp. 251--256. | DSATUR selects maximum saturation degree, with degree tie-breaking, inside an exact backtracking method. | Verified exact. |

All mandatory academic search variants were run: author/year/title words, full
title on the primary repository or publisher, author/year/venue, DOI where
available, and arXiv identifier where available. Exact searches for a later
resolution of `M_3(4)` returned no separate primary result as of the audit date;
this bounded search is not a priority or continuing-open-status proof. No
`literature/bibliography-revision-*.md` or `literature/crossref-*` files exist
in this project, so there were no supervisor captures to parse.

## Frozen claim decisions and coverage

All 18 frozen claims are verified; there are no numerical errors,
hallucinations, misleading attributions, unsupported strengthenings, or
unresolved claims. Mathematical and computational claims C02 and C06--C18 are
bound to the accepted mathematical report and the exact recorded outputs.

The bibliography is neither user-library-only nor padded. Hu--Kong--Wang is the
problem origin and closest prior result; Read--Wilson and Hagberg--Schult--Swart
cover the exact atlas/software dependency; Ignatiev--Morgado--Marques-Silva,
Audemard--Simon, and Brélaz cover the nontrivial verification methods. The
single active-library paper supports a genuinely nearby methodological claim.
The other 48 registry records do not support a distinct manuscript claim.

The manuscript has eight ordinary body-flow citation occurrences using seven
distinct keys. Every key occurs exactly once in `manuscript/references.bib`,
all entries are used, and the final `.aux` contains precisely those keys. No
official check required a BibTeX replacement or key change.

Mechanical command:

`python3 /home/ailab/.codex/skills/bib-reference-audit/scripts/check_bib_keys.py main.tex --aux main.aux`

Result: 7 cited keys, 7 bibliography keys, zero missing/unused keys, and exact
agreement with the `.aux`. Final `main.log` and `main.blg` contain no undefined
citation/reference, missing database entry, repeated entry, BibTeX warning, or
LaTeX/fatal diagnostic.
