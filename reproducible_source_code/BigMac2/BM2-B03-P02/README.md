# BM2-B03-P02 — reproduction source and evidence

Attained Three-Point Moment Selection for Five Labels with Direction Multiplicities 3+1+1

[Final PDF](../../../pdfs/BigMac2/BM2-B03-P02_Attained_Three_Point_Moment_Selection_for_Five_Labels_with_Direction_Multiplicities_3_1_1.pdf) · [Catalog](../../../README.md#bigmac2) · [Gate provenance](../../../assets/BigMac2/gates/BM2-B03-P02/packaging-review.json)

## Mathematical scope

Partial result; original problem unresolved. For every five-label finite moment system satisfying the frozen hypotheses whose unit directions take exactly three distinct values with multiplicities 3, 1, and 1, there exists an admissible probability vector q supported on at most three labels such that C(q) <= 5E/8.

## Reproduction coverage

Archived scientific programs and exact evidence; all original bytes preserved. Full computations not rerun during packaging.

The package contains 11 scientific source/evidence files, including 2 programs. Exact certificates, source/problem statements and independent verifier programs are included where archived. Search experiments and negative tests are not automatically proof validators. A file hash or syntax check is not mathematical verification.

## Prepare a working copy

Some large generated certificates are stored with lossless gzip compression (0 files). Do not run code against compressed filenames. From the repository root:

```sh
python3 reproducible_source_code/BigMac2/prepare.py BM2-B03-P02 --output /path/to/new-working-directory
```

This copies the selected source tree and decompresses data while verifying original SHA-256 hashes. The output must be a new directory. Run programs in that working copy, from the working directory specified by the individual script, to avoid changing the archive.

Python 3.12+ is recommended. Detected direct third-party imports: none (standard library for the archived Python programs). The optional requirements.txt records names, not a reproduced historical environment. C/C++ code and external tools (for example nauty, SAT solvers or Singular) must be rebuilt/installed separately when the script requires them. This packaging task installs nothing.

## Program entry points

- [`evidence/explore_311_segments.py`](source/evidence/explore_311_segments.py)
- [`evidence/explore_five.py`](source/evidence/explore_five.py)

## Portability notes

Historical program text is unchanged; these path references require review or a documented local adapter before another machine can run the relevant wrapper:

- No machine-specific path detected in archived program text.

Do not bypass a binary-hash/provenance assertion and call the historical run reproduced. See [collection reproduction notes](../REPRODUCTION_NOTES.md) for specific tools and limitations. Historical `publication.json` and claim/audit records are provenance, not ready-made manifests of this reorganized subset; primary-source downloads, environment directories, compiled binaries and old PDFs are deliberately omitted.

[Matching LaTeX](../../../latex_source_code/BigMac2/BM2-B03-P02/) · [Per-file hashes and storage map](package.json) · [Omitted files](../../../assets/BigMac2/gates/BM2-B03-P02/omitted-files.json)

<!-- BEGIN PACKAGING REPLAY -->
## Actual packaging check

Not rerun during packaging: No short positive exact checker selected; see archived source/proof dossier. Only floating discovery searches are archived as Python. The proof is in Markdown/LaTeX; no positive exact checker offered.

<!-- END PACKAGING REPLAY -->
