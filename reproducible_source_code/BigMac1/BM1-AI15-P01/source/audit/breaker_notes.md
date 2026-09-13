# Independent breaker report: exact rational decomposition found

## Conclusion

The proposed real nonfactorability claim is false.  In fact the displayed
matrix has a decomposition over \(\mathbb Q\):

\[
A=\begin{pmatrix}
1&1&1&1\\
1&1/2&1/4&1/4\\
3&1&0&0\\
1&1/3&0&0
\end{pmatrix},\qquad
B=\begin{pmatrix}
1&1&1&1\\
1&2&4&0\\
0&1&3&-1\\
1&0&-2&2
\end{pmatrix}.
\]

Direct multiplication entry by entry gives

\[
A\circ B=
\begin{pmatrix}
1&1&1&1\\
1&1&1&0\\
0&1&0&0\\
1&0&0&0
\end{pmatrix}=M.
\]

Both rank bounds have short exact witnesses.  With rows displayed in order,

\[
U=\begin{pmatrix}1&0\\1/4&1/4\\0&1\\0&1/3\end{pmatrix},\quad
V=\begin{pmatrix}1&3\\1&1\\1&0\\1&0\end{pmatrix},\qquad A=UV^{\mathsf T},
\]

and

\[
S=\begin{pmatrix}1&0\\1&1\\0&1\\1&-1\end{pmatrix},\quad
T=\begin{pmatrix}1&0\\1&1\\1&3\\1&-1\end{pmatrix},\qquad B=ST^{\mathsf T}.
\]

The upper-left \(2\times2\) minors of \(A\) and \(B\) are respectively
\(-1/2\) and \(1\), so the ranks are not merely at most two: both are exactly
two.

## Independent parameterization used

This audit did not search the \(3\times3\)-minor ideal.  Start from rank
factorizations \(a_{ij}=u_i^{\mathsf T}v_j\) and
\(b_{ij}=s_i^{\mathsf T}t_j\), and form the decomposable tensors

\[
w_i=u_i\otimes s_i,\qquad z_j=v_j\otimes t_j.
\]

Then \(M_{ij}=w_i^{\mathsf T}z_j\).  Taking the \(w_i\) as the rows of \(W\),
one only has to choose a basis of four decomposable tensors such that every
column of \(Z=W^{-1}M\) is also decomposable.  The exact boundary-chart choice

\[
W=\operatorname{diag}(1,1/4,1,1/3)
\begin{pmatrix}
1&0&0&0\\
1&1&1&1\\
0&0&0&1\\
0&0&1&-1
\end{pmatrix}
\]

gives

\[
Z=W^{-1}M=
\begin{pmatrix}
1&1&1&1\\
0&1&3&-1\\
3&1&0&0\\
0&1&0&0
\end{pmatrix}.
\]

On reshaping a vector \((x_1,x_2,x_3,x_4)\) to
\(\left(\begin{smallmatrix}x_1&x_2\\x_3&x_4\end{smallmatrix}\right)\), each
row of \(W\) and each column of \(Z\) has determinant zero.  Factoring those
rank-one \(2\times2\) matrices yields the displayed \(U,V,S,T\).

## Hidden assumption broken

In homogeneous coordinates for the fourth row tensor, this solution lies on
the stratum \(p_0=0\): its first projective factor is the point at infinity
and coincides with that of the third row tensor.  A parameterization that sets
both affine leading coordinates to one, or divides by \(p_0\), deletes this
entire stratum.  In the zero-pattern language, the exact zeros are

- \(A_{33}=A_{34}=A_{43}=A_{44}=0\), a \(2\times2\) block;
- \(B_{24}=B_{31}=B_{42}=0\), three isolated incidences.

There are no double-zero positions.  Thus the example also attacks any
implicit genericity assumption that the fourth projective row has distinct
coordinates from the first three.

## Reproduction

From the project root:

```bash
python3 discovery/breaker_projective_reconstruct.py
python3 certificates/breaker_verify.py certificates/breaker_decomposition.json
```

The trusted verifier uses only `fractions.Fraction`, rejects duplicate or
unexpected JSON keys, hard-codes and checks the designated target matrix, and
reconstructs the serialized rank factorizations, the Hadamard product, exact
Gaussian ranks, all \(3\times3\) minors, nonzero \(2\times2\) rank witnesses,
and \(\det M=1\).  It prints SHA-256 hashes of both input and verifier.  No
proof assistant and no floating-point computation were used.

Recorded on Python 3.14.7, Darwin 25.5.0 arm64:

```text
PASS exact rational Hadamard rank-(2,2) decomposition
ranks A,B,M = 2,2,4; det(M) = 1
certificate_sha256=8da5b54fe5ee2bee07ecb1ff1ec73d6128688c2a68942d992122c907e6856912
verifier_sha256=e10069de064c5a04e35b52d02831d80d469af5dbce95f3ec8bbb92c9275a3657
```

## Exact scope

This certificate settles only the status of the **specified displayed
candidate**: it disproves the assertion that this particular \(M\) is not a
rank-\((2,2)\) Hadamard product over \(\mathbb R\) (indeed, it is one over
\(\mathbb Q\)).  It does **not** prove that every full-rank real
\(4\times4\) matrix has such a decomposition, nor does it decide whether some
other real counterexample exists.  It also does not contradict a statement
about decompositions with both factors required to have integer entries,
because \(A\) contains nonintegral rational entries.
