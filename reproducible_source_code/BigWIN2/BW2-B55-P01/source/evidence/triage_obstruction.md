# Exact transverse obstruction at the all-ones vector

For parameters ordered as ((a,b_0,b_1,b_2,b_3,b_4)), the equations (K(a,b)x=0) are

\[
a x_i+b_{i-1}x_{i-1}+b_i x_{i+1}=0 \quad (i\bmod 5).
\]

The coefficient matrix of (b=(b_0,\ldots,b_4)^T) is

\[
B(x)=\begin{pmatrix}
x_1&0&0&0&x_4\\
x_0&x_2&0&0&0\\
0&x_1&x_3&0&0\\
0&0&x_2&x_4&0\\
0&0&0&x_3&x_0
\end{pmatrix},
\qquad
\det B(x)=2\prod_{i=0}^4x_i.
\]

At (x^*=\mathbf1), choose (a=2) and (b_i=-1). The resulting matrix is the ordinary cycle Laplacian (K^*). It satisfies (K^*x^*=0) and

\[
y^TK^*y=\sum_i(y_i-y_{i+1})^2,
\]

so it is PSD with kernel exactly (mathbb R\mathbf1). Its characteristic polynomial is

\[
t(t^2-5t+5)^2,
\]

whose four nonzero roots are positive. Because (det B(x^*)=2), setting (a=2) determines (b(x)=-2B(x)^{-1}x) continuously in an open neighborhood of (x^*). The matrices (K(x)=K(2,b(x))) satisfy (K(x)x=0), and continuity of the four positive eigenvalues of (K^*) shows that (K(x)) remains PSD of rank (4) after shrinking the neighborhood. Thus failure occurs on a nonempty open, hence positive-measure, set of observations.

Replay the exact symbolic identities with:

```sh
python3 evidence/triage_obstruction.py
```

Observed output on 2026-09-07:

```text
det B(x) = 2*x0*x1*x2*x3*x4
det B(1) = 2
b(1) for a=2 = [-1, -1, -1, -1, -1]
K*1 = [0, 0, 0, 0, 0]
leading principal minors = [2, 3, 4, 5, 0]
characteristic polynomial = lambda*(lambda**2 - 5*lambda + 5)**2
```
