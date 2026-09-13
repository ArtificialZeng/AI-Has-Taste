# Checkpoint

Job: `bigMac-00024-p01-release-c1ef70f8d6b1` (release phase).

## Current claim and decisive evidence

- The exact `n=18` resolution remains bound to accepted evidence snapshot
  `d0ca5ba0df04480ff06cbbca2b1700e66cf8802807299148fe8ab62fa9a77803`.
  The immutable `source.md` SHA-256 remains
  `3533a6e6b08b7f3161d134b1f78e35e56f85646369de027ff6d9e36e038f10c0`.
- All manuscript inputs still match snapshot
  `4bbf4ac8a77005d903c1e72d17958753350d4f534d8e5284d38783f79c42531e`;
  the five-page PDF SHA-256 remains
  `411261c85eb5ff25765d14dcdfdf65ccfc68a9987620f5e6dd7aff59b0679e0f`.
- The advisory two-pass citation check and manual source audit verified the
  convergence definition, Theorem D range, even-parameter question, `n=18`
  table, and standard Fatou-component facts in the supplied primary PDF.  All
  five bibliography records and their narrowly stated uses are supported.
  The two selected workbook papers remain methodological citations only;
  `metadata_basis=user_designated_workbook` controls their metadata.
- `manuscript/main.log` is a clean successful five-page build with SHA-256
  `3268adf87473c8de382727804e60d5bf1310e8b31dace4c9cad861b13d564587`.
  All keys and cross-references resolve, all fonts are embedded, and the exact
  certificate reruns successfully under the required research interpreter.
- Fresh 150-dpi renders `audit/rendered/page-1.png` through `page-5.png` were
  each inspected at original resolution.  No clipping, overlap, missing glyph,
  malformed equation/reference, or legibility defect was found.
- Fresh digest-bound reports and JSON records are in `audit/citations.*`,
  `audit/build.*`, and `audit/visual.*`.
- `release_gate.py check` passed on the current project, binding the accepted
  evidence, current manuscript/PDF, all three fresh audits, the existing build
  log, and the research/referee/release job provenance.

## Obstacles and limitations

No mathematical, citation, build, dependency, or visual obstacle remains.
The manuscript makes no priority claim beyond comparison with the supplied
preprint and no claim beyond `n=18`.  External refresh is not a replacement
authority for the designated workbook metadata; accessible landing pages were
used only as corroboration.

## One next test

Have the supervisor run `release_gate.py publish` to atomically activate the
already validated PDF and manifest without changing the audited state.
