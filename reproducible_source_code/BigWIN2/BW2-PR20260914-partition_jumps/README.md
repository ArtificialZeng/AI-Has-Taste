# BW2-PR20260914-partition_jumps — Sharp local-dimension jumps and degree-jump growth in the partition graph

[Final PDF / 最终稿](../../../pdfs/BigWIN2/BW2-PR20260914-partition_jumps_Sharp_local_dimension_jumps_and_degree_jump_growth_in_the_partition_graph.pdf) · [LaTeX entry / 入口](source/manuscript/main.tex) · [Sources, data and proof / 复现材料](source/) · [Gate records / 历史门控](../../../assets/BigWIN2/gates/BW2-PR20260914-partition_jumps/)

Original ID / 原始编号: `primary-20260914-partition-jumps`. Origin / 来源: primary.

## Accepted scope / 已接受范围

Partial-result note; parent problem not fully solved / 部分结果札记；母题未完整解决.

For the simple undirected unit-transfer graph on all integer partitions of n defined in source.md and problem.md, with d the degree and delta the largest clique containing a vertex minus one: for every integer n&gt;=2, D_delta(n) is 0 for n=2,3, is 1 for 4&lt;=n&lt;=10 and n=12,13, and is 2 for n=11 and all n&gt;=14. For every integer n&gt;=10, put T_s=s(s+1)/2 and choose the unique s with T_s&lt;=n&lt;T_(s+1). Then 4s-8&lt;=D_d(n)&lt;=4s+2, and consequently D_d(n)=4sqrt(2n)+O(1) with an absolute error bound as n tends to infinity. Lower witnesses exist for every n in the claimed ranges. Also orient any edge lambda-&gt;mu toward nondecreasing support and let k=r(mu)-r(lambda). Define H(v) to mean that some positive size x&gt;=2 occurs at least twice in v while x-1 is absent. The edge has absolute dimension jump two if and only if either k=1, lambda is neither a staircase nor H and mu is H, or k=2 and both endpoints are H. The separate qualitative localization question in source Problem 8.2 is not asserted resolved; no exact formula for D_d beyond these bounds is asserted.

The unchanged PDF retains its original authorship. This package reuses historical independent review and release evidence; it is not a new mathematical audit, journal acceptance, or a claim about a wider parent problem.

PDF保持原始字节及署名。本次核对配套文件，不重新审稿，不将部分结果或猜想包装成原题全解。

## Restore exact inputs / 还原精确输入

From this package directory / 在当前包目录执行:

```sh
python3 ../prepare.py --restore BW2-PR20260914-partition_jumps
```

No large input needs restoration.

Restoration verifies stored and original digests and refuses to overwrite modified data. Large restored files are excluded from Git; compressed copies are the distributed originals.

## Rebuild the manuscript / 重编译

```sh
python3 ../build.py BW2-PR20260914-partition_jumps
```

The helper uses a disposable copy and retains build output outside the archive. Requires `latexmk` and the TeX packages declared by the source. Build status during packaging: **pass**. A regenerated PDF is not a replacement for the historical released PDF.

Recorded build working directory / 已核验编译目录: `latex-parent`. The helper applies this automatically.

## Reproduction programs and proof / 程序与证明

Run programs from the `source/` directory unless their original instructions specify a subdirectory. Inspect their arguments first: discovery searches and full certificates can be long-running. Prefer a disposable copy; original programs may regenerate result files.

- `evidence/research_check.py`
- `evidence/triage_check.py`

Bounded replay status in this packaging task: **not-rerun**. Not rerun means archived but not re-executed here; it does not mean the historical proof failed. A short test does not certify assertions outside its encoded finite range.



## Dependencies and limitations / 依赖与限制

- No third-party Python import detected by static inspection; this is not a tested environment lock.

- Asset selection is a packaging recommendation, not a rerun of the proof or citation audit.
- Do not copy external literature PDFs, downloaded web pages, third-party archives, jobs, logs, prompts, or private operational metadata.
- Review absolute paths and third-party attribution markers before publishing. Import names are inferred dependencies, not a tested environment lock.
- The original question is unresolved; the released artifact is a partial result or unproved conjecture, according to its frozen claim.
- External reference literature is not redistributed. Consult the bibliography and archived source URLs.

`package.json` records every distributed scientific input, its original relative path, digest, and compression. External literature, account/configuration files, agent transcripts, installed environments and unrelated third-party binaries are not included. Bibliographic references remain in the LaTeX sources.
