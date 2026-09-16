# Citation and bibliography audit

## Verdict

**Accept.** Every ordinary body-flow citation in the canonical manuscript has a frozen claim entry, and each nearby claim is supported by an exact passage in a primary source. The six cited keys are defined once each, resolve in the clean build, and collectively provide natural coverage rather than decorative padding.

## Scope and method

The audit covered `manuscript/main.tex` and the canonical `manuscript/references.bib`. In stage one, the smallest citation-bearing sentences were frozen as claims C01--C06 for citation attempt 4 in `audit/citation-claim-ledger.json`; the union of their direct keys is exactly the set of ordinary body-flow citation keys. In stage two, each claim was independently rechecked against a primary record and a precise source location on 2026-09-09 UTC. The user explicitly prohibited sub-agents, so the six checks were performed sequentially. Metadata was then compared with the canonical BibTeX entries, and the compiled `.aux`, `.bbl`, and build log were checked for consistency.

## Claim-level verification

| Claim | Direct key(s) | Primary evidence and exact support | Result |
|---|---|---|---|
| C01 | `FazeliVardyYaakobi2015` | [arXiv 1505.06241](https://arxiv.org/pdf/1505.06241), printed pp. 1--2: the abstract introduces k-server PIR codes, and the definition states that each message bit has k disjoint recovery sets of coded bits. | Verified |
| C02 | `BoruchovskyEtAl2026` | [arXiv 2601.04041v2](https://arxiv.org/pdf/2601.04041v2), printed p. 3, Definitions 1--2: recovery sets and the information-symbol/all-symbol distinction. | Verified |
| C03 | `BoruchovskyEtAl2026` | Same source, printed p. 13, Theorem 23, and pp. 14--15, Remark 25 and the following computed cases: specialization at k=6 gives the odd-field 11/12 bounds, and the binary length-11 exclusion yields the binary value; the ternary length-11 case is not resolved there. | Verified |
| C04 | `WetzlerHeuleHunt2014`, `Heule2016` | [DRAT-trim paper](https://www.cs.utexas.edu/~marijn/publications/drat-trim.pdf), printed pp. 1--2, Definition 1 and the proof-sequence discussion; [DRAT format/checker note](https://arxiv.org/abs/1610.06229). These define the RUP/AT and RAT checking conventions and clausal additions/deletions used by the audit. | Verified |
| C05 | `AudemardSimon2009` | [IJCAI 2009 proceedings paper](https://www.ijcai.org/Proceedings/09/Papers/074.pdf), printed pp. 399--404: the primary paper introduces and names the GLUCOSE solver. | Verified |
| C06 | `ZengEtAl2026TernaryCertificates` | [Preprints.org v1](https://www.preprints.org/manuscript/202608.1658), Section 6: ancillary files separate discovery from certification, and the standard-library verifier independently reconstructs the finite predicates and checks stored colorings. | Verified |

## Bibliographic records

The titles, author lists, years, venues, arXiv identifiers, and DOI fields in all six retained BibTeX records agree with their primary publication records. No citation key or bibliographic record required replacement. The Zeng--Liu--Ratnavelu--Huat record is the sole selected entry from the active 49-row user library and is directly cited in ordinary body flow for its exact-certificate methodology. Its primary Preprints.org record confirms title, authors, version, and DOI. Selecting any additional user-library item would not support a natural manuscript claim.

The bibliography is not library-only: the five non-library primary sources cover the PIR-code origin, the closest all-symbol prior result, the DRAT/RUP verification method, and Glucose solver provenance. Conversely, no uncited or merely decorative entry remains in the canonical bibliography.

## Mechanical checks

- Six ordinary body-flow citation keys occur in the manuscript; their set exactly matches the ledger union.
- All six keys occur exactly once as entries in `manuscript/references.bib` and resolve in the clean LaTeX/BibTeX build.
- The canonical build has no undefined citation, missing BibTeX entry, duplicate entry, or unused bibliography entry.
- No comments, `nocite`, verbatim material, inert macros, or hidden conditionals contribute citation keys.
- `audit/user-bibliography-selection.json` is bound to citation attempt 4, launch `38c670db-415f-4c96-bb1b-351c545751e5`, the active registry digest, and the literal smallest citation-bearing sentence.

Detailed machine-readable source locations and support decisions are recorded in `audit/citation-verification.json`.
