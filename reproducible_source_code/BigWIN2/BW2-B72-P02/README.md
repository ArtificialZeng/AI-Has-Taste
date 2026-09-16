# BW2-B72-P02 — No Reversible Gray Representative in a Specified Orbit of a Length-34 Quaternary Legendre Pair

[Final PDF / 最终稿](../../../pdfs/BigWIN2/BW2-B72-P02_No_Reversible_Gray_Representative_in_a_Specified_Orbit_of_a_Length_34_Quaternary_Legendre_Pair.pdf) · [LaTeX entry / 入口](source/manuscript/main.tex) · [Sources, data and proof / 复现材料](source/) · [Gate records / 历史门控](../../../assets/BigWIN2/gates/BW2-B72-P02/)

Original ID / 原始编号: `win-00072-p02`. Origin / 来源: 72.

## Accepted scope / 已接受范围

Resolution of the frozen statement · disproved / 冻结命题的证明／反证（见精确范围） · disproved.

Let n=34; map digits 0,1,2,3 to 1,i,-1,-i; take A=2202202000022020222202000220200020 and B=1133303133112311101113211331303331; define (c_r X)_j=X_{j-r} and (d_k X)_j=X_{j k^{-1}} on Z_34; and let Gamma_34(A,B) be exactly the set of s^e(alpha c_r d_k(A^epsilon), beta c_t d_k(B^epsilon)) with alpha,beta in {1,i,-1,-i}, r,t in Z_34, k in Z_34^times, and epsilon,e in {0,1}. Then Gamma_34(A,B) contains no ordered pair whose four Gray rows all satisfy x_j=x_{-j} for every j in Z_34. This is only a conclusion about the displayed frozen Gamma_34, not about any larger qLP equivalence relation or other length-34 qLPs.

The unchanged PDF retains its original authorship. This package reuses historical independent review and release evidence; it is not a new mathematical audit, journal acceptance, or a claim about a wider parent problem.

PDF保持原始字节及署名。本次核对配套文件，不重新审稿，不将部分结果或猜想包装成原题全解。

## Restore exact inputs / 还原精确输入

From this package directory / 在当前包目录执行:

```sh
python3 ../prepare.py --restore BW2-B72-P02
```

No large input needs restoration.

Restoration verifies stored and original digests and refuses to overwrite modified data. Large restored files are excluded from Git; compressed copies are the distributed originals.

## Rebuild the manuscript / 重编译

```sh
python3 ../build.py BW2-B72-P02
```

The helper uses a disposable copy and retains build output outside the archive. Requires `latexmk` and the TeX packages declared by the source. Build status during packaging: **pass**. A regenerated PDF is not a replacement for the historical released PDF.

Recorded build working directory / 已核验编译目录: `latex-parent`. The helper applies this automatically.

## Reproduction programs and proof / 程序与证明

Run programs from the `source/` directory unless their original instructions specify a subdirectory. Inspect their arguments first: discovery searches and full certificates can be long-running. Prefer a disposable copy; original programs may regenerate result files.

- `evidence/orbit_census.py`
- `evidence/triage_check.py`
- `evidence/verify_orbit_census.py`

Bounded replay status in this packaging task: **not-rerun**. Not rerun means archived but not re-executed here; it does not mean the historical proof failed. A short test does not certify assertions outside its encoded finite range.



## Dependencies and limitations / 依赖与限制

- No third-party Python import detected by static inspection; this is not a tested environment lock.

- Asset selection is a packaging recommendation, not a rerun of the proof or citation audit.
- Do not copy external literature PDFs, downloaded web pages, third-party archives, jobs, logs, prompts, or private operational metadata.
- Review absolute paths and third-party attribution markers before publishing. Import names are inferred dependencies, not a tested environment lock.
- External reference literature is not redistributed. Consult the bibliography and archived source URLs.

`package.json` records every distributed scientific input, its original relative path, digest, and compression. External literature, account/configuration files, agent transcripts, installed environments and unrelated third-party binaries are not included. Bibliographic references remain in the LaTeX sources.
