# Triage evidence

Date checked: 2026-09-07 (Asia/Shanghai).  Job provenance:
`win-00066-p03-triage-9ca5b8b0c688`.

## Primary source inspection

Inspected the supplied nine-page PDF
`batches/inbox/bigWin-66-materials/2609.04257.pdf`.  Its computed SHA-256 is
`6a655bacced3f3c3a38f01b0dbf84638994491da8bcec8a6c4e415a5637828e4`,
matching `source.md`.  The corresponding record is
<https://arxiv.org/abs/2609.04257>.

- Theorem 1.2 (printed p. 2) states that a connected cubic bipartite graph has
  \(\gamma(G)=6\) and \(b(G)=5\).
- Eq. (3.1) (printed p. 3) is the same 27-edge graph as in `source.md`.
- Proposition 4.1 (printed pp. 5–6) deletes
  \(\{\{0,6\},\{0,10\},\{0,16\},\{6,7\},\{6,13\}\}\) and proves the
  resulting domination number is 7.
- Proposition 4.2 (printed p. 6) proves exactly that every four-edge deletion
  has domination number 6; the appendix supplies its verifier.
- A full-text search of the PDF found no automorphism-orbit classification and
  no enumeration of all qualifying five-edge deletions.  Exact-title, arXiv-ID,
  and exact-classification web searches on the date above located the preprint
  and general bondage literature, but no primary source supplying the requested
  classification.  This limited search is not a claim of novelty or priority.

Source status for triage: **new-question**.  The base values used to formulate
the finite classification are known from the cited preprint, while the
classification itself is not presented there.

## Independent cheap structural check

A fresh `python3` parse of the edge list found 18 vertices, 27 distinct
non-loop edges, degree sequence constantly 3, connectedness, and bipartition

`{0,1,4,5,7,9,13,15,17} | {2,3,6,8,10,11,12,14,16}`.

NetworkX 3.4.2 `GraphMatcher(G,G).isomorphisms_iter()` returned exactly six
automorphisms and three vertex orbits,

`{0,9,10,14,16,17}`, `{1,2,5,8,11,13}`, and `{3,4,6,7,12,15}`.

This is a useful tractability check, not yet an independently replayed group
certificate and not evidence for the screening counts 801 and 140.

