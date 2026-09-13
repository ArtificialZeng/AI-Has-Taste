# Exact obstruction to the proposed type-II geometric symmetrization

Provenance: `bigMac-00004-p01-research-3f3b3d092044`  
Scope: the orbit-geometric averaging lemma proposed in `checkpoint.md`; this
does not refute the original six-point bound.

For any real \(r>1\), partition the indices into
\(A=\{1,5,6\}\) and \(B=\{2,3,4\}\), and define
\[
 p_{ii}=1,\qquad
 p_{ij}=\begin{cases}
 1,&i,j\text{ lie in the same part},\\
 r,&i,j\text{ lie in different parts}.
 \end{cases}
 \tag{1}
\]
Every entry is positive.  On the four-dimensional subspace of vectors whose
coordinate sum on each part is zero, \(P_r\) vanishes.  On the orthonormal
basis \((\mathbf 1_A/\sqrt3,\mathbf 1_B/\sqrt3)\) of its complement, its
matrix is
\[
 \begin{pmatrix}3&3r\\3r&3\end{pmatrix},
\]
with eigenvalues \(3(1+r)>0\) and \(3(1-r)<0\).  Hence
\[
 \operatorname{In}(P_r)=(1,1,4),
\]
where the entries count positive, negative, and zero eigenvalues.  Thus
\(P_r\in\mathcal L^+_{6,1}\).

Let \(\bar P_r\) be the entrywise geometric mean of the 24 matrices obtained
by permuting indices \(3,4,5,6\).  Direct orbit counting gives the parameters
of the resulting \(S_4\)-invariant matrix:
\[
 a=r,\qquad b=c=\sqrt r,\qquad d=r^{2/3}.
 \tag{2}
\]
Indeed, each of the two four-edge orbits incident to index 1 or 2 contains two
entries equal to \(1\) and two equal to \(r\), while the six-edge orbit within
\(\{3,4,5,6\}\) contains two entries equal to \(1\) and four equal to \(r\).

The three last-coordinate contrasts have eigenvalue \(1-r^{2/3}<0\).  On the
remaining three-dimensional space, `evidence/typeII_s4_exact_bound.md` gives
the block
\[
 Q_r=\begin{pmatrix}
 1&r&2\sqrt r\\
 r&1&2\sqrt r\\
 2\sqrt r&2\sqrt r&1+3r^{2/3}
 \end{pmatrix}.
\]
The vector \((1,-1,0)\) has eigenvalue \(1-r<0\).  On its orthogonal
complement the block is
\[
 B_r=\begin{pmatrix}
 1+r&2\sqrt{2r}\\
 2\sqrt{2r}&1+3r^{2/3}
 \end{pmatrix}.
\]
Both diagonal entries are positive.  If \(x=r^{1/3}>1\), then
\[
 \det B_r=(1+r)(1+3r^{2/3})-8r
 =(x-1)^2(3x^3+6x^2+2x+1)>0. \tag{3}
\]
Therefore \(B_r\) is positive definite and
\[
 \operatorname{In}(\bar P_r)=(2,4,0).
\]
In particular, orbit-geometric averaging does not preserve the
one-positive-eigenvalue condition.

For a completely explicit algebraic witness, take \(r=8\):
\[
 P_8=\begin{pmatrix}
1&8&8&8&1&1\\
8&1&1&1&8&8\\
8&1&1&1&8&8\\
8&1&1&1&8&8\\
1&8&8&8&1&1\\
1&8&8&8&1&1
\end{pmatrix},
\quad \operatorname{spec}_{\ne0}(P_8)=\{27,-21\}.
\]
Its geometric average has \((a,b,c,d)=(8,2\sqrt2,2\sqrt2,4)\).  The two
positive eigenvalues of its \(Q\)-block are \(11\pm2\sqrt{17}\), the negative
one is \(-7\), and its other three eigenvalues are \(-3\).  This is an exact
inertia certificate with no numerical step.

The type-II exponent is constant on all three relevant edge orbits, so its
monomial is unchanged by this geometric averaging.  For the family (1) that
common value is \(1\).  Thus the witness refutes only the proposed closure
lemma, not the desired inequality \(F\le2\).
