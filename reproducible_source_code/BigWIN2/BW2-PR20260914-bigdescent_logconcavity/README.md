# BW2-PR20260914-bigdescent_logconcavity — Conditional Schur positivity for binary-word events with at most four free positions

[Final PDF / 最终稿](../../../pdfs/BigWIN2/BW2-PR20260914-bigdescent_logconcavity_Conditional_Schur_positivity_for_binary_word_events_with_at_most_four_free_positions.pdf) · [LaTeX entry / 入口](source/manuscript/main.tex) · [Sources, data and proof / 复现材料](source/) · [Gate records / 历史门控](../../../assets/BigWIN2/gates/BW2-PR20260914-bigdescent_logconcavity/)

Original ID / 原始编号: `primary-20260914-bigdescent-logconcavity`. Origin / 来源: primary.

## Accepted scope / 已接受范围

Partial-result note; parent problem not fully solved / 部分结果札记；母题未完整解决.

For every n&gt;=1, let a_n(A) count binary words of length n ending in 1 whose event set A consists exactly of the ending positions of factors 10 and 011. For every J subset of {2,...,n} with m=&#124;J&#124;&lt;=4 and every S subset of {2,...,n}\\J, the homogeneous symmetric polynomial H_(S,J)(x,y)=sum_(T subset J) a_n(S union T) a_n(S union (J\\T)) x^&#124;T&#124; y^(m-&#124;T&#124;) is Schur-positive in two variables. Thus, if G(t;z)=sum_(T subset J) a_n(S union T)t^&#124;T&#124; product_(i in T) z_i=sum_k g_k(z)t^k, every g_k(z)^2-g_(k-1)(z)g_(k+1)(z) is coefficientwise nonnegative, with g_k=0 outside its range. There is no bound on n, the spacing of J, or &#124;S&#124;; all other event indicators are fixed, and zero-count cases are included. The two-position inequality a_n(S)a_n(S union {i,j})&lt;=2a_n(S union {i})a_n(S union {j}) has optimal factor 2, attained at n=4,S=empty,{i,j}={2,4}. The pair-polynomial conclusion also holds for arbitrary &#124;J&#124; when J can be partitioned in its natural order into blocks of at most four positions such that, between each consecutive pair of blocks, S contains two adjacent positions. No unrestricted weighted theorem, full exceptional-class log-concavity, or resolution of the original 21-family assertion is claimed.

The unchanged PDF retains its original authorship. This package reuses historical independent review and release evidence; it is not a new mathematical audit, journal acceptance, or a claim about a wider parent problem.

PDF保持原始字节及署名。本次核对配套文件，不重新审稿，不将部分结果或猜想包装成原题全解。

## Restore exact inputs / 还原精确输入

From this package directory / 在当前包目录执行:

```sh
python3 ../prepare.py --restore BW2-PR20260914-bigdescent_logconcavity
```

No large input needs restoration.

Restoration verifies stored and original digests and refuses to overwrite modified data. Large restored files are excluded from Git; compressed copies are the distributed originals.

## Rebuild the manuscript / 重编译

```sh
python3 ../build.py BW2-PR20260914-bigdescent_logconcavity
```

The helper uses a disposable copy and retains build output outside the archive. Requires `latexmk` and the TeX packages declared by the source. Build status during packaging: **pass**. A regenerated PDF is not a replacement for the historical released PDF.

Recorded build working directory / 已核验编译目录: `latex-parent`. The helper applies this automatically.

## Reproduction programs and proof / 程序与证明

Run programs from the `source/` directory unless their original instructions specify a subdirectory. Inspect their arguments first: discovery searches and full certificates can be long-running. Prefer a disposable copy; original programs may regenerate result files.

- `evidence/intake/calibrate.py`
- `evidence/research/multi_singleton_certificate.py`
- `evidence/research/pass2_audit.py`
- `evidence/research/pass3_audit.py`
- `evidence/research/profile_audit.py`
- `evidence/research/profile_test.py`
- `evidence/research/schur_blocks.py`
- `evidence/research/schur_profiles.py`
- `evidence/research/suffix_diagnostics.py`
- `evidence/research/two_singleton_certificate.py`
- `evidence/triage/positive_formula.py`

Bounded replay status in this packaging task: **not-rerun**. Not rerun means archived but not re-executed here; it does not mean the historical proof failed. A short test does not certify assertions outside its encoded finite range.



## Dependencies and limitations / 依赖与限制

- numpy
- sympy

- Asset selection is a packaging recommendation, not a rerun of the proof or citation audit.
- Do not copy external literature PDFs, downloaded web pages, third-party archives, jobs, logs, prompts, or private operational metadata.
- Review absolute paths and third-party attribution markers before publishing. Import names are inferred dependencies, not a tested environment lock.
- The original question is unresolved; the released artifact is a partial result or unproved conjecture, according to its frozen claim.
- External reference literature is not redistributed. Consult the bibliography and archived source URLs.

`package.json` records every distributed scientific input, its original relative path, digest, and compression. External literature, account/configuration files, agent transcripts, installed environments and unrelated third-party binaries are not included. Bibliographic references remain in the LaTeX sources.
