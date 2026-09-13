# Final status: PROVED

## Conclusion

The requested \(n=5\) case of the transitive-array CYBE conjecture is proved.
In fact, the same argument proves the conjecture for every \(n\ge1\).

For \(\mathfrak h=\mathfrak g^{\oplus n}\) and
\(R=\mathbf r^{(a)}\), the ordinary residual satisfies the exact identity
\[
\operatorname{CYB}_{\mathfrak h}(R)
=\sum_{j,i,k=1}^{n}\Phi_{j,i,k}
T(a_{ij},a_{kj},a_{ki}).
\]
Transitivity at the ordered triple \((k,i,j)\) gives
\(a_{kj}\in\{a_{ij},a_{ki}\}\), so every displayed term is a defining
transitive-CYBE relation and vanishes.

## Source correction

The mathematical statement is Conjecture 1.4 in arXiv:2602.02342v1 and
Conjecture 1.5 in the current v2.  Version 2 explicitly reports the baseline
\(n\le4\).  No later public solution or formal journal publication was found
in the two dated search passes recorded in `literature/search_log.md`.

## Exact certificate and independent audit

- `certificates/transitive_arrays_n_le_5.json` contains every transitive
  equality pattern modulo color relabeling for \(2\le n\le5\).
- The requested size has 4,573 types and 571,625 ordered residual
  components.
- `verifier/verify_certificate.py` independently reconstructs the complete
  type set and fails closed.
- `verifier/verify_symbolic_expansion.py` independently reconstructs the
  three commutator expansions from ordered pairs of terms of \(R\).
- Six damaged inputs are rejected by `tests/test_verifier.py`.
- An exact integral \(\mathfrak{sl}_2\) breaker checked all 4,501 one- and
  two-color size-five types and found no residual.  This is diagnostic only;
  the theorem rests on the displayed identity.

Reproduction:

```bash
make certificate
make verify
make breaker
make audit
make build
```

The final clean run reported 4,996 total equality types, 596,974 residual
components, `cited=1 bib=1 missing=0 unused=0`, and no LaTeX warning.

## Deliverables

- Human proof: `proof/main_proof.md`
- Manuscript source: `paper/main.tex`
- Publishable PDF: `output/pdf/transitive_array_cybe_theorem.pdf`
- Source/certificate archive: `output/source/transitive_array_cybe_theorem_source.zip`
- Proof audit: `audit/PROOF_AUDIT.md`
- Citation audit: `audit/CITATION_AUDIT.md`
- PDF audit: `audit/PDF_AUDIT.md`
- Release manifest: `release/package/MANIFEST.json`

## Limitations and trust statement

The novelty conclusion is bounded to the recorded searches as of 2026-08-29;
the work has not undergone external peer review.  The finite classification
certificate uses Proposition 3.14 of the source, but the all-\(n\) proof does
not depend on that classification or on any computation.  This result does
not address the separate quantum conjecture.

No Lean, Coq, Isabelle, or other proof assistant was used.  No formalization
claim is made.
