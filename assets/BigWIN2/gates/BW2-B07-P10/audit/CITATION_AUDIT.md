# Citation and novelty audit

Search cutoff: 2026-08-31 (Asia/Shanghai).

## Claim-to-source checks

| Manuscript claim | Supporting source and checked location | Result |
|---|---|---|
| Unlabeled counts through 16 and \(U(16)\) | Brinkmann--McKay (2002), Table 1 | pass |
| Labeled counts through 17 used in the certificate | Brinkmann--McKay (2002), Table 2 | pass |
| Full order-16 strict-relation histogram | Brinkmann--McKay (2002), Table 59; all 121 entries parsed from the archived PDF | pass |
| Live A000112 endpoint is 16 | OEIS A000112, accessed 2026-08-31 | pass |
| Labeled frontier advanced to 19 but not the unlabeled frontier | Ayala, arXiv:2606.31526v1, abstract/results; shipped aggregation reproduced | pass with scope note |
| Published disconnected \(D(17)\) and component strata | Mohammad--Noor--Talukder (2022), equation (11) and Table 4 | pass; also independently recomputed |
| Colex maximizes the number of cliques of every fixed size for a fixed number of edges | Kirsch--Radcliffe (2021), Proposition 1, based on Kruskal (1963) | pass |

Crossref metadata was checked for the Brinkmann--McKay,
Kirsch--Radcliffe, and Kruskal references.  The Journal of Integer Sequences
publisher record and PDF were used for the disconnected result.  The arXiv
version is pinned to v1 and its public code/data revision is recorded in the
research audit.

The LaTeX citation audit reports six citation keys, six bibliography entries,
no missing keys, and no unused entries.  Each externally sourced numerical
input in the proof is attributed.  The 2026 residue reconstruction is not
presented as an independent rerun or as a certificate for \(U(17)\).

## Novelty search

Before derivation and again after certification, searches covered OEIS,
arXiv, Crossref/publisher records, author/software pages, broad web indexes,
and exact result fingerprints.  On the final pass, neither bound integer nor
the exact interval was located.  No exact \(U(17)\) was found, while the known
disconnected value was found and credited.  Queries and negative-result scope
are recorded in `literature/search_log.md`.

This is not a universal novelty proof.  The manuscript therefore says only
that the interval was not located in the named searches through the cutoff.

Status: **passed** for citation accuracy, primary-source use, and
search-bounded novelty wording.
