# BW2-PR20260913-qdescent_logconcavity — Strong q-log-concavity of q-descent coefficients

[Final PDF / 最终稿](../../../pdfs/BigWIN2/BW2-PR20260913-qdescent_logconcavity_Strong_q_log_concavity_of_q_descent_coefficients.pdf) · [LaTeX entry / 入口](source/manuscript/main.tex) · [Sources, data and proof / 复现材料](source/) · [Gate records / 历史门控](../../../assets/BigWIN2/gates/BW2-PR20260913-qdescent_logconcavity/)

Original ID / 原始编号: `primary-20260913-qdescent-logconcavity`. Origin / 来源: primary.

## Accepted scope / 已接受范围

Resolution of the frozen statement · proved / 冻结命题的证明／反证（见精确范围） · proved.

For every finite nonempty S subset of the positive integers, put m=max S and, for 1&lt;=k&lt;=m, let a_k(S;q) be the sum of q^inv(pi) over permutations pi in Sym(m+k) with Des(pi)=S and {m+1,...,m+k} contained in the first m values; set a_0=a_(m+1)=0. Every a_k for 1&lt;=k&lt;=m is nonzero, and a_i\*a_j-a_(i-1)\*a_(j+1) has nonnegative integer coefficients for all 1&lt;=i&lt;=j&lt;=m. This proves the frozen literal original with i&lt;j and, separately, the disclosed additional diagonal cases i=j. The same proof establishes the directed strengthening of frozen Target K: for every m&gt;=1, every 1&lt;=i&lt;=j&lt;=m, and independently every 1&lt;=r,s&lt;=m, K(m;i,r)\*K(m;j,s)-K(m;i-1,r)\*K(m;j+1,s) is in Z_&gt;=0\[q\], where K(m;k,r)=q^(k^2)(\[m choose k\]_q-\[m-r choose k\]_q) for 1&lt;=k&lt;=m, Gaussian coefficients are zero outside their natural range, and K(m;0,r)=K(m;m+1,r)=0. The complete proposed proof, including a weight-preserving injection, explicit left inverse, reversal and direct original-definition reduction, is in evidence/research/protected-minimum-proof.md.

The unchanged PDF retains its original authorship. This package reuses historical independent review and release evidence; it is not a new mathematical audit, journal acceptance, or a claim about a wider parent problem.

PDF保持原始字节及署名。本次核对配套文件，不重新审稿，不将部分结果或猜想包装成原题全解。

## Restore exact inputs / 还原精确输入

From this package directory / 在当前包目录执行:

```sh
python3 ../prepare.py --restore BW2-PR20260913-qdescent_logconcavity
```

No large input needs restoration.

Restoration verifies stored and original digests and refuses to overwrite modified data. Large restored files are excluded from Git; compressed copies are the distributed originals.

## Rebuild the manuscript / 重编译

```sh
python3 ../build.py BW2-PR20260913-qdescent_logconcavity
```

The helper uses a disposable copy and retains build output outside the archive. Requires `latexmk` and the TeX packages declared by the source. Build status during packaging: **pass**. A regenerated PDF is not a replacement for the historical released PDF.

Recorded build working directory / 已核验编译目录: `latex-parent`. The helper applies this automatically.

## Reproduction programs and proof / 程序与证明

Run programs from the `source/` directory unless their original instructions specify a subdirectory. Inspect their arguments first: discovery searches and full certificates can be long-running. Prefer a disposable copy; original programs may regenerate result files.

- `evidence/intake/qdescent-calibration.py`
- `evidence/intake/triage-kernel-check.py`
- `evidence/intake/triage-recovery-check.py`
- `evidence/research/protected-minimum-check.py`

Bounded replay status in this packaging task: **not-rerun**. Not rerun means archived but not re-executed here; it does not mean the historical proof failed. A short test does not certify assertions outside its encoded finite range.



## Dependencies and limitations / 依赖与限制

- No third-party Python import detected by static inspection; this is not a tested environment lock.

- Asset selection is a packaging recommendation, not a rerun of the proof or citation audit.
- Do not copy external literature PDFs, downloaded web pages, third-party archives, jobs, logs, prompts, or private operational metadata.
- Review absolute paths and third-party attribution markers before publishing. Import names are inferred dependencies, not a tested environment lock.
- External reference literature is not redistributed. Consult the bibliography and archived source URLs.

`package.json` records every distributed scientific input, its original relative path, digest, and compression. External literature, account/configuration files, agent transcripts, installed environments and unrelated third-party binaries are not included. Bibliographic references remain in the LaTeX sources.
