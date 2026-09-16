# Immutable source: win-00061-p04

## Frozen problem

Using the Frobenius Alexander quandle convention of arXiv:2609.02278v1, determine the least rational prime `ell != 5` with the following uniform property:

For every pair of elliptic curves `A,B` over `F_5`, if

`Q(A[ell](overline(F_5)), pi_A,ell)` and `Q(B[ell](overline(F_5)), pi_B,ell)`

are isomorphic as quandles, then `A` and `B` are `F_5`-isogenous.

Prove uniform sufficiency for the least prime and, for every smaller prime different from 5, either classify why it also suffices or give explicit nonisogenous elliptic curves whose Frobenius Alexander quandles are isomorphic. Certificates must include point counts/Frobenius traces, integral characteristic polynomials, their rational canonical forms modulo `ell`, and the isogeny/nonisogeny conclusion. Equality merely of characteristic polynomials modulo `ell` is not enough when it does not determine similarity.

## Primary source

- Yuta Taniguchi, *Frobenius Alexander quandles, knot colorings, and isogeny classes of abelian varieties over finite fields*, arXiv:2609.02278v1, Corollaries 4.3 and 4.5 and Example 4.9 (PDF pp.12–15).
- URL: https://arxiv.org/abs/2609.02278
- Local evidence: `batches/inbox/bigWin-61-materials/2609.02278.pdf`
- PDF SHA-256: `7c606d514c100aec480b8c2f9e5ea8ad860a9165c784afde717290e695e96329`.

Corollary 4.5 makes `ell=11` sufficient because `11>4*sqrt(5)`, while Example 4.9 proves failure at `ell=3`. The status of `ell=2,7` and sharpness of 11 are the proposed finite delta. This differs from registry neighbor `win-00042-p04`, which concerns idempotents in prime-order Alexander quandle rings rather than Frobenius modules or isogeny detection.

