# BM2-B15-P02 — reproduction source and evidence

Critical First Sign Failure of Even Cumulants for the Blume–Capel Single-Site Law

[Final PDF](../../../pdfs/BigMac2/BM2-B15-P02_Critical_First_Sign_Failure_of_Even_Cumulants_for_the_BlumeCapel_Single_Site_Law.pdf) · [Catalog](../../../README.md#bigmac2) · [Gate provenance](../../../assets/BigMac2/gates/BM2-B15-P02/packaging-review.json)

## Mathematical scope

Proof of the frozen original statement. For every Δ>log 2, let q=2e^(−Δ)/(1+2e^(−Δ)), let κ_j be the j-th derivative at zero of log(1−q+q cosh z), and let m_*(Δ)=min{m≥2: (−1)^(m+1)κ_(2m)(q)<0}. This minimum exists. If a=arcosh(e^Δ/2), β=arctan(a/π), and t=π/(4β), then for all sufficiently small a>0 one has t<m_*(Δ)≤ceil(t+1)<t+2. Consequently a m_*(Δ)→π²/4 as Δ↓log 2, equivalently lim_(ε↓0) sqrt(ε)m_*(log 2+ε)=π²/(4sqrt(2)).

## Reproduction coverage

Archived scientific programs and exact evidence; all original bytes preserved. Full computations not rerun during packaging.

The package contains 8 scientific source/evidence files, including 1 programs. Exact certificates, source/problem statements and independent verifier programs are included where archived. Search experiments and negative tests are not automatically proof validators. A file hash or syntax check is not mathematical verification.

## Prepare a working copy

Some large generated certificates are stored with lossless gzip compression (0 files). Do not run code against compressed filenames. From the repository root:

```sh
python3 reproducible_source_code/BigMac2/prepare.py BM2-B15-P02 --output /path/to/new-working-directory
```

This copies the selected source tree and decompresses data while verifying original SHA-256 hashes. The output must be a new directory. Run programs in that working copy, from the working directory specified by the individual script, to avoid changing the archive.

Python 3.12+ is recommended. Detected direct third-party imports: none (standard library for the archived Python programs). The optional requirements.txt records names, not a reproduced historical environment. C/C++ code and external tools (for example nauty, SAT solvers or Singular) must be rebuilt/installed separately when the script requires them. This packaging task installs nothing.

## Program entry points

- [`evidence/exact_recurrence.py`](source/evidence/exact_recurrence.py)

## Portability notes

Historical program text is unchanged; these path references require review or a documented local adapter before another machine can run the relevant wrapper:

- No machine-specific path detected in archived program text.

Do not bypass a binary-hash/provenance assertion and call the historical run reproduced. See [collection reproduction notes](../REPRODUCTION_NOTES.md) for specific tools and limitations. Historical `publication.json` and claim/audit records are provenance, not ready-made manifests of this reorganized subset; primary-source downloads, environment directories, compiled binaries and old PDFs are deliberately omitted.

[Matching LaTeX](../../../latex_source_code/BigMac2/BM2-B15-P02/) · [Per-file hashes and storage map](package.json) · [Omitted files](../../../assets/BigMac2/gates/BM2-B15-P02/omitted-files.json)

<!-- BEGIN PACKAGING REPLAY -->
## Actual packaging check

Bounded replay passed; N=1,2,10 is a bounded smoke test, not all archived default cases. No change to claimed analytic scope.

```sh
python3 evidence/exact_recurrence.py 1 2 10
```

<!-- END PACKAGING REPLAY -->
