# Gate 5 independent proof-builder notes

Date: 2026-08-29 (Asia/Shanghai)

Role scope: reconstruct the proposed nonexistence theorem from the definition,
with particular attention to rank-two parameterizations, zero-pattern strata,
and divisions by entries that might vanish.  This note does not assess novelty
or the cited paper.  No floating-point inference is used.

## Outcome

The proposed nonexistence statement for the displayed matrix is false.  In
fact the matrix has the following exact factorization over \(\mathbb Q\):

\[
 A=\begin{pmatrix}
 1&1&1&1\\
 1&2&3&3\\
 -2&-1&0&0\\
 -2&-1&0&0
 \end{pmatrix},\qquad
 B=\begin{pmatrix}
 1&1&1&1\\
 1&\tfrac12&\tfrac13&0\\
 0&-1&-\tfrac43&-2\\
 -\tfrac12&0&\tfrac16&\tfrac12
 \end{pmatrix}.
\]

Entrywise multiplication gives

\[
 A\circ B=
 \begin{pmatrix}
 1&1&1&1\\
 1&1&1&0\\
 0&1&0&0\\
 1&0&0&0
 \end{pmatrix}=M.
\]

Moreover, writing \(A_i,B_i\) for row \(i\),

\[
 A_3=A_4=A_2-3A_1,
 \qquad
 B_3=2B_2-2B_1,
 \qquad
 B_4=-B_2+\tfrac12B_1.
\]

Thus both row spaces have dimension at most two.  The \(2\times2\) submatrix
of either factor in rows 1,2 and columns 1,2 has determinant respectively
\(1\) and \(-\tfrac12\), so both factors actually have rank exactly two.
Also \(\det M=1\), confirming that the target is full rank.

This is a decisive exact disproof of the matrix-specific boxed assertion
\(\nexists A,B\in\mathbb R^{4\times4}\).  It does **not** settle the broader
question whether every invertible real \(4\times4\) matrix admits a
rank-\((2,2)\) Hadamard factorization.

The witness is one member of an elementary three-parameter family, so its
existence is not an isolated numerical coincidence.  Take pairwise distinct
nonzero \(x,y,z\), put

\[
 \mathbf 1=(1,1,1,1),\quad
 a=(x,y,z,z),\quad
 b=(x^{-1},y^{-1},z^{-1},0),
\]

and define

\[
\begin{aligned}
 &A_1=B_1=\mathbf1,\qquad A_2=a,\qquad B_2=b,\\
 &A_3=A_4=a-z\mathbf1,\\
 &B_3=\frac{xy}{(y-z)(x-y)}(b-x^{-1}\mathbf1),\\
 &B_4=\frac{xy}{(x-z)(y-x)}(b-y^{-1}\mathbf1).
\end{aligned}
\]

Direct multiplication gives \(A\circ B=M\): in row 3, the \(A\)-factor
vanishes at columns 3,4 and the \(B\)-factor at column 1, while the displayed
coefficient makes the column-2 product one; row 4 is analogous with columns
1 and 2 interchanged.  Every row lies in the span of \(\mathbf1,a\), or of
\(\mathbf1,b\), respectively.  Setting \((x,y,z)=(1,2,3)\) gives the
serialized witness above.

## Structural route that exposed the factorization

At every nonzero entry of \(M\), both factors are nonzero.  Paired column
scalings permit normalization of the first row of both factors to
\((1,1,1,1)\).  If the first two rows span each rank-two row space, write

\[
 A_2=(a_1,a_2,a_3,a_4),\qquad
 B_2=(a_1^{-1},a_2^{-1},a_3^{-1},b_4),
\]

where \(a_1,a_2,a_3\ne0\) and \(a_4b_4=0\).  Every later row of \(A\) is an
affine function of the four \(a_j\), and every later row of \(B\) is an
affine function of the four corresponding \(b_j\).  Consequently a nonempty
zero set in one such row is an equality fiber of the relevant four-tuple.

The equality pattern

\[
 (a_1,a_2,a_3,a_4)=(1,2,3,3),\qquad
 (b_1,b_2,b_3,b_4)=(1,\tfrac12,\tfrac13,0)
\]

covers the row-3 zeros by the \(A\)-fiber \(\{3,4\}\) and the \(B\)-fiber
\(\{1\}\), and covers the row-4 zeros by the same \(A\)-fiber and the
\(B\)-fiber \(\{2\}\).  Scaling the corresponding affine rows so their sole
nonzero target entries equal one yields exactly the displayed factorization.

This also identifies the likely failure mode of any purported zero-pattern
obstruction: the legal branch

\[
 Z(A_3)=Z(A_4)=\{3,4\},\quad
 Z(B_3)=\{1\},\quad Z(B_4)=\{2\},\quad B_{24}=0
\]

must not be discarded.

## Exact certificate and reproduction

Serialized input:
`certificates/builder_counterexample.json`.

Independent standard-library verifier:
`certificates/builder_verify_counterexample.py`.

Run from the project root:

```bash
python certificates/builder_verify_counterexample.py \
  certificates/builder_counterexample.json
```

The verifier fails closed on malformed dimensions or rational entries,
hard-codes the target matrix, reconstructs the Hadamard product, checks all
16 three-by-three minors of each factor, finds nonzero two-by-two rank
witnesses, checks \(\det M\ne0\), and prints SHA-256 hashes of its input and
own code.

## Remaining scope and audit warnings

1. No proof assistant was used; the certificate is elementary exact rational
   arithmetic plus a small independent verifier.
2. This certificate refutes only the claim that the **displayed** matrix is a
   real counterexample.  It neither proves nor disproves the universal
   statement for all full-rank real \(4\times4\) matrices.
3. The source attribution and whether the matrix was transcribed correctly
   require a separate source audit.  If the source uses a different matrix,
   convention, or factor domain, this computation should not be transferred
   to it without verification.
4. An assertion that this same matrix is nonfactorable over \(\mathbb Z\)
   is not logically contradicted by the rational certificate unless that
   assertion meant a property stable under passage to \(\mathbb Q\).  Domain
   conventions must be checked against the primary source.
