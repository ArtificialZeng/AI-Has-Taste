# BigWIN2 packaging report / 打包检查报告

## Scope

One new six-page gated final PDF is added to the preserved 452-paper local archive. All 258 current v4 projects were reconciled against the existing archive and topic aliases. The new release passed the nonmutating current-release validator, including PDF, source snapshot and historical review bindings. No new mathematical review or priority claim is implied.

Six conjecture PDFs were relocated to the exact requested pdfs/ai-conjecture/ directory. Forty Subject: display-title errors were corrected from manuscript headings; PDF/source bytes remain frozen. The 19 historical duplicate/version aliases are preserved rather than copied into another collection.

## Verification

Current checks are recorded in validation.json after packaging. Historical gate records, clean builds and finite verification outputs are separate evidence layers. The original PDF is retained even if a rebuild has a different nondeterministic PDF digest.

## Limits

This is a local review copy, not an external publication. Older upstream excluded LaTeX remains unavailable in this clone. Third-party papers, private operational transcripts and installed environments are not republished. Exact finite computational evidence does not replace the paper's general proof. Citation-access limitations documented by the original audits remain in force.


## Completed checks / 已完成检查

- All 453 PDFs / 2,312 pages match their manifest hashes; all 452 previously packaged PDF contents are unchanged. No duplicate PDF hashes or stray PDFs exist.
- All 223 WIN source packages / 4,092 scientific source files and their copied gate records match stored digests. Required source/PDF files are not ignored by Git; no publishable file is 100 MB or larger.
- The new six-page paper clean-builds without final warnings. Its regenerated bibliography, extracted text and all six rendered pages match the frozen release. All six pages were visually inspected. Rebuild timestamps differ, so the original released PDF is retained.
- A bounded exact replay matches the archived JSON bytes: 264 local identities, 225 operator identities, 80,011 subset objects, 17,065 word tests and three direct cases. This is not a new proof audit.
- The older WSL v3 archive was also checked: its three eligible releases were already included; no additional unique final manuscript was found.

See [file and byte verification](validation.json), [build/replay evidence](rebuild-replay.json), and [current intake reconciliation](intake-reconciliation.json). Link/render verification is recorded separately when completed.


## README checks / 目录链接与显示

[Offline GFM validation](readme-validation.json): 27/27 checks passed. English and Chinese each contain 453 unique canonical paper rows and 1,277 resolving local links; all 223 paired package READMEs contribute 892 resolving local links. Tested local heading anchors resolve. All 40 corrected titles and the exact singular conjecture paths are reflected in both catalogs. The permanent ratio is rendered as plain Unicode, R(C) = per(C ∘ C) / per(C)², avoiding the reported macro error.

The supplied BigWIN2 prepare.py --verify and build.py helpers were also executed successfully. Verification checks all 18 new source files; the builder returns a six-page PDF in its disposable working directory and does not alter archived inputs.
