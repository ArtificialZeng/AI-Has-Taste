# GitHub 上传说明 / Git upload policy

## repository 与 work

- `repository/`：准备合并到 AI-Has-Taste 的项目内容。里面的 `README.md`、`pdfs/`、`assets/`、`reproducible_source_code/` 对应 GitHub 项目的根目录内容。
- 同级的 `work/`：整理脚本、临时构建、审查截图和工作日志，不属于发布内容，不要放进 Git 仓库。
- **不要在原项目根目录内再套一层 `repository/`**；应合并它的内容。

## 本次 Git 策略：保留 PDF 与复现代码，不上传 LaTeX

`.gitignore` 排除整个 `latex_source_code/`，也排除复现目录中重复的 `.tex`、`.bib`、`.bbl`、`.sty`、`.cls`、`.bst` 等 LaTeX 文件及构建副产物。文件仍保留在本地，没有删除。数学程序、JSON 数据、证书、证明日志以及最终 PDF 不会因为这份规则被整体忽略。

The Git distribution contains PDFs and selected reproduction code/evidence, **not manuscript LaTeX**. LaTeX sources remain in the local review copy. The README's LaTeX column is informational and has no link to an omitted directory.

## 如何推送

当前这个下载整理副本没有 `.git`。推荐先克隆原来的 `ArtificialZeng/AI-Has-Taste` 仓库，再把本目录内容合并到克隆的根目录（保留克隆中的 `.git`）。不要另建不相关历史后强制推送覆盖远端。

在克隆根目录检查变更后，正常 `git add`、`git commit`、`git push` 即可。不要用 `git add -f` 强制加入已忽略的 LaTeX。这里没有替你执行提交或推送。

**注意：`.gitignore` 只影响尚未被 Git 跟踪的文件。** 如果你的克隆里已经跟踪了 LaTeX，需要先针对那些已跟踪文件解除跟踪，再提交；忽略规则不会自动从远端删除它们。解除跟踪应保留本地文件，不要使用删除工作目录的命令。

## 复现范围

当前 BigMac1 的 41 个项目都附有选定的程序和精确证据。它们不包含原机器的完整运行环境，也不包含所有大型历史输入：AI15 P11、AF04 P03、MAN P06 的外部工具或大体积数据需求见 [复现说明](assets/BigMac1/REPRODUCTION_NOTES.md)。因此，“复现代码在里面”不等于“41 篇都能无依赖、一键完整复现”。

本次不上传 LaTeX，也意味着 Git 克隆不能重编译论文 PDF；某些历史发布审计包装器若绑定 `.tex/.bib` 哈希，需要本地完整副本。不要通过忽略缺失输入来伪造审计通过。

## 清单与历史检查

- `assets/BigMac1/package-manifest.json`：本次 Git 包含的 BigMac1 PDF/选定源码字节。
- `assets/BigMac1/review-manifest.sha256` 和 `file-tree.txt`：按当前 `.gitignore` 筛选后的上传内容，不包含被忽略的本地文件。
- 历史 proof/citation/build 审计记录保留原样。此前 41/41 LaTeX 构建通过发生在**含 LaTeX 的本地完整副本**，不代表新 Git 分发包含 LaTeX。
- [本次 Git 排除验证](assets/BigMac1/git-upload-validation.json)。

后续再修改文件或加入新批次时，应刷新相应清单；本清单不是自动更新服务。
