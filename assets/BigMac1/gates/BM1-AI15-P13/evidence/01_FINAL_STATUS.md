# Final status: DISPROVED

Terminal date: 2026-08-29 (Asia/Shanghai)

## Verdict

The natural uniform, condition-number-only form of the
Hashemi--Nakatsukasa conjecture is false for the literal fixed-precision
SM--IR Algorithm 2.

For radix-two precision `p` with round-to-nearest/ties-to-even, take

\[
A=[1],\qquad u=b=[1],\qquad v=[2^p].
\]

The exact updated coefficient is `B=[2^p+1]`, so both exact 2-norm condition
numbers are one. Yet

\[
\operatorname{RN}_{\rm even}(2^p+1)=2^p.
\]

The initial Sherman--Morrison solve therefore returns zero. At zero the
source-ordered split residual is exactly one, while the reused SM corrector
returns zero. Hence `x_k=0` for every iteration by induction, and the normwise
and componentwise relative backward errors are exactly one. Since
`eta/epsilon_p=2^p`, no precision-independent `O(epsilon_p)` constant can
absorb this family.

The nondegenerate embedding

\[
A_p=\operatorname{diag}(1,2^{\lfloor p/2\rfloor}),\qquad
u_p=b_p=e_1,\qquad v_p=2^p e_1
\]

has the same fixed point and error, while

\[
\epsilon_p\kappa_2(A_p)\to0,
\qquad
\epsilon_p\kappa_2(A_p+u_pv_p^T)\to0.
\]

Thus the obstruction is not scalar degeneracy and satisfies the conjecture's
stated condition-number safety regime asymptotically.

## Certified evidence

- Exact proof and structural reduction: `proof/main_proof.md`.
- Binary64 certificates: `certificates/binary64_stagnation.json` and
  `certificates/binary64_stagnation_2x2.json`.
- Strict integer/`Fraction` verifiers: `verification/verify_stagnation.py` and
  `verification/verify_stagnation_2x2.py`.
- Main certificate/verifier SHA-256:
  `28c6865ee1d22bf1def7565758fc3ddb254563be31ef69d3e1578a8180366eea` /
  `49c359401a23ca036108667e1ea22802c6266641498330b9daa88c7102467385`.
- 2-by-2 certificate/verifier SHA-256:
  `662374272407d01b56fd18c86153d7fdfc69508a1cbbab0a51026524948c6e9a` /
  `0969a71fb3e8f6579557b565f648ddf94f03d818cf7545c25cd22d6b1d9be2dd`.
- Independent IEEE binary64 hardware trace:
  `verification/verify_stagnation_hardware.c`.

The verifiers enforce exact keys and exact types at every certificate object,
reject duplicate keys and nonstandard JSON constants, pin the certificate
hash, and recompute the system and trace. The root tamper suite reports
nonzero exits for bad hash, extra key, dropped key, changed input, changed
trace, changed arithmetic, and six additional malformed/semantic attacks. An
independent hostile audit rejected all 132 generated mutations. See
`audit/TAMPER_AUDIT.md`.

The referee independently rebuilt Algorithms 1--2 from the downloaded source,
including the residual operation graph and both natural associations of the
correction addition. The fixed point survives both associations, ordinary
nonzero-denominator guards, and FMA evaluation. See
`audit/REFEREE_OPERATION_ORDER.md`.

## Reproduction

From the project root:

```bash
python3 verification/verify_stagnation.py \
  certificates/binary64_stagnation.json
python3 verification/verify_stagnation_2x2.py \
  certificates/binary64_stagnation_2x2.json
python3 verification/test_tamper_fail_closed.py
cc -std=c11 -O0 -frounding-math -ffp-contract=off \
  verification/verify_stagnation_hardware.c -lm \
  -o verification/verify_stagnation_hardware
./verification/verify_stagnation_hardware \
  certificates/binary64_stagnation.json
cd paper && latexmk -C && \
  latexmk -pdf -interaction=nonstopmode -halt-on-error main.tex
```

The final source ZIP was independently unpacked into a fresh temporary
directory, and all exact, tamper, hardware, independent-verifier, BibTeX, and
LaTeX checks passed there. See `audit/CLEAN_REPRODUCIBILITY.md`.

## Novelty, citations, and release audits

The initial novelty lock, second pass, and release-refresh search found no
prior proof or counterexample in the named databases and queries through
2026-08-29. This is bounded search evidence, not a claim of absolute novelty;
see `literature/search_log.md` and `literature/claim_ledger.md`.

The one cited paper was independently verified against arXiv, its downloaded
PDF/source, the arXiv API, and DataCite. Citation counts are one cited, one in
the bibliography, zero missing, zero unused. Primary-source byte hashes are
frozen in `audit/SOURCE_INTEGRITY.md`.

The final LaTeX build is clean. All six pages were rendered and inspected;
there are no observed clipping, overlap, missing glyphs, anomalous blanks, or
log warnings. `paper/main.pdf` and the release PDF are byte-identical.

## Release artifacts

- PDF SHA-256:
  `24dabee471d37e8995e58ec9010f6873a131d7bd587a7a5e54fca0a4823e931e`.
- Source ZIP SHA-256:
  `cf351d07c859a591a635d8833f9fbfbef50e164b2b7185628437a83149a846f1`.
- `release_manifest.json` binds the final project files and is checked by the
  independent manifest verifier.

## Exact scope and open repaired conjecture

This result refutes only the original broad condition-number-only conjecture
under its standard uniform interpretation, plus the source paper's concrete
binary64 `5 epsilon` experimental threshold. It does not contradict the
paper's conditional one-step results.

A genuinely repaired conjecture that adds scale-sensitive no-lost-addend or
uniform correction-contraction guards, extra-precision recomputation, explicit
formation of the updated matrix, or a stable fallback remains open. A mere
`beta != 0` breakdown test and FMA use do not exclude this example.

## Proof-assistant disclosure

No proof assistant was used. No SAT/SMT, CAD, Groebner, Sturm, or computer
algebra system was used for the terminal proof. Numerical search contributed
only to discovery; all decisive claims rest on exact arithmetic, finite
serialized certificates, direct identities, and induction.
