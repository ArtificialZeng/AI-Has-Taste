# BW2-N01-P05 — Maximal sorting time under clumped-letter insertion in two short multiplicity profiles

[Final PDF / 最终稿](../../../pdfs/BigWIN2/BW2-N01-P05_Maximal_sorting_time_under_clumped_letter_insertion_in_two_short_multiplicity_profiles.pdf) · [LaTeX entry / 入口](source/manuscript/main.tex) · [Sources, data and proof / 复现材料](source/) · [Gate records / 历史门控](../../../assets/BigWIN2/gates/BW2-N01-P05/)

Original ID / 原始编号: `newwin-00001-p05`. Origin / 来源: 新WIN-1批次.

## Accepted scope / 已接受范围

Partial-result note; parent problem not fully solved / 部分结果札记；母题未完整解决.

Let phi be the greedy aba-avoiding stack map, and let T be its sorting time. For every integer r&gt;=3, let q be any word using exactly r letters, each occurring twice except that at most one letter may occur three times. Let W be any word whose deletion of a set A of additional letters equals q, with every letter of A occurring in one contiguous nonempty block in W. There is no bound on &#124;A&#124; or on those block multiplicities. Then T(W)=r if and only if T(q)=r. The proof uses a complete 28,800-input computer-assisted base at r=3 and induction on r. In particular, for every run-free q on r&gt;=3 letters, each occurring at least twice, with 2r&lt;=&#124;q&#124;&lt;=2r+1, and every new terminal letter x, T(qx)=r iff T(q)=r. This proves the original first-letter deletion bridge for k&gt;=4; it does not provide the requested complete uniform classification or enumeration M_k of length-2k+2 inputs.

The unchanged PDF retains its original authorship. This package reuses historical independent review and release evidence; it is not a new mathematical audit, journal acceptance, or a claim about a wider parent problem.

PDF保持原始字节及署名。本次核对配套文件，不重新审稿，不将部分结果或猜想包装成原题全解。

## Restore exact inputs / 还原精确输入

From this package directory / 在当前包目录执行:

```sh
python3 ../prepare.py --restore BW2-N01-P05
```

No large input needs restoration.

Restoration verifies stored and original digests and refuses to overwrite modified data. Large restored files are excluded from Git; compressed copies are the distributed originals.

## Rebuild the manuscript / 重编译

```sh
python3 ../build.py BW2-N01-P05
```

The helper uses a disposable copy and retains build output outside the archive. Requires `latexmk` and the TeX packages declared by the source. Build status during packaging: **pass**. A regenerated PDF is not a replacement for the historical released PDF.

Recorded build working directory / 已核验编译目录: `latex-parent`. The helper applies this automatically.

## Reproduction programs and proof / 程序与证明

Run programs from the `source/` directory unless their original instructions specify a subdirectory. Inspect their arguments first: discovery searches and full certificates can be long-running. Prefer a disposable copy; original programs may regenerate result files.

- `evidence/b2-search.py`
- `evidence/b2-validation.py`
- `evidence/check-p05-small.py`
- `evidence/clumped-marker-base.py`
- `evidence/clumped-marker-heldout.py`
- `evidence/inverse-census.py`
- `evidence/research-pass1.py`
- `evidence/research-validation.py`
- `evidence/terminal-marker.py`
- `evidence/triage-recheck.py`
- `evidence/two-double-marker.py`

Bounded replay status in this packaging task: **not-rerun**. Not rerun means archived but not re-executed here; it does not mean the historical proof failed. A short test does not certify assertions outside its encoded finite range.



## Dependencies and limitations / 依赖与限制

- numba
- numpy

- Asset selection is a packaging recommendation, not a rerun of the proof or citation audit.
- Do not copy external literature PDFs, downloaded web pages, third-party archives, jobs, logs, prompts, or private operational metadata.
- Review absolute paths and third-party attribution markers before publishing. Import names are inferred dependencies, not a tested environment lock.
- The original question is unresolved; the released artifact is a partial result or unproved conjecture, according to its frozen claim.
- External reference literature is not redistributed. Consult the bibliography and archived source URLs.

`package.json` records every distributed scientific input, its original relative path, digest, and compression. External literature, account/configuration files, agent transcripts, installed environments and unrelated third-party binaries are not included. Bibliographic references remain in the LaTeX sources.
