# Citation and bibliography audit

Mode: search verification.  Date: 2026-09-07.  The fixed pass-1 extraction is
`audit/claim-ledger.json`; pass 2 used that ledger without re-extraction.  The
user explicitly prohibited subagents, so the requested per-reference checks
were performed serially in this release context.

## Result

All nine ledger claims are verified.  There are no numerical errors, missing
citations, misquotations, hallucinations, misleading citations, or unverified
claims.  Exact claim-level source locations are recorded in
`audit/source-locations.json`, and the machine-readable decisions are in
`audit/citation-verification.json`.

| claim | result | decisive source location |
|---|---|---|
| C01 | Verified (paraphrase) | Fokam Souop--Bitjoka, abstract and Definition 1 |
| C02 | Verified (paraphrase) | Babai--S\H{o}s, publisher abstract |
| C03 | Verified (exact) | Fokam Souop--Bitjoka, Remark 12, PDF p. 6 |
| C04 | Verified (exact) | Fokam Souop--Bitjoka, Theorem 6, PDF p. 5 |
| C05 | Verified (paraphrase) | Zeng et al., abstract and Sections 3 and 6 |
| C06 | Verified (exact) | enumeration log and accepted mathematical audit |
| C07 | Verified (exact) | exhaustive-search source and accepted audit |
| C08 | Verified (exact) | witness and 21-pair verification record |
| C09 | Verified (exact) | both program sources and project inventory |

## Bibliographic records and nearby support

- `FokamSouopBitjoka2026`: arXiv's current record gives Rigobert Fokam Souop
  and Laurent Bitjoka, title, v2 revision date 3 September 2026, subject, and
  DOI.  The local primary PDF has matching authors/version and directly
  supports every nearby use (Definition 1, Theorem 6, Remark 12).
- `BabaiSos1985`: the Elsevier DOI record gives the title, both authors,
  journal, volume/issue, pages 101--114, year 1985, and an abstract directly
  discussing induced subgraphs of Cayley graphs.  The citation is necessary
  historical/closest-framework context, not decorative.
- `ZengLiuRatnaveluOng2026`: the primary Preprints.org version-1 page gives the
  four authors, title, posted date, and the exact symmetry-reduced enumeration,
  integer-predicate, and independent-verification features asserted nearby.
  It is the sole selected active-library entry and appears through an ordinary
  body-flow `\cite{ZengLiuRatnaveluOng2026}`.

The bibliography is not library-only: it includes the primary problem source
and foundational primary literature in addition to the one genuinely relevant
library paper.  A second library item would not support a natural claim and
would be padding.  The manuscript's finite-abelian-group classification and
elementary difference criterion are proved or explained locally and need no
additional citation.  No broad novelty or priority claim is made.

The canonical bibliography contains exactly the three cited keys.  The
read-only key checker found no missing bibliography file, missing key, unused
entry, or `.aux` mismatch.  No key or BibTeX replacement was needed: title,
author, year, venue/version, DOI, and nearby support all agree with the primary
records checked.

Scope limitation: the recent arXiv item is a preprint, and the library item is
explicitly a non-peer-reviewed version-1 preprint.  Their status is not
strengthened in the manuscript.  The literature check establishes source
existence and support as of the stated date, not journal acceptance or proof of
priority.
