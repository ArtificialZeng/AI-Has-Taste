# Citation and bibliography release audit

## Summary

Mode: primary-source search verification, performed as two non-interactive
stages. Stage 1 froze 18 manuscript claims and 10 claim/citation pairs in
`audit/claim-ledger.json` before source checking. Stage 2 verified that fixed
ledger and is recorded in `audit/citation-verification.json`.

All 18 claims are supported; all 10 citation pairs are verified. There are no
numerical errors, hallucinations, misleading attributions, unverified claims,
undefined citation keys, or blocked records. The bibliography checker found
five cited keys, five canonical BibTeX entries, and identical source/AUX key
sets. No BibTeX or citation-key change was necessary.

The bibliography audit was performed by the primary worker because the user
expressly prohibited agents and background workers.

## Claim-to-source verification

| Key | Nearby claim | Primary source and exact location | Result |
|---|---|---|---|
| `DongEtAl2023` | Differential elimination produces input-output relations used for structural identifiability. | Official SIAM article page, abstract; DOI `10.1137/22M1469067`. | Verified, paraphrase. |
| `MukhinaPogudin2025Projection` | Coordinate-projection support bounds yield an evaluation-interpolation algorithm. | arXiv `2501.13680v4`, abstract and version record. | Verified, paraphrase. |
| `MukhinaPogudin2026` | The support-bound method includes general polynomial outputs and unknown constant symbolic parameters. | Official Springer chapter page, abstract and citation block; DOI `10.1007/978-3-032-09645-6_15`. | Verified, paraphrase. |
| `JeronimoLanciano2026` | Differential-input support bounds, the specialized 7-to-6 row, eliminant definition, highest-derivative observation, and open broader problem. | Local primary PDF `evidence/external/2609.03828.pdf`: Definition 3.3 p.9; Theorem 3.7 pp.11-12; Corollary 3.11 pp.15-16; Section 4.2 table p.23; Section 5 pp.23-24. Metadata also checked at the official arXiv record for `2609.03828v1`. | Verified; exact for the table and theorem locator, paraphrase elsewhere. |
| `Zeng2026Bezout` | A methodological parallel involving a generic characteristic-zero conclusion, nonempty Zariski-open locus, and exceptional inputs. | Official Preprints.org full text for DOI `10.20944/preprints202608.2160.v1`, abstract, Theorem 3.1, Lemma 3.2, and Theorem 4.1. | Verified, paraphrase; the manuscript expressly says this is not differential elimination. |

The manuscript's new eliminant claims are not attributed to outside
literature. They are supported by the self-contained coefficient-ring proof,
the accepted independent mathematical audit in `audit/math.md`, and the exact
certificate `evidence/research_symbolic_certificate.py`. The local source PDF
confirms that the cited preprint reports only stable finite-field evidence for
the 7-to-6 row, so the manuscript does not strengthen a source statement into
a prior symbolic proof.

## Coverage and relevance

Coverage is scholarly rather than library-only: the bibliography includes the
direct problem source, both closest support-bound predecessors, a primary
structural-identifiability context source, and the single active user-library
item with a defensible nearby methodological claim. A second user-library item
was rejected because none of the remaining 48 records concerns differential
elimination or the same generic-locus issue closely enough; including one would
be padding. The bound selection is in
`audit/user-bibliography-selection.json`, using citation attempt 1 and launch
ID `42680f52-78c6-48c9-8275-d145c60e5599`.

No citation is decorative: each retained item supports the claim immediately
around its ordinary body-flow `\\cite{FinalKey}`. No standard proof fact used
here requires another natural citation: the Cayley--Hamilton identity and
polynomial division are explicitly worked out, while the exact computation is
fully disclosed and reproducible.
