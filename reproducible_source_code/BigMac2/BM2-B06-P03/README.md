# BM2-B06-P03 — reproduction source and evidence

An Exact Counterexample to a Modulo-Five Congruence for b̄²₄,₄

[Final PDF](../../../pdfs/BigMac2/BM2-B06-P03_An_Exact_Counterexample_to_a_Modulo_Five_Congruence_for_b24_4.pdf) · [Catalog](../../../README.md#bigmac2) · [Gate provenance](../../../assets/BigMac2/gates/BM2-B06-P03/packaging-review.json)

## Mathematical scope

Disproof of the frozen original statement. Let F(q)=prod_{m>=1}(1-q^(2m))^8(1-q^m)^(-16)=sum_{N>=0} b(N)q^N in Z[[q]]. Then b(5)=25056, so b(5) is congruent to 1 modulo 5. Hence n=1 is an exact counterexample to, and disproves, the frozen claim that b(5n) is congruent to 0 modulo 5 for every integer n>=1.

## Reproduction coverage

Archived scientific programs and exact evidence; all original bytes preserved. Full computations not rerun during packaging.

The package contains 22 scientific source/evidence files, including 3 programs. Exact certificates, source/problem statements and independent verifier programs are included where archived. Search experiments and negative tests are not automatically proof validators. A file hash or syntax check is not mathematical verification.

## Prepare a working copy

Some large generated certificates are stored with lossless gzip compression (0 files). Do not run code against compressed filenames. From the repository root:

```sh
python3 reproducible_source_code/BigMac2/prepare.py BM2-B06-P03 --output /path/to/new-working-directory
```

This copies the selected source tree and decompresses data while verifying original SHA-256 hashes. The output must be a new directory. Run programs in that working copy, from the working directory specified by the individual script, to avoid changing the archive.

Python 3.12+ is recommended. Detected direct third-party imports: none (standard library for the archived Python programs). The optional requirements.txt records names, not a reproduced historical environment. C/C++ code and external tools (for example nauty, SAT solvers or Singular) must be rebuilt/installed separately when the script requires them. This packaging task installs nothing.

## Program entry points

- [`audit/release-validation.py`](source/audit/release-validation.py)
- [`evidence/research_b5_independent.py`](source/evidence/research_b5_independent.py)
- [`evidence/triage_b5.py`](source/evidence/triage_b5.py)

## Portability notes

Historical program text is unchanged; these path references require review or a documented local adapter before another machine can run the relevant wrapper:

- No machine-specific path detected in archived program text.

Do not bypass a binary-hash/provenance assertion and call the historical run reproduced. See [collection reproduction notes](../REPRODUCTION_NOTES.md) for specific tools and limitations. Historical `publication.json` and claim/audit records are provenance, not ready-made manifests of this reorganized subset; primary-source downloads, environment directories, compiled binaries and old PDFs are deliberately omitted.

[Matching LaTeX](../../../latex_source_code/BigMac2/BM2-B06-P03/) · [Per-file hashes and storage map](package.json) · [Omitted files](../../../assets/BigMac2/gates/BM2-B06-P03/omitted-files.json)

<!-- BEGIN PACKAGING REPLAY -->
## Actual packaging check

Bounded replay passed; Independent code is finite evidence supporting the analytic theorem; finite checks are not an infinite proof.

```sh
python3 evidence/research_b5_independent.py
```

<!-- END PACKAGING REPLAY -->
