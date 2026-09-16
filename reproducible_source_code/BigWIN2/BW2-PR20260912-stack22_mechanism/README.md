# BW2-PR20260912-stack22_mechanism — A direct first-return enumeration of (2,2)-stack-sortable permutations

[Final PDF / 最终稿](../../../pdfs/BigWIN2/BW2-PR20260912-stack22_mechanism_A_direct_first_return_enumeration_of_2_2_stack_sortable_permutations.pdf) · [LaTeX entry / 入口](source/manuscript/main.tex) · [Sources, data and proof / 复现材料](source/) · [Gate records / 历史门控](../../../assets/BigWIN2/gates/BW2-PR20260912-stack22_mechanism/)

Original ID / 原始编号: `primary-20260912-stack22-mechanism`. Origin / 来源: primary.

## Accepted scope / 已接受范围

Resolution of the frozen statement · proved / 冻结命题的证明／反证（见精确范围） · proved.

For every integer n&gt;=0, in the frozen (2,2)-stack input-sorting model of source.md and problem.md, the sortable permutations of \[n\] are in size-preserving bijection with the following canonical rank words: words with n pushes and n pops that start and end with an empty bit stack, obey P1: empty -&gt; 0 and aT -&gt; 1aT; P2: aT -&gt; 10T; Q1: aT -&gt; T; Q2: 0bT -&gt; 0T, where a,b are bits and T is any suffix, and avoid the adjacent factor P2 Q1. Token labeling by increasing pop order reconstructs the unique input. The complete unambiguous first-return specification proved in evidence/first_return_proof.md derives F=1+xAF and A=1+xA(4A-2F-1) directly from these operations. Hence the ordinary generating function F(x)=sum_{n&gt;=0}u_n x^n, with each sortable input counted once and F(0)=1, is the unique such formal series satisfying 2xF^3-(2x+3)F^2-(x-7)F-4=0. This supplies the requested mechanism-level derivation for all n, without using the forbidden pattern basis or presupposing the polynomial.

The unchanged PDF retains its original authorship. This package reuses historical independent review and release evidence; it is not a new mathematical audit, journal acceptance, or a claim about a wider parent problem.

PDF保持原始字节及署名。本次核对配套文件，不重新审稿，不将部分结果或猜想包装成原题全解。

## Restore exact inputs / 还原精确输入

From this package directory / 在当前包目录执行:

```sh
python3 ../prepare.py --restore BW2-PR20260912-stack22_mechanism
```

No large input needs restoration.

Restoration verifies stored and original digests and refuses to overwrite modified data. Large restored files are excluded from Git; compressed copies are the distributed originals.

## Rebuild the manuscript / 重编译

```sh
python3 ../build.py BW2-PR20260912-stack22_mechanism
```

The helper uses a disposable copy and retains build output outside the archive. Requires `latexmk` and the TeX packages declared by the source. Build status during packaging: **pass**. A regenerated PDF is not a replacement for the historical released PDF.

Recorded build working directory / 已核验编译目录: `latex-parent`. The helper applies this automatically.

## Reproduction programs and proof / 程序与证明

Run programs from the `source/` directory unless their original instructions specify a subdirectory. Inspect their arguments first: discovery searches and full certificates can be long-running. Prefer a disposable copy; original programs may regenerate result files.

- `evidence/first_return_algebra.py`
- `evidence/first_return_exact.py`
- `evidence/first_return_grammar.py`
- `evidence/first_return_holdout.py`
- `evidence/triage_exact.py`

Bounded replay status in this packaging task: **not-rerun**. Not rerun means archived but not re-executed here; it does not mean the historical proof failed. A short test does not certify assertions outside its encoded finite range.



## Dependencies and limitations / 依赖与限制

- sympy

- Asset selection is a packaging recommendation, not a rerun of the proof or citation audit.
- Do not copy external literature PDFs, downloaded web pages, third-party archives, jobs, logs, prompts, or private operational metadata.
- Review absolute paths and third-party attribution markers before publishing. Import names are inferred dependencies, not a tested environment lock.
- {'path': '/home/ailab/4math-open-problems/projects/primary-20260912-stack22-mechanism/manuscript/references.bib', 'indicators': ['absolute-local-path']}
- {'path': '/home/ailab/4math-open-problems/projects/primary-20260912-stack22-mechanism/manuscript/build/main.bbl', 'indicators': ['absolute-local-path']}
- External reference literature is not redistributed. Consult the bibliography and archived source URLs.

`package.json` records every distributed scientific input, its original relative path, digest, and compression. External literature, account/configuration files, agent transcripts, installed environments and unrelated third-party binaries are not included. Bibliographic references remain in the LaTeX sources.
