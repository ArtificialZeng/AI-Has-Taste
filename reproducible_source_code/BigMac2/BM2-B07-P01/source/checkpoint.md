# Checkpoint

Job provenance: `bigMac-00007-p01-research-b0cf55c4c707` (research pass 1,
2026-09-08).

## Candidate claim

`claim.json` proposes a `resolution-paper` with `original_status=proved`.
For every integer `c>5`, `c!=7`, the full wall-convention nim sequence of
`{2,5,c}` is purely periodic exactly when

`c mod 7 in {1,2,3,5,6}`.

The least periods are `c+2` for residue 1, `7` for residues 2 and 5, and
`c+5` for residues 3 and 6.  This is full nim-value periodicity, not only
outcome periodicity.

## Decisive evidence

- The local primary PDF `literature/2609.05358v1.pdf` was inspected.
  Lemma 14, Theorems 28 and 57 specialize the source predicates to
  `Theta_7={2,5}`, `Theta_{c+2}={1,5}`, and
  `Theta_{c+5}={2,3,6}`.  Theorem 32 and Proposition 46 prove the positive
  cases and their least periods, with no divisor exception for this
  primitive non-harmonic shape.
- `evidence/fixed_shape_proof.md` proves exact full-nim words in both
  non-admissible families.  With the finite blocks defined there,
  `c=7k+4` gives `B^k E (A C^(k-1) D)^omega`, whose tail starts at `c+3`,
  and `c=7k` (`k>=2`) gives `B^k F (H^(k-1) I J)^omega`, whose tail starts
  at `c+8`.  Both tails have period `p=c+2`, while respectively
  `G(c+2)=3` and `G(c+2)=2`, versus `G(0)=0`.
- The all-parameter step is a finite word/signature proof: after the tail
  begins, `-c == 2 mod (c+2)`; the transition words reduce to aligned
  length-7 blocks.  The only mex signatures are the 20/25 exact tuples
  serialized in `evidence/fixed_shape_certificate.py`, all of which satisfy
  the recurrence.  If a sequence were pure with any period while eventually
  having period `p`, then `p` would already be a period from zero, contradicting
  the displayed mismatch.
- The certificate script independently agreed with direct exact mex
  recurrence for 1,999 instances through `k=1000`.  This is sanity evidence;
  the universal claim rests on the block/signature argument.
- `evidence/literature_screen.md` records a focused search.  An anonymous
  2009 note states the same preperiod classification without proof and has
  an apparent typo in two positive-case periods.  The contribution is
  described conservatively as a complete proof/certificate, not priority for
  first stating the classification.

The immutable `source.md` still has SHA-256
`853c88405c8f85aa43a3734cbe5b6f712db56a31f58467cd1b257593ec0207fb`.

## Obstacles / audit focus

The mathematical referee accepted the exact frozen scope in `audit/math.md`.
The remaining limitation is bibliographic: the 2009 note has no identified
author or proof, and `literature/user_bibliography_check.md` is absent.  The
manuscript therefore makes no priority claim and records bibliography metadata
only from the local Manabe PDF and the frozen literature screen.

## One next test

Run the separate release-phase citation, clean-build, and rendered-page audit
against the frozen manuscript; release only if those checks pass.

## Writing pass (2026-09-08)

The mathematical gate accepted snapshot
`9321a384fea2f8a429ec15c60513abbd0d01bcac9930a376dfb34109fc0ae600`.
The manuscript preserves the accepted resolution scope, gives both
all-parameter block words and the period-transfer argument, and cites the
local Manabe v1 primary source plus Zhang's relevant 2024 paper.  A clean
`latexmk` build produced the four-page `manuscript/main.pdf` (SHA-256
`cd8a6637dfa33792b5621517e74dc132e646d8cef53ada25973fb31de7aba5a2`)
with no LaTeX/BibTeX warnings, undefined references, or overfull boxes; all
four rendered pages were inspected and are legible.  DOI/arXiv/URL metadata
is visible in the bibliography.  The exact certificate was rerun through
`k=1000` and again passed all 1,999 instances with the 20/25 signature counts.
The absent `literature/user_bibliography_check.md` remains a disclosed
citation-audit limitation, not a mathematical or build blocker.  The immutable
`source.md` hash remains unchanged.  `freeze-manuscript` succeeded with
manuscript digest
`f63cefc8a9ff9fc263b7570e55378cf83499b8e7ac4c39d704c19c2c8744f380`.

## Fresh release pass (2026-09-08)

Current release job: `bigMac-00007-p01-release-73c3ff96116c`.

The advisory `citation-check-skill` was explicitly invoked; its fixed two-pass
review, fresh primary-record searches, and direct source inspection verified
every cited record and nearby attribution.  The Zhang bibliography author is
the DOI publisher form, Shenxing Zhang; the anonymous note's Theorem 6.6 and
discrepant table were verified directly.
`literature/user_bibliography_check.md` is absent, so no workbook metadata was
available to override or add; this was disclosed without treating any cited
record as nonexistent.  PDF title/author/subject/keyword metadata was added.

The current clean `latexmk` build log has no warnings, undefined citations or
references, or box overflow.  All four pages were freshly rendered at 170 dpi,
inspected at original image resolution, and are legible.  Fresh citation,
build, and visual audit records bind the current job to manuscript digest
`a54cf7713f0456e4c89c78ae0be13055078943c8aff22b3dd0889a345004821c` and
PDF digest is
`53197fd923d493f4a3bf1bd7351ffb47945e90ab77357feec09307a31491aaa7`.
The immutable `source.md` SHA-256 remains
`853c88405c8f85aa43a3734cbe5b6f712db56a31f58467cd1b257593ec0207fb`.
The final `release_gate.py check` succeeded for these exact digests with
`kind=resolution-paper`, `original_status=proved`, and `pages=4`.

## One next test

The supervisor may run `release_gate.py publish` and then verify that the active
manifest and `release/main.pdf` retain the validated PDF digest above.
