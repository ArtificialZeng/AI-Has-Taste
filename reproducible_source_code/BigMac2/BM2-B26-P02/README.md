# BM2-B26-P02 — reproduction source and evidence

Fixed-Start Cover Times Change Under Every Edge Addition on Connected Cyclic Graphs of Order Eight

[Final PDF](../../../pdfs/BigMac2/BM2-B26-P02_Fixed_Start_Cover_Times_Change_Under_Every_Edge_Addition_on_Connected_Cyclic_Graphs_of_Order_Eight.pdf) · [Catalog](../../../README.md#bigmac2) · [Gate provenance](../../../assets/BigMac2/gates/BM2-B26-P02/packaging-review.json)

## Mathematical scope

Proof of the frozen original statement. For every connected non-tree finite simple graph G on exactly eight vertices, every unordered genuine nonedge {u,v}, and every starting vertex s in V(G), the expected discrete-time simple-random-walk cover times satisfy t_cov(G+uv,s) != t_cov(G,s), where the start is visited at time zero and time is counted in edge transitions.

## Reproduction coverage

Archived scientific programs and exact evidence; all original bytes preserved. Full computations not rerun during packaging. Some historical wrappers contain machine-specific paths; see the per-package instructions before replay.

The package contains 23 scientific source/evidence files, including 5 programs. Exact certificates, source/problem statements and independent verifier programs are included where archived. Search experiments and negative tests are not automatically proof validators. A file hash or syntax check is not mathematical verification.

## Prepare a working copy

Some large generated certificates are stored with lossless gzip compression (4 files). Do not run code against compressed filenames. From the repository root:

```sh
python3 reproducible_source_code/BigMac2/prepare.py BM2-B26-P02 --output /path/to/new-working-directory
```

This copies the selected source tree and decompresses data while verifying original SHA-256 hashes. The output must be a new directory. Run programs in that working copy, from the working directory specified by the individual script, to avoid changing the archive.

Python 3.12+ is recommended. Detected direct third-party imports: networkx, sympy. The optional requirements.txt records names, not a reproduced historical environment. C/C++ code and external tools (for example nauty, SAT solvers or Singular) must be rebuilt/installed separately when the script requires them. This packaging task installs nothing.

## Program entry points

- [`evidence/build_rooted_streams.py`](source/evidence/build_rooted_streams.py)
- [`evidence/census_modular.cpp`](source/evidence/census_modular.cpp)
- [`evidence/exact_regression.py`](source/evidence/exact_regression.py)
- [`evidence/graph6_crosscheck.py`](source/evidence/graph6_crosscheck.py)
- [`evidence/reproduce.sh`](source/evidence/reproduce.sh)

## Portability notes

Historical program text is unchanged; these path references require review or a documented local adapter before another machine can run the relevant wrapper:

- `evidence/build_rooted_streams.py` (lines 1)
- `evidence/exact_regression.py` (lines 1)
- `evidence/graph6_crosscheck.py` (lines 1)
- `evidence/reproduce.sh` (lines 4, 5, 6, 7, 9, 74, 75)

Do not bypass a binary-hash/provenance assertion and call the historical run reproduced. See [collection reproduction notes](../REPRODUCTION_NOTES.md) for specific tools and limitations. Historical `publication.json` and claim/audit records are provenance, not ready-made manifests of this reorganized subset; primary-source downloads, environment directories, compiled binaries and old PDFs are deliberately omitted.

[Matching LaTeX](../../../latex_source_code/BigMac2/BM2-B26-P02/) · [Per-file hashes and storage map](package.json) · [Omitted files](../../../assets/BigMac2/gates/BM2-B26-P02/omitted-files.json)

<!-- BEGIN PACKAGING REPLAY -->
## Actual packaging check

Bounded replay passed; Exact regression uses SymPy; graph6_crosscheck uses NetworkX. Full reproduce.sh is machine-specific (old project/interpreter/Homebrew/private-tmp/compiler paths). Provide a new documented portable wrapper; retain original bytes as provenance. Full modular census C++ requires C++20 and nauty geng/labelg.

```sh
python3 evidence/exact_regression.py
```

<!-- END PACKAGING REPLAY -->
