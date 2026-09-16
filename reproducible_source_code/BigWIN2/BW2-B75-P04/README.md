# BW2-B75-P04 — Quantitative Endpoint Classification of a Sufficient Condition in a Weighted Bergman Hilbert-Operator Norm Argument

[Final PDF / 最终稿](../../../pdfs/BigWIN2/BW2-B75-P04_Quantitative_Endpoint_Classification_of_a_Sufficient_Condition_in_a_Weighted_Bergman_Hilbert_Operator_Norm_Ar.pdf) · [LaTeX entry / 入口](source/manuscript/main.tex) · [Sources, data and proof / 复现材料](source/) · [Gate records / 历史门控](../../../assets/BigWIN2/gates/BW2-B75-P04/)

Original ID / 原始编号: `win-00075-p04`. Origin / 来源: 75.

## Accepted scope / 已接受范围

Partial-result note; parent problem not fully solved / 部分结果札记；母题未完整解决.

Let alpha &gt;= 0, A = alpha+2, C_alpha = B(1+alpha,2+alpha/2), and fix 0 &lt;= b &lt; 1. For the displayed function G_(alpha,b)(p) in source.md, lim_{p downarrow A} G_(alpha,b)(p) = 4b; moreover, if b &gt; C_alpha/4, an explicit epsilon &gt; 0 makes every admissible p in (A,A+epsilon) satisfy G_(alpha,b)(p) &gt; C_alpha. For L_(alpha,b)(p), the exact left side of condition (3.38) in arXiv:2609.04833v1, writing h=p-A gives the certified expansion &#124;L_(alpha,b)(A+h) - pi^2 b/3 - D(A,b)h&#124; &lt;= K_L(A,b)h^2 for 0&lt;h&lt;=1/4, where D(A,b)=pi^2/(3A)-2b zeta(3)(2-1/A) and K_L(A,b) is the explicit positive constant in evidence/quantitative-taylor-audit.md. Consequently, there exists an admissible punctured right neighborhood on which condition (3.38), L_(alpha,b)(p) &lt;= C_alpha, holds if and only if 0 &lt;= b &lt; 3C_alpha/pi^2. At equality b=3C_alpha/pi^2, D(A,b)&gt;0 for every A&gt;=2, so (3.38) fails throughout an explicit punctured right neighborhood. Hence the published Corollary-3.5 route does not prove Theorem 3.4's natural uniform-in-b reading. This statement neither disproves the operator-norm identity nor asserts that (3.38) is necessary.

The unchanged PDF retains its original authorship. This package reuses historical independent review and release evidence; it is not a new mathematical audit, journal acceptance, or a claim about a wider parent problem.

PDF保持原始字节及署名。本次核对配套文件，不重新审稿，不将部分结果或猜想包装成原题全解。

## Restore exact inputs / 还原精确输入

From this package directory / 在当前包目录执行:

```sh
python3 ../prepare.py --restore BW2-B75-P04
```

No large input needs restoration.

Restoration verifies stored and original digests and refuses to overwrite modified data. Large restored files are excluded from Git; compressed copies are the distributed originals.

## Rebuild the manuscript / 重编译

```sh
python3 ../build.py BW2-B75-P04
```

The helper uses a disposable copy and retains build output outside the archive. Requires `latexmk` and the TeX packages declared by the source. Build status during packaging: **pass**. A regenerated PDF is not a replacement for the historical released PDF.

Recorded build working directory / 已核验编译目录: `latex-parent`. The helper applies this automatically.

## Reproduction programs and proof / 程序与证明

Run programs from the `source/` directory unless their original instructions specify a subdirectory. Inspect their arguments first: discovery searches and full certificates can be long-running. Prefer a disposable copy; original programs may regenerate result files.

- `evidence/endpoint-audit.py`
- `evidence/quantitative-taylor-audit.py`

Bounded replay status in this packaging task: **not-rerun**. Not rerun means archived but not re-executed here; it does not mean the historical proof failed. A short test does not certify assertions outside its encoded finite range.



## Dependencies and limitations / 依赖与限制

- mpmath
- sympy

- Asset selection is a packaging recommendation, not a rerun of the proof or citation audit.
- Do not copy external literature PDFs, downloaded web pages, third-party archives, jobs, logs, prompts, or private operational metadata.
- Review absolute paths and third-party attribution markers before publishing. Import names are inferred dependencies, not a tested environment lock.
- The original question is unresolved; the released artifact is a partial result or unproved conjecture, according to its frozen claim.

`package.json` records every distributed scientific input, its original relative path, digest, and compression. External literature, account/configuration files, agent transcripts, installed environments and unrelated third-party binaries are not included. Bibliographic references remain in the LaTeX sources.
