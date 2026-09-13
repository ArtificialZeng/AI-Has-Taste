# Builder branch notes

## Scope and source findings

This branch independently reconstructed the source definitions and implemented
the finite reduction in src/builder_coinvariant.py and
src/builder_verify_blocks.py. It did not import or inspect another branch's
discovery code.

The published paper's Remark 3.3 (p. 717) and arXiv v3 source line 711 say only
that Conjecture 3.2 “has been verified for \(n\le4\).” Neither source gives the
term order, software, invariant generators, ranks, logs, or a certificate.
There is no ancillary code in the arXiv v3 source archive. Therefore the task
requirement to “reproduce \(n=3,4\)” necessarily means an independent
reconstruction, not rerunning a documented author computation.

## Implementation contract

The implementation uses only exact integer/rational operations in certification
mode:

1. polynomial normal forms modulo \((e_1,\ldots,e_n)\) use the monic lexicographic
   Gröbner basis \(h_i(x_i,\ldots,x_n)\);
2. odd monomials are bit masks with an explicit cross-species Koszul sign;
3. the \(S_n\)-action is reconstructed on every Artin--exterior monomial;
4. invariant subspaces are images of the unnormalized Reynolds sum
   \(\sum_{\sigma\in S_n}\sigma\);
5. the positive invariant ideal is closed by the exact block recurrence (5.1)
   in structural_reduction.md;
6. candidate vectors are tested for both spanning and independence, separately
   in every tridegree.

Prime-field mode (--prime) is explicitly discovery-only. It is not accepted
as a characteristic-zero certificate.

## Tests and exact baseline

Command:

    python tests/builder_test_coinvariant.py

Current result: PASS 9 builder tests. These include Artin reduction, odd
signs and squares, rational sparse elimination, candidate cardinalities through
\(n=5\), \(S_n\)-action involutions, Reynolds invariance, and the representation-
theoretic check
\(\dim(C_n^{S_n})=4^n\) for small \(n\). They additionally check the Coxeter
relations on every coordinate vector of the full \(n=3\) finite model and the
exact zero Reynolds sum caused by the signed stabilizer of
\(\theta_1\theta_2\).

Exact runs:

    python src/builder_verify_blocks.py 3 > /tmp/builder_n3_q.json
    python src/builder_verify_blocks.py 4 > /tmp/builder_n4_q.json

| \(n\) | field | \(\dim C_n\) | \(\dim C_n^{S_n}\) | computed \(\dim R_n^{(1,2)}\) | candidates | every block spans | every block independent |
|---:|---|---:|---:|---:|---:|---|---|
| 2 | \(\mathbb Q\) | 32 | 16 | 4 | 4 | yes | yes |
| 3 | \(\mathbb Q\) | 384 | 64 | 24 | 24 | yes | yes |
| 4 | \(\mathbb Q\) | 6144 | 256 | 192 | 192 | yes | yes |

The \(n=4\) JSON content digest (computed before inserting the digest field) is
6a48c29e1c95e1a12cb51acce00308741618f3174cc947fa8c474fda12d03799.
The run took about 107 seconds on the recorded local environment. Runtime is
diagnostic only; the conclusion comes from rational row reduction.

## \(n=5\) status

The independent Builder calculation completed over \(\mathbb Q\), using
python-flint 0.9.0 and its exact fmpq_mat.rref implementation. No modular result
is used in the conclusion.

Dependency and run commands:

    python -m pip install --user python-flint
    python src/builder_flint_verify.py 5 --batch-size 512 \
      > /tmp/builder_flint_n5_q.json \
      2> /tmp/builder_flint_n5_q.log

Exact aggregate result:

| quantity | result |
|---|---:|
| field | \(\mathbb Q\) |
| tridegree blocks audited | 396 |
| nonzero quotient blocks | 95 |
| \(\dim C_5\) | 122880 |
| \(\dim C_5^{S_5}\) | 1024 |
| \(\dim R_5^{(1,2)}\) | 1920 |
| \(|B_5^{(1,2)}|\) | 1920 |
| all blocks spanned by candidates | yes |
| candidates independent in every block | yes |
| recorded elapsed time | 976.355208158493 seconds |

The serialized result with every block's ambient, invariant, ideal, quotient,
and candidate ranks is proof/builder_n5_exact_blocks.json. Its SHA-256 is
1b94fd44826a6726f993f4debadf293692f00d68af0658b1cfb4a89a84d85951.
The canonical JSON content digest recorded internally before adding its digest
field is
796cce75b1ab19e3471abfefc74824d08f65cb5e48eea08cfe32c4409ed83dda.

Relevant source hashes for this run are:

| file | SHA-256 |
|---|---|
| src/builder_coinvariant.py | db8a1eefcbe74ffc8b4ae4712e0f17ac614431e4dd9aaf6c2099f8ceeb669871 |
| src/builder_flint_verify.py | 48c8329109bede2842a506f16b802ca2545605eef2c7dfa7f473815aeae2109b |
| tests/builder_test_coinvariant.py | 69bdc8e5f29994213e9739ab4f62b27a5bfb25936a82fb732ec9d74e97b527be |

This is a characteristic-zero Builder result for the finite endpoint \(n=5\).
It establishes the direct-sum identities (5.2) within this implementation.
The initially open release condition has since been closed by
`independent/verify_exact.py`: that frozen no-import implementation rebuilds
the algebra and exact rational ranks from a small hash-bound configuration and
passes all 396 blocks.  Its record and hashes are audited in
`audit/PROOF_AUDIT.md`.

## Gaps exposed by this branch

| ID | Gap | Severity | Required repair/test |
|---|---|---|---|
| B-G1 | The source reports \(n\le4\) without a reproducible method or certificate. | source/reproducibility | Use the independent exact baseline above; do not attribute its method to Lentfer. |
| B-G2 | Step-ordered path weights and species-ordered \(\theta_T\xi_S\) can differ by a sign. | local, harmless for basis | Canonicalize every serialized monomial and store the sign; reject ambiguous encodings. |
| B-G3 | No term order is specified in the source. | major for any “standard monomial” claim | Either state only the vector-space basis result or provide a separate super-Gröbner term order and initial-ideal certificate. |
| B-G4 | The characteristic-zero Builder calculation and its block audit share the same algebra implementation. | fatal for release | Closed: the frozen no-import verifier independently reconstructs all 396 blocks and checks their ranks over \(\mathbb Q\). |
| B-G5 | A finite \(n=5\) computation, even exact, does not prove the all-\(n\) conjecture. | fatal for a general theorem | Terminal endpoint must be CERTIFIED_FINITE_RESULT unless a separate general proof closes this gap. |
| B-G6 | No proof assistant is used in this branch. | disclosure | State explicitly that the endpoint is exact-computation based, not Lean/Coq/Isabelle formalized. |
