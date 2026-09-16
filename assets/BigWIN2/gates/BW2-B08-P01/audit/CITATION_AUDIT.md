# Final independent citation audit

Audit date: 2026-08-31  
Audited files: `paper/main.tex`, `paper/references.bib`

## Verdict: **PASS**

All cited mathematical and enumeration claims now have appropriate sources. No cited theorem is misquoted or used outside its hypotheses.

## Findings

- **`Holleben_2026`: PASS.** The official DOI-exported BibTeX metadata and DOI 10.1016/j.jpaa.2026.108238 were verified against the publisher record and the authors' arXiv version. The cited Corollary 3.12, Theorem 3.10, Conjecture 3.15, and Remark 3.16 support each use and all hypotheses match.
- **`McKay_2014`: PASS.** The official DOI-exported BibTeX metadata and DOI 10.1016/j.jsc.2013.09.003 were verified. The article supports nauty's canonical-labelling and mass-generation context; the exact command semantics and census count are separately sourced below.
- **`NautyGuide`: PASS after correction.** The prior `nug.pdf` URL was the older, McKay-only version 2.4 guide and did not match the entry. It has been replaced by the official `nug27.pdf`, the McKay--Piperno version 2.7 guide distributed byte-identically with nauty 2.7r3; its `geng` help supports the command and graph6 output description.
- **`McKayData`: PASS.** The official Brendan McKay ANU graph-data page is cited at lines 122--124 and directly lists 12,346 unlabelled simple graphs on eight vertices.
- **Lines 128--149:** the independence-number distribution and kernel certificates are new certified results, not borrowed assertions, so they do not require literature citations. Their provenance is the named supplementary archive and independently checked project artifacts.
- **Lines 171--172:** the certificate, verifier, and supporting data are identified as the supplementary archive distributed with the article. This is sufficient at manuscript stage provided the archive is actually attached to the submission.

The official DOI-exported blocks were inserted verbatim for the two journal articles. Both prior citation blockers and the subsequently discovered guide-version mismatch are resolved. There are no undefined citation keys in the current source, and all four bibliography entries are cited.

The separate manuscript-policy failure concerning lines 151--157 is recorded in `audit/PROOF_AUDIT.md`; it is not a citation defect.
