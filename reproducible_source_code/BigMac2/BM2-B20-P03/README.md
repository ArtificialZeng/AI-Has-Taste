# BM2-B20-P03 — reproduction source and evidence

Three Probes Suffice for Directional Localization on the Three-Cube

[Final PDF](../../../pdfs/BigMac2/BM2-B20-P03_Three_Probes_Suffice_for_Directional_Localization_on_the_Three_Cube.pdf) · [Catalog](../../../README.md#bigmac2) · [Gate provenance](../../../assets/BigMac2/gates/BM2-B20-P03/packaging-review.json)

## Mathematical scope

Proof of the frozen original statement. For the Jones--Kinnersley partial-feedback directional localization game on Q_3 frozen in source.md and read precisely in problem.md (simultaneous ordered probes, one adversarial legal shortest-path neighbor returned per probe, and a stay-or-one-edge robber move after each unresolved round), zeta_d(Q_3)=3. More precisely, the explicit strategy in evidence/proof.md guarantees localization with three cops within two probing rounds.

## Reproduction coverage

Archived scientific programs and exact evidence; all original bytes preserved. Full computations not rerun during packaging.

The package contains 11 scientific source/evidence files, including 2 programs. Exact certificates, source/problem statements and independent verifier programs are included where archived. Search experiments and negative tests are not automatically proof validators. A file hash or syntax check is not mathematical verification.

## Prepare a working copy

Some large generated certificates are stored with lossless gzip compression (0 files). Do not run code against compressed filenames. From the repository root:

```sh
python3 reproducible_source_code/BigMac2/prepare.py BM2-B20-P03 --output /path/to/new-working-directory
```

This copies the selected source tree and decompresses data while verifying original SHA-256 hashes. The output must be a new directory. Run programs in that working copy, from the working directory specified by the individual script, to avoid changing the archive.

Python 3.12+ is recommended. Detected direct third-party imports: none (standard library for the archived Python programs). The optional requirements.txt records names, not a reproduced historical environment. C/C++ code and external tools (for example nauty, SAT solvers or Singular) must be rebuilt/installed separately when the script requires them. This packaging task installs nothing.

## Program entry points

- [`evidence/check_q3_certificate.py`](source/evidence/check_q3_certificate.py)
- [`evidence/solve_q3.py`](source/evidence/solve_q3.py)

## Portability notes

Historical program text is unchanged; these path references require review or a documented local adapter before another machine can run the relevant wrapper:

- No machine-specific path detected in archived program text.

Do not bypass a binary-hash/provenance assertion and call the historical run reproduced. See [collection reproduction notes](../REPRODUCTION_NOTES.md) for specific tools and limitations. Historical `publication.json` and claim/audit records are provenance, not ready-made manifests of this reorganized subset; primary-source downloads, environment directories, compiled binaries and old PDFs are deliberately omitted.

[Matching LaTeX](../../../latex_source_code/BigMac2/BM2-B20-P03/) · [Per-file hashes and storage map](package.json) · [Omitted files](../../../assets/BigMac2/gates/BM2-B20-P03/omitted-files.json)

<!-- BEGIN PACKAGING REPLAY -->
## Actual packaging check

Bounded replay passed; Finite exact supporting checks only; consult the proof dossier for the full quantified claim.

```sh
python3 evidence/check_q3_certificate.py
```

<!-- END PACKAGING REPLAY -->
