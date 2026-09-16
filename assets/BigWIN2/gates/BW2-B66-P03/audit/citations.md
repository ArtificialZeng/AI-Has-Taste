# Fresh citation and bibliography audit

Mode: search verification with frozen local primary evidence  
Document: `manuscript/main.tex` and `manuscript/references.bib`  
Generated: 2026-09-07 (UTC)

Release job: `win-00066-p03-release-5211be7d8dff`; citation attempt 3;
launch `80f30c50-cc69-46a9-87b1-af85f2d69182`.

## Summary

| Metric | Count |
|---|---:|
| Claim/citation pairs frozen in pass 1 | 3 |
| Verified | 3 |
| Numerical error | 0 |
| Unverified | 0 |
| Hallucination | 0 |
| Misleading | 0 |
| Citation not found | 0 |

Overall status: **PASS**. The body-flow citation-key union in
`audit/citation-claim-ledger.json` is exactly the three keys extracted from the
canonical TeX. Pass 2 found direct primary support for every nearby claim. The
detailed passages, source URLs, limitations, and coverage rationale are in
`audit/citation-source-verification.md`.

## Claim results

| ID | Key | Status | Confidence | Primary support |
|---|---|---|---|---|
| C01 | `FinkEtAl1990` | Verified | exact | Elsevier article record and abstract give the four authors, publication metadata, and the stated definition. |
| C02 | `Yavari2026` | Verified | exact | arXiv v1 Eq. (3.1), Propositions 3.2, 4.1, and 4.2, and full-paper inspection support the graph, values, witness, four-edge result, and precise classification gap. |
| C03 | `Zeng2026Whiskered` | Verified | paraphrase | Official SSRN abstract explicitly reports exhaustive canonical graph enumeration and independent checking by a short verifier. |

The audit was serial because this bounded job expressly prohibited subagents,
other Codex processes, and background workers.

## Bibliography and coverage

| Final key | Role in paper | Action | Uncertainty |
|---|---|---|---|
| `FinkEtAl1990` | Natural non-library primary source for the parameter's origin and definition | retained; metadata verified | none |
| `Yavari2026` | Natural non-library primary source for the graph and closest prior result | retained; local primary PDF inspected | arXiv record search indexing was incomplete, but the checksum-bound arXiv-generated v1 PDF supplies the complete primary text and metadata |
| `Zeng2026Whiskered` | Active-library row 42; direct method comparison | retained; official SSRN record verified | none |

The active 49-entry first sheet was screened. Row 42 is the sole genuinely close
library match to both canonical graph enumeration and a short independent
verifier; a second library citation would be decorative. The bibliography is
not library-only: its two non-library primary sources cover the actual origin
and closest prior theorem. The self-contained finite proof invokes no external
algorithmic theorem requiring another method citation.

No BibTeX or citation-key changes were necessary. The mechanical audit reports
three cited keys, three BibTeX entries, no missing or unused entries, and exact
AUX agreement. The converged log and BLG contain no undefined citation or
reference, missing database entry, repeated entry, LaTeX error, fatal stop,
undefined control sequence, runaway argument, overfull box, or underfull box.
