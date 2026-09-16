# BW2-N01-P18 — Recurrent constant-term words for a degenerate Laurent polynomial

[Final PDF / 最终稿](../../../pdfs/BigWIN2/BW2-N01-P18_Recurrent_constant_term_words_for_a_degenerate_Laurent_polynomial.pdf) · [LaTeX entry / 入口](source/manuscript/main.tex) · [Sources, data and proof / 复现材料](source/) · [Gate records / 历史门控](../../../assets/BigWIN2/gates/BW2-N01-P18/)

Original ID / 原始编号: `newwin-00001-p18`. Origin / 来源: 新WIN-1批次.

## Accepted scope / 已接受范围

Resolution of the frozen statement · proved / 冻结命题的证明／反证（见精确范围） · proved.

For every prime p, set K=F_p and P(x)=x^(p-1)+x^(-1). For every Laurent polynomial Q in K\[x,x^(-1)\], define u_n=\[x^0\](P(x)^n Q(x)) for every integer n&gt;=0. Then the following are equivalent: (i) for every i&gt;=0, l&gt;=1, and N&gt;=0 there exists j&gt;N such that u_(j+k)=u_(i+k) for all integers 0&lt;=k&lt;l; (ii) u_n=0 for every n&gt;=0; (iii) Q=P F(P) for some polynomial F in K\[t\]. The condition in (iii) is the subspace P K\[P\], not the full Laurent-ring ideal. This covers all primes, including 2, zero Q, and arbitrary finite positive and negative Laurent exponents. It settles source.md for this specified P, without claiming a classification for other degenerate P or higher prime powers.

The unchanged PDF retains its original authorship. This package reuses historical independent review and release evidence; it is not a new mathematical audit, journal acceptance, or a claim about a wider parent problem.

PDF保持原始字节及署名。本次核对配套文件，不重新审稿，不将部分结果或猜想包装成原题全解。

## Restore exact inputs / 还原精确输入

From this package directory / 在当前包目录执行:

```sh
python3 ../prepare.py --restore BW2-N01-P18
```

No large input needs restoration.

Restoration verifies stored and original digests and refuses to overwrite modified data. Large restored files are excluded from Git; compressed copies are the distributed originals.

## Rebuild the manuscript / 重编译

```sh
python3 ../build.py BW2-N01-P18
```

The helper uses a disposable copy and retains build output outside the archive. Requires `latexmk` and the TeX packages declared by the source. Build status during packaging: **pass**. A regenerated PDF is not a replacement for the historical released PDF.

Recorded build working directory / 已核验编译目录: `latex-parent`. The helper applies this automatically.

## Reproduction programs and proof / 程序与证明

Run programs from the `source/` directory unless their original instructions specify a subdirectory. Inspect their arguments first: discovery searches and full certificates can be long-running. Prefer a disposable copy; original programs may regenerate result files.

- `evidence/check-p18-small.py`
- `evidence/check-research.py`
- `evidence/check-triage-reduction.py`

Bounded replay status in this packaging task: **not-rerun**. Not rerun means archived but not re-executed here; it does not mean the historical proof failed. A short test does not certify assertions outside its encoded finite range.



## Dependencies and limitations / 依赖与限制

- No third-party Python import detected by static inspection; this is not a tested environment lock.

- Asset selection is a packaging recommendation, not a rerun of the proof or citation audit.
- Do not copy external literature PDFs, downloaded web pages, third-party archives, jobs, logs, prompts, or private operational metadata.
- Review absolute paths and third-party attribution markers before publishing. Import names are inferred dependencies, not a tested environment lock.
- {'path': '/home/ailab/4math-open-problems/projects/newwin-00001-p18/evidence/triage-registry-screen.json', 'indicators': ['absolute-local-path']}
- External reference literature is not redistributed. Consult the bibliography and archived source URLs.

`package.json` records every distributed scientific input, its original relative path, digest, and compression. External literature, account/configuration files, agent transcripts, installed environments and unrelated third-party binaries are not included. Bibliographic references remain in the LaTeX sources.
