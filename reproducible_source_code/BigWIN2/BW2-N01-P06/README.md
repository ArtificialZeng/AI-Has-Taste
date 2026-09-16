# BW2-N01-P06 — A first counterexample to the Archer-Bourne recurrence for the avoidance chain (312,54321:132)

[Final PDF / 最终稿](../../../pdfs/BigWIN2/BW2-N01-P06_A_first_counterexample_to_the_Archer_Bourne_recurrence_for_the_avoidance_chain_312_54321_132.pdf) · [LaTeX entry / 入口](source/manuscript/main.tex) · [Sources, data and proof / 复现材料](source/) · [Gate records / 历史门控](../../../assets/BigWIN2/gates/BW2-N01-P06/)

Original ID / 原始编号: `newwin-00001-p06`. Origin / 来源: 新WIN-1批次.

## Accepted scope / 已接受范围

Resolution of the frozen statement · disproved / 冻结命题的证明／反证（见精确范围） · disproved.

Let C_n be the permutations pi in S_n avoiding the classical subsequence patterns 312 and 54321 such that the composition square pi^2 avoids 132, and let a_n=&#124;C_n&#124; with a_0=1. Then (a_0,...,a_11)=(1,1,2,5,11,22,45,89,174,338,655,1265). The recurrence a_n=a_(n-1)+a_(n-2)+a_(n-3)+a_(n-4)+n-1 holds for 6&lt;=n&lt;=10 and first fails at n=11, where its right-hand side is 1266 instead of 1265. Thus the universally quantified original claim is false. The computer-assisted proof uses the complete nine-member classification of C_11 permutations ending in 1, the exact endpoint census through 11, and a proved direct-sum reduction; it makes no claim about a corrected all-n recurrence.

The unchanged PDF retains its original authorship. This package reuses historical independent review and release evidence; it is not a new mathematical audit, journal acceptance, or a claim about a wider parent problem.

PDF保持原始字节及署名。本次核对配套文件，不重新审稿，不将部分结果或猜想包装成原题全解。

## Restore exact inputs / 还原精确输入

From this package directory / 在当前包目录执行:

```sh
python3 ../prepare.py --restore BW2-N01-P06
```

No large input needs restoration.

Restoration verifies stored and original digests and refuses to overwrite modified data. Large restored files are excluded from Git; compressed copies are the distributed originals.

## Rebuild the manuscript / 重编译

```sh
python3 ../build.py BW2-N01-P06
```

The helper uses a disposable copy and retains build output outside the archive. Requires `latexmk` and the TeX packages declared by the source. Build status during packaging: **pass**. A regenerated PDF is not a replacement for the historical released PDF.

Recorded build working directory / 已核验编译目录: `latex-parent`. The helper applies this automatically.

## Reproduction programs and proof / 程序与证明

Run programs from the `source/` directory unless their original instructions specify a subdirectory. Inspect their arguments first: discovery searches and full certificates can be long-running. Prefer a disposable copy; original programs may regenerate result files.

- `evidence/bruteforce.cpp`
- `evidence/compare_enumerations.py`
- `evidence/endpoint_exhaustive.py`
- `evidence/insertion_verify.py`
- `evidence/triage_count.py`
- `evidence/verify_endpoint_certificate.py`

Bounded replay status in this packaging task: **not-rerun**. Not rerun means archived but not re-executed here; it does not mean the historical proof failed. A short test does not certify assertions outside its encoded finite range.



## Dependencies and limitations / 依赖与限制

- No third-party Python import detected by static inspection; this is not a tested environment lock.

- Asset selection is a packaging recommendation, not a rerun of the proof or citation audit.
- Do not copy external literature PDFs, downloaded web pages, third-party archives, jobs, logs, prompts, or private operational metadata.
- Review absolute paths and third-party attribution markers before publishing. Import names are inferred dependencies, not a tested environment lock.
- {'path': '/home/ailab/4math-open-problems/projects/newwin-00001-p06/evidence/endpoint_certificate_verification.json', 'indicators': ['absolute-local-path']}
- {'path': '/home/ailab/4math-open-problems/projects/newwin-00001-p06/evidence/registry_screen.json', 'indicators': ['absolute-local-path']}
- External reference literature is not redistributed. Consult the bibliography and archived source URLs.

`package.json` records every distributed scientific input, its original relative path, digest, and compression. External literature, account/configuration files, agent transcripts, installed environments and unrelated third-party binaries are not included. Bibliographic references remain in the LaTeX sources.
