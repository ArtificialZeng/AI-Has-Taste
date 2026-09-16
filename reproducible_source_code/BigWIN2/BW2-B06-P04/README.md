# BW2-B06-P04 — The Eleven-Vertex Case of the Unique NAC-Colouring Conjecture

[Final PDF / 最终稿](../../../pdfs/BigWIN2/BW2-B06-P04_The_Eleven_Vertex_Case_of_the_Unique_NAC_Colouring_Conjecture.pdf) · [LaTeX entry / 入口](source/paper/main.tex) · [Sources, data and proof / 复现材料](source/) · [Gate records / 历史门控](../../../assets/BigWIN2/gates/BW2-B06-P04/)

Original ID / 原始编号: `legacy-b06-p04`. Origin / 来源: 6.

## Accepted scope / 已接受范围

Historically gated final manuscript; see accepted scope / 历史门控终稿；见已接受范围.

All 2039273 eleven-vertex Laman isomorphism classes; not arbitrary order.

The unchanged PDF retains its original authorship. This package reuses historical independent review and release evidence; it is not a new mathematical audit, journal acceptance, or a claim about a wider parent problem.

PDF保持原始字节及署名。本次核对配套文件，不重新审稿，不将部分结果或猜想包装成原题全解。

## Restore exact inputs / 还原精确输入

From this package directory / 在当前包目录执行:

```sh
python3 ../prepare.py --restore BW2-B06-P04
```

- `source/certificates/nac11_four_way.cert` ← `compressed/certificates/nac11_four_way.cert.gz` (104314385 original bytes)
- `source/experiments/upstream/LamanGraphs11.txt` ← `compressed/experiments/upstream/LamanGraphs11.txt.gz` (37270710 original bytes)

Restoration verifies stored and original digests and refuses to overwrite modified data. Large restored files are excluded from Git; compressed copies are the distributed originals.

## Rebuild the manuscript / 重编译

```sh
python3 ../build.py BW2-B06-P04
```

The helper uses a disposable copy and retains build output outside the archive. Requires `latexmk` and the TeX packages declared by the source. Build status during packaging: **pass**. A regenerated PDF is not a replacement for the historical released PDF.

Recorded build working directory / 已核验编译目录: `latex-parent`. The helper applies this automatically.

## Reproduction programs and proof / 程序与证明

Run programs from the `source/` directory unless their original instructions specify a subdirectory. Inspect their arguments first: discovery searches and full certificates can be long-running. Prefer a disposable copy; original programs may regenerate result files.

- `scripts/build_and_verify.sh`
- `src/discover_n11.c`
- `src/verify_n11.c`
- `tests/adversarial_verifier.sh`

Bounded replay status in this packaging task: **not-rerun**. Not rerun means archived but not re-executed here; it does not mean the historical proof failed. A short test does not certify assertions outside its encoded finite range.



## Dependencies and limitations / 依赖与限制

- Bash and C11 compiler cc. Full verification requires certificates/nac11_four_way.cert and experiments/upstream/LamanGraphs11.txt.

- Current PDF, LaTeX ZIP and reproducibility ZIP hashes all match audit/MANIFEST.sha256.
- No standalone short full-result verifier is claimed: the build-and-verify entry checks all 2039273 classes.
- Retain the numeric Laman graph input dataset and Description.txt with attribution DOI 10.5281/zenodo.1245517; exclude nauty toolchain archives and binaries.
- nac11_four_way.cert is 104314385 bytes, close to GitHub's 100 MiB individual-file limit.
- Original entrypoints: []
- Long/full or external-tool entrypoints: ['bash scripts/build_and_verify.sh']

`package.json` records every distributed scientific input, its original relative path, digest, and compression. External literature, account/configuration files, agent transcripts, installed environments and unrelated third-party binaries are not included. Bibliographic references remain in the LaTeX sources.
