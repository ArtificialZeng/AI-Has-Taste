# BW2-B61-P04 — The Least Frobenius Alexander Quandle Isogeny-Detection Prime over F_5

[Final PDF / 最终稿](../../../pdfs/BigWIN2/BW2-B61-P04_The_Least_Frobenius_Alexander_Quandle_Isogeny_Detection_Prime_over_F_5.pdf) · [LaTeX entry / 入口](source/manuscript/main.tex) · [Sources, data and proof / 复现材料](source/) · [Gate records / 历史门控](../../../assets/BigWIN2/gates/BW2-B61-P04/)

Original ID / 原始编号: `win-00061-p04`. Origin / 来源: 61.

## Accepted scope / 已接受范围

Resolution of the frozen statement · proved / 冻结命题的证明／反证（见精确范围） · proved.

Using the Frobenius Alexander quandle convention and the quandle-isomorphism/Frobenius-similarity equivalence of arXiv:2609.02278v1, the least rational prime ell != 5 such that, uniformly for all elliptic curves A,B over F_5, isomorphic quandles Q(A\[ell\],pi_A,ell) and Q(B\[ell\],pi_B,ell) force A and B to be F_5-isogenous is ell=11. Uniform sufficiency holds at 11. The smaller eligible primes all fail: at ell=2 use y^2=x^3+3x and y^2=x^3+1; at ell=3 use y^2=x^3+3x+2 and y^2=x^3+4x; at ell=7 use y^2=x^3+3x and y^2=x^3+4x+2. In each pair the curves are nonsingular and nonisogenous, while their torsion Frobenius operators have the same explicitly certified rational canonical form.

The unchanged PDF retains its original authorship. This package reuses historical independent review and release evidence; it is not a new mathematical audit, journal acceptance, or a claim about a wider parent problem.

PDF保持原始字节及署名。本次核对配套文件，不重新审稿，不将部分结果或猜想包装成原题全解。

## Restore exact inputs / 还原精确输入

From this package directory / 在当前包目录执行:

```sh
python3 ../prepare.py --restore BW2-B61-P04
```

No large input needs restoration.

Restoration verifies stored and original digests and refuses to overwrite modified data. Large restored files are excluded from Git; compressed copies are the distributed originals.

## Rebuild the manuscript / 重编译

```sh
python3 ../build.py BW2-B61-P04
```

The helper uses a disposable copy and retains build output outside the archive. Requires `latexmk` and the TeX packages declared by the source. Build status during packaging: **pass**. A regenerated PDF is not a replacement for the historical released PDF.

Recorded build working directory / 已核验编译目录: `latex-parent`. The helper applies this automatically.

## Reproduction programs and proof / 程序与证明

Run programs from the `source/` directory unless their original instructions specify a subdirectory. Inspect their arguments first: discovery searches and full certificates can be long-running. Prefer a disposable copy; original programs may regenerate result files.

- `evidence/verify_certificates.py`

Bounded replay status in this packaging task: **not-rerun**. Not rerun means archived but not re-executed here; it does not mean the historical proof failed. A short test does not certify assertions outside its encoded finite range.



## Dependencies and limitations / 依赖与限制

- No third-party Python import detected by static inspection; this is not a tested environment lock.

- Asset selection is a packaging recommendation, not a rerun of the proof or citation audit.
- Do not copy external literature PDFs, downloaded web pages, third-party archives, jobs, logs, prompts, or private operational metadata.
- Review absolute paths and third-party attribution markers before publishing. Import names are inferred dependencies, not a tested environment lock.
- External reference literature is not redistributed. Consult the bibliography and archived source URLs.

`package.json` records every distributed scientific input, its original relative path, digest, and compression. External literature, account/configuration files, agent transcripts, installed environments and unrelated third-party binaries are not included. Bibliographic references remain in the LaTeX sources.
