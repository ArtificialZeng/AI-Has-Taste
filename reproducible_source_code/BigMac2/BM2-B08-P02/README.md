# BM2-B08-P02 — reproduction source and evidence

Time-Eight Positive-Sojourn Classification for Arbitrary Two-State Unitary Coins

[Final PDF](../../../pdfs/BigMac2/BM2-B08-P02_Time_Eight_Positive_Sojourn_Classification_for_Arbitrary_Two_State_Unitary_Coins.pdf) · [Catalog](../../../README.md#bigmac2) · [Gate provenance](../../../assets/BigMac2/gates/BM2-B08-P02/packaging-review.json)

## Mathematical scope

Proof of the frozen original statement. For the frozen positive-sojourn-time experiment with phi_*=(1,i)^T/sqrt(2), the complete solution set is S={D (1/sqrt(2))[[1,z],[1,-z]] : D is diagonal unitary and |z|=1}. For every such coin the only nonzero time-eight weights are w_8(2)=w_8(4)=w_8(6)=1/128, so R_8=3/128. The full zero-return locus is exactly the diagonal coins. Under left-diagonal gauge and ordinary unitary changes of internal basis that preserve the ordered chirality projectors and the fixed initial ray, z remains a full circle invariant and H_left is only z=1; right diagonal multiplication is not an experiment symmetry. If antiunitary basis changes are admitted, the sole additional nontrivial setup symmetry identifies z with -conjugate(z). Thus all solutions are complex Hadamard matrices in the entry-modulus sense, but the stronger claim that every allowed-equivalence class meets H_left is false.

## Reproduction coverage

Archived scientific programs and exact evidence; all original bytes preserved. Full computations not rerun during packaging.

The package contains 8 scientific source/evidence files, including 2 programs. Exact certificates, source/problem statements and independent verifier programs are included where archived. Search experiments and negative tests are not automatically proof validators. A file hash or syntax check is not mathematical verification.

## Prepare a working copy

Some large generated certificates are stored with lossless gzip compression (0 files). Do not run code against compressed filenames. From the repository root:

```sh
python3 reproducible_source_code/BigMac2/prepare.py BM2-B08-P02 --output /path/to/new-working-directory
```

This copies the selected source tree and decompresses data while verifying original SHA-256 hashes. The output must be a new directory. Run programs in that working copy, from the working directory specified by the individual script, to avoid changing the archive.

Python 3.12+ is recommended. Detected direct third-party imports: none (standard library for the archived Python programs). The optional requirements.txt records names, not a reproduced historical environment. C/C++ code and external tools (for example nauty, SAT solvers or Singular) must be rebuilt/installed separately when the script requires them. This packaging task installs nothing.

## Program entry points

- [`audit/referee_recheck.py`](source/audit/referee_recheck.py)
- [`evidence/time8_exact.py`](source/evidence/time8_exact.py)

## Portability notes

Historical program text is unchanged; these path references require review or a documented local adapter before another machine can run the relevant wrapper:

- No machine-specific path detected in archived program text.

Do not bypass a binary-hash/provenance assertion and call the historical run reproduced. See [collection reproduction notes](../REPRODUCTION_NOTES.md) for specific tools and limitations. Historical `publication.json` and claim/audit records are provenance, not ready-made manifests of this reorganized subset; primary-source downloads, environment directories, compiled binaries and old PDFs are deliberately omitted.

[Matching LaTeX](../../../latex_source_code/BigMac2/BM2-B08-P02/) · [Per-file hashes and storage map](package.json) · [Omitted files](../../../assets/BigMac2/gates/BM2-B08-P02/omitted-files.json)

<!-- BEGIN PACKAGING REPLAY -->
## Actual packaging check

Bounded replay passed; Finite exact supporting checks only; consult the proof dossier for the full quantified claim.

```sh
python3 evidence/time8_exact.py
```

<!-- END PACKAGING REPLAY -->
