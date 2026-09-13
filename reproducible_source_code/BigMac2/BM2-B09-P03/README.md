# BM2-B09-P03 — reproduction source and evidence

The Exact Uniform Scrambling Horizon of the Order-Four Almost-Sarymsakov Class Is Eleven

[Final PDF](../../../pdfs/BigMac2/BM2-B09-P03_The_Exact_Uniform_Scrambling_Horizon_of_the_Order_Four_Almost_Sarymsakov_Class_Is_Eleven.pdf) · [Catalog](../../../README.md#bigmac2) · [Gate provenance](../../../assets/BigMac2/gates/BM2-B09-P03/packaging-review.json)

## Mathematical scope

Proof of the frozen original statement. For the full order-four almost-Sarymsakov class A_4 with the single fixed ordering and definitions frozen in problem.md, the exact uniform scrambling horizon is h_scr(A_4)=11. Every product of 11 admitted stochastic matrices is scrambling for every choice of positive supported weights. Sharpness is witnessed by the ten admitted Boolean supports a126, 423a, c586, a215, 4643, 21a6, 42a3, 9368, 3126, 2345 (listed as P_1 through P_10 in the row-packed hexadecimal encoding of evidence/computation_notes.md): their product P_10...P_1 is 17ef, whose second and fourth row supports are disjoint. The upper bound is certified by complete enumeration of all 15^4 row-nonempty supports, exact admission tests at levels 1 through 4, and exact Boolean-product reachability; the nonscrambling frontier has 120 states at length 10 and is empty at length 11.

## Reproduction coverage

Archived scientific programs and exact evidence; all original bytes preserved. Full computations not rerun during packaging.

The package contains 11 scientific source/evidence files, including 2 programs. Exact certificates, source/problem statements and independent verifier programs are included where archived. Search experiments and negative tests are not automatically proof validators. A file hash or syntax check is not mathematical verification.

## Prepare a working copy

Some large generated certificates are stored with lossless gzip compression (1 files). Do not run code against compressed filenames. From the repository root:

```sh
python3 reproducible_source_code/BigMac2/prepare.py BM2-B09-P03 --output /path/to/new-working-directory
```

This copies the selected source tree and decompresses data while verifying original SHA-256 hashes. The output must be a new directory. Run programs in that working copy, from the working directory specified by the individual script, to avoid changing the archive.

Python 3.12+ is recommended. Detected direct third-party imports: none (standard library for the archived Python programs). The optional requirements.txt records names, not a reproduced historical environment. C/C++ code and external tools (for example nauty, SAT solvers or Singular) must be rebuilt/installed separately when the script requires them. This packaging task installs nothing.

## Program entry points

- [`evidence/search_exact.cpp`](source/evidence/search_exact.cpp)
- [`evidence/verify_certificate.cpp`](source/evidence/verify_certificate.cpp)

## Portability notes

Historical program text is unchanged; these path references require review or a documented local adapter before another machine can run the relevant wrapper:

- No machine-specific path detected in archived program text.

Do not bypass a binary-hash/provenance assertion and call the historical run reproduced. See [collection reproduction notes](../REPRODUCTION_NOTES.md) for specific tools and limitations. Historical `publication.json` and claim/audit records are provenance, not ready-made manifests of this reorganized subset; primary-source downloads, environment directories, compiled binaries and old PDFs are deliberately omitted.

[Matching LaTeX](../../../latex_source_code/BigMac2/BM2-B09-P03/) · [Per-file hashes and storage map](package.json) · [Omitted files](../../../assets/BigMac2/gates/BM2-B09-P03/omitted-files.json)

<!-- BEGIN PACKAGING REPLAY -->
## Actual packaging check

Not rerun during packaging: No short positive exact checker selected; see archived source/proof dossier. C++17 verifier reconstructs entire alphabet/frontiers. Compiler invocation c++ -O3 -std=c++17 evidence/verify_certificate.cpp -o replay-verify; then ./replay-verify evidence/frontier_certificate.txt replay-report.txt. No external linked libraries.

<!-- END PACKAGING REPLAY -->
