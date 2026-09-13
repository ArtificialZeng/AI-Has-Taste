# Approach registry

| ID | Route | Status | Next discriminating test |
|---|---|---|---|
| BS-D01 | Low-rank unit real Gram matrices and Fock-polynomial evaluation of `F_A` | closed without candidate | Do not treat the 99,850-evaluation negative scan as an exclusion theorem. |
| BS-P01 | Prove a nontrivial real rank-two family | closed exact | The regular-projective-polygon family supplies the theorem and complete spectrum. |
| BS-A01 | Independent definition-level subset-DP/cyclotomic audit | closed PASS | Normal and optimized runs are byte-identical; three corrupted-formula attacks fail closed. |
| BS-P02 | Regular projective polygon Gram matrices in every order | closed exact | Preserve the root-of-unity proof, exact spectrum, cyclotomic no-import reconstruction, and fail-closed formula attacks. |

Discovery and proof are kept separate.  The Fock evaluator is a fast search
interface; a final certificate must be reconstructed independently from the
definition with integers or rational numbers.

The first reconnaissance pass completed 99,850 floating-point evaluations
for ranks 2--5 and orders 6--15.  It found no strict candidate.  This negative
scan redirected the route toward proof.  The regular projective polygon family
then yielded a closed formula: the constant Fourier mode is the unique top
eigenvalue and the exact second/permanent ratio is `n/(2(n-1))`.  A separate
no-import verifier rebuilt the relevant permanents in cyclotomic quotient
rings for orders 3--8 and rejected three deliberately corrupted formulas.
The resulting partial theorem is the terminal outcome for this task.  The
unrestricted real conjecture and the existence of an order-at-most-15 real
counterexample remain open; further computation requires a new research task,
not another PDF revision.
