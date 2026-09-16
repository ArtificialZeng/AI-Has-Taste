# BW2-PR20260912-ray_west_j — A direct-sum law for the Ray–West correction and a statistic for separable permutations

[Final PDF / 最终稿](../../../pdfs/BigWIN2/BW2-PR20260912-ray_west_j_A_direct_sum_law_for_the_RayWest_correction_and_a_statistic_for_separable_permutations.pdf) · [LaTeX entry / 入口](source/manuscript/main.tex) · [Sources, data and proof / 复现材料](source/) · [Gate records / 历史门控](../../../assets/BigWIN2/gates/BW2-PR20260912-ray_west_j/)

Original ID / 原始编号: `primary-20260912-ray-west-j`. Origin / 来源: primary.

## Accepted scope / 已接受范围

Partial-result note; parent problem not fully solved / 部分结果札记；母题未完整解决.

For every nonempty alpha in S_a and beta in S_b, let j(p)=(m^4+2m^3+m^2+4m+4)/2-g_2(p) for m=&#124;p&#124;, and let T(alpha), H(beta) indicate a decreasing last, respectively first, sum-indecomposable component, including singletons. Then j(alpha direct-sum beta)=j(alpha)+j(beta)+T(alpha)H(beta). Internal Ray--West good gaps restrict exactly to the summands and the join is good exactly when T(alpha)H(beta)=1. Value complementation gives the skew-sum rule with increasing skew components. Consequently j on every separable permutation equals the sum over maximal decomposition-tree nodes of adjacent decreasing-child pairs at sum nodes and adjacent increasing-child pairs at skew nodes. Among sum-decomposable permutations j(p)=&#124;p&#124;-1 if and only if p is layered; among skew-decomposable permutations equality holds if and only if p is colayered. No full-scope formula or equality classification is claimed for permutations indecomposable in both senses.

The unchanged PDF retains its original authorship. This package reuses historical independent review and release evidence; it is not a new mathematical audit, journal acceptance, or a claim about a wider parent problem.

PDF保持原始字节及署名。本次核对配套文件，不重新审稿，不将部分结果或猜想包装成原题全解。

## Restore exact inputs / 还原精确输入

From this package directory / 在当前包目录执行:

```sh
python3 ../prepare.py --restore BW2-PR20260912-ray_west_j
```

No large input needs restoration.

Restoration verifies stored and original digests and refuses to overwrite modified data. Large restored files are excluded from Git; compressed copies are the distributed originals.

## Rebuild the manuscript / 重编译

```sh
python3 ../build.py BW2-PR20260912-ray_west_j
```

The helper uses a disposable copy and retains build output outside the archive. Requires `latexmk` and the TeX packages declared by the source. Build status during packaging: **pass**. A regenerated PDF is not a replacement for the historical released PDF.

Recorded build working directory / 已核验编译目录: `latex-parent`. The helper applies this automatically.

## Reproduction programs and proof / 程序与证明

Run programs from the `source/` directory unless their original instructions specify a subdirectory. Inspect their arguments first: discovery searches and full certificates can be long-running. Prefer a disposable copy; original programs may regenerate result files.

- `evidence/inspect_active_pairs.py`
- `evidence/separable_statistic.py`
- `evidence/test_extremal.py`
- `evidence/test_gap_deletion.py`
- `evidence/test_length8.py`
- `evidence/test_length9.py`
- `evidence/test_statistics.py`
- `evidence/test_sum_gaps.py`
- `evidence/test_sum_rule.py`
- `evidence/verify_structural.py`
- `evidence/verify_sum_restriction.py`

Bounded replay status in this packaging task: **not-rerun**. Not rerun means archived but not re-executed here; it does not mean the historical proof failed. A short test does not certify assertions outside its encoded finite range.



## Dependencies and limitations / 依赖与限制

- numba
- numpy

- Asset selection is a packaging recommendation, not a rerun of the proof or citation audit.
- Do not copy external literature PDFs, downloaded web pages, third-party archives, jobs, logs, prompts, or private operational metadata.
- Review absolute paths and third-party attribution markers before publishing. Import names are inferred dependencies, not a tested environment lock.
- The original question is unresolved; the released artifact is a partial result or unproved conjecture, according to its frozen claim.
- {'path': '/home/ailab/4math-open-problems/projects/primary-20260912-ray-west-j/evidence/registry-screen.json', 'indicators': ['absolute-local-path']}
- External reference literature is not redistributed. Consult the bibliography and archived source URLs.

`package.json` records every distributed scientific input, its original relative path, digest, and compression. External literature, account/configuration files, agent transcripts, installed environments and unrelated third-party binaries are not included. Bibliographic references remain in the LaTeX sources.
