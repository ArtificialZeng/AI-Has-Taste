# Exact disproof of the candidate's real nonexpressibility

## Theorem

For

\[
M=\begin{pmatrix}
1&1&1&1\\
1&1&1&0\\
0&1&0&0\\
1&0&0&0
\end{pmatrix},
\]
there exist \(A,B\in\mathbb Q^{4\times4}\) with
\(A\circ B=M\) and \(\operatorname{rank}A=\operatorname{rank}B=2\).
Consequently the proposed assertion that no such real factors exist is false.

## Short exact certificate

Take

\[
A=\begin{pmatrix}
1&1&1&1\\
1&2&3&3\\
-2&-1&0&0\\
-2&-1&0&0
\end{pmatrix},\qquad
B=\begin{pmatrix}
1&1&1&1\\
1&\frac12&\frac13&0\\
0&-1&-\frac43&-2\\
-\frac12&0&\frac16&\frac12
\end{pmatrix}.
\]

Entrywise multiplication gives \(A\circ B=M\).  If rows are denoted by
subscripts, then

\[
A_3=A_4=A_2-3A_1,
\quad B_3=2B_2-2B_1,
\quad B_4=-B_2+\tfrac12B_1.
\]

Thus both ranks are at most two.  Their minors on rows 1,2 and columns 1,2
are respectively \(1\) and \(-\tfrac12\), so both ranks are exactly two.
Also \(\det M=1\), so the target meets the prompt's full-rank condition.

## Three-parameter family

The certificate is not isolated.  Let \(x,y,z\in\mathbb R\) be pairwise
distinct and nonzero, and set

\[
\mathbf1=(1,1,1,1),\quad
a=(x,y,z,z),\quad b=(x^{-1},y^{-1},z^{-1},0).
\]

Define rows

\[
\begin{aligned}
&A_1=B_1=\mathbf1,\qquad A_2=a,\qquad B_2=b,\\
&A_3=A_4=a-z\mathbf1,\\
&B_3=\frac{xy}{(y-z)(x-y)}(b-x^{-1}\mathbf1),\\
&B_4=\frac{xy}{(x-z)(y-x)}(b-y^{-1}\mathbf1).
\end{aligned}
\]

All denominators are nonzero by hypothesis.  Every row of \(A\) lies in
\(\operatorname{span}\{\mathbf1,a\}\), and every row of \(B\) lies in
\(\operatorname{span}\{\mathbf1,b\}\), so both ranks are at most two.
The four Hadamard products are

\[
\begin{aligned}
A_1\circ B_1&=(1,1,1,1),\\
A_2\circ B_2&=(1,1,1,0),\\
A_3\circ B_3&=(0,1,0,0),\\
A_4\circ B_4&=(1,0,0,0).
\end{aligned}
\]

For example, the only potentially nontrivial entry in the third row is

\[
(y-z)\frac{xy}{(y-z)(x-y)}(y^{-1}-x^{-1})=1,
\]

and the first entry in the fourth row is checked analogously.  Since
\(\mathbf1,a\) and \(\mathbf1,b\) are each independent under the hypotheses,
both ranks equal two.  The specialization \((x,y,z)=(1,2,3)\) is the short
certificate above.

## Scope

This theorem disproves only the matrix-specific nonexistence assertion.  It
does not prove or disprove that every invertible real \(4\times4\) matrix has
such a decomposition.
