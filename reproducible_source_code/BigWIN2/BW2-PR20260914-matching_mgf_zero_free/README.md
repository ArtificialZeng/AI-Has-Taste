# BW2-PR20260914-matching_mgf_zero_free — A zero-free disk for the minimum cost of a four-edge bipartite matching

[Final PDF / 最终稿](../../../pdfs/BigWIN2/BW2-PR20260914-matching_mgf_zero_free_A_zero_free_disk_for_the_minimum_cost_of_a_four_edge_bipartite_matching.pdf) · [LaTeX entry / 入口](source/manuscript/main.tex) · [Sources, data and proof / 复现材料](source/) · [Gate records / 历史门控](../../../assets/BigWIN2/gates/BW2-PR20260914-matching_mgf_zero_free/)

Original ID / 原始编号: `primary-20260914-matching-mgf-zero-free`. Origin / 来源: primary-20260914.

## Accepted scope / 已接受范围

Partial-result note; parent problem not fully solved / 部分结果札记；母题未完整解决.

For every pair of integers m,n&gt;=4, assign independent rate-one exponential costs to the edges of K_{m,n}, and let C_{4,m,n} be the minimum total cost of a matching of four edges. Then F_{4,m,n}(t)=E exp(t C_{4,m,n}) is nonzero for every complex t with &#124;t&#124;&lt;mn/4. Moreover, every zero of the reduced numerator of its rational continuation has modulus strictly greater than mn/4. The proof establishes the stronger algebraic statement that the explicit sextic P_{m,n} in evidence/k4-proof.md has no root in &#124;t&#124;&lt;=mn/4 for all real m,n&gt;=4, using F_{4,m,n}=A P_{m,n}/Q for integer parameters. Boundary poles are not claimed to be finite nonzero values. The frozen conjecture for unrestricted k remains unresolved.

The unchanged PDF retains its original authorship. This package reuses historical independent review and release evidence; it is not a new mathematical audit, journal acceptance, or a claim about a wider parent problem.

PDF保持原始字节及署名。本次核对配套文件，不重新审稿，不将部分结果或猜想包装成原题全解。

## Restore exact inputs / 还原精确输入

From this package directory / 在当前包目录执行:

```sh
python3 ../prepare.py --restore BW2-PR20260914-matching_mgf_zero_free
```

No large input needs restoration.

Restoration verifies stored and original digests and refuses to overwrite modified data. Large restored files are excluded from Git; compressed copies are the distributed originals.

## Rebuild the manuscript / 重编译

```sh
python3 ../build.py BW2-PR20260914-matching_mgf_zero_free
```

The helper uses a disposable copy and retains build output outside the archive. Requires `latexmk` and the TeX packages declared by the source. Build status during packaging: **pass**. A regenerated PDF is not a replacement for the historical released PDF.

Recorded build working directory / 已核验编译目录: `latex-parent`. The helper applies this automatically.

## Reproduction programs and proof / 程序与证明

Run programs from the `source/` directory unless their original instructions specify a subdirectory. Inspect their arguments first: discovery searches and full certificates can be long-running. Prefer a disposable copy; original programs may regenerate result files.

- `evidence/research_k4_certificate.py`
- `evidence/triage_certificate_screen.py`
- `evidence/triage_symbolic.py`
- `evidence/verify_k4_certificate.py`

Bounded replay status in this packaging task: **not-rerun**. Not rerun means archived but not re-executed here; it does not mean the historical proof failed. A short test does not certify assertions outside its encoded finite range.



## Dependencies and limitations / 依赖与限制

- sympy

- Asset selection is a packaging recommendation, not a rerun of the proof or citation audit.
- Do not copy external literature PDFs, downloaded web pages, third-party archives, jobs, logs, prompts, or private operational metadata.
- Review absolute paths and third-party attribution markers before publishing. Import names are inferred dependencies, not a tested environment lock.
- The original question is unresolved; the released artifact is a partial result or unproved conjecture, according to its frozen claim.
- {'path': '/home/ailab/4math-open-problems/projects/primary-20260914-matching-mgf-zero-free/manuscript/main.tex', 'indicators': ['third-party-attribution-or-license-marker']}
- External reference literature is not redistributed. Consult the bibliography and archived source URLs.

`package.json` records every distributed scientific input, its original relative path, digest, and compression. External literature, account/configuration files, agent transcripts, installed environments and unrelated third-party binaries are not included. Bibliographic references remain in the LaTeX sources.
