# BW2-PR20260914-vishnyakova_shifts — Interval shape and endpoint collisions for totally positive shifted even powers

[Final PDF / 最终稿](../../../pdfs/BigWIN2/BW2-PR20260914-vishnyakova_shifts_Interval_shape_and_endpoint_collisions_for_totally_positive_shifted_even_powers.pdf) · [LaTeX entry / 入口](source/manuscript/main.tex) · [Sources, data and proof / 复现材料](source/) · [Gate records / 历史门控](../../../assets/BigWIN2/gates/BW2-PR20260914-vishnyakova_shifts/)

Original ID / 原始编号: `primary-20260914-vishnyakova-shifts`. Origin / 来源: primary.

## Accepted scope / 已接受范围

Partial-result note; parent problem not fully solved / 部分结果札记；母题未完整解决.

For every even integer n&gt;=2, for the sets M_n defined verbatim in source.md and precisely in problem.md, there exists c_n with M_n=\[-c_n,1+c_n\] and (sqrt(2)-1)/2&lt;=c_n&lt;1-1/sqrt(2). At t=-c_n, Q_(n,t) has exactly one double zero r in (-1,0), all other zeros are simple and smaller than r, partial_z^2 Q_(n,t)(r)&gt;0, and partial_t Q_(n,t)(r)&lt;0; the other endpoint has the reflected configuration. The proof establishes the following operator theorem: if -3/10&lt;=t&lt;0, h has even degree d&gt;=2, positive leading coefficient, and d simple zeros in (-1,0), S=h'(0)/h(0), delta=(1+2t)/(1+t)^2, and 0&lt;lambda&lt;=1/(S+delta), then T_t^2\[(z-lambda)h\] has d+2 simple zeros in (-1,0) and one simple positive zero, where T_t p=z(1+z)p'+(z+t)p. Equality in the lambda bound is included. Consequently every odd Q_(m,t), m&gt;=1, has m-1 simple zeros in (-1,0) and one simple positive zero for -3/10&lt;=t&lt;0. The original successive-nesting assertion c_n&lt;=c_(n+2) is not claimed and remains unresolved.

The unchanged PDF retains its original authorship. This package reuses historical independent review and release evidence; it is not a new mathematical audit, journal acceptance, or a claim about a wider parent problem.

PDF保持原始字节及署名。本次核对配套文件，不重新审稿，不将部分结果或猜想包装成原题全解。

## Restore exact inputs / 还原精确输入

From this package directory / 在当前包目录执行:

```sh
python3 ../prepare.py --restore BW2-PR20260914-vishnyakova_shifts
```

No large input needs restoration.

Restoration verifies stored and original digests and refuses to overwrite modified data. Large restored files are excluded from Git; compressed copies are the distributed originals.

## Rebuild the manuscript / 重编译

```sh
python3 ../build.py BW2-PR20260914-vishnyakova_shifts
```

The helper uses a disposable copy and retains build output outside the archive. Requires `latexmk` and the TeX packages declared by the source. Build status during packaging: **pass**. A regenerated PDF is not a replacement for the historical released PDF.

Recorded build working directory / 已核验编译目录: `latex-parent`. The helper applies this automatically.

## Reproduction programs and proof / 程序与证明

Run programs from the `source/` directory unless their original instructions specify a subdirectory. Inspect their arguments first: discovery searches and full certificates can be long-running. Prefer a disposable copy; original programs may regenerate result files.

- `evidence/intake-calibration.py`
- `evidence/lemma-l-check.py`
- `evidence/lemma-l-discovery.py`
- `evidence/odd-strip.py`
- `evidence/sextic-collision.py`
- `evidence/triage-exact.py`
- `evidence/two-step-pass-2.py`
- `evidence/two-step-sturm-check.py`

Bounded replay status in this packaging task: **not-rerun**. Not rerun means archived but not re-executed here; it does not mean the historical proof failed. A short test does not certify assertions outside its encoded finite range.



## Dependencies and limitations / 依赖与限制

- numpy
- scipy
- sympy

- Asset selection is a packaging recommendation, not a rerun of the proof or citation audit.
- Do not copy external literature PDFs, downloaded web pages, third-party archives, jobs, logs, prompts, or private operational metadata.
- Review absolute paths and third-party attribution markers before publishing. Import names are inferred dependencies, not a tested environment lock.
- The original question is unresolved; the released artifact is a partial result or unproved conjecture, according to its frozen claim.
- External reference literature is not redistributed. Consult the bibliography and archived source URLs.

`package.json` records every distributed scientific input, its original relative path, digest, and compression. External literature, account/configuration files, agent transcripts, installed environments and unrelated third-party binaries are not included. Bibliographic references remain in the LaTeX sources.
