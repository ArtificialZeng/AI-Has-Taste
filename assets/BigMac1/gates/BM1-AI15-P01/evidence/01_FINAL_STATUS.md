# Final status: DISPROVED

## Exact endpoint

The proposed matrix-specific assertion

\[
\nexists A,B\in\mathbb R^{4\times4}:\quad
A\circ B=M,\qquad \operatorname{rank}A,\operatorname{rank}B\le2
\]

is false. In fact the displayed matrix has rational factors of rank exactly
two. A short witness is

\[
A=\begin{pmatrix}
1&1&1&1\\1&2&3&3\\-2&-1&0&0\\-2&-1&0&0
\end{pmatrix},\qquad
B=\begin{pmatrix}
1&1&1&1\\1&\tfrac12&\tfrac13&0\\
0&-1&-\tfrac43&-2\\-\tfrac12&0&\tfrac16&\tfrac12
\end{pmatrix}.
\]

Directly, \(A\circ B=M\). Moreover
\(A_3=A_4=A_2-3A_1\),
\(B_3=2B_2-2B_1\), and
\(B_4=-B_2+\tfrac12B_1\), while each factor has a nonzero
\(2\times2\) minor. Hence both ranks equal two. The project also contains a
three-parameter family and two additional independently derived witnesses.

## Limitation

This terminal status disproves only the claim that the specified candidate is
a real counterexample. It does not decide whether every invertible real
\(4\times4\) matrix is rank-(2,2) Hadamard expressible, and it does not refute
an integer-only restriction on both factors.

## Reproduction

```bash
python verifier/run_all.py --fast
python verifier/run_all.py
python /Users/mac/.codex/skills/prove-or-disprove-math/scripts/audit_latex.py \
  paper/main.tex paper/references.bib
```

All exact verifiers pass. The LaTeX audit reports
`cited=1 bib=1 missing=0 unused=0`; the final clean TeX log has no warnings,
undefined references, or overfull/underfull boxes. All three PDF pages were
rendered and visually inspected.

The corrected source ZIP is built from an explicit 28-file whitelist and has
SHA-256
`10a4d0fe5c1f6389a904af683272e81782a47612c4c038138df28e79eefc1d1a`.
It contains no Python bytecode/cache or temporary entry.  From a fresh ZIP
extraction, three exact verifiers pass under `python3 -I`; changing
`A[0][0]` to 2 exits 1 with `A != U V`; LaTeX citation audit and a warning-free
three-page clean build pass.  Rebuilt PDF text equals the released PDF text.

## Evidence and audits

- Human proof: `proof/exact_disproof.md`
- Canonical certificate: `certificates/builder_counterexample.json`
- Canonical verifier: `certificates/builder_verify_counterexample.py`
- Independent breaker certificate/verifier: `certificates/breaker_decomposition.json`, `certificates/breaker_verify.py`
- Proof audit: `audit/PROOF_AUDIT.md`
- Referee report: `audit/referee_notes.md`
- Novelty lock: `literature/NOVELTY_LOCK.md`
- Citation audit: `audit/CITATION_AUDIT.md`
- PDF audit: `audit/PDF_AUDIT.md`
- Release portability audit: `audit/RELEASE_PORTABILITY_AUDIT.md`
- Manuscript: `paper/main.tex`
- Final PDF: `output/pdf/hadamard_rank22_rational_factorization.pdf`
- LaTeX/source bundle: `release/hadamard_rank22_rational_factorization_source.zip`
- Release manifest: `release/MANIFEST.json`

No Lean, Coq, Isabelle, or other proof assistant was used.
