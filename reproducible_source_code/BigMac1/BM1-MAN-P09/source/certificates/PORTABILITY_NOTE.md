# Portability repair for the v18 candidate

## What was excluded

The first v18 candidate ZIP failed the first independent portability audit:
277 historical generated files below `certificate_workspace/` contained a
literal builder-home path.  The repaired candidate applies one mechanical
exclusion rule:

```text
exclude a file iff
  (1) it is below certificate_workspace/,
  (2) its suffix is .log or .txt, and
  (3) its bytes contain the literal builder-home path detected by the audit.
```

Exactly 277 files satisfy that rule.  They are old execution transcripts,
attack logs, or generated diagnostic outputs.  They were omitted rather than
rewritten: no retained evidence byte has had a path string redacted or
substituted.  No `.py`, `.md`, `.sha256`, `.json`, `.tex`, `.bib`, or PDF is
excluded by this rule.

The failed predecessor ZIP has SHA-256
`0e549206bb0d2a809fe650fe818d0023868f407322d7c50da10dcf2b7a91763e`.
That hash is recorded only to identify the audit-failed archive; it is not a
passing portability result.

## What remains frozen

The 32 principal post-v17 files in `xy_box_post_v17/` remain present and
byte-identical.  They comprise, for each of the four rational cells, the
source script, source note, source normal result, source manifest,
independent-referee script, referee result, referee report, and referee
manifest.  `xy_box_post_v17/INDEX.md` gives their exact relative paths and
SHA-256 values.

The package also retains the native source/referee code dependencies, notes,
reports, normal result summaries, and original historical manifests under
`certificate_workspace/`.  Some original manifests name an omitted generated
transcript.  Such a manifest is retained as provenance but is not advertised
as a complete portable `shasum -c` replay; a missing transcript is expected
and is not silently replaced.

## Fresh mathematical replay

Reconstruct the environment described by
`certificate_workspace/requirements-portable.txt`.  Then change to
`certificate_workspace/` and run, serially:

```sh
python3 -B -u tmp/research/compact_ball_uncovered_box_x5_8_xy_adjacent_x627_1000_exact_gate.py
python3 -B -u tmp/research/audit/verify_compact_ball_uncovered_box_x5_8_xy_adjacent_x627_1000_independent_referee.py
python3 -B -u tmp/research/compact_ball_uncovered_box_x5_8_xy_adjacent_x63_100_exact_gate.py
python3 -B -u tmp/research/audit/verify_compact_ball_uncovered_box_x5_8_xy_adjacent_x63_100_independent_referee.py
python3 -B -u tmp/research/compact_ball_uncovered_box_x5_8_xy_adjacent_x16_25_exact_gate.py
python3 -B -u tmp/research/audit/verify_compact_ball_uncovered_box_x5_8_xy_adjacent_x16_25_independent_referee.py
python3 -B -u tmp/research/compact_ball_uncovered_box_x5_8_xy_adjacent_x7_10_exact_gate.py
python3 -B -u tmp/research/audit/verify_compact_ball_uncovered_box_x5_8_xy_adjacent_x7_10_independent_referee.py
```

The source programs rebuild the fully conjugated Hermitian `Q,Q^2` gate and
all 531 exact Bernstein controls per cell.  The independent referees use a
separate literal-free reconstruction and do not import a source coefficient
table.  Redirect fresh output outside the package when preserving release
bytes.

These commands replay the four mathematical normal gates and four independent
normal referees for the post-v17 stitched theorem.  They do not promise to
recreate every historical attack transcript, filesystem timestamp, or shell
diagnostic from earlier project versions.

## Parallel manifest-chain repair

A later independent audit correctly found two further defects: the eight
historical post-v17 manifests were not self-contained after transcript
omission, and retained generated files still contained absolute temporary-
directory paths.  The historical manifests therefore remain immutable
provenance anchors only.

The package now provides `xy_box_post_v17_portable/`, a parallel chain made
from fresh relative-path runs of the unchanged mathematical source/referee
programs.  It contains complete source and referee portable manifests,
fail-closed verifier attacks, and a 16-record cell manifest for each cell.
Its `README.md` lists every frozen hash and replay command.

The second repair omits 15 generated or old-audit files containing 16
absolute temporary-path occurrences.  Fourteen non-audit payload files
account for the 15 occurrences reported by the independent audit; the audit-
result transcript itself supplied the additional file and occurrence in the
builder's full-tree scan.  None is a theorem source, coefficient table,
bibliography input, or principal post-v17 certificate.  No old byte was
rewritten.
