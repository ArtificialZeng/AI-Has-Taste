# Fresh citation and bibliography audit

Job: `win-00064-p02-release-0573327856cc`  
Search date: 2026-09-07  
Method: citation-check-skill v2 search verification, followed by the mechanical
BibTeX audit.  Subagents were not used because this bounded job explicitly
prohibited agents and background workers.

## Two-stage protocol

Extraction was completed first and frozen in
`audit/citation-claim-ledger.json` (SHA-256
`27eb6aab3788a72216d9644bc0b0d311b02da2f96c5564fcacd89c22426e03a2`).
The ledger contains five claim/citation pairs and four unique citation keys.
The second stage verified only those frozen pairs.  The structured results and
source locations are in `audit/citation-source-verification.json`.

## Claim-to-source verification

| Claim | Final manuscript location | Source and exact support | Result |
|---|---|---|---|
| C01 | lines 45--53 | Lewis, *Studia Mathematica* 63(2), pp. 207--212, DOI `10.4064/sm-63-2-207-212`; the historical attribution is explicitly corroborated by Padmanabhan, Definition 1.1, p. 2, footnote 1. | Verified (paraphrase) |
| C02 | lines 45--53 | Padmanabhan, arXiv:2609.04338v1, Definition 1.1 and (1.1), p. 2. | Verified (exact) |
| C03 | lines 55--67 | Padmanabhan, Section 3.2, Lemma 3.1 and (3.8)--(3.9), p. 13. | Verified (exact) |
| C04 | lines 71--75 | Edidin--Gonzalez--Tamo, arXiv:2511.09505v1, Sections 2.2 and 2.5 and Proposition 3.2 in Section 3.2. | Verified (exact) |
| C05 | lines 76--78 | Zeng--Liu--Ratnavelu, Preprints version 1, Section 2.2, Lemma 1 and equations (6), (10)--(11). | Verified (exact) |

Primary records inspected:

- <https://www.impan.pl/en/publishing-house/journals-and-series/studia-mathematica/all/63/2>
- <https://arxiv.org/abs/2609.04338v1>
- <https://arxiv.org/html/2511.09505>
- <https://www.preprints.org/manuscript/202608.1346>

The Edidin locator initially omitted Section 2.5, where the whitening statement
actually occurs.  The manuscript was repaired and re-audited.  The Lewis entry
was augmented with its official DOI.  No citation key changed.  All four final
entries agree on author, title, year, venue/version, and identifier with their
authoritative records.

## User-library binding and coverage

The active 49-record first-sheet registry and source workbook were checksum
verified.  Row 23 is the one genuinely relevant library item and is bound to
publication attempt 1 and launch
`dad70831-ac57-441a-bdff-20442bbfed95` in
`audit/user-bibliography-selection.json`.  Its primary Preprints.org text
directly supports the nearby symmetric-tensor claim, and the final key appears
in an ordinary body-flow `\cite{ZengLiuRatnavelu2026}`.  The dynamic BigWin
selection validator passed.

One library item is appropriate here.  The only plausible second library lead
concerns a different Hadamard-factorization problem and would not support any
nearby claim.  The bibliography is not library-only: it also includes the
primary problem/rate source, the original Lewis record, and the closest
frame/whitening construction.  The proof is deductive and self-contained, so
it does not depend on an uncited computational verification technique.  The
manuscript makes no verified-open-status or priority claim.  Coverage is
complete without decorative references.

## Mechanical audit

The canonical bibliography is `manuscript/references.bib`.  Four unique keys
are cited and all four are defined and emitted into `main.aux`/`main.bbl`; no
entry is unused.  The bibliography checker reports zero missing files, missing
keys, unused entries, or AUX discrepancies.  Final log scans found no undefined
citations/references, BibTeX missing-database warnings, duplicate entries, or
LaTeX errors.  No official verification blocker remains.

**Verdict: accept.**
