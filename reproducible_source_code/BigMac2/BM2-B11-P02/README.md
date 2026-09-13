# BM2-B11-P02 — reproduction source and evidence

Polyregular Classification of Additive-Level Sorts with Coprime Weights of Absolute Value at Most Two

[Final PDF](../../../pdfs/BigMac2/BM2-B11-P02_Polyregular_Classification_of_Additive_Level_Sorts_with_Coprime_Weights_of_Absolute_Value_at_Most_Two.pdf) · [Catalog](../../../README.md#bigmac2) · [Gate provenance](../../../assets/BigMac2/gates/BM2-B11-P02/packaging-review.json)

## Mathematical scope

Proof of the frozen original statement. For every admissible coprime integer weight pair (u,d) with |u|,|d|<=2 and (u,d)!=(0,0), and for each tie order t in {L,R}, the additive-level sort Phi_{u,d}^t restricted to the Dyck language is realizable by a partial polyregular map if and only if u*d>=0. The supplied evidence gives an explicit one-copy MSO/regular presentation for every positive labeled case and a regular-slice pumping obstruction for every negative labeled case, covering all 32 triples under the precise interpretation in problem.md.

## Reproduction coverage

Archived scientific programs and exact evidence; all original bytes preserved. Full computations not rerun during packaging.

The package contains 8 scientific source/evidence files, including 1 programs. Exact certificates, source/problem statements and independent verifier programs are included where archived. Search experiments and negative tests are not automatically proof validators. A file hash or syntax check is not mathematical verification.

## Prepare a working copy

Some large generated certificates are stored with lossless gzip compression (0 files). Do not run code against compressed filenames. From the repository root:

```sh
python3 reproducible_source_code/BigMac2/prepare.py BM2-B11-P02 --output /path/to/new-working-directory
```

This copies the selected source tree and decompresses data while verifying original SHA-256 hashes. The output must be a new directory. Run programs in that working copy, from the working directory specified by the individual script, to avoid changing the archive.

Python 3.12+ is recommended. Detected direct third-party imports: none (standard library for the archived Python programs). The optional requirements.txt records names, not a reproduced historical environment. C/C++ code and external tools (for example nauty, SAT solvers or Singular) must be rebuilt/installed separately when the script requires them. This packaging task installs nothing.

## Program entry points

- [`evidence/verify_mixed_sign.py`](source/evidence/verify_mixed_sign.py)

## Portability notes

Historical program text is unchanged; these path references require review or a documented local adapter before another machine can run the relevant wrapper:

- No machine-specific path detected in archived program text.

Do not bypass a binary-hash/provenance assertion and call the historical run reproduced. See [collection reproduction notes](../REPRODUCTION_NOTES.md) for specific tools and limitations. Historical `publication.json` and claim/audit records are provenance, not ready-made manifests of this reorganized subset; primary-source downloads, environment directories, compiled binaries and old PDFs are deliberately omitted.

[Matching LaTeX](../../../latex_source_code/BigMac2/BM2-B11-P02/) · [Per-file hashes and storage map](package.json) · [Omitted files](../../../assets/BigMac2/gates/BM2-B11-P02/omitted-files.json)

<!-- BEGIN PACKAGING REPLAY -->
## Actual packaging check

Bounded replay passed; Finite exact supporting checks only; consult the proof dossier for the full quantified claim.

```sh
python3 evidence/verify_mixed_sign.py
```

<!-- END PACKAGING REPLAY -->
