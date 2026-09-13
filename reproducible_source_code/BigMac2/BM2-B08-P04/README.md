# BM2-B08-P04 — reproduction source and evidence

A Degree-Four Boundary for the v-Number under Integral Closure

[Final PDF](../../../pdfs/BigMac2/BM2-B08-P04_A_Degree_Four_Boundary_for_the_v_Number_under_Integral_Closure.pdf) · [Catalog](../../../README.md#bigmac2) · [Gate provenance](../../../assets/BigMac2/gates/BM2-B08-P04/packaging-review.json)

## Mathematical scope

Proof of the frozen original statement. Let K be any field and let I be a proper (x,y,z)-primary monomial ideal in K[x,y,z]. If the unique minimal monomial generating set of I has at most four members and every such member has total degree at most four, then v(overline(I)) <= v(I), with v-number and integral-closure conventions exactly as frozen in source.md and problem.md.

## Reproduction coverage

Archived scientific programs and exact evidence; all original bytes preserved. Full computations not rerun during packaging.

The package contains 14 scientific source/evidence files, including 4 programs. Exact certificates, source/problem statements and independent verifier programs are included where archived. Search experiments and negative tests are not automatically proof validators. A file hash or syntax check is not mathematical verification.

## Prepare a working copy

Some large generated certificates are stored with lossless gzip compression (2 files). Do not run code against compressed filenames. From the repository root:

```sh
python3 reproducible_source_code/BigMac2/prepare.py BM2-B08-P04 --output /path/to/new-working-directory
```

This copies the selected source tree and decompresses data while verifying original SHA-256 hashes. The output must be a new directory. Run programs in that working copy, from the working directory specified by the individual script, to avoid changing the archive.

Python 3.12+ is recommended. Detected direct third-party imports: none (standard library for the archived Python programs). The optional requirements.txt records names, not a reproduced historical environment. C/C++ code and external tools (for example nauty, SAT solvers or Singular) must be rebuilt/installed separately when the script requires them. This packaging task installs nothing.

## Program entry points

- [`audit/referee_independent.py`](source/audit/referee_independent.py)
- [`evidence/compare_runs.py`](source/evidence/compare_runs.py)
- [`evidence/enumerate_facets.py`](source/evidence/enumerate_facets.py)
- [`evidence/enumerate_lp.py`](source/evidence/enumerate_lp.py)

## Portability notes

Historical program text is unchanged; these path references require review or a documented local adapter before another machine can run the relevant wrapper:

- No machine-specific path detected in archived program text.

Do not bypass a binary-hash/provenance assertion and call the historical run reproduced. See [collection reproduction notes](../REPRODUCTION_NOTES.md) for specific tools and limitations. Historical `publication.json` and claim/audit records are provenance, not ready-made manifests of this reorganized subset; primary-source downloads, environment directories, compiled binaries and old PDFs are deliberately omitted.

[Matching LaTeX](../../../latex_source_code/BigMac2/BM2-B08-P04/) · [Per-file hashes and storage map](package.json) · [Omitted files](../../../assets/BigMac2/gates/BM2-B08-P04/omitted-files.json)

<!-- BEGIN PACKAGING REPLAY -->
## Actual packaging check

Not rerun during packaging: Exact Fourier-Motzkin elimination can expand substantially; not selected for short smoke execution. Referee checker is a fresh exact implementation; review its archived input expectations before running a copied subset.

```sh
python3 audit/referee_independent.py
```

<!-- END PACKAGING REPLAY -->
