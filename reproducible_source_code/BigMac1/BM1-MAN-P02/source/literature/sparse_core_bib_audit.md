# Bibliography and bounded novelty audit for the sparse-core manuscript

Date: 2026-08-27  
Mode: serial, following the user's instruction not to run the two research
problems concurrently.

## Result

The manuscript `paper_sparse_core/main.tex` cites nine keys and
`paper_sparse_core/references.bib` contains exactly those nine entries.  The
post-build auxiliary file contains the same nine keys.  There are no missing
bibliography files, missing entries, unused entries, or unresolved citations.

Eight entries were already checked against the publisher, DOI-registry,
author, or arXiv records recorded in:

- `literature/official_bib_audit_batch1.md`;
- `literature/second_batch_official_bib_audit.md`;
- `literature/stanic_official_bib_audit.md`;
- `audit/CITATION_AUDIT.md`.

The ninth entry is Md Isheteyak Zaffer's *Unimodular Bicyclic Graphs*, checked
against the official arXiv record and official arXiv BibTeX export for
arXiv:2608.21475.  The record states the title, sole author, 2026 year and
primary class `math.CO`.  Its inclusion is contextual: the present theorem
does not import Zaffer's classification or any unproved premise from it.

Official record:
<https://arxiv.org/abs/2608.21475>

## Claim support and scope

- Akbari--Elphick--Kumar--Pragada--Tang supports the formulation and the
  publication-state statement that the general rank--order question is posed
  as a conjecture.
- Haemers--Peeters, Ghorbani--Mohammadian--Tayfeh-Rezaie, and
  Esmailian--Ghorbani--Hossein Ghorban--Khosrovshahi support the historical
  rank--order and maximal-graph context.
- Ellingham supports the basic-subgraph determinant factorisation used in the
  paper's reduction.
- Stanić's two papers support the fixed-rank/star-complement context.
- Zaffer supplies current determinant context for bicyclic graphs only.

A bounded primary-source and citation-chain search found no earlier theorem
with the exact scope proved here: every reduced adjacency-rank-ten graph
containing a connected nonsingular induced ten-vertex core with at most eleven
edges has at most 62 vertices.  This is a recorded “not found” result, not a
proof of bibliographic novelty.  The manuscript states this limitation and
does not claim that the unrestricted rank-ten conjecture is solved.

## Mechanical gate

The serial citation checker reported:

```text
cited_keys: 9
bib_keys: 9
cited_keys_missing_from_bib: 0
bib_keys_not_cited: 0
aux_bibcite_keys: 9
cited_keys_missing_from_aux: 0
aux_keys_not_cited: 0
```

Status: **PASS**, with no citation blocker.
