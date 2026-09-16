# BW2-B73-P01 — An Exact Exterior Abel-Power Square Function for a Single Atom in ℝ³

[Final PDF / 最终稿](../../../pdfs/BigWIN2/BW2-B73-P01_An_Exact_Exterior_Abel_Power_Square_Function_for_a_Single_Atom_in_R3.pdf) · [LaTeX entry / 入口](source/manuscript/main.tex) · [Sources, data and proof / 复现材料](source/) · [Gate records / 历史门控](../../../assets/BigWIN2/gates/BW2-B73-P01/)

Original ID / 原始编号: `win-00073-p01`. Origin / 来源: 73.

## Accepted scope / 已接受范围

Resolution of the frozen statement · proved / 冻结命题的证明／反证（见精确范围） · proved.

Under the Fourier convention f-hat(xi)=integral exp(-2 pi i x dot xi) f(x) dx, Delta=sum_j partial_j^2, H_t=exp(t Delta), A_s=s(s-Delta)^{-1}, and the cap-kappa radial partial-balayage domain Omega=B(0,R) with R^3=3m/(4 pi kappa), for every m&gt;0, kappa&gt;0, and integer N&gt;=1, the exterior square function I_N=integral_{Omega^c} integral_0^infinity &#124;s partial_s(A_s^N(m delta_0))(x)&#124;^2 ds/s dx equals kappa\*m\*2\*Gamma(N+3/2)^2/\[3\*pi\*(N+1)\*(N+2)\*(2\*N+1)\*Gamma(N)^2\]. Consequently I_N/(kappa\*m) tends to 1/(3\*pi) as N tends to infinity.

The unchanged PDF retains its original authorship. This package reuses historical independent review and release evidence; it is not a new mathematical audit, journal acceptance, or a claim about a wider parent problem.

PDF保持原始字节及署名。本次核对配套文件，不重新审稿，不将部分结果或猜想包装成原题全解。

## Restore exact inputs / 还原精确输入

From this package directory / 在当前包目录执行:

```sh
python3 ../prepare.py --restore BW2-B73-P01
```

No large input needs restoration.

Restoration verifies stored and original digests and refuses to overwrite modified data. Large restored files are excluded from Git; compressed copies are the distributed originals.

## Rebuild the manuscript / 重编译

```sh
python3 ../build.py BW2-B73-P01
```

The helper uses a disposable copy and retains build output outside the archive. Requires `latexmk` and the TeX packages declared by the source. Build status during packaging: **pass**. A regenerated PDF is not a replacement for the historical released PDF.

Recorded build working directory / 已核验编译目录: `latex-parent`. The helper applies this automatically.

## Reproduction programs and proof / 程序与证明

Run programs from the `source/` directory unless their original instructions specify a subdirectory. Inspect their arguments first: discovery searches and full certificates can be long-running. Prefer a disposable copy; original programs may regenerate result files.

- `evidence/check_exact_range.py`

Bounded replay status in this packaging task: **passed**. Not rerun means archived but not re-executed here; it does not mean the historical proof failed. A short test does not certify assertions outside its encoded finite range.

Exact Fraction polynomial-integral checks of the half-integer kernel constant for N=1..30.

## Dependencies and limitations / 依赖与限制

- No third-party Python import detected by static inspection; this is not a tested environment lock.

- Asset selection is a packaging recommendation, not a rerun of the proof or citation audit.
- Do not copy external literature PDFs, downloaded web pages, third-party archives, jobs, logs, prompts, or private operational metadata.
- Review absolute paths and third-party attribution markers before publishing. Import names are inferred dependencies, not a tested environment lock.

`package.json` records every distributed scientific input, its original relative path, digest, and compression. External literature, account/configuration files, agent transcripts, installed environments and unrelated third-party binaries are not included. Bibliographic references remain in the LaTeX sources.
