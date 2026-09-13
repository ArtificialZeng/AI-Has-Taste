# BigMac2 local packaging review — 2026-09-13

This is a local review copy. No GitHub push, upload, submission or new mathematical research was performed. The research queue remained paused.

| Item | Result |
|---|---:|
| Current gate-passed source manuscripts inspected | 60 |
| Same-result manuscripts consolidated into existing Smallmac entries | 5 |
| Newly copied final BigMac2 PDFs | 55 |
| New PDF pages | 233 |
| Repository PDF total after this addition | 230 / 1,250 pages |
| Paired local manuscript-source packages | 55 |
| Paired scientific source/evidence packages | 55 |
| Clean temporary LaTeX builds | 55 passed |
| Materialization and original-digest checks | 55 passed |
| Selected bounded computational replays | 36 passed |
| Packages without a selected replay | 19, reasons recorded individually |

The PDFs are exact copies of the accepted historical release versions. Rebuilt PDFs were checked in disposable directories and did not replace the originals. Matching page counts and successful builds are not a new visual, mathematical or novelty audit. Partial and finite results retain their stated scope; manuscript counts are not counts of fully solved parent problems.

The five omitted same-result manuscripts remain traceable through the [duplicate mapping](dedup-review.json) and the original [gate records](gates/). No existing canonical PDF was deleted. Six of the new packages have no standalone program; their proof dossiers are labeled honestly rather than presented as executable verification.

## Local sources versus Git distribution

The existing repository ignore policy excludes manuscript LaTeX. All 55 complete manuscript-source packages are present locally, and all 55 builds were tested there. That does not promise manuscript rebuilds from the Git distribution. The 671 selected scientific source/data inputs are not excluded by the existing ignore policy, so the reproduction-package materialization inputs remain available.

- [Full local copied-source manifest](package-manifest.json): includes 149 manuscript build inputs excluded by the existing Git policy.
- [Git-distribution copied-source manifest](git-distribution-manifest.json): the corresponding non-ignored subset, not a mathematical proof checker.
- [Git-policy check](git-policy-check.json): counts and precise scope of the exclusions.
- Large scientific data are losslessly gzip-compressed. Materialization verifies both stored and original hashes.
- Machine-specific executables, environments, downloaded third-party papers and worker transcripts are not redistributed. Some original scientific wrappers retain historical host assumptions; those limitations are documented, not silently bypassed.

Concurrent BigMac1 documentation and Git-distribution metadata edits were preserved. The new material does not replace the existing BigMac1 or Smallmac source collections. The final English and Chinese catalogs identify local-only LaTeX availability in accordance with the existing upload policy.

## Navigation and check scope

- [English catalog](../../README.md#bigmac2) / [中文目录](../../README.zh-CN.md#bigmac2)
- [Complete local directory layout](../../DIRECTORY_STRUCTURE.md)
- [Machine-readable catalog](catalog.json)
- [Clean build results](build-checks.json)
- [Materialization and selected replay results](reproduction-checks.json)
- [Final local packaging validation](packaging-validation.json): zero errors; preserves concurrent metadata and explicitly distinguishes local completeness from the LaTeX-excluding Git policy.
- [Replay instructions and limitations](../../reproducible_source_code/BigMac2/REPRODUCTION_NOTES.md)

This review describes packaging and reproducibility checks, not external peer review or a guarantee of publication acceptance. Full historical searches were not rerun merely to package the archive. Please review the local directory and its existing upload policy before publication.
