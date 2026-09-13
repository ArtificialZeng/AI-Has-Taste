# Proof audit

Audit date: 2026-08-29 (Asia/Shanghai). Final mathematical status:
**DISPROVED**, meaning that the displayed candidate's real nonexpressibility
assertion is false.

## Endpoint and scope

The displayed matrix \(M\) admits \(M=A\circ B\) with
\(A,B\in\mathbb Q^{4\times4}\) and
\(\operatorname{rank}A=\operatorname{rank}B=2\).

This theorem is strictly matrix-specific. It does not decide whether every
invertible real \(4\times4\) matrix is rank-(2,2) Hadamard expressible, nor
whether another real counterexample exists.

## Human-readable exact proof

The canonical certificate is printed in `proof/exact_disproof.md` and
`paper/main.tex`. Exact entrywise multiplication gives \(A\circ B=M\). The
row relations

\[
A_3=A_4=A_2-3A_1,\quad B_3=2B_2-2B_1,\quad
B_4=-B_2+\tfrac12B_1
\]

give rank at most two, while the upper-left \(2\times2\) minors \(1\) and
\(-1/2\) give rank at least two. Also \(\det M=1\). No numerical,
compactness, genericity, or limiting step occurs.

## Independent roles and witnesses

- Builder: canonical \((x,y,z)=(1,2,3)\) witness and a three-parameter family;
  see `audit/builder_notes.md`.
- Breaker: a different rational witness derived from a Segre/tensor boundary
  chart, with explicit rank factorizations; see `audit/breaker_notes.md`.
- Referee: a third rational witness, reconstructed without importing either
  serialized certificate; see `audit/referee_notes.md`.

The referee verified all family denominators. The hypotheses that
\(x,y,z\) are pairwise distinct and nonzero are exactly what the formulas
need. Rank-zero and rank-one boundaries are independently excluded by
nonzero \(2\times2\) minors.

## Machine-checkable exact certificates

`python verifier/run_all.py` returns `ALL_PASS`. The run includes three
serialized rational certificates, two discovery parameterizations, exact
Gaussian ranks, explicit rank factorizations, all order-three minors,
nonzero order-two minors, the Hadamard identity, and \(\det M=1\).

Canonical short certificate/verifier hashes:

- input: `07367eb903e471f833dd2d5229765ffa1c96a360b7d961b0f3e5a192d82a6184`
- verifier: `d5e22bf05c15a84052f2b5396187660759d233016a620cd401e9c5bbcddc19f1`

Independent breaker certificate/verifier hashes:

- input: `8da5b54fe5ee2bee07ecb1ff1ec73d6128688c2a68942d992122c907e6856912`
- verifier: `e10069de064c5a04e35b52d02831d80d469af5dbce95f3ec8bbb92c9275a3657`

The verifiers share CPython's `Fraction` and are therefore not independent
software stacks. This is not a trust gap for the short certificate because
the printed row relations and three different witnesses are directly
checkable by hand.

## Gap resolution

- The proposed real infeasibility theorem is false and has been replaced by
  the exact positive factorization theorem.
- All fatal and major gaps for the matrix-specific theorem are closed.
- The broader universal question is explicitly outside the proved endpoint.
- Rivin's integer-only theorem is not imported into the proof.
- Novelty is stated only within the frozen database search scope.

## Proof-assistant disclosure

No proof assistant was used. SymPy was used only as a non-trusted exact
cross-check; the certificate verification requires only Python's standard
library, and the printed proof requires only rational arithmetic.
