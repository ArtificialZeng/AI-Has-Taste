# BW2-PR20260913-subsum_denominator — A Newton-positivity conjecture for dyadic stages of reciprocal-subsum denominators

[Final PDF / 最终稿](../../../pdfs/ai-conjecture/BW2-PR20260913-subsum_denominator_A_Newton_positivity_conjecture_for_dyadic_stages_of_reciprocal_subsum_denominators.pdf) · [LaTeX entry / 入口](source/manuscript/main.tex) · [Sources, data and proof / 复现材料](source/) · [Gate records / 历史门控](../../../assets/BigWIN2/gates/BW2-PR20260913-subsum_denominator/)

Original ID / 原始编号: `primary-20260913-subsum-denominator`. Origin / 来源: primary.

## Accepted scope / 已接受范围

Conjectural note; original problem unresolved / 猜想札记；原问题仍未解决.

Explicitly unproved conjecture K_sharp_v1. Let D_N(x)=product_{i=1}^N(1+x^i)^{#{q&gt;=0:2^q i&lt;=N}}. For every integer j&gt;=0 and every integer 1&lt;=s&lt;=j+1, let tau be the least t&gt;=0 with s\*2^t&gt;=9 and 2\*s\*2^t&gt;j+1. For t with s\*2^t&gt;=9 set a_{s,t}(x)=D_{s\*2^t-1}(x) product_{ell=1}^{v_2(s)}(1+x^{s/2^ell}); coefficients are zero outside support. Set T_r(a)=a_r^2-a_{r-1}a_{r+1} and F_{s,j}(t)=2T_j(a_{s,t}(1+x^s))-T_j(a_{s,t})-T_{j-s}(a_{s,t}). Conjecture: Delta_t^h F_{s,j}(tau)&gt;=0 for all integers 0&lt;=h&lt;=2j, where Delta has step one in t. Supporting established claims submitted for review: (i) the exact affine reduction and degree bound deg_u F(tau+u)&lt;=2j; (ii) the complete exact certificate through j=96, yielding H at every actual stage for all n&gt;=9 at indices 0&lt;=j&lt;=96 and their reflections, and original log-concavity for all n outside {3,5,6,7} when min(j,deg(D_n)-j)&lt;=96; (iii) the generic positive band h=2j-k when j&gt;=2k^2+k-1, with the top two Catalan formulas; (iv) for every n&gt;=9 and every actual stage adding s at n=s\*2^t, at j=2n-1 the actual value differs from its polynomial tail extrapolation by -a_{2n-2}-2a_{2n-s-2}&lt;0, so every even forward difference of order at least 4n is negative. The boundary obstruction is outside K_sharp and is not a counterexample to H or to the original conjecture. K_sharp is not claimed equivalent to, or a complete proof of, the original all-n, all-index problem. All supporting statements, proof details and computational limits are specified in evidence/research3.md and its cited evidence.

The unchanged PDF retains its original authorship. This package reuses historical independent review and release evidence; it is not a new mathematical audit, journal acceptance, or a claim about a wider parent problem.

PDF保持原始字节及署名。本次核对配套文件，不重新审稿，不将部分结果或猜想包装成原题全解。

## Restore exact inputs / 还原精确输入

From this package directory / 在当前包目录执行:

```sh
python3 ../prepare.py --restore BW2-PR20260913-subsum_denominator
```

- `source/evidence/research3_sharp_probe.json` ← `compressed/evidence/research3_sharp_probe.json.gz` (36591320 original bytes)

Restoration verifies stored and original digests and refuses to overwrite modified data. Large restored files are excluded from Git; compressed copies are the distributed originals.

## Rebuild the manuscript / 重编译

```sh
python3 ../build.py BW2-PR20260913-subsum_denominator
```

The helper uses a disposable copy and retains build output outside the archive. Requires `latexmk` and the TeX packages declared by the source. Build status during packaging: **pass**. A regenerated PDF is not a replacement for the historical released PDF.

Recorded build working directory / 已核验编译目录: `latex-parent`. The helper applies this automatically.

## Reproduction programs and proof / 程序与证明

Run programs from the `source/` directory unless their original instructions specify a subdirectory. Inspect their arguments first: discovery searches and full certificates can be long-running. Prefer a disposable copy; original programs may regenerate result files.

- `evidence/research2_bivariate_verify.py`
- `evidence/research2_integrity.py`
- `evidence/research2_kernel_probe.py`
- `evidence/research2_sharp_probe.py`
- `evidence/research2_verify.py`
- `evidence/research3_boundary_probe.py`
- `evidence/research3_boundary_verify.py`
- `evidence/research3_design_verify.py`
- `evidence/research3_integrity.py`
- `evidence/research3_sharp_probe.py`
- `evidence/research3_verify.py`
- `evidence/research_edge_probe.py`
- `evidence/research_h_probe.py`
- `evidence/research_integrity.py`
- `evidence/research_kernel_probe.py`
- `evidence/research_verify.py`
- `evidence/smoothing_probe.py`
- `evidence/triage_probe.py`

Bounded replay status in this packaging task: **not-rerun**. Not rerun means archived but not re-executed here; it does not mean the historical proof failed. A short test does not certify assertions outside its encoded finite range.



## Dependencies and limitations / 依赖与限制

- flint

- Asset selection is a packaging recommendation, not a rerun of the proof or citation audit.
- Do not copy external literature PDFs, downloaded web pages, third-party archives, jobs, logs, prompts, or private operational metadata.
- Review absolute paths and third-party attribution markers before publishing. Import names are inferred dependencies, not a tested environment lock.
- The original question is unresolved; the released artifact is a partial result or unproved conjecture, according to its frozen claim.
- External reference literature is not redistributed. Consult the bibliography and archived source URLs.

`package.json` records every distributed scientific input, its original relative path, digest, and compression. External literature, account/configuration files, agent transcripts, installed environments and unrelated third-party binaries are not included. Bibliographic references remain in the LaTeX sources.
