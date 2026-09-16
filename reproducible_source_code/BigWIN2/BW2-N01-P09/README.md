# BW2-N01-P09 — The associative-commutative spectrum of SC229

[Final PDF / 最终稿](../../../pdfs/BigWIN2/BW2-N01-P09_The_associative_commutative_spectrum_of_SC229.pdf) · [LaTeX entry / 入口](source/manuscript/main.tex) · [Sources, data and proof / 复现材料](source/) · [Gate records / 历史门控](../../../assets/BigWIN2/gates/BW2-N01-P09/)

Original ID / 原始编号: `newwin-00001-p09`. Origin / 来源: 新WIN-1批次.

## Accepted scope / 已接受范围

Resolution of the frozen statement · proved / 冻结命题的证明／反证（见精确范围） · proved.

For A={0,1,2} with operation table rows (0,0,0), (1,0,1), (1,1,1), and every finite nonempty fixed label set I, two full linear binary terms on I (each variable once, arbitrary order, no constants) induce the same function A^I -&gt; A if and only if their leftmost-decomposition trees agree as rooted labelled trees with exactly one distinguished child at each nonleaf and all other children unordered. Every such decorated tree is realised. Hence for every n&gt;=1 the number c_n of these term functions is (n-1)! times the sum, for k=0,...,n-1, of binom(n,k) k^(n-1-k)/(n-1-k)!, with 0^0=1. Equivalently T(x)=sum_{n&gt;=1}c_n x^n/n! satisfies T=x(1+T exp(T)); a direct integer recurrence and a function-only recursive decoder are supplied. This resolves the exact all-n counting question in source.md at its frozen interpretation in problem.md.

The unchanged PDF retains its original authorship. This package reuses historical independent review and release evidence; it is not a new mathematical audit, journal acceptance, or a claim about a wider parent problem.

PDF保持原始字节及署名。本次核对配套文件，不重新审稿，不将部分结果或猜想包装成原题全解。

## Restore exact inputs / 还原精确输入

From this package directory / 在当前包目录执行:

```sh
python3 ../prepare.py --restore BW2-N01-P09
```

No large input needs restoration.

Restoration verifies stored and original digests and refuses to overwrite modified data. Large restored files are excluded from Git; compressed copies are the distributed originals.

## Rebuild the manuscript / 重编译

```sh
python3 ../build.py BW2-N01-P09
```

The helper uses a disposable copy and retains build output outside the archive. Requires `latexmk` and the TeX packages declared by the source. Build status during packaging: **pass**. A regenerated PDF is not a replacement for the historical released PDF.

Recorded build working directory / 已核验编译目录: `latex-parent`. The helper applies this automatically.

## Reproduction programs and proof / 程序与证明

Run programs from the `source/` directory unless their original instructions specify a subdirectory. Inspect their arguments first: discovery searches and full certificates can be long-running. Prefer a disposable copy; original programs may regenerate result files.

- `evidence/check-p09-small.py`
- `evidence/decoder-check.py`
- `evidence/triage-check.py`

Bounded replay status in this packaging task: **not-rerun**. Not rerun means archived but not re-executed here; it does not mean the historical proof failed. A short test does not certify assertions outside its encoded finite range.



## Dependencies and limitations / 依赖与限制

- No third-party Python import detected by static inspection; this is not a tested environment lock.

- Asset selection is a packaging recommendation, not a rerun of the proof or citation audit.
- Do not copy external literature PDFs, downloaded web pages, third-party archives, jobs, logs, prompts, or private operational metadata.
- Review absolute paths and third-party attribution markers before publishing. Import names are inferred dependencies, not a tested environment lock.
- {'path': '/home/ailab/4math-open-problems/projects/newwin-00001-p09/manuscript/main.tex', 'indicators': ['third-party-attribution-or-license-marker']}
- External reference literature is not redistributed. Consult the bibliography and archived source URLs.

`package.json` records every distributed scientific input, its original relative path, digest, and compression. External literature, account/configuration files, agent transcripts, installed environments and unrelated third-party binaries are not included. Bibliographic references remain in the LaTeX sources.
