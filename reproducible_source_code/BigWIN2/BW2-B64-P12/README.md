# BW2-B64-P12 — Quartic convergence in a diagonal counterexample to a claimed sixth-order inverse-matrix iteration

[Final PDF / 最终稿](../../../pdfs/BigWIN2/BW2-B64-P12_Quartic_convergence_in_a_diagonal_counterexample_to_a_claimed_sixth_order_inverse_matrix_iteration.pdf) · [LaTeX entry / 入口](source/manuscript/main.tex) · [Sources, data and proof / 复现材料](source/) · [Gate records / 历史门控](../../../assets/BigWIN2/gates/BW2-B64-P12/)

Original ID / 原始编号: `win-00064-p12`. Origin / 来源: 64.

## Accepted scope / 已接受范围

Resolution of the frozen statement · disproved / 冻结命题的证明／反证（见精确范围） · disproved.

For the CTM iteration of Cordero--Torregrosa, arXiv:2609.04433v1, with residual R_k=I-AX_k and nu_k=&#124;&#124;R_k^2&#124;&#124;_F^2/&#124;&#124;R_k&#124;&#124;_F^2, the general order-six assertion in PDF Theorem 2.1 is false. Precisely, take A=I_3 and X_0=I_3-t diag(1,2,3). For every 0&lt;t&lt;=10^{-2}, the exact first residual is R_1=t^4 diag(-6,-12,18)+7t^6 diag(1,16,81), and the entire nonterminating orbit has Q-order exactly four: for every k&gt;=1, (27/512)&#124;&#124;R_k&#124;&#124;_F^4&lt;&#124;&#124;R_{k+1}&#124;&#124;_F&lt;(4/3)&#124;&#124;R_k&#124;&#124;_F^4, and &#124;&#124;R_{k+1}&#124;&#124;_F/&#124;&#124;R_k&#124;&#124;_F^4 converges to a positive finite limit explicitly described by the limiting projective direction. Hence the quartic term is persistent, not a one-step artifact. The source proof's equation (2.7) both asserts an unjustified vanishing normalized quartic coefficient and then substitutes the moving value &#124;&#124;e_k&#124;&#124;^2 for a fixed epsilon in the definition of convergence. The claim refutes the theorem's stated general order, but does not claim failure of convergence or classify all CTM orbits.

The unchanged PDF retains its original authorship. This package reuses historical independent review and release evidence; it is not a new mathematical audit, journal acceptance, or a claim about a wider parent problem.

PDF保持原始字节及署名。本次核对配套文件，不重新审稿，不将部分结果或猜想包装成原题全解。

## Restore exact inputs / 还原精确输入

From this package directory / 在当前包目录执行:

```sh
python3 ../prepare.py --restore BW2-B64-P12
```

No large input needs restoration.

Restoration verifies stored and original digests and refuses to overwrite modified data. Large restored files are excluded from Git; compressed copies are the distributed originals.

## Rebuild the manuscript / 重编译

```sh
python3 ../build.py BW2-B64-P12
```

The helper uses a disposable copy and retains build output outside the archive. Requires `latexmk` and the TeX packages declared by the source. Build status during packaging: **pass**. A regenerated PDF is not a replacement for the historical released PDF.

Recorded build working directory / 已核验编译目录: `latex-parent`. The helper applies this automatically.

## Reproduction programs and proof / 程序与证明

Run programs from the `source/` directory unless their original instructions specify a subdirectory. Inspect their arguments first: discovery searches and full certificates can be long-running. Prefer a disposable copy; original programs may regenerate result files.

- `evidence/verify_identities.py`

Bounded replay status in this packaging task: **not-rerun**. Not rerun means archived but not re-executed here; it does not mean the historical proof failed. A short test does not certify assertions outside its encoded finite range.



## Dependencies and limitations / 依赖与限制

- sympy

- Asset selection is a packaging recommendation, not a rerun of the proof or citation audit.
- Do not copy external literature PDFs, downloaded web pages, third-party archives, jobs, logs, prompts, or private operational metadata.
- Review absolute paths and third-party attribution markers before publishing. Import names are inferred dependencies, not a tested environment lock.
- External reference literature is not redistributed. Consult the bibliography and archived source URLs.

`package.json` records every distributed scientific input, its original relative path, digest, and compression. External literature, account/configuration files, agent transcripts, installed environments and unrelated third-party binaries are not included. Bibliographic references remain in the LaTeX sources.
