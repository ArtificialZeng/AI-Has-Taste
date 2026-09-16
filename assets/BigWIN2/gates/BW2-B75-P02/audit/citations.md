# Fresh citation and bibliography audit

Release job: `win-00075-p02-release-5bd5d68455de`  
Citation attempt: 3  
Launch: `8a0a1c2f-60d7-4dcf-8390-65008a43f368`  
Search and verification date (UTC): 2026-09-08

## Result and method

**Accept.** I used the requested two-pass citation-check workflow.  Pass 1
read the complete canonical manuscript and froze eight substantive
claim/citation pairs in `audit/citation-claim-ledger.json`, before verifying
their sources.  Its five-key union is exactly the ordinary body-flow citation
set extracted from `manuscript/main.tex`.  Pass 2 retained that extraction and
verified every frozen claim in sequence against its recorded primary-source
locator and exact support statement.  The canonical manuscript and bibliography
match the accepted live snapshot, and no source edit was needed in this run.
The user prohibited sub-agents, so the per-key bibliography audit was performed
sequentially in this release context.

This release audit ran fresh title/author/year, exact-title, venue, DOI, and
arXiv-ID searches as applicable and inspected the primary landing pages or full
texts.  The structured verification evidence, including exact locators, is
preserved in `audit/citation-source-verification.json`.

## Frozen claims and source support

| Claim | Key | Primary record and exact locator | Decision |
|---|---|---|---|
| C01 | `Filippov1985` | [MathNet primary record](https://www.mathnet.ru/eng/smj7078), English translation metadata pp. 879--891 and DOI 10.1007/BF00969110; the historical attribution and definition are independently explicit in Zhang's primary introductions. | Verified (paraphrase) |
| C02, C08 | `Zhang2022` | [Publisher record](https://doi.org/10.1080/00927872.2021.1984493) and [arXiv 1401.4656](https://arxiv.org/abs/1401.4656), abstracts: extending structures/unified products for 3-Lie algebras and their classification using deformation-map theory. | Verified (exact) |
| C03 | `Zhang2026` | [arXiv 2609.05051v1](https://arxiv.org/abs/2609.05051v1), abstract and Sections 1, 7, 8. | Verified (exact) |
| C04 | `Zhang2026` | [Primary HTML](https://arxiv.org/html/2609.05051v1), Example 8.7, equations (8.31)--(8.35), and Corollary 8.8. | Verified (exact) |
| C05 | `Zhang2026` | Same primary HTML, Definition 7.1, equations (7.1)--(7.3), specialized using Example 8.7 equations (8.31)--(8.32).  Hypotheses and all surviving signs agree with equation (DM). | Verified (exact) |
| C06 | `MeurerEtAl2017` | [PeerJ Computer Science 3:e103](https://doi.org/10.7717/peerj-cs.103), bibliographic header and abstract identify SymPy as an open-source Python computer-algebra system.  The actual exact run is separately recorded in the accepted project evidence. | Verified (exact) |
| C07 | `ZengLiuRatnavelu2026` | [DOI record](https://doi.org/10.20944/preprints202608.1067.v1) and [arXiv 2608.15558v1](https://arxiv.org/html/2608.15558v1), proof of Theorem 1.1, the seven displayed positive rational differences in equations (11)--(18), Remark 2.1, and final certificate statement.  These passages say the decimals play no role and require no numerical linear algebra. | Verified (paraphrase) |

No claim was misleading, numerically inconsistent, contradicted, or left
unverified.  The manuscript makes no novelty or priority assertion about the
uninspected ternary matrix specialization; the citations therefore do not
overstate the verified literature boundary.

## Bibliographic records and coverage

All five entries in `manuscript/references.bib` agree in author, title, year,
venue/version, pages or article number, and DOI/arXiv identifier with the
primary records above.  No replacement or key change was required.  The active
49-record user library was read through its checksum-bound registry.  Row 2 is
the one natural library selection; its exact body citation, literal nearby
context, primary support, and issued attempt identity are bound in
`audit/user-bibliography-selection.json`.

The bibliography is not library-only: four natural non-library sources occur
in ordinary body flow.  They cover the foundational n-Lie definition, the
ternary predecessor, the exact problem source and closest framework, and the
symbolic-computation method.  Each is used by a nearby claim.  No decorative
reference, omitted natural primary dependency, or unsupported strengthening
was found.

## Mechanical consistency

The final bibliography audit extracted five cited keys and five BibTeX entries:
there are no missing, unused, duplicate, stale-AUX, or undefined keys.  BibTeX
converged without database warnings.  The final LaTeX log has no undefined
citations or references.  The only diagnostics are two harmless underfull
boxes in the long bibliography entry; rendered inspection confirms no clipping
or overlap.

Bibliography entries verified: **5**.  Frozen claims verified: **8**.  BibTeX
replacements: **0**.  Citation-key changes: **none**.  Official-verification
blockers: **none**.
