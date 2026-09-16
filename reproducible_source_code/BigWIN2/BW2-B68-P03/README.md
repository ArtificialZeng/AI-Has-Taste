# BW2-B68-P03 — A Conjectural Unary-Theta Formula for the 6n+1-Section of 18-Colored Generalized Frobenius Partitions

[Final PDF / 最终稿](../../../pdfs/ai-conjecture/BW2-B68-P03_A_Conjectural_Unary_Theta_Formula_for_the_6n_1_Section_of_18_Colored_Generalized_Frobenius_Partitions.pdf) · [LaTeX entry / 入口](source/manuscript/main.tex) · [Sources, data and proof / 复现材料](source/) · [Gate records / 历史门控](../../../assets/BigWIN2/gates/BW2-B68-P03/)

Original ID / 原始编号: `win-00068-p03`. Origin / 来源: 68.

## Accepted scope / 已接受范围

Conjectural note; original problem unresolved / 猜想札记；原问题仍未解决.

Unproved conjecture in (Z/16Z)\[\[q\]\]: for Andrews's 18-colored generalized Frobenius partition function, sum_{m&gt;=0} cphi_18(6m+1) q^m is congruent to 4\*f_2\*f_3^2/(f_1\*f_6), equivalently 4\*sum_{k in Z} q^{k(3k-1)/2}. The Jacobi-triple-product equality of the two right-hand expressions and their absence of exponents 3 or 4 modulo 5 are proved; the left-to-right congruence is not proved. Exact supporting computation covers 0&lt;=m&lt;=504, with 0&lt;=m&lt;=99 used for discovery and 100&lt;=m&lt;=504 held out.

The unchanged PDF retains its original authorship. This package reuses historical independent review and release evidence; it is not a new mathematical audit, journal acceptance, or a claim about a wider parent problem.

PDF保持原始字节及署名。本次核对配套文件，不重新审稿，不将部分结果或猜想包装成原题全解。

## Restore exact inputs / 还原精确输入

From this package directory / 在当前包目录执行:

```sh
python3 ../prepare.py --restore BW2-B68-P03
```

No large input needs restoration.

Restoration verifies stored and original digests and refuses to overwrite modified data. Large restored files are excluded from Git; compressed copies are the distributed originals.

## Rebuild the manuscript / 重编译

```sh
python3 ../build.py BW2-B68-P03
```

The helper uses a disposable copy and retains build output outside the archive. Requires `latexmk` and the TeX packages declared by the source. Build status during packaging: **pass**. A regenerated PDF is not a replacement for the historical released PDF.

Recorded build working directory / 已核验编译目录: `latex-parent`. The helper applies this automatically.

## Reproduction programs and proof / 程序与证明

Run programs from the `source/` directory unless their original instructions specify a subdirectory. Inspect their arguments first: discovery searches and full certificates can be long-running. Prefer a disposable copy; original programs may regenerate result files.

- `evidence/computation/constant_term_mod16.py`
- `evidence/computation/h_identity_mod16.py`
- `evidence/computation/projection_term_audit.py`
- `evidence/computation/source_formula_mod16.py`

Bounded replay status in this packaging task: **not-rerun**. Not rerun means archived but not re-executed here; it does not mean the historical proof failed. A short test does not certify assertions outside its encoded finite range.



## Dependencies and limitations / 依赖与限制

- numpy

- Asset selection is a packaging recommendation, not a rerun of the proof or citation audit.
- Do not copy external literature PDFs, downloaded web pages, third-party archives, jobs, logs, prompts, or private operational metadata.
- Review absolute paths and third-party attribution markers before publishing. Import names are inferred dependencies, not a tested environment lock.
- The original question is unresolved; the released artifact is a partial result or unproved conjecture, according to its frozen claim.

`package.json` records every distributed scientific input, its original relative path, digest, and compression. External literature, account/configuration files, agent transcripts, installed environments and unrelated third-party binaries are not included. Bibliographic references remain in the LaTeX sources.
