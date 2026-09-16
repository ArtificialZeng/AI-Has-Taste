# BW2-PR20260914-comb_inverse — A compositional inverse for the support polynomials of comb preorder polytopes

[Final PDF / 最终稿](../../../pdfs/BigWIN2/BW2-PR20260914-comb_inverse_A_compositional_inverse_for_the_support_polynomials_of_comb_preorder_polytopes.pdf) · [LaTeX entry / 入口](source/manuscript/main.tex) · [Sources, data and proof / 复现材料](source/) · [Gate records / 历史门控](../../../assets/BigWIN2/gates/BW2-PR20260914-comb_inverse/)

Original ID / 原始编号: `primary-20260914-comb-inverse`. Origin / 来源: primary.

## Accepted scope / 已接受范围

Resolution of the frozen statement · proved / 冻结命题的证明／反证（见精确范围） · proved.

Let tau_0 be empty, and for every integer n&gt;=0 obtain tau_(n+1) by taking the disjoint union of tau_n with a singleton and then adjoining a new minimum. Let Q_n consist of the nonnegative real vectors on the 2n vertices satisfying sum_(v in I) x_v &lt;= &#124;I&#124; for every lower ideal I of tau_n, and let h_n(t)=sum_(a in Q_n intersect Z^(2n)) t^(number of positive coordinates of a), with h_0(t)=1. For an indeterminate t, define F(t,x)=sum_(n&gt;=0) t^(-n) h_n(t) x^(n+1) and R(t,x)=sum_(m&gt;=1) (-1)^(m-1) \[1+(1+t)^m t^(1-m) sum_(j=0)^(m-2) t^j\] x^m, where the inner sum is zero for m=1. Then R(t,F(t,x))=x=F(t,R(t,x)) in Q(t)\[\[x\]\]. Equivalently, the same R is x/\[(1+x)(1+(1+t)x)(1+(1+t)x/t)\] and is the compositional inverse of the full support-refined comb generating series. This is the entire identity frozen in source.md, with no restriction to a finite range or scalar specialization of t.

The unchanged PDF retains its original authorship. This package reuses historical independent review and release evidence; it is not a new mathematical audit, journal acceptance, or a claim about a wider parent problem.

PDF保持原始字节及署名。本次核对配套文件，不重新审稿，不将部分结果或猜想包装成原题全解。

## Restore exact inputs / 还原精确输入

From this package directory / 在当前包目录执行:

```sh
python3 ../prepare.py --restore BW2-PR20260914-comb_inverse
```

No large input needs restoration.

Restoration verifies stored and original digests and refuses to overwrite modified data. Large restored files are excluded from Git; compressed copies are the distributed originals.

## Rebuild the manuscript / 重编译

```sh
python3 ../build.py BW2-PR20260914-comb_inverse
```

The helper uses a disposable copy and retains build output outside the archive. Requires `latexmk` and the TeX packages declared by the source. Build status during packaging: **pass**. A regenerated PDF is not a replacement for the historical released PDF.

Recorded build working directory / 已核验编译目录: `latex-parent`. The helper applies this automatically.

## Reproduction programs and proof / 程序与证明

Run programs from the `source/` directory unless their original instructions specify a subdirectory. Inspect their arguments first: discovery searches and full certificates can be long-running. Prefer a disposable copy; original programs may regenerate result files.

- `evidence/intake-calibration.py`
- `evidence/research-forest-check.py`
- `evidence/triage-prefix-check.py`

Bounded replay status in this packaging task: **not-rerun**. Not rerun means archived but not re-executed here; it does not mean the historical proof failed. A short test does not certify assertions outside its encoded finite range.



## Dependencies and limitations / 依赖与限制

- No third-party Python import detected by static inspection; this is not a tested environment lock.

- Asset selection is a packaging recommendation, not a rerun of the proof or citation audit.
- Do not copy external literature PDFs, downloaded web pages, third-party archives, jobs, logs, prompts, or private operational metadata.
- Review absolute paths and third-party attribution markers before publishing. Import names are inferred dependencies, not a tested environment lock.
- External reference literature is not redistributed. Consult the bibliography and archived source URLs.

`package.json` records every distributed scientific input, its original relative path, digest, and compression. External literature, account/configuration files, agent transcripts, installed environments and unrelated third-party binaries are not included. Bibliographic references remain in the LaTeX sources.
