# BigWIN2 origin correction / 本会话归属纠正

Date: 2026-09-17. This is a repository-packaging update, not a new mathematical review.

## Corrected ownership

All **223** WIN manuscripts from this conversation belong to **BigWIN2**. The previous packaging mistakenly labeled 222 as BigWIN1 and treated BigWIN2 as only one newly added manuscript. This update corrects that distinction; it does not copy those papers a second time.

- `pdfs/BigWIN2/`: **218** ordinary final manuscripts.
- `pdfs/ai-conjecture/`: **5** BigWIN2 conjectural papers, alongside the unchanged Smallmac `SM2-P11` conjecture.
- `reproducible_source_code/BigWIN2/`: **223** paired LaTeX/reproduction packages.
- Entire repository: **453** unique PDFs, **2,312** pages; **6** conjecture PDFs in total.

The [old/new mapping](reclassification-20260917.json) records every changed PDF/package path and presentation ID. Original mathematical problem IDs, accepted scope, authorship, frozen PDF contents, scientific source files, and gate-file bytes are preserved. `BW1-` presentation IDs are now `BW2-`; literature follow-ups are not relabeled as invented browser batches.

本次按“本对话产生的成果”纠正归属，不以“上次尚未收录的增量”定义 BigWIN2。旧42篇 Windows/v3 档案缺少逐篇精确聊天 UUID；归属依据历史主控记录与用户本轮明确纠正，不声称完成原始聊天逐轮取证。

## Incremental check

No additional eligible final manuscript or newer final version was found in the current known research roots. The [incremental summary](incremental-check-20260917.json) distinguishes active releases from drafts, duplicates, and unreleased projects:

- WSL v4: 258 projects, including 181 exact already-archived releases, 18 existing topic/version aliases, and 59 without an eligible current release.
- WSL v3: 60 projects, including 3 eligible already-archived releases and 57 without an eligible release.
- Windows: 39 selected historical final PDFs matched their archived hashes; 667 associated source/gate checks found no differences. A 404-PDF metadata sweep found no PDFs modified since 2026-09-14 in the known local research roots.

No original queue, gate state, research source, or release PDF was changed by this scan. Missing or unreleased work is not promoted to a final paper. The 19 historical semantic/version aliases remain recorded in [selection.json](selection.json) and are not duplicated.

## Verification and limits

Current byte, page, unique-ID, source/gate, Git-inclusion, and size checks are recorded in [validation.json](validation.json). Current English/Chinese catalog and package-link checks are recorded in [readme-validation.json](readme-validation.json). A passing packaging check is not a proof of the papers' mathematical claims.

The completed migration checks found all 453 PDF hashes/pages intact, all 223 original research IDs unchanged, all 4,092 scientific files and 2,405 gate files intact, and no duplicate or missing PDF, ignored required file, or publishable file of 100 MB or larger. The public `prepare.py --verify` helper independently reported 223 packages and 4,092 verified stored files, without restoring or changing inputs. English/Chinese and all 223 package READMEs passed the current link/structure checks. Secret-pattern screening found no high-specificity credential matches; pattern screening is not a guarantee about every possible form of private information.

The [historical snapshots](history/README.md) preserve prior audit/build/replay records and prior display metadata. Their old paths and publication-status statements are historical only. The previously added arbor-polytopes paper's [clean build and bounded replay](history/20260914-incremental-only/rebuild-replay.json) remain available; those checks were not represented as new proof audits.

Older upstream Smallmac/BigMac LaTeX excluded from the downloaded repository remains unavailable where documented; no missing source was fabricated. Bibliographic and mathematical limitations recorded in individual papers and historical audits remain in force. Private operational logs, credentials, installed environments and external literature PDFs are not part of this publication package.

The user has authorized publication to `ArtificialZeng/AI-Has-Taste`. A Git transport outcome must be established from the actual push and remote commit verification, not inferred from these packaging records.
