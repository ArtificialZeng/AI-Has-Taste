# Exact counterexample certificate

## Exact poset

The eight elements are
\(a_1,a_2,a_3,d,b_0,b_1,b_2,b_3\).  Apart from reflexivity, the only
relations are
\[
 a_i<b_0,\qquad a_i<b_i,\qquad d<b_i\quad(1\le i\le3).
\]
This is an ordinary height-two poset and hence a preorder.  The machine-readable
data are in `data/counterexample_poset.json`.

In the element order \((a_1,a_2,a_3,d,b_0,b_1,b_2,b_3)\), its reflexive
relation matrix (row \(x\), column \(y\) means \(x\le y\)) is
\[
\begin{pmatrix}
1&0&0&0&1&1&0&0\\
0&1&0&0&1&0&1&0\\
0&0&1&0&1&0&0&1\\
0&0&0&1&0&1&1&1\\
0&0&0&0&1&0&0&0\\
0&0&0&0&0&1&0&0\\
0&0&0&0&0&0&1&0\\
0&0&0&0&0&0&0&1
\end{pmatrix}.
\]

## Exact support count

Direct enumeration from all 44 order ideals gives 1281 lattice points and
\[
h_P(t)=1+17t+106t^2+303t^3+427t^4+303t^5+106t^6+17t^7+t^8.
\]
The direct verifier reconstructs the relation closure and ideals from the
serialized edges; it does not import a list of feasible points.  A second
evaluator uses a different height-two branch formula and agrees coefficient by
coefficient.

## Exact non-real-root obstruction

Exact coefficient comparison gives
\[
h_P(t)=(1+t)^8G\!\left(\frac{t}{(1+t)^2}\right),\qquad
G(z)=1+9z+24z^2+16z^3+z^4.
\]
At \(s=-1/4\),
\[
G(s)=1/256,\quad G'(s)=-1/16,\quad G''(s)=99/4,
\]
and hence
\[
G'(s)^2-G(s)G''(s)=-95/1024<0.
\]
Every real-rooted real polynomial \(q\) satisfies
\((q')^2-qq''\ge0\) on the real line: off its roots this follows by logarithmic
differentiation, and at roots by continuity.  Thus \(G\) has a non-real root
\(z\).  Every solution of \(z(1+t)^2-t=0\) is different from \(-1\), is a root
of \(h_P\), and cannot be real because \(t/(1+t)^2\) would then be real.
Therefore \(h_P\) is not real-rooted.

As an independent exact cross-check, the Sturm chain in
`code/verify_sturm.py` has variations 3 and 1 at minus and plus infinity, so
\(G\) has exactly two real roots and one non-real conjugate pair.

## Supplementary isolating rectangles

SymPy 1.14.0 exact complex isolation (`intervals(..., all=True)`) returns four
multiplicity-one non-real boxes for \(h_P\).  Interpreting each ordered pair as
the open axis-aligned rectangle from lower-left to upper-right, two lower-half
boxes are
\[
\left(-\frac{383873}{65536},-\frac{191723}{32768}\right)
\times
\left(-\frac{9821}{32768},-\frac{19215}{65536}\right)
\]
and
\[
\left(-\frac{11529}{65536},-\frac{5551}{32768}\right)
\times
\left(-\frac{427}{32768},-\frac{427}{65536}\right).
\]
Their conjugates are the other two boxes.  These rectangles are supplementary;
the theorem depends only on the short rational Laguerre certificate and the
independent Sturm count.

## One-command verification

From the project root run:
```
bash code/run_all_checks.sh
```
No random search or floating-point arithmetic occurs in the decisive checks.
