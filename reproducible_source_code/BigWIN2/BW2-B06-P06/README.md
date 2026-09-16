# BW2-B06-P06 — The sharp variation constant for the centered Hardy–Littlewood maximal operator on P₁₁

[Final PDF / 最终稿](../../../pdfs/BigWIN2/BW2-B06-P06_The_sharp_variation_constant_for_the_centered_Hardy_Littlewood_maximal_operator_on_P11.pdf) · [LaTeX entry / 入口](source/paper/main.tex) · [Sources, data and proof / 复现材料](source/) · [Gate records / 历史门控](../../../assets/BigWIN2/gates/BW2-B06-P06/)

Original ID / 原始编号: `legacy-b06-p06`. Origin / 来源: 6.

## Accepted scope / 已接受范围

Historically gated final manuscript; see accepted scope / 历史门控终稿；见已接受范围.

Exact C(P11)=10/11 theorem only; arbitrary-n continuation remains open.

The unchanged PDF retains its original authorship. This package reuses historical independent review and release evidence; it is not a new mathematical audit, journal acceptance, or a claim about a wider parent problem.

PDF保持原始字节及署名。本次核对配套文件，不重新审稿，不将部分结果或猜想包装成原题全解。

## Restore exact inputs / 还原精确输入

From this package directory / 在当前包目录执行:

```sh
python3 ../prepare.py --restore BW2-B06-P06
```

- `source/certificates/p11_radius_certificate.bin` ← `compressed/certificates/p11_radius_certificate.bin.gz` (45011088 original bytes)

Restoration verifies stored and original digests and refuses to overwrite modified data. Large restored files are excluded from Git; compressed copies are the distributed originals.

## Rebuild the manuscript / 重编译

```sh
python3 ../build.py BW2-B06-P06
```

The helper uses a disposable copy and retains build output outside the archive. Requires `latexmk` and the TeX packages declared by the source. Build status during packaging: **pass**. A regenerated PDF is not a replacement for the historical released PDF.

Recorded build working directory / 已核验编译目录: `latex-parent`. The helper applies this automatically.

## Reproduction programs and proof / 程序与证明

Run programs from the `source/` directory unless their original instructions specify a subdirectory. Inspect their arguments first: discovery searches and full certificates can be long-running. Prefer a disposable copy; original programs may regenerate result files.

- `code/breaker_search.py`
- `code/discovery_chamber.py`
- `code/generate_radius_certificate.py`
- `code/test_verifier_fail_closed.py`
- `code/verify_radius_certificate.py`

Bounded replay status in this packaging task: **not-rerun**. Not rerun means archived but not re-executed here; it does not mean the historical proof failed. A short test does not certify assertions outside its encoded finite range.



## Dependencies and limitations / 依赖与限制

- Python 3.10+ standard library.

- Select the final citation-corrected seven-page manuscript bound by audit/release_manifest.json. Do not merge unresolved all-n follow-up into this paper.
- Original entrypoints: ['python3 code/test_verifier_fail_closed.py']
- Long/full or external-tool entrypoints: ['python3 code/verify_radius_certificate.py certificates/p11_radius_certificate.json certificates/p11_radius_certificate.bin']

`package.json` records every distributed scientific input, its original relative path, digest, and compression. External literature, account/configuration files, agent transcripts, installed environments and unrelated third-party binaries are not included. Bibliographic references remain in the LaTeX sources.
