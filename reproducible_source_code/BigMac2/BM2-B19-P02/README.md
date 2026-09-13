# BM2-B19-P02 — reproduction source and evidence

Power-of-Two Cycles in 24-Vertex Graphs with Degree Sequence (5, followed by 23 threes)

[Final PDF](../../../pdfs/BigMac2/BM2-B19-P02_Power_of_Two_Cycles_in_24_Vertex_Graphs_with_Degree_Sequence_5_followed_by_23_threes.pdf) · [Catalog](../../../README.md#bigmac2) · [Gate provenance](../../../assets/BigMac2/gates/BM2-B19-P02/packaging-review.json)

## Mathematical scope

Partial result; original problem unresolved. Every finite simple undirected graph on exactly 24 vertices in which one vertex has degree 5 and each of the other 23 vertices has degree 3 contains a simple cycle whose length is one of 4, 8, or 16.

## Reproduction coverage

Archived scientific programs and exact evidence; all original bytes preserved. Full computations not rerun during packaging.

The package contains 20 scientific source/evidence files, including 5 programs. Exact certificates, source/problem statements and independent verifier programs are included where archived. Search experiments and negative tests are not automatically proof validators. A file hash or syntax check is not mathematical verification.

## Prepare a working copy

Some large generated certificates are stored with lossless gzip compression (4 files). Do not run code against compressed filenames. From the repository root:

```sh
python3 reproducible_source_code/BigMac2/prepare.py BM2-B19-P02 --output /path/to/new-working-directory
```

This copies the selected source tree and decompresses data while verifying original SHA-256 hashes. The output must be a new directory. Run programs in that working copy, from the working directory specified by the individual script, to avoid changing the archive.

Python 3.12+ is recommended. Detected direct third-party imports: none (standard library for the archived Python programs). The optional requirements.txt records names, not a reproduced historical environment. C/C++ code and external tools (for example nauty, SAT solvers or Singular) must be rebuilt/installed separately when the script requires them. This packaging task installs nothing.

## Program entry points

- [`evidence/attachment_orbit_crosscheck.cpp`](source/evidence/attachment_orbit_crosscheck.cpp)
- [`evidence/cycle_detector_crosscheck.cpp`](source/evidence/cycle_detector_crosscheck.cpp)
- [`evidence/excess2_lazy_sat.cpp`](source/evidence/excess2_lazy_sat.cpp)
- [`evidence/geng_excess2_search.cpp`](source/evidence/geng_excess2_search.cpp)
- [`evidence/graph6_parser_dump.cpp`](source/evidence/graph6_parser_dump.cpp)

## Portability notes

Historical program text is unchanged; these path references require review or a documented local adapter before another machine can run the relevant wrapper:

- No machine-specific path detected in archived program text.

Do not bypass a binary-hash/provenance assertion and call the historical run reproduced. See [collection reproduction notes](../REPRODUCTION_NOTES.md) for specific tools and limitations. Historical `publication.json` and claim/audit records are provenance, not ready-made manifests of this reorganized subset; primary-source downloads, environment directories, compiled binaries and old PDFs are deliberately omitted.

[Matching LaTeX](../../../latex_source_code/BigMac2/BM2-B19-P02/) · [Per-file hashes and storage map](package.json) · [Omitted files](../../../assets/BigMac2/gates/BM2-B19-P02/omitted-files.json)

<!-- BEGIN PACKAGING REPLAY -->
## Actual packaging check

Not rerun during packaging: No short positive exact checker selected; see archived source/proof dossier. No cheap complete proof replay. C++17 search uses nauty geng input streams; exhaustive nonexistence audit records are short evidence/pass2_A_m{0,1,2}.log. Keep them. Crosscheck C++ files include geng_excess2_search.cpp relatively. Avoid rerunning full graph streams. Large A_m0_test.cnf/.cycles are discovery data, preserve gzip if including.

<!-- END PACKAGING REPLAY -->
