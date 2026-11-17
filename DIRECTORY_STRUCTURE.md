# Repository directory / 完整目录层级

**457 manuscripts / 2,373 pages** (edition of 2026-11-17: the Claude Code collection has four manuscripts, CC-P01, added on 2026-11-16 and revised since, and CC-P02, CC-P03 and CC-P04, added on 2026-11-17; the edition of 2026-09-17 had 453 / 2,312). BigWIN2 is the corrected origin collection for all 223 manuscripts from this workflow, not a one-paper net increment. This correction adds no new PDFs. GitHub publication is user-authorized; only a verified remote push establishes completion.

```text
AI-Has-Taste/
├── README.md / README.zh-CN.md         English / 中文 catalogs
├── DIRECTORY_STRUCTURE.md             layout and naming
├── UPLOAD_GUIDE.md                    authorized publication checklist
├── archive-manifest.json              457 PDFs / 2373 pages
├── assets/
│   ├── BigWIN2/
│   │   ├── catalog.json               223 manuscripts from this workflow
│   │   ├── reclassification-20260917.json
│   │   ├── validation.json / readme-validation.json
│   │   ├── PACKAGING_REPORT.md / file-tree.txt
│   │   ├── gates/                     preserved historical gate bytes
│   │   └── history/
│   │       ├── 20260914-misclassified-BigWIN1/
│   │       └── 20260914-incremental-only/
│   │                                  superseded metadata, not current counts
│   └── ai-conjectures/                conjecture classification evidence
├── pdfs/
│   ├── smallmac_1/                    17 PDFs
│   ├── smallmac_2/                    116 PDFs
│   ├── BigMac1/                       41 PDFs
│   ├── BigMac2/                       55 PDFs
│   ├── BigWIN2/                       218 PDFs
│   ├── ClaudeCode/                    4 PDFs (added 2026-11-16 and 2026-11-17)
│   └── ai-conjecture/                 6 PDFs: 5 BigWIN2 + 1 Smallmac
└── reproducible_source_code/
    ├── BigMac1/ / BigMac2/            unchanged upstream source availability
    ├── ClaudeCode/                    4 paired packages (CC-P01, CC-P02, CC-P03, CC-P04)
    └── BigWIN2/                       223 paired packages, including conjectures
        ├── prepare.py / build.py      verify bytes / disposable rebuild
        └── <archive-id>/
            ├── README.md / package.json
            └── source/               original relative paths and file bytes
                ├── manuscript/       or original paper/conjecture-note layout
                └── evidence/         code, exact data and proof
```

## Collections and deduplication / 分组与去重

The original 230 Smallmac/BigMac manuscripts are preserved. The 222 WIN manuscripts previously misclassified as BigWIN1 and the one already archived arbor-polytope paper now form **BigWIN2: 223 manuscripts**. Its 218 ordinary PDFs are in `pdfs/BigWIN2/`; 5 conjecture papers join the one Smallmac conjecture in `pdfs/ai-conjecture/`. All 223 paired source packages are under `reproducible_source_code/BigWIN2/`. No paper is duplicated between PDF folders.

本会话223篇统一归属BigWIN2，而不是把BigWIN2定义为“净新增1篇”。此次只是纠正合集归属与展示路径；没有增量PDF，仓库总数不变。42篇较早的Windows/v3文稿以历史流程记录和用户明确归属为依据，缺少逐篇聊天UUID，不声称逐条聊天取证。

The 19 historical same-result/final-version aliases remain in the README and [historical selection record](assets/BigWIN2/history/20260914-misclassified-BigWIN1/selection.json). These are not extra manuscripts. Superseded BigWIN1 packaging reports are retained under `assets/BigWIN2/history/20260914-misclassified-BigWIN1/`, not presented as current inventories. Current collection paths are recorded in [catalog.json](assets/BigWIN2/catalog.json) and [reclassification-20260917.json](assets/BigWIN2/reclassification-20260917.json).

## Names / 命名

- `BW2-BNN-PNN_Title.pdf`: retains the historical browser batch and item.
- `BW2-N01-PNN_Title.pdf`: retains the separately supplied newWIN-1 batch.
- `BW2-L…` / `BW2-PRYYYYMMDD-topic`: dated literature follow-ups, not invented browser batches.
- The display prefix `BW1-` became `BW2-`; original research IDs such as `win-00037-p01` did not change. The reclassification mapping preserves the old and new archive paths.

PDF bytes, authorship, frozen scientific source files and historical gate contents remain unchanged. The earlier correction of forty erroneous `Subject:` display titles is historical metadata maintenance, not a new mathematical result. Its [original mapping](assets/BigWIN2/history/20260914-incremental-only/relocations-and-title-corrections.json) is retained; use the current reclassification mapping for present paths. The earlier incremental-only BigWIN2 reports are retained under `assets/BigWIN2/history/20260914-incremental-only/`; their one-paper count is superseded. Recoverable staging backups and working scripts stay outside the repository in the sibling `support/` directory.

## Paired sources / 配套源码

Each WIN paper has links to its PDF, exact LaTeX entry and complete paired package. `source/` preserves original relative paths; `package.json` records hashes, dependencies and known limitations. Losslessly compressed large inputs must be restored before computations that need them. Older Smallmac/BigMac LaTeX excluded from the downloaded repository is not fabricated or claimed to be present.

```sh
python3 reproducible_source_code/BigWIN2/prepare.py --verify
python3 reproducible_source_code/BigWIN2/build.py BW2-PR20260914-arbor_ehrhart_words
```

Read package-specific instructions before scientific replay. A PDF build, a file-hash check, a finite experiment and a general-proof audit are different checks. Reclassification is not a fresh proof or novelty audit. External literature PDFs, account files, installed environments and agent transcripts are not republished.

[English catalog](README.md) · [中文目录](README.zh-CN.md) · [Repository paths](assets/BigWIN2/file-tree.txt) · [Current packaging report](assets/BigWIN2/PACKAGING_REPORT.md) · [Publication checklist](UPLOAD_GUIDE.md)
