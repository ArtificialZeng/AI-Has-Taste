# Citation and bibliography audit

## Binding and method

This is the release citation audit for job
`win-00068-p07-release-862fda6bd033`, citation attempt 2, launch
`4537f319-9748-454d-a993-7626123bae99`.  It is bound to accepted
mathematical snapshot
`a880303a4e43dbf97139b6534dd02b8dbe50202ac203f9101f52b594b8b30519`,
manuscript snapshot
`34cf4cefa7e5a40c2841ab0f2ee3574e62a8df18ac6e4cc2ec9b9a7f05facd9f`,
and PDF
`b0b40018b6154f1d80fdbf0ab95e3acefb138dce2c61ab070945e8c9cde78ad3`.
The verification date is 2026-09-09 UTC.

The audit used two non-interactive stages.  First, all ordinary body-flow
citations were extracted from `manuscript/main.tex` and frozen in
`audit/citation-claim-ledger.json`; its eight claim records cover exactly the
seven active citation keys.  There are no custom citation macros, `nocite`
entries, hidden conditionals, or comment-only citations.  Second, the frozen
claims were checked against the original papers, publisher records, or primary
book text.  The user prohibited subagents for this bounded job, so the release
worker performed the same per-key protocol serially.

## Frozen claim-to-source verification

| Claim | Direct keys | Primary passage checked | Result |
|---|---|---|---|
| C01 | `Joyal1981`, `BergeronLabelleLeroux1998` | Joyal's publisher abstract states that species of structures are formulated categorically and that cycle-index polynomials enumerate isomorphism classes; Cambridge's book description and front matter identify a comprehensive treatment of species, labelled/unlabelled enumeration, and cycle indices. | Verified (paraphrase). |
| C02 | `Macdonald1995` | Macdonald, Chapter I, Section 7, printed pp. 115--116, explicitly defines the internal product under the Frobenius characteristic; the index points to “internal product: I, 7.” | Verified (exact topic and locator). |
| C03 | `GarsiaRemmel1985` | The Springer abstract states that the paper gives a general result relating shuffles and Kronecker products and a combinatorial interpretation when one Schur factor is a product of homogeneous functions.  The explicit homogeneous-basis rule is also restated as Corollary 5.3 of arXiv:2604.10336v1. | Verified (paraphrase). |
| C04 | `BaolahyBenjamin2026` | arXiv:2604.10336v1, Definition 3.3 (PDF p. 8), groups equal-sized rows into one diagonal cyclic factor; Corollary 5.5 (PDF p. 23) states closure of the resulting `KEsp` category under Cartesian/Hadamard product. | Verified (exact). |
| C05 | `BaolahyRandrianirina2026` | arXiv:2609.05010v1, Remark 3.2 (PDF p. 3), defines one independent factor per row for the companion species; Open Problem 5.1 (PDF p. 8) asks for the associated coefficient formula. | Verified (exact). |
| C06 | `Zeng2026MultiplicityArxiv` | arXiv:2608.18179v1, abstract, Theorem 1.1, and Lemma 2.2 state that the leading star-basis partition and immediately adjacent layer recover weighted-core data and yield reconstruction for the stated class of proper trees. | Verified (paraphrase). |
| C07 | `BaolahyBenjamin2026` | The earlier paper's Definition 3.3 uses the diagonal repeated-part convention, whereas the theorem in this manuscript explicitly assumes independent row factors. | Verified (direct comparison). |
| C08 | `BaolahyRandrianirina2026` | Open Problem 5.1 asks for a closed-form coefficient formula over the full subgroup lattice; the present theorem decides only nonnegative closure and the first failing degree. | Verified (direct scope comparison). |

No numerical citation claim was rounded or altered.  The exact counts in the
computational section are claims of the frozen reproducibility evidence rather
than claims attributed to the bibliography, and the manuscript labels the
computations as corroboration.

## Bibliographic record audit

| Key | Current and authoritative identity | Authoritative source | Action / uncertainty |
|---|---|---|---|
| `BaolahyRandrianirina2026` | J. Baolahy and B. Randrianirina, *The Molecular Species C-alpha: Geometric Realization and a Closed Formula for Kronecker Coefficients*, arXiv:2609.05010v1 (2026) | https://arxiv.org/html/2609.05010v1 | Retained; title, authors, date, identifier, and version agree. None. |
| `BaolahyBenjamin2026` | J. Baolahy and B. Randrianirina, *Species, Symmetric Functions, and Kronecker Product*, ECA 6(3), Article S2R19 (2026) | https://ecajournal.haifa.ac.il/Volumes.html and https://arxiv.org/html/2604.10336v1 | Retained; DOI `10.54550/ECA2026V6S3R19`, venue, article number, authors, and title agree. None. |
| `Joyal1981` | A. Joyal, *Une théorie combinatoire des séries formelles*, Advances in Mathematics 42(1), 1--82 (1981) | https://www.sciencedirect.com/science/article/pii/0001870881900529 | Retained; DOI `10.1016/0001-8708(81)90052-9` and all core fields agree. None. |
| `BergeronLabelleLeroux1998` | F. Bergeron, G. Labelle, and P. Leroux, *Combinatorial Species and Tree-Like Structures*, Encyclopedia of Mathematics and its Applications 67, CUP (1998) | https://www.cambridge.org/core/books/combinatorial-species-and-tree-like-structures/D994A1F2877BDE63FF0C9EDE2F9788A8 | Retained; authors, series, ISBN, publisher, and DOI `10.1017/CBO9781107325913` agree. None. |
| `GarsiaRemmel1985` | A. M. Garsia and J. Remmel, *Shuffles of Permutations and the Kronecker Product*, Graphs and Combinatorics 1, 217--263 (1985) | https://link.springer.com/article/10.1007/BF02582950 | Retained; DOI, title, authors, volume, year, and pages agree; issue 3 is consistent with the journal record. None. |
| `Macdonald1995` | I. G. Macdonald, *Symmetric Functions and Hall Polynomials*, second edition, OUP (1995) | https://academic.oup.com/book/52932 | Retained; author, edition, publisher, year, ISBN, and DOI `10.1093/oso/9780198534891.001.0001` agree. None. |
| `Zeng2026MultiplicityArxiv` | Z. Zeng, *Multiplicity-Isolated Cores and Chromatic Symmetric Reconstruction of Trees*, arXiv:2608.18179v1 (2026) | https://arxiv.org/html/2608.18179v1 | Retained; author, title, identifier, version, and DOI `10.48550/arXiv.2608.18179` agree. None. |

Seven of seven cited records were verified.  No BibTeX key or record required
replacement, so there is no old-to-new key mapping and no unresolved official-
record blocker.

## Coverage and mechanical checks

The bibliography is claim-driven rather than library-only.  The two Baolahy--
Randrianirina papers are the problem origin and closest prior work; Joyal and
Bergeron--Labelle--Leroux support the species framework; Macdonald supports the
internal product; and Garsia--Remmel is the natural primary source for the
classical homogeneous-basis comparison.  These six non-library sources occur
in ordinary body flow.  The single selected active-library work, registry row
17, is retained only for its narrow, explicitly qualified comparison about
basis coefficients carrying combinatorial information.  The other 48 active
records supply no natural source for a claim in this paper, so adding a second
would be padding.

The hook-compatible selection validator passed for attempt 2 and row 17.  The
BibTeX consistency checker found seven cited keys, seven bibliography entries,
no missing or unused entries, and exact agreement with the seven `aux` keys.
The final `.log` and `.blg` contain no undefined citation, undefined reference,
missing database entry, repeated entry, LaTeX error, or fatal diagnostic.

Verdict: **accept**.  All citation-bearing claims are supported at their stated
scope, bibliography coverage is complete for the manuscript's actual external
dependencies, and no decorative non-library reference or unsupported priority
claim remains.
