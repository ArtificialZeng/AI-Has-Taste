# Submission audit

Status: pass for a concise restricted-class research note.

Audit date: 2026-08-28.

## Scientific endpoint

- The claimed exact result is only for finite linearly ordered split graphs:
  the ordered edge has small Ramsey degree exactly three.
- The upper bound treats arbitrary target and color count, explicitly forgets
  the chosen split marks, and does not assume an expansion property.
- The lower bound uses a fixed ordered four-vertex path and has the correct
  host/coloring quantifier order.
- The full ordered chordal problem is not claimed solved.  The paper records
  only the lower bound two and exact free-amalgamation/PEO-amalgamation
  obstructions.

## Proof and novelty gates

- Builder, adversarial breaker, exact certifier, and definition-level referee
  passes are recorded separately under `proof/`.
- The external ordered relational Ramsey theorem was checked against every
  hypothesis in the encoded marked class.
- The finite witness certificate passes an independent verifier that reads the
  serialized instance and recomputes all split partitions.
- Exact-title, exact-phrase, broader web, arXiv, and Crossref searches located
  no prior explicit computation of the ordered split-graph value.  The paper
  states this only as bounded search evidence and makes no global priority
  claim.

## Manuscript gates

- Author name, institutional address, and both supplied email addresses match
  the requested attribution.
- All five cited records exist, their metadata and supporting statements were
  checked, and the LaTeX citation audit reports five cited entries, five
  bibliography entries, no missing keys, and no unused entries.
- The final LaTeX build has no warnings or unresolved references.
- The final five-page PDF passed page-by-page visual inspection and forbidden-
  content scanning.
- The submission ZIP passed archive-integrity testing, was extracted into an
  empty directory, and there passed the manifest, exact-witness, citation, and
  from-source LaTeX build checks.
- Limitations, computer assistance, AI assistance, and absence of proof-
  assistant verification are disclosed accurately.

The manuscript is suitable for author review and journal-specific formatting.
No claim is made that acceptance is guaranteed.
