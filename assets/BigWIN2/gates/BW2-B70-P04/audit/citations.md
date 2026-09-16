# Citation and bibliography audit

## Scope and decision

This is the second pass of a two-stage, non-interactive citation audit for
`win-00070-p04-release-9532e2561464`, citation attempt 2, launch
`b7e53416-35c3-42a7-8358-a91325c339b3`.  The first pass froze the five
claim/citation pairs in `audit/citation-claim-ledger.json` before any source
verification.  This pass used that ledger without re-extraction.
The release prompt explicitly prohibited subagents, so the fresh per-key
verification was performed sequentially in this single release context.

All five claims are verified against primary records.  The three ordinary
body-flow keys are defined, used, and supported by their nearby claims.  No
decorative citation, unsupported strengthening, undefined key, or bibliography
coverage gap was found.  Verdict: **accept**.

## Claim-to-source verification

| Claim | Key | Primary locator and exact support | Status |
|---|---|---|---|
| CIT-001 | `Mantovanelli2026` | Marco Mantovanelli, arXiv:2609.04993v1, abstract and Theorem 1.1 (official HTML lines 30--55 and 81--116) state the right-edge value and the closed zero-free half-plane. Section 7, official HTML lines 697--709, gives the displayed near-edge zero and explicitly characterizes the search as targeted rather than exhaustive. | Verified, exact numerical value and paraphrase |
| CIT-002 | `Mantovanelli2026` | Remark 7.5 and the surrounding discussion (official HTML lines 669--699) label the shrinking-target statement as heuristic and say it is not proved. | Verified, paraphrase |
| CIT-003 | `Mantovanelli2026` | Proposition 7.1 (official HTML lines 558--582) has the same hypothesis, definitions, and inequalities (17)--(20) reproduced in manuscript lines 96--131. | Verified, exact mathematical transcription |
| CIT-004 | `Johansson2017Arb` | Fredrik Johansson, *IEEE Transactions on Computers* 66(8), 1281--1292 (2017), DOI 10.1109/TC.2017.2690633. The author-hosted paper, page 1 abstract and Section 1, identifies Arb as arbitrary-precision midpoint-radius interval/ball arithmetic and explicitly supports real and complex arithmetic and transcendental evaluation. | Verified, paraphrase |
| CIT-005 | `ZengEtAl2026FiniteCertificates` | Zijian Zeng, Houde Liu, Kuru Ratnavelu, and Ong Seng Huat, Preprints.org Version 1, DOI 10.20944/preprints202608.1658.v1, Section 6 (official page lines 207--218). It separates discovery from certification, reconstructs finite instances, uses exact integer predicates, includes an independent implementation, and states its trust boundary. Manuscript lines 458--463 expressly limit the comparison to this architecture. | Verified, paraphrase |

Primary records inspected:

- https://arxiv.org/html/2609.04993v1 and the frozen primary PDF
  `evidence/external/2609.04993v1.pdf`.
- https://fredrikj.net/math/arbpaper.pdf and
  https://doi.org/10.1109/TC.2017.2690633.
- https://www.preprints.org/manuscript/202608.1658/v1 and
  https://doi.org/10.20944/preprints202608.1658.v1.

For each record, the audit ran the applicable author/year/title, exact-title,
author/year/venue, DOI, and arXiv-identifier search templates on 2026-09-08,
then relied on the primary text rather than search snippets for support.

## Metadata and BibTeX consistency

| Key | Current title versus primary title | Authors/year/venue or version | Action |
|---|---|---|---|
| `Mantovanelli2026` | Exact title match | Marco Mantovanelli; arXiv:2609.04993v1; 2026 | Retained |
| `Johansson2017Arb` | Exact title match apart from BibTeX capitalization protection | Fredrik Johansson; IEEE Transactions on Computers 66(8), 1281--1292; 2017; DOI exact | Retained |
| `ZengEtAl2026FiniteCertificates` | Exact title match | Four authors, Preprints.org Version 1; 2026; DOI exact | Retained |

No key changed and no BibTeX replacement was needed.  The mechanical audit
found three cited keys, three unique database entries, no unused entry, and
complete agreement with the final `.aux` file.  The converged `.log` and `.blg`
contain no undefined citation, missing database entry, repeated entry, or
BibTeX warning.

## Coverage and user-library gate

The bibliography is claim-driven rather than quota-driven.  Mantovanelli is
the problem-origin and closest prior source; Johansson is the natural primary
method source for Arb; and the directly cited user-library item supplies the
bounded certificate-architecture comparison.  The latter is registry row 9
and is bound in `audit/user-bibliography-selection.json`.  It is an ordinary
body-flow citation, while the two natural non-library sources also appear in
ordinary body flow.  A second library item would not support a distinct nearby
claim and would be padding.

The union of citation keys in the frozen ledger is exactly
`{Johansson2017Arb, Mantovanelli2026, ZengEtAl2026FiniteCertificates}`, equal to
the ordinary body-flow citation-key set in `manuscript/main.tex`.
