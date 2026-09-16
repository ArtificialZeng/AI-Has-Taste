# Citation and novelty audit

Search date: **2026-08-29**.  Status: **PASS, with bounded novelty wording**.

The manuscript has one bibliographic entry and one citation.  The cited work
is Enrico Formenti and Supreeti Kamilya, *The Curious Case of Reversible
Elementary Second Order Cellular Automaton 115*, EPTCS 445 (2026), 95--103,
DOI `10.4204/EPTCS.445.12`, arXiv `2606.13159v1`.

Primary-source checks:

- arXiv exposes v1, submitted 2026-06-11, and identifies the EPTCS journal
  reference and DOI;
- Crossref identifies the publisher as Open Publishing Association, the
  volume/pages/DOI metadata, and two authors;
- the full primary text states the odd formula as Conjecture 2 and supports
  the manuscript's attribution;
- the source archive used for statement repair has SHA-256
  `ac94238b79e5d356bfe2a62c13e6e262774aac49fbc832d77b562c61e56cca9c`.

Endpoint novelty searches covered exact title, formula, family, conjecture
number, author pair, arXiv version history, Crossref, OpenAlex, and Semantic
Scholar.  Crossref, OpenAlex, and Semantic Scholar each reported zero forward
citations at the check time; no distinct proof, disproof, correction, journal
expansion, or superseding preprint was found.  Because the source is recent,
the manuscript and handoff state only “no public solution found through the
recorded searches as of 2026-08-29”; they do not claim that unindexed or
private work cannot exist.

Static LaTeX audit: `cited=1`, `bib=1`, `missing=0`, `unused=0`.  The BibTeX
run completed without warnings.  No borrowed theorem beyond the original
problem attribution is used; the tree lemma and all cellular identities are
proved in the manuscript.
