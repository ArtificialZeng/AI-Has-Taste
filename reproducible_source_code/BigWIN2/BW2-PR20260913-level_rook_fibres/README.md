# BW2-PR20260913-level_rook_fibres — Polynomial-time counting of two-level transpose fibres

[Final PDF / 最终稿](../../../pdfs/BigWIN2/BW2-PR20260913-level_rook_fibres_Polynomial_time_counting_of_two_level_transpose_fibres.pdf) · [LaTeX entry / 入口](source/manuscript/main.tex) · [Sources, data and proof / 复现材料](source/) · [Gate records / 历史门控](../../../assets/BigWIN2/gates/BW2-PR20260913-level_rook_fibres/)

Original ID / 原始编号: `primary-20260913-level-rook-fibres`. Origin / 来源: primary.

## Accepted scope / 已接受范围

Partial-result note; parent problem not fully solved / 部分结果札记；母题未完整解决.

For every finite weakly increasing sequence C=(c_1,...,c_t) of positive integers that is 2-singleton (no repeated odd height), the number F_2(C) of Ferrers shapes B with l_2(B)=C, with leading zero columns identified and preimage width unrestricted, is computable in time polynomial in the binary input length log(t+1)+sum_i log(c_i+1). The empty target has count 1. For t&gt;=1, put s_i=c_(t+1-i), s_(t+1)=0 and a_i=floor(s_i/2)-ceil(s_(i+1)/2). There is an explicit bijection between the fibre and integer vectors d&gt;=0 satisfying d_i+d_(i+1)&lt;=a_i for i&lt;t and d_t&lt;=a_t. More generally, for every nonnegative integer vector a of length t&gt;=1, with A=max_i a_i, the proposed exact algorithm counts these vectors in O(t^4) integer arithmetic operations on O(t log(A+t+2))-bit integers and O(t^2) stored integers. Thus O(t^6 log^2(A+t+2)) elementary bit operations suffice. Its layer-i count function has at most i integer-interval polynomial pieces of degree at most i-1. The claim is restricted to m=2 and does not resolve the original arbitrary-m problem.

The unchanged PDF retains its original authorship. This package reuses historical independent review and release evidence; it is not a new mathematical audit, journal acceptance, or a claim about a wider parent problem.

PDF保持原始字节及署名。本次核对配套文件，不重新审稿，不将部分结果或猜想包装成原题全解。

## Restore exact inputs / 还原精确输入

From this package directory / 在当前包目录执行:

```sh
python3 ../prepare.py --restore BW2-PR20260913-level_rook_fibres
```

No large input needs restoration.

Restoration verifies stored and original digests and refuses to overwrite modified data. Large restored files are excluded from Git; compressed copies are the distributed originals.

## Rebuild the manuscript / 重编译

```sh
python3 ../build.py BW2-PR20260913-level_rook_fibres
```

The helper uses a disposable copy and retains build output outside the archive. Requires `latexmk` and the TeX packages declared by the source. Build status during packaging: **pass**. A regenerated PDF is not a replacement for the historical released PDF.

Recorded build working directory / 已核验编译目录: `latex-parent`. The helper applies this automatically.

## Reproduction programs and proof / 程序与证明

Run programs from the `source/` directory unless their original instructions specify a subdirectory. Inspect their arguments first: discovery searches and full certificates can be long-running. Prefer a disposable copy; original programs may regenerate result files.

- `evidence/m2-compressed-check.py`
- `evidence/m2-compressed.py`
- `evidence/m2-path-check.py`

Bounded replay status in this packaging task: **not-rerun**. Not rerun means archived but not re-executed here; it does not mean the historical proof failed. A short test does not certify assertions outside its encoded finite range.



## Dependencies and limitations / 依赖与限制

- No third-party Python import detected by static inspection; this is not a tested environment lock.

- Asset selection is a packaging recommendation, not a rerun of the proof or citation audit.
- Do not copy external literature PDFs, downloaded web pages, third-party archives, jobs, logs, prompts, or private operational metadata.
- Review absolute paths and third-party attribution markers before publishing. Import names are inferred dependencies, not a tested environment lock.
- The original question is unresolved; the released artifact is a partial result or unproved conjecture, according to its frozen claim.
- {'path': '/home/ailab/4math-open-problems/projects/primary-20260913-level-rook-fibres/evidence/triage-registry-check.json', 'indicators': ['absolute-local-path']}
- External reference literature is not redistributed. Consult the bibliography and archived source URLs.

`package.json` records every distributed scientific input, its original relative path, digest, and compression. External literature, account/configuration files, agent transcripts, installed environments and unrelated third-party binaries are not included. Bibliographic references remain in the LaTeX sources.
