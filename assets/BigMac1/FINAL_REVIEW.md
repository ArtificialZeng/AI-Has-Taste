# BigMac1 packaging review — 2026-09-13

> **Git distribution update:** Manuscript LaTeX is now local-only and Git-ignored, including copies inside reproduction bundles. Earlier clean-build/syntax/link results describe the complete local snapshot. See the [upload policy](../../UPLOAD_GUIDE.md) and the current Git-upload validation; they are not a claim that Git contains LaTeX.

**Local review copy only. No GitHub publication or new mathematical research was performed.**

| Check | Result |
|---|---|
| Selected BigMac1 final manuscripts | 41 PDFs, 280 pages |
| Full repository after addition | 175 PDFs, 1,017 pages |
| Original 134 PDF files | Byte-for-byte unchanged |
| PDF duplicates | No identical PDF hashes; one final manuscript per retained BigMac1 topic |
| LaTeX clean builds | 41/41 passed; all page counts matched |
| Missing citations / references / dependencies | 0 in the new clean builds |
| Copied source Python syntax | 552 files passed Python 3.12 checks without execution |
| Isolated exact smoke checks | 5/5 passed; not an all-paper proof audit |
| Reported README formula | Rendered successfully in the local MathJax regression check |
| BigMac1 README catalog | 41 rows; PDF, LaTeX and reproduction links present in six editions |
| Third-party manuscript downloads and machine binaries | Excluded from the new source distributions |

## Read the scope correctly

Selection is based on historical submission gates, recorded final versions and matching assets. Some historical audits used independent contexts, while others recorded serial roles. This packaging review does not retroactively claim every historical audit was a fresh-context review. It also does not perform a new citation-content or novelty search. Partial and finite results are identified as such; publication counts do not measure the number of solved parent problems.

The original final PDFs were copied without alteration. Newly compiled QA PDFs stay outside the repository and do not replace the frozen manuscripts. This pass checked builds and page counts, not a fresh page-by-page visual mathematical audit of 280 pages.

## Reports

- [Catalog with scope and paired sources](catalog.json)
- [Historical gate provenance by paper](gates/)
- [Exclusions and merged records](exclusions.json)
- [Topic relationships](topic-relations.json)
- [Clean LaTeX build results](latex-build-review.json)
- [Code and dependency limitations](REPRODUCTION_NOTES.md)
- [Reproduction static review and five smoke tests](reproduction-review.json)
- [README rendering check](readme-render-review.json)
- [File/link/syntax validation](packaging-validation.json)
- [Copied-source manifest](package-manifest.json)
- [Source archive fingerprints](source-provenance.json)
- [Whole review-copy SHA-256 manifest](review-manifest.sha256)
- [Full relative-path file list](file-tree.txt)

To verify the whole review copy, run this from the repository root:

```sh
shasum -a 256 -c assets/BigMac1/review-manifest.sha256
```

Do not confuse this package-integrity command with any mathematical verifier. The three especially large/external-dependent reproduction cases—AI15 P11, AF04 P03 and MAN P06—are documented in the reproduction notes. Their omitted inputs were not silently treated as verified.
