# Checkpoint

Provenance: `bigMac-00011-p02-release-8e7a7826a299` (release phase,
2026-09-07).

## Release status

Fresh release audit is ready.  `release_gate.py check` passes for the accepted
`resolution-paper` with evidence snapshot
`05b0d264c597be99e9081bf9accf3db7b34c6ea6f8cf3c597332fbb9be9d8b71`,
manuscript digest
`5f91c30536387a229ce1b3a6f402ce926aced88a3f8fcbf74311b440ba18b036`,
and PDF digest
`f1561ebd6cb8af5486dd854ca5544d1f49567b0214ba6d35f9a5509f06e9a8d6`.
The six-page PDF preserves the exact accepted 32-case classification.

## Fresh evidence

- A clean `latexmk -C` then `latexmk -pdf` build completed; the final bound
  `manuscript/main.log` has SHA-256
  `7dfd5cacae8007aa0de5eba1d26ded6e46e197e3979413c65d5b246d2ecefedb`
  and no unresolved citation/reference, layout, or fatal diagnostic.
- Citation-check pass 1 fixed 18 claims in `audit/citation_claims.md`.  Pass 2
  verified all claims against the official arXiv/Dagstuhl records, accepted
  math audit, and fresh exact regression output.  Both authored dependencies
  were checked and all three bibliography keys resolve.
- The exact verifier again returned 6,400 height-formula pairs and 25,600
  suffix-probe pairs using integer sorting only.
- Pages 1 through 6 were rendered at 150 dpi and inspected individually.  No
  clipping, overlap, unreadable formula/table/reference, missing glyph, or
  visible unresolved marker was found; all fonts are embedded.
- `source.md` remains byte-identical at SHA-256
  `b7828252e7882bc261940004f89d319fcf4d7f3f2e6655b0674f6e3def45c0d5`.

## Limitation

The sole paper in `literature/user_bibliography_check.md` concerns Rule 115
cellular-automaton periods and explicitly does not support polyregularity or
an additive-level-sort obstruction.  It was inspected but not inserted as a
misleading citation.  Its optional SSRN/DOI page was inaccessible through the
bounded web endpoint; this does not affect any cited record.

## One next test

After the supervisor runs `release_gate.py publish`, verify that
`release/manifest.json` exists and that `release/main.pdf` has the audited PDF
digest above.
