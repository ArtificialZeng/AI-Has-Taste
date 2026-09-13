# Exact time-eight classification for a general two-state unitary coin

This note proves the classification in source.md under the precise reading in
problem.md. It makes no priority claim beyond the cited boundary. The finite
path calculation is independently reproducible with evidence/time8_exact.py,
which uses only exact integer/rational arithmetic.

## 1. A complete normal form and the proved invariance

Every \(U=(u_{ij})\in U(2)\) can be written

\[
 U=D V(r,z),\qquad
 V(r,z)=\begin{pmatrix}r&s z\\s&-r z\end{pmatrix},
 \qquad r,s\geq0,\quad r^2+s^2=1,\quad |z|=1,
\]

with \(D\) diagonal unitary. Indeed, left row phases make the first column
\((r,s)^T\) nonnegative, and its unit orthogonal complement is
\(z(s,-r)^T\). The same formula covers \(r=0\) and \(s=0\), although \(z\) is
then nonunique.

If \(D=\operatorname{diag}(\lambda,\nu)\), then the left and right step
matrices of \(DU\) are respectively \(\lambda P\) and \(\nu Q\). Every
time-eight return word has four of each, so every amplitude and every coherent
sojourn sum is multiplied by the common phase \(\lambda^4\nu^4\). It is
therefore enough to classify \(V(r,z)\), including its endpoint faces.

## 2. Exact path sums

Put

\[
 x=r^2,\quad y=s^2=1-x,\quad u=rs,\quad h=\operatorname{Im}z,
\]

and define

\[
\begin{aligned}
 f&=y^3-6xy^2+6x^2y-x^3,\\
 A&=-y^2+3xy-x^2, &B&=y^2-5xy+3x^2,\\
 C&=-3y^2+5xy-x^2,&M&=-2y^2+4xy-x^2,\\
 N&=-y^2+4xy-2x^2.
\end{aligned}
\]

Directly grouping all \({8\choose4}=70\) return words with the interval
sojourn convention gives fourteen words in each of \(k=0,2,4,6,8\), no odd
class, and

\[
\begin{aligned}
\Gamma_8(0)&=f\begin{pmatrix}0&0\\rsz^3&s^2z^4\end{pmatrix},\\
\Gamma_8(2)&=\begin{pmatrix}
 u^2Az^4&uyAz^5\\uyBz^3&u^2Cz^4
\end{pmatrix},\\
\Gamma_8(4)&=\begin{pmatrix}
 u^2Mz^4&uyNz^5\\-uyNz^3&u^2Mz^4
\end{pmatrix},\\
\Gamma_8(6)&=\begin{pmatrix}
 u^2Cz^4&-uyBz^5\\-uyAz^3&u^2Az^4
\end{pmatrix},\\
\Gamma_8(8)&=f\begin{pmatrix}s^2z^4&-rsz^5\\0&0\end{pmatrix}.
\end{aligned}
\]

For real \(X,Y\),

\[
 |X+i zY|^2=X^2+Y^2-2XYh.
\]

Consequently, if

\[
 W=\frac12\left(u^4A^2+u^2y^2A^2+u^2y^2B^2+u^4C^2\right),
\]

then

\[
\begin{aligned}
 w_8(0)&=\frac{yf^2}{2}(1-2uh),&
 w_8(8)&=\frac{yf^2}{2}(1+2uh),\\
 w_8(2)&=W-u^3yh(A^2+BC),&
 w_8(6)&=W+u^3yh(A^2+BC),\\
 w_8(4)&=u^4M^2+u^2y^2N^2.
\end{aligned}
\]

The decisive exact identities are

\[
\begin{aligned}
 f&=(1-2x)(1-7x+7x^2),\\
 A^2+BC&=2(2x-1)f,\\
 W-w_8(4)&=x^2y^3(2x-1)^2. \tag{1}
\end{aligned}
\]

The verifier expands every matrix product and checks all three identities; it
does not use floating point or an external computer-algebra package.

## 3. Solving every branch

The two forbidden endpoint weights satisfy

\[
 w_8(0)+w_8(8)=yf^2.
\]

Thus their simultaneous vanishing gives either \(y=0\) or \(f=0\). If
\(y=0\), then \(s=0\) and every displayed return amplitude is zero, so
\(R_8=0\); this branch is excluded from the conditional distribution.

Now take \(y>0\) and \(f=0\). Since \(f(0)=1\), also \(x>0\). The middle
weights lose all \(z\)-dependence by (1), and

\[
 w_8(2)=w_8(6)=w_8(4)+x^2y^3(2x-1)^2.
\]

Equality of the three positive target weights therefore forces \(x=1/2\).
Conversely, at \(x=y=1/2\), all forbidden weights vanish and exact substitution
gives

\[
 w_8(2)=w_8(4)=w_8(6)=\frac1{128},\qquad R_8=\frac3{128},
\]

for every \(|z|=1\). The other two roots
\(x=(7\pm\sqrt{21})/14\) of \(f\) fail equality because the square term in
(1) is strictly positive.

For completeness, the zero-return locus has no hidden branch. If \(y>0\)
and \(f\ne0\), then \(w_8(0)+w_8(8)>0\). If \(y>0\) and \(f=0\), then
\(x>0\), and \(w_8(4)>0\): simultaneous \(M=N=0\) would imply
\(M-N=x^2-y^2=2x-1=0\), whereas \(M=N=1/4\) at \(x=1/2\). Hence
\(R_8=0\) exactly when \(s=0\), i.e. exactly for diagonal coins.

It follows that the complete raw solution set is

\[
 \boxed{\mathcal S=
 \left\{
 D\,\frac1{\sqrt2}\begin{pmatrix}1&z\\1&-z\end{pmatrix}:
 D\text{ diagonal unitary},\ |z|=1
 \right\}.}
\]

Equivalently, \(\mathcal S\) is exactly the set of \(2\times2\) unitary
matrices all four of whose entries have modulus \(1/\sqrt2\). Thus every raw
solution is a complex Hadamard matrix; there is no solution with non-Hadamard
entry moduli.

## 4. What the fixed experiment permits one to quotient

On the balanced face, \(z=b/a\), so \(z\) is unchanged by all allowed left
row phases. The restricted orbit \(\mathcal H_{\rm left}\) is precisely the
slice \(z=1\). Right multiplication by
\(\operatorname{diag}(1,\xi)\) changes \(z\) to \(z\xi\), but it is not a
symmetry of the fixed experiment. For example, at \(x=1/4\), the coins with
\(z=1\) and \(z=i\) are related by that right multiplication, while

\[
 w_8(0;z=1)=\frac{75}{8192},\qquad
 w_8(0;z=i)=\frac{75}{8192}\left(1-\frac{\sqrt3}{2}\right).
\]

Nor does a nontrivial unitary change of the internal basis preserve the stated
setup. A unitary preserving the two ordered chirality projectors must be
diagonal; preserving the ray of
\(\phi_*=(1,i)^T/\sqrt2\) then forces its two diagonal phases to agree, so it
is scalar and acts trivially by conjugation. Hence, with ordinary unitary
basis equivalence, the quotient retains the full circle parameter \(z\), and
all \(z\ne1\) lie outside \(\mathcal H_{\rm left}\). The exact family above is
therefore a counterfamily to “left-Hadamard-orbit rigidity,” even though every
member is complex Hadamard in the standard matrix sense.

If antiunitary Wigner changes of basis are also admitted, there is exactly one
additional nontrivial setup symmetry up to phase:
\(T=J K\), where \(J=\operatorname{diag}(1,-1)\) and \(K\) is complex
conjugation. It preserves each chirality projector and fixes \(\phi_*\). The
induced coin map is \(U\mapsto J\overline UJ\), and pathwise
\(\Gamma\mapsto J\overline\Gamma J\), so all weights are unchanged. Modulo
left row phases it sends

\[
 z\longmapsto-\overline z.
\]

Thus even under this optional enlargement the quotient is
\(S^1/(z\sim-\overline z)\), not a point; the class meeting
\(\mathcal H_{\rm left}\) contains \(z=1\) and \(z=-1\), while, for example,
\(z=i\) remains outside it.

## Gap list

Empty for the frozen mathematical classification and the stated class of
unitary (optionally antiunitary) basis equivalences. No assertion is made
about arbitrary ad hoc maps of the coin space that are not changes of basis
or the proved left-diagonal gauge.
