# BM2-B10-P03 — reproduction source and evidence

Inverse-Weight Lin–Lu–Yau Curvature on a Weighted Triangle: Exact Interior Fixed Points and a Nonuniform Stationary Metric

[Final PDF](../../../pdfs/BigMac2/BM2-B10-P03_Inverse_Weight_LinLuYau_Curvature_on_a_Weighted_Triangle_Exact_Interior_Fixed_Points_and_a_Nonuniform_Stationary_Metric.pdf) · [Catalog](../../../README.md#bigmac2) · [Gate provenance](../../../assets/BigMac2/gates/BM2-B10-P03/packaging-review.json)

## Mathematical scope

Partial result; original problem unresolved. For the inverse-weight Lin--Lu--Yau curvature and normalized flow on C3 fixed in source.md and problem.md, the curvature vector is given exactly by equations (4) and (5) of evidence/curvature_fixed_points.md in the four shortest-path chambers, with componentwise wall agreement. The complete positive normalized fixed-point set is the uniform point together with all permutations of (r,1,1)/(r+2) for r >= 2. In particular, (2/3,1/6,1/6) is a strict-chamber fixed point with singleton omega-limit set and disproves universal convergence to the uniform metric. No claim is made here about omega limits of non-fixed initial data.

## Reproduction coverage

Archived scientific programs and exact evidence; all original bytes preserved. Full computations not rerun during packaging.

The package contains 7 scientific source/evidence files, including 1 programs. Exact certificates, source/problem statements and independent verifier programs are included where archived. Search experiments and negative tests are not automatically proof validators. A file hash or syntax check is not mathematical verification.

## Prepare a working copy

Some large generated certificates are stored with lossless gzip compression (0 files). Do not run code against compressed filenames. From the repository root:

```sh
python3 reproducible_source_code/BigMac2/prepare.py BM2-B10-P03 --output /path/to/new-working-directory
```

This copies the selected source tree and decompresses data while verifying original SHA-256 hashes. The output must be a new directory. Run programs in that working copy, from the working directory specified by the individual script, to avoid changing the archive.

Python 3.12+ is recommended. Detected direct third-party imports: none (standard library for the archived Python programs). The optional requirements.txt records names, not a reproduced historical environment. C/C++ code and external tools (for example nauty, SAT solvers or Singular) must be rebuilt/installed separately when the script requires them. This packaging task installs nothing.

## Program entry points

- [`evidence/check_curvature.py`](source/evidence/check_curvature.py)

## Portability notes

Historical program text is unchanged; these path references require review or a documented local adapter before another machine can run the relevant wrapper:

- No machine-specific path detected in archived program text.

Do not bypass a binary-hash/provenance assertion and call the historical run reproduced. See [collection reproduction notes](../REPRODUCTION_NOTES.md) for specific tools and limitations. Historical `publication.json` and claim/audit records are provenance, not ready-made manifests of this reorganized subset; primary-source downloads, environment directories, compiled binaries and old PDFs are deliberately omitted.

[Matching LaTeX](../../../latex_source_code/BigMac2/BM2-B10-P03/) · [Per-file hashes and storage map](package.json) · [Omitted files](../../../assets/BigMac2/gates/BM2-B10-P03/omitted-files.json)

<!-- BEGIN PACKAGING REPLAY -->
## Actual packaging check

Bounded replay passed; Finite exact supporting checks only; consult the proof dossier for the full quantified claim.

```sh
python3 evidence/check_curvature.py
```

<!-- END PACKAGING REPLAY -->
