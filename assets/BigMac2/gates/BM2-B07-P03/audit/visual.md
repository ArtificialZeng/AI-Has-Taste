# Fresh rendered-page visual audit

Job: `bigMac-00007-p03-release-81cefd28b28f`. Reviewed: 2026-09-08T01:29:21.569617+00:00.

Evidence snapshot: `cde79d0ffca4c534449707d908f5983ea532054c14cc11a1f03e5d6913fcb0c1`.
Manuscript digest: `01fa45de2f853484308b276235d642c8f28098bd86c264922d2333c9e4dae501`.
PDF digest: `f363137820632afdb2f4d961be62835e867bc9334e9a32269a8566997f37cd4a`.

Verdict: **accept**. Actually rendered and visually inspected every page of the current rebuilt PDF using `pdftoppm -r 115 -png manuscript/build/main.pdf audit/release-visual/page`; then opened all five PNG images with the image-viewing tool in this release context. Each image is 978 by 1265 pixels. This review is separate from the writer's images and is not based on text extraction alone.

| Page | Image | Actual visual observations |
|---|---|---|
| 1 | `audit/release-visual/page-1.png` | Two-line title, author/affiliation/email and abstract are clear. The domination formula, theorem, conditional corollary and citations fit. Bottom corollary remains above the page number; no overlap or clipping. |
| 2 | `audit/release-visual/page-2.png` | Bundle notation, quantified equivalence and equation number are legible and separated. All twelve generator arrays fit, with visible degree/edge options. No clipped monospace text or corrupted math symbol. |
| 3 | `audit/release-visual/page-3.png` | Both census and certificate tables have clear headers, aligned cells and intact rules. Counts, multiplicities and scan ranks are readable; captions do not collide. The edge-order convention is clear. The final paragraph continues normally on page 4. |
| 4 | `audit/release-visual/page-4.png` | Pair-distribution superscripts are distinguishable; proof and end mark fit. Supplement paths, replay commands, limitations and AI-assistance disclosure are legible. No line extends beyond margins. |
| 5 | `audit/release-visual/page-5.png` | Four numbered references are fully visible. Titles, author lists, journal years, arXiv version and all DOI strings render correctly. The references-only page has ample whitespace and no layout defect. |

There are no figures, charts or graphical data requiring separate value extraction. All values in the two tables were compared against the accepted machine-readable evidence in `audit/release-content-check.md`. Body fonts and mathematical symbols remain readable, page numbers are consistent, and no substantive presentation defect was found. Metadata and font embedding checks are documented in the build report.
