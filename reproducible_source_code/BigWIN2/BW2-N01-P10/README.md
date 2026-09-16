# BW2-N01-P10 — Schur (2,2) reconstruction for explicit length classes

[Final PDF / 最终稿](../../../pdfs/BigWIN2/BW2-N01-P10_Schur_2_2_reconstruction_for_explicit_length_classes.pdf) · [LaTeX entry / 入口](source/manuscript/main.tex) · [Sources, data and proof / 复现材料](source/) · [Gate records / 历史门控](../../../assets/BigWIN2/gates/BW2-N01-P10/)

Original ID / 原始编号: `newwin-00001-p10`. Origin / 来源: 新WIN-1批次.

## Accepted scope / 已接受范围

Partial-result note; parent problem not fully solved / 部分结果札记；母题未完整解决.

Let n&gt;=2 and c_j(n)=n\*(n^2-1+3\*2^(j-1)-3^j)/3. If c_j(n) is nonzero for every 1&lt;=j&lt;=n, then every n-element multiset of positive real numbers, including repetitions, is uniquely determined by the cardinality and first n logarithmic power sums of its complete Schur-(2,2) monomial-value multiset, with tableau multiplicities. This condition holds for every n&gt;=3 with n!=4 and n modulo 60 outside {14,26,34,46}. Moreover, lengths 2 and 4 are uniquely reconstructible when the positive input sum is prescribed. Consequently, for every integer N&gt;=2, positive integer partitions lambda,mu of N of length at least two and common length outside {14,26,34,46} modulo 60 satisfy S22(lambda)=S22(mu) only if lambda=mu. Equal output cardinalities force equal lengths. No converse, counterexample at an excluded length, or all-length resolution is claimed. Exact scope and proofs are Theorems A--C of evidence/research-moment-proof.md.

The unchanged PDF retains its original authorship. This package reuses historical independent review and release evidence; it is not a new mathematical audit, journal acceptance, or a claim about a wider parent problem.

PDF保持原始字节及署名。本次核对配套文件，不重新审稿，不将部分结果或猜想包装成原题全解。

## Restore exact inputs / 还原精确输入

From this package directory / 在当前包目录执行:

```sh
python3 ../prepare.py --restore BW2-N01-P10
```

No large input needs restoration.

Restoration verifies stored and original digests and refuses to overwrite modified data. Large restored files are excluded from Git; compressed copies are the distributed originals.

## Rebuild the manuscript / 重编译

```sh
python3 ../build.py BW2-N01-P10
```

The helper uses a disposable copy and retains build output outside the archive. Requires `latexmk` and the TeX packages declared by the source. Build status during packaging: **pass**. A regenerated PDF is not a replacement for the historical released PDF.

Recorded build working directory / 已核验编译目录: `latex-parent`. The helper applies this automatically.

## Reproduction programs and proof / 程序与证明

Run programs from the `source/` directory unless their original instructions specify a subdirectory. Inspect their arguments first: discovery searches and full certificates can be long-running. Prefer a disposable copy; original programs may regenerate result files.

- `evidence/check-p10-p11-small.py`
- `evidence/check-p10-prefix.py`
- `evidence/check-research-moments.py`
- `evidence/check-triage-log-moments.py`

Bounded replay status in this packaging task: **not-rerun**. Not rerun means archived but not re-executed here; it does not mean the historical proof failed. A short test does not certify assertions outside its encoded finite range.



## Dependencies and limitations / 依赖与限制

- No third-party Python import detected by static inspection; this is not a tested environment lock.

- Asset selection is a packaging recommendation, not a rerun of the proof or citation audit.
- Do not copy external literature PDFs, downloaded web pages, third-party archives, jobs, logs, prompts, or private operational metadata.
- Review absolute paths and third-party attribution markers before publishing. Import names are inferred dependencies, not a tested environment lock.
- The original question is unresolved; the released artifact is a partial result or unproved conjecture, according to its frozen claim.
- External reference literature is not redistributed. Consult the bibliography and archived source URLs.

`package.json` records every distributed scientific input, its original relative path, digest, and compression. External literature, account/configuration files, agent transcripts, installed environments and unrelated third-party binaries are not included. Bibliographic references remain in the LaTeX sources.
