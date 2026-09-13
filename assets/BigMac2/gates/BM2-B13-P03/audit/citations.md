# Fresh citation audit

## Binding and method

- Release job: `bigMac-00013-p03-release-4189b067aff7`.
- Evidence snapshot: `393c635435e81b9dc70256f6851164d5d45067c12ff2d04143ac46090b6303c6`.
- Manuscript snapshot: `8487aa4f23241b4179277a1ce3bdde7e416eebd1cfe23df81005e94282a62ca3`.
- PDF: `manuscript/main.pdf`, SHA-256
  `0bef46e936a25d8d0af1f3ea63a3cf60c8b5c982e46281d50a845a7ea5f88909`.
- Search date: 2026-09-07.
- Method: the requested `citation-check-skill`, search mode, with extraction and
  verification performed as separate passes. The final TeX, BibTeX database,
  compiled bibliography, and extracted PDF references were all checked.

## Pass 1: fixed claim extraction

The following citation-dependent claims were fixed before source verification.

| ID | Claim | Type | Location |
|---|---|---|---|
| C01 | The Gwóźdź preprint exists with the cited author, title, arXiv identifier, version, and date. | Existence/attribution | bibliography [1] |
| C02 | Its Remark 5.7 treats this exact tilted-Gaussian family and monotone map. | Attribution | section 1, paragraph 3 |
| C03 | Remark 5.7 computes \(T_L'(0)=Z_L\). | Attribution | section 1, paragraph 3 |
| C04 | Remark 5.7 uses that value as a lower bound for \(\operatorname{Lip}(T_L)\), without asserting the paper's exact global equality. | Attribution/comparative | section 1, paragraph 3 |
| C05 | The Zeng preprint exists with the cited author, title, version, posting date, and DOI. | Existence/attribution | bibliography [2] |
| C06 | Zeng distinguishes a sharp constant on a restricted model class from the unrestricted ambient constant; it supplies no optimal-transport result. | Attribution/comparative | section 1, paragraph 3 |

No chart, table, quoted passage, or external numerical statistic occurs in the
manuscript. The theorem and asymptotic are proved in the manuscript and are
bound to the accepted mathematical audit rather than outsourced to a citation.

## Pass 2: source verification

| ID | Status | Primary-source finding | Confidence |
|---|---|---|---|
| C01 | Verified | The official arXiv record gives Maja Gwóźdź, the cited title, arXiv:2609.04052v1, and 3 September 2026. | exact |
| C02 | Verified | The official v1 HTML/PDF, Remark 5.7, defines \(B^{(L)}(t)=-L|t|\), \(Z_L\), \(\nu_L\), and the monotone map \(T_L\) exactly as described. | exact |
| C03 | Verified | Remark 5.7 explicitly derives \(T_L'(0)=Z_L\). | exact |
| C04 | Verified | Remark 5.7 concludes \(\operatorname{Lip}(T_L)\geq T_L'(0)\geq e^{L^2/2}\); the introduction describes this only as the obstruction establishing quadratic order. No exact-equality assertion was found. | paraphrase |
| C05 | Verified | The official Preprints.org version-1 record gives Zijian Zeng, the exact title, submission on 18 August 2026, posting on 19 August 2026, and the record identified by DOI `10.20944/preprints202608.1272.v1`. | exact |
| C06 | Verified | The abstract and section 1 compute an exact constant only for a specified square-zero subclass while saying the unrestricted fixed-lens value remains open. The full primary text contains no optimal-transport claim. | paraphrase |

Primary sources consulted:

1. Maja Gwóźdź, official arXiv abstract and v1 full text:
   <https://arxiv.org/abs/2609.04052> and
   <https://arxiv.org/html/2609.04052v1>.
2. Zijian Zeng, official Preprints.org version-1 record and full text:
   <https://www.preprints.org/manuscript/202608.1272>.
3. The DOI query for `10.20944/preprints202608.1272.v1` returned the same
   official Preprints.org record. Direct DOI-resolver and Crossref-API opens
   returned no usable body through the audit interface, so that optional route
   was not pursued further; the authoritative publisher record supplied the
   metadata and complete text, leaving no citation unverified.

The nearby wording is conservative. The Zeng citation is genuinely relevant
only to the stated model-versus-ambient methodological distinction, exactly as
authorized in `literature/user_bibliography_check.md`; the manuscript expressly
disclaims optimal-transport support from it. The Gwóźdź comparison makes no
priority claim beyond the cited source.

## Dependency and resolution checks

`publication.json` lists exactly `manuscript/main.tex` and
`manuscript/references.bib`. Inspection of `main.fls`, the BibTeX run, and all
TeX imports found no other authored input. Both citation keys appear in the
auxiliary file and resolve to bibliography entries [1] and [2]. The compiled
PDF displays both entries with legible author names, titles, dates, identifiers,
and links. There are no undefined citations, contradicted attributions,
unsupported novelty claims, or removable references.

## Verdict

**Accept.** All cited records and all six extracted citation-dependent claims
were verified against primary sources. The publication dependency scope is
complete and there are no undefined citations.
