# Exact dual obstruction to the direct type-II product proof class

Provenance: `bigMac-00004-p01-research-3ba5da36b35c`  
Scope: products of nonnegative powers of all lifted sharp triangular and
pentagonal inequalities, together with nonnegative powers of
\(p_{ij}^{-1}\le 1\).  This obstruction does not decide the type-II
inequality itself.

For an exponent vector \(x\in\mathbb R^{E_6}\), define the integer linear
functional
\[
 \Lambda(x)=3x_{12}+\sum_{k=3}^6x_{1k}
 +2\sum_{k=3}^6x_{2k}
 +2\sum_{3\le i<j\le6}x_{ij}. \tag{1}
\]
All coefficients in (1) are positive.  If
\(q(h)_{ij}=h_i h_j\), direct substitution for the type-II vector
\(h_*=(-2,-1,1,1,1,1)\) gives
\[
 \Lambda(q(h_*))=3(2)+4(-2)+2\cdot4(-1)+2\cdot6(1)=2>0. \tag{2}
\]

It remains to check the two classes of available sharp inequalities.  For
compactness, write
\[
 (c_{12},c_1,c_2,c_3)=\left(q_{12},\frac14\sum_{k=3}^6q_{1k},
 \frac14\sum_{k=3}^6q_{2k},
 \frac16\sum_{3\le i<j\le6}q_{ij}\right).
\]
The following tables exhaust the orbits under permutations of
\(\{3,4,5,6\}\); the counts sum to 60 in each case.  Since (1) is invariant
under this group, every member of an orbit has the displayed value
\(3c_{12}+4c_1+8c_2+12c_3\).

| triangular count | \(c_{12}\) | \(c_1\) | \(c_2\) | \(c_3\) | \(\Lambda(q)\) |
|---:|---:|---:|---:|---:|---:|
| 4  | -1 | -1/4 |  1/4 | 0    | -2 |
| 4  | -1 |  1/4 | -1/4 | 0    | -4 |
| 6  |  0 | -1/2 |  0   | 1/6  |  0 |
| 6  |  0 |  0   | -1/2 | 1/6  | -2 |
| 36 |  0 |  0   |  0   | -1/6 | -2 |
| 4  |  1 | -1/4 | -1/4 | 0    |  0 |

| pentagonal count | \(c_{12}\) | \(c_1\) | \(c_2\) | \(c_3\) | \(\Lambda(q)\) |
|---:|---:|---:|---:|---:|---:|
| 12 | -1 | -1/4 |  1/4 | -1/6 | -4 |
| 12 | -1 |  1/4 | -1/4 | -1/6 | -6 |
| 4  |  0 | -1/2 |  0   |  0   | -2 |
| 4  |  0 |  0   | -1/2 |  0   | -4 |
| 12 |  0 |  0   |  0   | -1/3 | -4 |
| 4  |  1 | -3/4 | -3/4 |  1/2 |  0 |
| 12 |  1 | -1/4 | -1/4 | -1/6 | -2 |

Thus \(\Lambda(q_T)\le0\) for every triangular lift and
\(\Lambda(q_P/2)\le0\) for every normalized pentagonal lift.  Also the
elementary inequality \(p_{ij}^{-1}\le1\), which follows from
\(p_{ij}\ge1\), has exponent \(-e_{ij}\) and
\(\Lambda(-e_{ij})<0\).

Let \(\alpha_*=q(h_*)/4\).  A product certificate of the specified kind
would have nonnegative real weights \(\lambda_T,\lambda_P,\mu_{ij}\) with
\[
 \alpha_*=\sum_T\lambda_Tq_T+
 \sum_P\lambda_P\frac{q_P}{2}-\sum_{i<j}\mu_{ij}e_{ij},
 \qquad
 \sum_T\lambda_T+\sum_P\lambda_P\le1. \tag{3}
\]
(A componentwise exponent cover is the same statement after absorbing its
nonnegative slack into the \(\mu_{ij}\).)  Applying (1) to (3) makes its
right-hand side nonpositive, whereas (2) gives
\(\Lambda(\alpha_*)=1/2>0\), a contradiction.  Hence no such certificate
exists.  In fact, the separator excludes this conic representation even when
the total-weight restriction in (3) is removed.

`check_typeII_product_dual.py` independently enumerates all 60 triangular
and all 60 pentagonal lifts using exact integer arithmetic.  It returns
\[
\begin{aligned}
\{\Lambda(q_T)\}&:\quad -4\ (4),\ -2\ (46),\ 0\ (10),\\
\{\Lambda(q_P)\}&:\quad -6\ (12),\ -4\ (28),\ -2\ (16),\ 0\ (4),
\end{aligned}
\]
and verifies \(\Lambda(q(h_*))=2\).
