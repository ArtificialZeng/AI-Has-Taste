# Citation and bibliography audit

Release job: `win-00054-p05-release-c2293515b74f`  
Verification date (UTC): 2026-09-06  
Mode: primary-source web verification  
Pass-1 input: `audit/citation-claim-ledger.md`

## Method

The four claim/citation pairs were frozen before verification. In this second
pass, each pair was checked without re-extraction. For every cited work, the
title/author/year query, full-title query, author/venue query, and DOI or arXiv
identifier query were run. Only the primary arXiv record, journal-publisher
record, and preprint-publisher manuscript were used as verification evidence.
The job expressly prohibited subagents, so the required per-citation checks
were performed serially in this release context.

## Frozen-claim verification

| ID | Status | Confidence | Primary source and exact location | Support |
|---|---|---|---|---|
| C01 | Verified | exact | arXiv `2609.03411v1`, abstract (official record lines 16--17) and HTML Introduction (line 30) | The source gives the same proper-total-coloring, local-color-set, adjacent-pair inequality, and minimum-palette convention used in the manuscript. |
| C02 | Verified | paraphrase | AIMS publisher page for DOI `10.3934/naco.2014.4.49`, bibliographic header and abstract (official page lines 58--86) | The record identifies Tian--Chen--Shao--Wang and studies the two AVD parameters for Cartesian graph products. |
| C03 | Verified | paraphrase | AIMS publisher abstract, line 86 | The abstract explicitly says exact values are determined for listed Cartesian-product classes, including products of regular graphs. The manuscript correctly avoids inferring an unquoted theorem or novelty conclusion from this abstract. |
| C04 | Verified | paraphrase | Preprints.org manuscript `202608.1658`, abstract (official page lines 62--65), exact clique certificate (lines 187--195), and Section 6 (lines 207--218) | The source documents exact distance-layer colorings, exhaustive finite enumeration, exact maximum-clique computations, released certificates, and standard-library verification. This supports only the stated methodological comparison. |

No numerical discrepancy, contradiction, omitted hypothesis, misleading
strengthening, or unsupported cited claim was found.

## Bibliographic record audit

| Key | Current and official record | Authority | Action | Uncertainty |
|---|---|---|---|---|
| `BanerjeeGeethaSomasundaram2026` | Title, all three authors, year, arXiv ID, subject, version, and arXiv-issued DOI agree. | <https://arxiv.org/abs/2609.03411> | BibTeX retained; key retained. | None affecting the cited claim. |
| `TianChenShaoWang2014` | Title, four authors, journal, volume 4, issue 1, pages 49--58, and DOI agree with the publisher. The site records online publication in December 2013; the cited issue year is 2014. | <https://www.aimsciences.org/article/doi/10.3934/naco.2014.4.49> | BibTeX retained; key retained. | Full theorem text was not needed or invoked. |
| `ZengEtAl2026Certificates` | Title, four authors, August 2026 posting, venue/status, and DOI agree with the publisher manuscript. | <https://www.preprints.org/manuscript/202608.1658> | BibTeX retained; key retained. | Version 1 is a non-peer-reviewed preprint, and the manuscript uses it only as a method example. |

All three cited keys exist exactly once in `manuscript/references.bib`, all are
used in ordinary body-flow citations, and the converged `.aux` contains the
same three keys. No key replacement was needed.

## Coverage and necessity

The bibliography covers the recent primary formulation that supplied the
problem context, the closest identified primary Cartesian-product result, and
the only external methodological comparison. The proof of the lower bound and
the nine-vertex coloring certificate are self-contained and do not rely on an
uncited theorem or solver technique. The Tian citation is necessary to avoid
an unsupported prior-work description; the Banerjee--Geetha--Somasundaram
citation anchors the parameter convention and current graph-product context;
the Zeng et al. citation supports the explicit exact-certificate comparison.
None is decorative.

The active 49-record user library was checked. Row 9 is genuinely relevant to
the exact finite certification claim and is directly cited as
`ZengEtAl2026Certificates`. No second library item supports another natural
claim in this short paper closely enough to avoid padding, so exactly one was
selected. The bibliography is not library-only: its other two entries are the
primary problem-context and closest-prior-result sources.

## Mechanical citation checks

`check_bib_keys.py` found three cited keys, three BibTeX entries, no missing or
unused key, and exact agreement with `main.aux`. The final LaTeX/BibTeX logs
contain no undefined citation, missing database entry, repeated entry, or
BibTeX warning.

Verdict: **accept**.
