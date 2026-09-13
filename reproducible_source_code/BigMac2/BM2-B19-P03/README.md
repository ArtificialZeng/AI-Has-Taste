# BM2-B19-P03 — reproduction source and evidence

An Exact Weighted-Cycle Obstruction for the 812-Vertex AGL(1,29) Orientation Instance

[Final PDF](../../../pdfs/BigMac2/BM2-B19-P03_An_Exact_Weighted_Cycle_Obstruction_for_the_812_Vertex_AGL_1_29_Orientation_Instance.pdf) · [Catalog](../../../README.md#bigmac2) · [Gate provenance](../../../assets/BigMac2/gates/BM2-B19-P03/packaging-review.json)

## Mathematical scope

Disproof of the frozen original statement. For the exact labelled 812-vertex cubic graph B encoded by agl_29_g14.g6 in the frozen archive specified by source.md, there is no function u:V(B)->E(B) such that u(v) is incident with v for every vertex and, for every simple cycle C of every length ell in {14,15,16}, #{v in V(C): u(v) is an edge of C} <= 3*ell-33.

## Reproduction coverage

Archived scientific programs and exact evidence; all original bytes preserved. Full computations not rerun during packaging.

The package contains 49 scientific source/evidence files, including 13 programs. Exact certificates, source/problem statements and independent verifier programs are included where archived. Search experiments and negative tests are not automatically proof validators. A file hash or syntax check is not mathematical verification.

## Prepare a working copy

Some large generated certificates are stored with lossless gzip compression (8 files). Do not run code against compressed filenames. From the repository root:

```sh
python3 reproducible_source_code/BigMac2/prepare.py BM2-B19-P03 --output /path/to/new-working-directory
```

This copies the selected source tree and decompresses data while verifying original SHA-256 hashes. The output must be a new directory. Run programs in that working copy, from the working directory specified by the individual script, to avoid changing the archive.

Python 3.12+ is recommended. Detected direct third-party imports: numpy, scipy. The optional requirements.txt records names, not a reproduced historical environment. C/C++ code and external tools (for example nauty, SAT solvers or Singular) must be rebuilt/installed separately when the script requires them. This packaging task installs nothing.

## Program entry points

- [`audit/referee-88e58f34133f-verify.py`](source/audit/referee-88e58f34133f-verify.py)
- [`evidence/build_compact_orientation_cnf.py`](source/evidence/build_compact_orientation_cnf.py)
- [`evidence/build_exact_weight_certificate.py`](source/evidence/build_exact_weight_certificate.py)
- [`evidence/build_good_edge_cnf.py`](source/evidence/build_good_edge_cnf.py)
- [`evidence/build_orientation_cnf.py`](source/evidence/build_orientation_cnf.py)
- [`evidence/build_quotient_cnf.py`](source/evidence/build_quotient_cnf.py)
- [`evidence/build_search_instance.py`](source/evidence/build_search_instance.py)
- [`evidence/check_exact_weight_certificate.py`](source/evidence/check_exact_weight_certificate.py)
- [`evidence/cycle_census.py`](source/evidence/cycle_census.py)
- [`evidence/extract_lp_dual_ray.cpp`](source/evidence/extract_lp_dual_ray.cpp)
- [`evidence/replay_exact_weight_certificate.py`](source/evidence/replay_exact_weight_certificate.py)
- [`evidence/search_orientation.cpp`](source/evidence/search_orientation.cpp)
- [`evidence/solve_orientation_milp.py`](source/evidence/solve_orientation_milp.py)

## Portability notes

Historical program text is unchanged; these path references require review or a documented local adapter before another machine can run the relevant wrapper:

- No machine-specific path detected in archived program text.

Do not bypass a binary-hash/provenance assertion and call the historical run reproduced. See [collection reproduction notes](../REPRODUCTION_NOTES.md) for specific tools and limitations. Historical `publication.json` and claim/audit records are provenance, not ready-made manifests of this reorganized subset; primary-source downloads, environment directories, compiled binaries and old PDFs are deliberately omitted.

[Matching LaTeX](../../../latex_source_code/BigMac2/BM2-B19-P03/) · [Per-file hashes and storage map](package.json) · [Omitted files](../../../assets/BigMac2/gates/BM2-B19-P03/omitted-files.json)

<!-- BEGIN PACKAGING REPLAY -->
## Actual packaging check

Bounded replay passed; Two exact weight replay paths are stdlib and do not depend on SciPy/HiGHS. Discovery requires SciPy/NumPy, CaDiCaL and C++ HiGHS headers/library. Avoid orientation CNF/MILP searches in a smoke check.

```sh
python3 evidence/replay_exact_weight_certificate.py evidence/exact_cycle_weights.tsv evidence/cycles_14_16.tsv evidence/orientation_search_instance.tsv replay-packaging.json
```

<!-- END PACKAGING REPLAY -->
