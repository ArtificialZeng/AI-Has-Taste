# BigWIN1 packaging report / 整理与检查报告

Prepared 2026-09-14. This is a local, byte-preserving archive integration, not a new mathematics review or a publication acceptance decision. No commit or push was made.

## Selection / 收录

- 241 historically gated candidates inspected; 222 final PDFs selected, 1056 pages.
- 19 incoming duplicate/older-result aliases map to an existing or newer canonical manuscript; no second PDF copy is introduced.
- 117 inspected projects without an eligible current release are excluded. Broader unresolved project inventory is not a PDF inventory.
- 4074 paired source inputs: 540,990,140 stored bytes, 1,517,622,401 original bytes. 10 large inputs use lossless compression.
- Original 230 PDF bytes and upstream scientific source trees are preserved. New manuscript kinds: `{"historical-gated-manuscript": 39, "conjecture-note": 5, "resolution-paper": 134, "result-note": 44}`.

Original problem status and a manuscript's accepted scope are separate. A partial-result note or conjectural note is not a full resolution of its parent question. Historical legacy gates are retained under their original format and limitations, rather than relabeled as modern gates. Local primary-literature follow-ups have explicit controller provenance; their IDs are not fabricated browser batches.

原问题状态与文稿结论范围分开记录。历史终稿审核依据与新版门控并不强行等同；本次没有追加Astra复审，也没有更改既有PDF或署名。19条映射的范围和限制均公开在目录中。

## Checks performed / 已做检查

- Every included PDF is copied with its recorded digest. Every scientific input is byte-checked; compressed assets are also checked against the original decompressed digest.
- LaTeX rebuild status: `{'pass': 222}`. Builds use temporary copies, no shell escape, and compare page counts / unresolved citations. A fresh build is a packaging check, not a replacement released PDF or a new proof audit.
- Bounded scientific replay status: `{'not-rerun': 202, 'passed': 20}`. Only statically reviewed short checks are executed in temporary copies. The per-package README and [verification results](verification-results.json) state their scope; larger searches are archived but not rerun in this task.
- Static Python syntax checks covered all 222 packages and 679 Python files, with no syntax errors; files were compiled in memory without imports or execution. Syntax correctness is not a proof-validity check.
- The distributed `prepare.py` verified all 4,074 stored inputs; a 45 MB certificate was restored and digest-checked in a temporary copy, with a second restore making no writes. The distributed `build.py` passed both default-directory and source-root-directory integration tests.
- English and Chinese indexes link each PDF to its own `main.tex` and reproduction tree. The reported permanent formula is now portable Unicode: R(C) = per(C ∘ C) / per(C)².
- All BigWIN1 LaTeX sources must be Git-addable under the narrow new exceptions; restored large raw inputs remain ignored. Distributed files stay below the repository's 100,000,000-byte packaging cap.
- The release gates' historical per-page PDF audits remain the publication evidence. Any representative preview checks here are packaging spot-checks, not a claim of re-reviewing all 1,056 pages.
- Eight first/last pages from four manuscript kinds were visually inspected: [spot-check scope](pdf-spot-checks.json). No cropping, overlaps or unreadable layout was observed on those pages.

## Limitations / 限制

No external peer-review or open-problem novelty claim is added by this packaging task. Not every program is short-running or dependency-free, and full SAT certificates/discovery searches were not indiscriminately rerun. Build/replay failures or unavailable dependencies, if any, are recorded separately from the historical mathematical status. Read each package's accepted scope and limitations.

External literature PDFs, account/configuration files, agent transcripts, installed environments and unrelated binaries are not distributed. Historical audit/proof material can contain original local paths or tool identifiers as provenance; these are not executable setup instructions. Third-party scientific input attribution remains in its original files and bibliography. Original scientific files are never silently patched to manufacture a passing check.

本次只是配套归档，不以复现资产数量、编译成功或PDF数量代替数学真实性。发布前由用户审阅；对于第三方数据、引用和许可，请保留原有署名与说明。

## Lossless large-input distribution / 大数据无损分发

Run the documented `prepare.py --restore ARCHIVE_ID` command before a computation that needs these inputs. Original research locations are unaffected.

| Package | Original relative input | Original bytes | Distributed gzip bytes |
|---|---|---:|---:|
| `BW1-B06-P04` | `source/certificates/nac11_four_way.cert` | 104,314,385 | 40,748,463 |
| `BW1-B06-P04` | `source/experiments/upstream/LamanGraphs11.txt` | 37,270,710 | 14,222,513 |
| `BW1-B06-P06` | `source/certificates/p11_radius_certificate.bin` | 45,011,088 | 7,539,541 |
| `BW1-B17-P02` | `source/certificates/f3_126_ge17.drat` | 417,189,026 | 56,305,397 |
| `BW1-B17-P13` | `source/certificates/no_66.drup` | 35,331,788 | 10,044,735 |
| `BW1-B36-P02` | `source/evidence/k17.drat` | 389,369,126 | 60,414,458 |
| `BW1-B70-P02` | `source/evidence/research_taylor_cover_1024_certificate.json` | 53,714,057 | 12,524,046 |
| `BW1-L260905848-P01` | `source/evidence/nonstar_equality.cnf` | 44,431,500 | 6,682,113 |
| `BW1-L260905848-P01` | `source/evidence/product_above_bound.cnf` | 44,439,753 | 6,691,249 |
| `BW1-PR20260913-subsum_denominator` | `source/evidence/research3_sharp_probe.json` | 36,591,320 | 15,857,977 |

## Navigation / 定位

[English index](../../README.md#bigwin1) · [中文索引](../../README.zh-CN.md#bigwin1) · [Directory](../../DIRECTORY_STRUCTURE.md) · [Catalog](catalog.json) · [Selection and aliases](selection.json) · [Machine-readable summary](packaging-summary.json)


**Classification update:** New-conjecture PDFs have been relocated to `pdfs/ai-conjectures/`; the 222-paper BigWIN1 origin count and source packages are unchanged. Consult the current root manifest and bilingual catalogs.
