# Final status: CERTIFIED_FINITE_RESULT

## Conclusion

Let \(C_0\) be the 333-plane code reconstructed from Appendix C of Heinlein,
Kiermaier, Kurz, and Wassermann.  Among **all** codes obtained by deleting at
most seven planes of \(C_0\) and adding arbitrary mutually compatible
subspaces of any dimension in \(\mathbb F_2^7\), the exact maximum is

\[
\boxed{334}.
\]

The maximum is attained by deleting nothing and adding the full seven-space.
No 335-word code exists in this complete radius-seven exchange neighborhood.

This does **not** prove \(A_2(7,4)=334\).  A distant 335-word code is not
excluded, and the published SDP upper bound 388 was cited rather than
independently exactified.  At the 2026-08-30 search cutoff the global problem
therefore remains

\[
334\le A_2(7,4)\le388.
\]

## Exact certificate

- Appendix C data: `data/appendix_c_333.json`
- Explicit 334-word baseline certificate:
  `certificates/published_334_code.json`
- Radius-seven discovery transcript:
  `experiments/radius7_search_diagnostic.json`
- Independent acceptance record:
  `certificates/radius7_verification.json`
- Independent verifier: `verification/verify_radius6.py`

The accepted search has 2,561,563 normalized removal unions; every eligible
compatibility graph has at most 15 vertices.  Discovery uses membership masks
and coloring branch-and-bound.  Verification imports no discovery module and
instead uses rank-based distances, an alternative union closure, and complete
subset enumeration.  The verifier SHA-256 is
`9186cbfcfeaa06a84c4464c99f321586b961674c2fe8f82e5b0d00ab00ac8393`.

## Independent audit

Five corrupt inputs are rejected fail closed: a duplicate codeword, an unknown
schema field, a singular group generator, malformed JSON, and a forged 335
optimum.  Builder, Breaker, Certifier, and Referee records are in
`audit/roles/`.  The proof audit is `audit/PROOF_AUDIT.md`, the citation audit
is `audit/CITATION_AUDIT.md`, and the five-page visual inspection is
`audit/PDF_AUDIT.md`.

The post-result novelty pass found no prior public closure of radius six or
seven within the explicitly logged databases and queries.  This is bounded
novelty wording, not a claim that an unindexed or private computation cannot
exist.

## Reproduction

From the project root:

```bash
python3 scripts/replay_appendix_c.py
python3 verification/verify_radius6.py \
  --radius 7 \
  --result experiments/radius7_search_diagnostic.json
python3 tests/test_fail_closed.py --full
python3 /Users/mac/.codex/skills/bib-reference-audit/scripts/check_bib_keys.py \
  paper/main.tex --aux paper/main.aux
(cd paper && latexmk -C main.tex && \
  latexmk -pdf -interaction=nonstopmode -halt-on-error main.tex)
python3 /Users/mac/.codex/skills/prove-or-disprove-math/scripts/verify_manifest.py \
  release release/MANIFEST.json
```

To rerun discovery itself, which is slower:

```bash
python3 scripts/search_radius6.py \
  --radius 7 \
  --output experiments/radius7_replay.json
python3 verification/verify_radius6.py \
  --radius 7 \
  --result experiments/radius7_replay.json
```

## Publication artifacts and authorship

The retained paper is `paper/main.pdf`, mirrored as `release/main.pdf`; its
source and exact finite certificates are in
`release/radius7_exchange_source.zip`.  PDF metadata, PDF body, and LaTeX name
Zijian Zeng as the sole author and contain the required UCSI University
affiliation and both specified email addresses.  No proof assistant was used.
