# Proof dependency graph

## Matrix-specific endpoint

1. **D0 (serialized data):** the exact rational matrices \(M,A,B\) are stored
   in `certificates/builder_counterexample.json`.
2. **L1 (Hadamard identity):** direct multiplication of all 16 pairs gives
   \(A\circ B=M\).
3. **L2 (upper rank bounds):**
   \(A_3=A_4=A_2-3A_1\),
   \(B_3=2B_2-2B_1\), and
   \(B_4=-B_2+\tfrac12B_1\), so both ranks are at most two.
4. **L3 (lower rank bounds):** the rows 1,2 and columns 1,2 minors are
   \(1\) for \(A\) and \(-\tfrac12\) for \(B\); hence both ranks equal two.
5. **L4 (target full rank):** direct determinant expansion gives
   \(\det M=1\).
6. **T1:** L1--L3 prove that \(M\) is rank-(2,2) Hadamard expressible over
   \(\mathbb Q\), hence over \(\mathbb R\).
7. **C1:** T1 disproves the matrix-specific nonexistence assertion \((C_M)\).

The standard-library verifier independently checks L1, all 16 order-three
minors of each factor, nonzero order-two minors, and L4 from serialized input.

## Structural-family endpoint

1. **F0:** assume \(x,y,z\) are pairwise distinct and nonzero.
2. **F1:** define the rows in `proof/exact_disproof.md`; every \(A\)-row lies
   in \(\operatorname{span}\{\mathbf1,a\}\), and every \(B\)-row lies in
   \(\operatorname{span}\{\mathbf1,b\}\).
3. **F2:** the nonzero denominator conditions in F0 make both scaling
   coefficients defined.
4. **F3:** four row-wise exact products give \(A\circ B=M\).
5. **T2:** the formulas give a three-parameter family of rank-(2,2)
   factorizations; \((x,y,z)=(1,2,3)\) gives D0.
