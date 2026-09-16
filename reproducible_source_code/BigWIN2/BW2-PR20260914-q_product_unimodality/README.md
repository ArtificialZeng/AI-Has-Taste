# BW2-PR20260914-q_product_unimodality — A two-factor criterion for unimodality of stretched q-integer products

[Final PDF / 最终稿](../../../pdfs/BigWIN2/BW2-PR20260914-q_product_unimodality_A_two_factor_criterion_for_unimodality_of_stretched_q_integer_products.pdf) · [LaTeX entry / 入口](source/manuscript/main.tex) · [Sources, data and proof / 复现材料](source/) · [Gate records / 历史门控](../../../assets/BigWIN2/gates/BW2-PR20260914-q_product_unimodality/)

Original ID / 原始编号: `primary-20260914-q-product-unimodality`. Origin / 来源: primary-20260914.

## Accepted scope / 已接受范围

Partial-result note; parent problem not fully solved / 部分结果札记；母题未完整解决.

For every integer r&gt;=2 and all positive integers a,c,b, define \[a\]_q=sum_{i=0}^{a-1}q^i and \[b\]_(q^r)=sum_{j=0}^{b-1}q^(rj). The full integer-indexed coefficient sequence of \[a\]_q\[c\]_q\[b\]_(q^r), including zero coefficients, is weakly unimodal if and only if r divides a, or r divides c, or b&lt;=1+floor(a/r)+floor(c/r). The disjunction is inclusive and factor-1 cases are included. This is exactly the k=2 restriction of the original Conjecture 5.4; no assertion resolving its other parameter ranges is submitted.

The unchanged PDF retains its original authorship. This package reuses historical independent review and release evidence; it is not a new mathematical audit, journal acceptance, or a claim about a wider parent problem.

PDF保持原始字节及署名。本次核对配套文件，不重新审稿，不将部分结果或猜想包装成原题全解。

## Restore exact inputs / 还原精确输入

From this package directory / 在当前包目录执行:

```sh
python3 ../prepare.py --restore BW2-PR20260914-q_product_unimodality
```

No large input needs restoration.

Restoration verifies stored and original digests and refuses to overwrite modified data. Large restored files are excluded from Git; compressed copies are the distributed originals.

## Rebuild the manuscript / 重编译

```sh
python3 ../build.py BW2-PR20260914-q_product_unimodality
```

The helper uses a disposable copy and retains build output outside the archive. Requires `latexmk` and the TeX packages declared by the source. Build status during packaging: **pass**. A regenerated PDF is not a replacement for the historical released PDF.

Recorded build working directory / 已核验编译目录: `latex-parent`. The helper applies this automatically.

## Reproduction programs and proof / 程序与证明

Run programs from the `source/` directory unless their original instructions specify a subdirectory. Inspect their arguments first: discovery searches and full certificates can be long-running. Prefer a disposable copy; original programs may regenerate result files.

- `evidence/desk_screen.py`
- `evidence/research_verify.py`
- `evidence/triage_boundary.py`

Bounded replay status in this packaging task: **not-rerun**. Not rerun means archived but not re-executed here; it does not mean the historical proof failed. A short test does not certify assertions outside its encoded finite range.



## Dependencies and limitations / 依赖与限制

- No third-party Python import detected by static inspection; this is not a tested environment lock.

- Asset selection is a packaging recommendation, not a rerun of the proof or citation audit.
- Do not copy external literature PDFs, downloaded web pages, third-party archives, jobs, logs, prompts, or private operational metadata.
- Review absolute paths and third-party attribution markers before publishing. Import names are inferred dependencies, not a tested environment lock.
- The original question is unresolved; the released artifact is a partial result or unproved conjecture, according to its frozen claim.
- External reference literature is not redistributed. Consult the bibliography and archived source URLs.

`package.json` records every distributed scientific input, its original relative path, digest, and compression. External literature, account/configuration files, agent transcripts, installed environments and unrelated third-party binaries are not included. Bibliographic references remain in the LaTeX sources.
