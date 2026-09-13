# BM2-B29-P13 — reproduction source and evidence

The Least Residue-Choice Incompatibility Layer for Finite Survivor Sets: A Complete Classification

[Final PDF](../../../pdfs/BigMac2/BM2-B29-P13_The_Least_Residue_Choice_Incompatibility_Layer_for_Finite_Survivor_Sets_A_Complete_Classification.pdf) · [Catalog](../../../README.md#bigmac2) · [Gate provenance](../../../assets/BigMac2/gates/BM2-B29-P13/packaging-review.json)

## Mathematical scope

Partial result; original problem unresolved. For the finite problem precisely defined in problem.md, the least genuine residue-choice incompatibility layer is n_*=24, and the complete literal exception family is G_24={{2} union T : T is a subset of {8,14,20}}; equivalently, G_n is empty for every 1<=n<24 and G_24 consists of exactly eight sets.

## Reproduction coverage

Archived scientific programs and exact evidence; all original bytes preserved. Full computations not rerun during packaging. Some historical wrappers contain machine-specific paths; see the per-package instructions before replay.

The package contains 13 scientific source/evidence files, including 5 programs. Exact certificates, source/problem statements and independent verifier programs are included where archived. Search experiments and negative tests are not automatically proof validators. A file hash or syntax check is not mathematical verification.

## Prepare a working copy

Some large generated certificates are stored with lossless gzip compression (1 files). Do not run code against compressed filenames. From the repository root:

```sh
python3 reproducible_source_code/BigMac2/prepare.py BM2-B29-P13 --output /path/to/new-working-directory
```

This copies the selected source tree and decompresses data while verifying original SHA-256 hashes. The output must be a new directory. Run programs in that working copy, from the working directory specified by the individual script, to avoid changing the archive.

Python 3.12+ is recommended. Detected direct third-party imports: none (standard library for the archived Python programs). The optional requirements.txt records names, not a reproduced historical environment. C/C++ code and external tools (for example nauty, SAT solvers or Singular) must be rebuilt/installed separately when the script requires them. This packaging task installs nothing.

## Program entry points

- [`audit/referee_replay.py`](source/audit/referee_replay.py)
- [`evidence/find_first_incompatibility.py`](source/evidence/find_first_incompatibility.py)
- [`evidence/independent_audit.py`](source/evidence/independent_audit.py)
- [`evidence/prop36_generator.py`](source/evidence/prop36_generator.py)
- [`evidence/theorem30_csp.py`](source/evidence/theorem30_csp.py)

## Portability notes

Historical program text is unchanged; these path references require review or a documented local adapter before another machine can run the relevant wrapper:

- `audit/referee_replay.py` (lines 1)
- `evidence/find_first_incompatibility.py` (lines 1)
- `evidence/independent_audit.py` (lines 1)
- `evidence/prop36_generator.py` (lines 1)
- `evidence/theorem30_csp.py` (lines 1)

Do not bypass a binary-hash/provenance assertion and call the historical run reproduced. See [collection reproduction notes](../REPRODUCTION_NOTES.md) for specific tools and limitations. Historical `publication.json` and claim/audit records are provenance, not ready-made manifests of this reorganized subset; primary-source downloads, environment directories, compiled binaries and old PDFs are deliberately omitted.

[Matching LaTeX](../../../latex_source_code/BigMac2/BM2-B29-P13/) · [Per-file hashes and storage map](package.json) · [Omitted files](../../../assets/BigMac2/gates/BM2-B29-P13/omitted-files.json)

<!-- BEGIN PACKAGING REPLAY -->
## Actual packaging check

Bounded replay passed; Finite exact supporting checks only; consult the proof dossier for the full quantified claim.

```sh
python3 evidence/independent_audit.py
```

<!-- END PACKAGING REPLAY -->
