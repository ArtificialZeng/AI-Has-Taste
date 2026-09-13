# Checkpoint

Provenance: release job `bigMac-00020-p03-release-c9a19d6ffd27`, following
accepted referee job `bigMac-00020-p03-referee-464f57f86a73`.

## Current claim

- Accepted `resolution-paper`: in the frozen Jones--Kinnersley
  partial-feedback directional localization game,
  `zeta_d(Q_3)=3`; the explicit three-cop strategy localizes within two
  probing rounds.
- Original status is `proved`. No result for `Q_n`, `n>3`, and no exhaustive
  priority claim is asserted.

## Fresh release evidence

- The accepted evidence snapshot remains
  `ba716a810c205d214da52cc5b993cc6650f9d7be715542223f01b7730d054ed1`.
- `source.md` remains immutable with SHA-256
  `a5f6ee89bf21df93a868c15c50725b26f03e8d259a210c27788063657b7da7a5`.
- A clean-from-generated-files LaTeX/BibTeX build produced the current
  three-page `manuscript/main.pdf`, SHA-256
  `26b9137506abf8974f01d8805d27f89cd4d89d54d67312fbb31aabe629b8257c`.
  The authored manuscript digest is
  `bd015dc13f52987325070cf4e693b435b741af53cfb4ca39b5833614c783acac`.
- `audit/build.{md,json}` binds the current nonempty
  `manuscript/main.log`, SHA-256
  `f5adace40bf4471053d4baa26a83761778bf1f5bddc162717badfdf2fd0a6846`.
  The final log has no fatal errors, unresolved citations/references, LaTeX
  warnings, rerun requests, or box warnings. PDF metadata, text extraction,
  and embedded fonts pass.
- `audit/citations.{md,json}` records a fresh two-pass
  `$citation-check-skill` audit. The user-designated hash-matching arXiv v1
  paper and the official arXiv record verify the sole bibliography entry and
  its limited use for the game context, Corollary 3.9, and Question 6.1. The
  immutable source's page-14 locator is one page early, but the manuscript
  cites the correct theorem label. No citation remains unverified.
- `audit/visual.{md,json}` records actual inspection of rendered pages
  `[1, 2, 3]` at 180 dpi. No clipping, overlap, illegibility, malformed table,
  broken glyph, or unresolved marker was found.
- All fresh audit JSON records use job ID
  `bigMac-00020-p03-release-c9a19d6ffd27`, current digests, exact sorted
  `publication.json` sources, the current build-log digest, and the exact page
  list.
- `release_gate.py check` passed for the current artifact and provenance.

## Obstacles and limitations

No mathematical, citation, build, visual, provenance, or tool obstacle remains.
The literature search is bounded and is not a priority guarantee, consistently
with the manuscript's express limitation.

## One next test

The supervisor should run `release_gate.py publish` and verify that
`release/manifest.json` and `release/main.pdf` bind PDF digest
`26b9137506abf8974f01d8805d27f89cd4d89d54d67312fbb31aabe629b8257c`.
