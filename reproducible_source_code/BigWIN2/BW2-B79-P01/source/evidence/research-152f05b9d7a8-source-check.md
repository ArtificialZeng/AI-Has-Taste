# Primary-source and nearest-result check

Research job: `win-00079-p01-research-152f05b9d7a8`.

Checked on 2026-09-10.  This is a bounded comparison, not an openness,
novelty, or priority certificate.

## Primary file

The PDF identified by `source.md` was located in the supervisor's batch input
and copied byte-for-byte to
`evidence/external/2609.04258v1.pdf`.  Both copies have SHA-256

```
1e6b85a758b8e4a3b380d633d74fc54722bc1dfa1edef79b87a589a2ec7e346a
```

The file is Andrey Egorov, *Minimal-Volume Equiangular Hyperbolic
4-Polytopes*, arXiv:2609.04258v1 (11 pages).  The official HTML at
<https://arxiv.org/html/2609.04258v1> was also inspected live.

## Decisive locators

- Proposition 2.1 (PDF pp. 3--4) states that every vertex is ideal at
  \(\alpha_0=\arccos(1/3)\).
- Proposition 2.3 (PDF pp. 4--5) constructs the Klein cube and asserts
  uniqueness for cube combinatorics only when \(\alpha>\alpha_0\).  Its proof
  expressly says that endpoint uniqueness is not needed.
- Proposition 5.1 and Remark 5.2 (PDF p. 9) likewise restrict isometric cube
  uniqueness to \(\alpha>\alpha_0\).

Thus the primary paper does not contain a resolution of the frozen endpoint
assertion.  The proposed proof in
`evidence/research-152f05b9d7a8-proof.md` is self-contained and in fact
rederives ideality from the singular four-facet vertex Gram matrix.

## Bounded search

The triage searches recorded in `evidence/triage-226b85b4cb78.md` were
supplemented by searches restricted to arXiv for combinations of:

- hyperbolic 4-cube, ideal endpoint, equiangular rigidity, and
  \(\arccos(1/3)\);
- regular ideal 4-cube and rigidity;
- ideal hyperbolic polytope rigidity in dimensions at least four;
- the identifier `2609.04258` with endpoint uniqueness.

The exact-source hit above and unrelated dimension-three/circle-pattern
rigidity papers were returned; no explicit theorem matching the endpoint
claim was identified.  General rigidity literature was not exhaustively
surveyed, and search nonreturn is not evidence that the result is open or new.
