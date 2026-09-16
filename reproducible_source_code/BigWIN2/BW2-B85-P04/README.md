# BW2-B85-P04 — A Two-Coloring of the Edges of KG(11,3) with No Monochromatic Triangle

[Final PDF / 最终稿](../../../pdfs/BigWIN2/BW2-B85-P04_A_Two_Coloring_of_the_Edges_of_KG_11_3_with_No_Monochromatic_Triangle.pdf) · [LaTeX entry / 入口](source/manuscript/main.tex) · [Sources, data and proof / 复现材料](source/) · [Gate records / 历史门控](../../../assets/BigWIN2/gates/BW2-B85-P04/)

Original ID / 原始编号: `win-00085-p04`. Origin / 来源: 85.

## Accepted scope / 已接受范围

Partial-result note; parent problem not fully solved / 部分结果札记；母题未完整解决.

For the ordinary red-blue edge-coloring problem on the three-uniform Kneser graph, KG(11,3) admits a complete two-coloring of its 4,620 edges in which none of its 15,400 triangles is monochromatic. Consequently R_3^KG(3,3) &gt;= 12. This does not decide the KG(12,3) case, so the frozen original exact-value problem remains unresolved with value in {12,13}.

The unchanged PDF retains its original authorship. This package reuses historical independent review and release evidence; it is not a new mathematical audit, journal acceptance, or a claim about a wider parent problem.

PDF保持原始字节及署名。本次核对配套文件，不重新审稿，不将部分结果或猜想包装成原题全解。

## Restore exact inputs / 还原精确输入

From this package directory / 在当前包目录执行:

```sh
python3 ../prepare.py --restore BW2-B85-P04
```

No large input needs restoration.

Restoration verifies stored and original digests and refuses to overwrite modified data. Large restored files are excluded from Git; compressed copies are the distributed originals.

## Rebuild the manuscript / 重编译

```sh
python3 ../build.py BW2-B85-P04
```

The helper uses a disposable copy and retains build output outside the archive. Requires `latexmk` and the TeX packages declared by the source. Build status during packaging: **pass**. A regenerated PDF is not a replacement for the historical released PDF.

Recorded build working directory / 已核验编译目录: `latex-parent`. The helper applies this automatically.

## Reproduction programs and proof / 程序与证明

Run programs from the `source/` directory unless their original instructions specify a subdirectory. Inspect their arguments first: discovery searches and full certificates can be long-running. Prefer a disposable copy; original programs may regenerate result files.

- `evidence/check_n11_coloring.py`
- `evidence/check_n12_cnf.py`
- `evidence/check_n12_coloring.py`
- `evidence/generate_n12_cnf.py`
- `evidence/run_n12_proof_sat.py`
- `evidence/triage_probe.py`

Bounded replay status in this packaging task: **passed**. Not rerun means archived but not re-executed here; it does not mean the historical proof failed. A short test does not certify assertions outside its encoded finite range.

Checks the serialized coloring on the 3-uniform Kneser graph at n=11 and excludes monochromatic disjoint triples.

## Dependencies and limitations / 依赖与限制

- pysat

- Asset selection is a packaging recommendation, not a rerun of the proof or citation audit.
- Do not copy external literature PDFs, downloaded web pages, third-party archives, jobs, logs, prompts, or private operational metadata.
- Review absolute paths and third-party attribution markers before publishing. Import names are inferred dependencies, not a tested environment lock.
- The original question is unresolved; the released artifact is a partial result or unproved conjecture, according to its frozen claim.

`package.json` records every distributed scientific input, its original relative path, digest, and compression. External literature, account/configuration files, agent transcripts, installed environments and unrelated third-party binaries are not included. Bibliographic references remain in the LaTeX sources.
