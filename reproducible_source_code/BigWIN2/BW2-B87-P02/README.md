# BW2-B87-P02 — Restricted-Sumset Saturation with Two Missing Sums in Prime Fields

[Final PDF / 最终稿](../../../pdfs/BigWIN2/BW2-B87-P02_Restricted_Sumset_Saturation_with_Two_Missing_Sums_in_Prime_Fields.pdf) · [LaTeX entry / 入口](source/manuscript/main.tex) · [Sources, data and proof / 复现材料](source/) · [Gate records / 历史门控](../../../assets/BigWIN2/gates/BW2-B87-P02/)

Original ID / 原始编号: `win-00087-p02`. Origin / 来源: 87.

## Accepted scope / 已接受范围

Resolution of the frozen statement · proved / 冻结命题的证明／反证（见精确范围） · proved.

For every prime p &gt;= 11 and every integer 3 &lt;= ell &lt;= (p-3)/2, every ordered pair (A,B) of subsets of F_p with &#124;B&#124;=ell, &#124;A&#124;=p-ell, and &#124;A dotplus B&#124;=p-2 is simultaneously affinely equivalent to (A_(a,b),B_(a,b)) for some nonnegative a,b with a+b=ell, with B_(a,b)={-2j:0&lt;=j&lt;a} union {1+2j:0&lt;=j&lt;b}, C_(a,b)={2+2j:0&lt;=j&lt;a} union {-1-2j:0&lt;=j&lt;b}, and A_(a,b)=F_p minus C_(a,b). Every displayed pair has missing restricted sums exactly {0,2}. Two displayed representatives are affinely equivalent if and only if (a,b) agrees up to swapping, so there are floor(ell/2)+1 affine classes.

The unchanged PDF retains its original authorship. This package reuses historical independent review and release evidence; it is not a new mathematical audit, journal acceptance, or a claim about a wider parent problem.

PDF保持原始字节及署名。本次核对配套文件，不重新审稿，不将部分结果或猜想包装成原题全解。

## Restore exact inputs / 还原精确输入

From this package directory / 在当前包目录执行:

```sh
python3 ../prepare.py --restore BW2-B87-P02
```

No large input needs restoration.

Restoration verifies stored and original digests and refuses to overwrite modified data. Large restored files are excluded from Git; compressed copies are the distributed originals.

## Rebuild the manuscript / 重编译

```sh
python3 ../build.py BW2-B87-P02
```

The helper uses a disposable copy and retains build output outside the archive. Requires `latexmk` and the TeX packages declared by the source. Build status during packaging: **pass**. A regenerated PDF is not a replacement for the historical released PDF.

Recorded build working directory / 已核验编译目录: `latex-parent`. The helper applies this automatically.

## Reproduction programs and proof / 程序与证明

Run programs from the `source/` directory unless their original instructions specify a subdirectory. Inspect their arguments first: discovery searches and full certificates can be long-running. Prefer a disposable copy; original programs may regenerate result files.

- `evidence/triage_enumerate.py`

Bounded replay status in this packaging task: **not-rerun**. Not rerun means archived but not re-executed here; it does not mean the historical proof failed. A short test does not certify assertions outside its encoded finite range.



## Dependencies and limitations / 依赖与限制

- No third-party Python import detected by static inspection; this is not a tested environment lock.

- Asset selection is a packaging recommendation, not a rerun of the proof or citation audit.
- Do not copy external literature PDFs, downloaded web pages, third-party archives, jobs, logs, prompts, or private operational metadata.
- Review absolute paths and third-party attribution markers before publishing. Import names are inferred dependencies, not a tested environment lock.

`package.json` records every distributed scientific input, its original relative path, digest, and compression. External literature, account/configuration files, agent transcripts, installed environments and unrelated third-party binaries are not included. Bibliographic references remain in the LaTeX sources.
