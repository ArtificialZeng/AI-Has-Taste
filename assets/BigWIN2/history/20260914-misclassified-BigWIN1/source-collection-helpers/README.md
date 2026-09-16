# BigWIN1 — paired LaTeX and reproducible research assets

[English catalog](../../README.md#bigwin1) · [中文目录](../../README.zh-CN.md#bigwin1) · [Package checks](../../assets/BigWIN1/PACKAGING_REPORT.md)

Every cataloged PDF has a package below. `source/` preserves original project-relative paths. Its LaTeX entry, code, exact data and proof documents are paired with the unchanged released PDF. This directory does not contain installed environments, credentials, agent transcripts, external literature PDFs or unrelated binaries.

```sh
python3 prepare.py --verify
python3 prepare.py --restore PACKAGE_ID
python3 build.py PACKAGE_ID
```

Large inputs are distributed as lossless gzip files with exact restoration metadata in each `package.json`. Restore before full reproduction. Restored large originals are Git-ignored to avoid accidentally committing an oversized file. Build checks use temporary copies and do not rewrite historical PDFs. Individual packages list dependencies and any bounded replay coverage. Not every proof has a short executable certificate; no universal one-click scientific reproduction is claimed.

每个PDF配一个包；LaTeX、代码和证据保留相对路径。先校验文件，需要时还原大数据，再参考逐题README运行。短回放、全文证明审查、完整穷举与重新编译不是同一件事；请按各包说明理解已完成的检查范围。


PDF classification update / PDF归类更新：BigWIN1来源的222套源码仍在此目录；其中提出新猜想的论文PDF移入[ai-conjectures](../../pdfs/ai-conjecture/)，每套README和package.json均指向新地址。
