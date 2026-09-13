# Citation-check pass 1: frozen claim extraction

Document: `paper/main.tex`

Extraction only; verification is recorded separately in
`audit/CITATION_AUDIT.md`.

| ID | Claim | Type | Location |
|---|---|---|---|
| CC01 | Earlier work associates every \(n\)-vertex tree with a homogeneous \(n\)-component, \((3n-2)\)-parameter LV class having \(n-1\) additional edge DPs. | attribution + statistic + existence | Introduction, first paragraph |
| CC02 | Van der Kamp studied linear Darboux-coordinate changes and the induced LV-equivalence of admissible hypergraphs. | attribution | Introduction, first paragraph |
| CC03 | Conjecture 12 states that nonisomorphic trees are not LV-equivalent, and the source reports verification for \(n<9\). | attribution + quote/paraphrase + statistic | Introduction, first paragraph |
| CC04 | The version of record studies general parametric classes and explicitly excludes classification of special subclasses. | attribution | Introduction, second paragraph |
| CC05 | The free diagonal and directed-edge parameters, with row equalities off edge endpoints, are the standard generic tree-system parametrization. | attribution + existence | Section 2, first paragraph |
| CC06 | Lemma 2 of the source gives the displayed C2 and C3 conditions as the linear-DP criterion, sufficient in the homogeneous case. | attribution | Section 3, before Lemma 3.2 |
| CC07 | The exact counts of unlabeled trees for orders \(2,\ldots,9\) are \(1,1,2,3,6,11,23,47\). | statistic | Proposition 5.1 table |
| CC08 | The exact circuit-incidence invariant has respectively \(1,1,2,3,6,11,23,47\) distinct values at orders \(2,\ldots,9\). | statistic + existence | Proposition 5.1 table |
| CC09 | The no-import verifier enumerates all Prüfer words, recomputes both invariants, and rejects six specified corrupted inputs. | statistic + existence | Section 5, verification description |
| CC10 | The exact certificate SHA-256 is `5be053e1f8e676769ad33237055bed21c76f9825fd373f7832fb2d21dc414fe6`. | exact identifier | Section 5, verification block |
| CC11 | On a three-vertex path the C3 coefficient determinant has the displayed exact factorization. | existence + exact formula | Remark 3.3 |
| CC12 | No floating-point calculation is used in the finite certificate verification. | existence/negative fact | Section 5, verification description |
