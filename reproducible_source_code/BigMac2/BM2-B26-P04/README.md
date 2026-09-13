# BM2-B26-P04 — reproduction source and evidence

An Explicit 13-Vertex Graph with No Edgeless Five-Vertex Vertex-Minor

[Final PDF](../../../pdfs/BigMac2/BM2-B26-P04_An_Explicit_13_Vertex_Graph_with_No_Edgeless_Five_Vertex_Vertex_Minor.pdf) · [Catalog](../../../README.md#bigmac2) · [Gate provenance](../../../assets/BigMac2/gates/BM2-B26-P04/packaging-review.json)

## Mathematical scope

Proof of the frozen original statement. There exists a simple graph G on exactly 13 vertices with beta(G) <= 4. Explicitly, the graph6 string LlthgsL`mEkLkL decodes to the Paley graph P(13), its complete labeled local-complementation orbit has 711440 members, and beta(P(13)) = 4.

## Reproduction coverage

Archived scientific programs and exact evidence; all original bytes preserved. Full computations not rerun during packaging.

The package contains 13 scientific source/evidence files, including 3 programs. Exact certificates, source/problem statements and independent verifier programs are included where archived. Search experiments and negative tests are not automatically proof validators. A file hash or syntax check is not mathematical verification.

## Prepare a working copy

Some large generated certificates are stored with lossless gzip compression (1 files). Do not run code against compressed filenames. From the repository root:

```sh
python3 reproducible_source_code/BigMac2/prepare.py BM2-B26-P04 --output /path/to/new-working-directory
```

This copies the selected source tree and decompresses data while verifying original SHA-256 hashes. The output must be a new directory. Run programs in that working copy, from the working directory specified by the individual script, to avoid changing the archive.

Python 3.12+ is recommended. Detected direct third-party imports: networkx, numpy. The optional requirements.txt records names, not a reproduced historical environment. C/C++ code and external tools (for example nauty, SAT solvers or Singular) must be rebuilt/installed separately when the script requires them. This packaging task installs nothing.

## Program entry points

- [`audit/referee_verify.cpp`](source/audit/referee_verify.cpp)
- [`evidence/lc13_search.cpp`](source/evidence/lc13_search.cpp)
- [`evidence/verify_paley13.py`](source/evidence/verify_paley13.py)

## Portability notes

Historical program text is unchanged; these path references require review or a documented local adapter before another machine can run the relevant wrapper:

- No machine-specific path detected in archived program text.

Do not bypass a binary-hash/provenance assertion and call the historical run reproduced. See [collection reproduction notes](../REPRODUCTION_NOTES.md) for specific tools and limitations. Historical `publication.json` and claim/audit records are provenance, not ready-made manifests of this reorganized subset; primary-source downloads, environment directories, compiled binaries and old PDFs are deliberately omitted.

[Matching LaTeX](../../../latex_source_code/BigMac2/BM2-B26-P04/) · [Per-file hashes and storage map](package.json) · [Omitted files](../../../assets/BigMac2/gates/BM2-B26-P04/omitted-files.json)

<!-- BEGIN PACKAGING REPLAY -->
## Actual packaging check

Not rerun during packaging: No short positive exact checker selected; see archived source/proof dossier. paley13_lc_orbit.bin is SCIENTIFIC DATA, not executable. Preserve it losslessly. Python verifier uses NumPy/NetworkX and checks915,623,280 five-subsets; C++20 independent verifier does the same. Both are long replays, not smoke checks. Compile c++ -O3 -std=c++20 audit/referee_verify.cpp -o replay-verify. Then pass the literal graph6 string LlthgsL`mEkLkL as argv1 and evidence/paley13_lc_orbit.bin as argv2 (use an argument array or single shell quotes; the backtick must not execute).

<!-- END PACKAGING REPLAY -->
