# BigWIN2 — paired LaTeX and reproduction assets

[English catalog](../../README.md#bigwin2) · [中文目录](../../README.zh-CN.md#bigwin2) · [Current catalog](../../assets/BigWIN2/catalog.json) · [Checks and limits](../../assets/BigWIN2/PACKAGING_REPORT.md)

This directory holds **223 paired packages from the current research workflow**: 222 previously misclassified as BigWIN1 and the already archived arbor-polytope package. BigWIN2 denotes origin, not a net-new increment. Its 218 ordinary PDFs are in `../../pdfs/BigWIN2/`; its 5 conjecture PDFs are in `../../pdfs/ai-conjecture/`. No PDF is copied twice.

The [reclassification mapping](../../assets/BigWIN2/reclassification-20260917.json) records the archive-prefix and path correction from `BW1-`/BigWIN1 to `BW2-`/BigWIN2. Original research IDs, frozen scientific source bytes, historical gate bytes and PDF bytes are preserved. The 42 older Windows/v3 papers have workflow-level provenance and explicit user attribution, but no per-paper chat UUID is claimed. Dated literature follow-ups keep their real source IDs, not invented browser batch numbers.

Each package contains its exact manuscript sources, curated code/data/proof and a byte manifest. `source/` preserves original relative paths. `prepare.py --verify` checks stored files; losslessly compressed inputs must be restored before full replay. Follow the helper's current help and the package instructions. `build.py PACKAGE_ID` uses a disposable source copy and requires Python 3.10+, latexmk and the manuscript's TeX dependencies. It does not change the archived final PDF.

```sh
python3 reproducible_source_code/BigWIN2/prepare.py --verify
python3 reproducible_source_code/BigWIN2/build.py BW2-PR20260914-arbor_ehrhart_words
```

Run these commands from the repository root. Hash checking, clean compilation, bounded computational replay and mathematical proof review are distinct checks. This collection correction does not certify a fresh full replay, external peer review or novelty review. Package-specific limitations and the 19 historical semantic/final-version aliases remain disclosed.
