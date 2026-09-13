# Exact resolution dossier: optimal two-step gradient schedule

This dossier proves the frozen statement in `source.md`.  It does **not** claim
uniqueness.  All functions used for the global lower bound are one-dimensional;
the upper bound is dimension-free.

## 1. Normalization and constants

The scaling in `problem.md` reduces the problem exactly to `L=1`,
`x_*=0`, `f_*=0`, and `||x_0||=1`, with positive normalized steps
`a=L eta_1` and `b=L eta_2`.  Write

\[
 s=\sqrt2,\qquad t=\sqrt{9+8\sqrt2},\qquad
 r=\frac{2}{1+t},\qquad C=\frac{r^2}{2}.
\]

Directly from `t^2=9+8s`,

\[
 C=\frac1{5+4\sqrt2+t},\qquad
 b_*=1+r(1+s)=\frac{3+t}{4}.
\]

Put

\[
 u_0=s-1,\qquad v_0=r(1+s),\qquad
 H=2+u_0+v_0.
\]

The identities needed below are

\[
 u_0v_0=r,\qquad v_0=r(u_0+2),\qquad
 H=s+b_*=\frac{r^{-2}-1}{2}.                 \tag{1}
\]

## 2. Four exact adversarial lower bounds

For every `a,b>0`, the normalized worst-case value `R(a,b)` obeys

\[
R(a,b)\ \ge\ \max\left\{
 \frac1{2(1+2(a+b))},
 \frac{((a-1)(b-1))^2}{2},
 \frac{(b-1)^2}{2(a+1)^2}
 \right\}.                                      \tag{2}
\]

If additionally `a>1`, then

\[
 R(a,b)\ge \frac{(a-1)^2}{2(b+1)^2}.             \tag{3}
\]

Here are exact witnesses for these bounds.

1. Let `delta=1/(1+2(a+b))` and use the standard Huber function
   \[
   H_\delta(x)=\begin{cases}x^2/2,&|x|\le\delta,\\
   \delta|x|-\delta^2/2,&|x|\ge\delta.
   \end{cases}
   \]
   Starting at `x_0=1`, both iterates stay above `delta`, and
   `H_delta(x_2)=1/(2(1+2(a+b)))`.

2. For `f(x)=x^2/2`, one has `x_2=(1-a)(1-b)` and obtains the
   second bound in (2).

3. Let `delta=1/(1+a)` and use the right-capped quadratic
   \[
   P^+_\delta(x)=\begin{cases}x^2/2,&x\le\delta,\\
   \delta x-\delta^2/2,&x\ge\delta.
   \end{cases}
   \]
   Its gradient is `min(x,delta)`.  Thus `x_1=delta` and
   `x_2=delta(1-b)`, giving the third bound in (2).

4. When `a>1`, let `delta=(a-1)/(b+1)` and use the left-capped
   quadratic
   \[
   P^-_\delta(x)=\begin{cases}-\delta x-\delta^2/2,&x\le-\delta,\\
   x^2/2,&x\ge-\delta.
   \end{cases}
   \]
   Its gradient is `max(x,-delta)`.  Hence
   `x_1=1-a=-(b+1)delta` and `x_2=-delta`, proving (3).

Each displayed function is differentiable, convex, has 1-Lipschitz gradient,
and has the proper minimizer set `{0}`.  Therefore all are admissible members
of the frozen class.

## 3. Exact partition of the positive step quadrant

We prove that the maximum of the applicable quantities (2)--(3) is at least
`C`.  Suppose to the contrary that `R(a,b)<C`, and set

\[
u=a-1>-1,\qquad v=b-1>-1.
\]

The Huber bound and (1) imply

\[
a+b>\frac{r^{-2}-1}{2}=H.                        \tag{4}
\]

The quadratic and capped-quadratic bounds imply

\[
 |uv|<r,\qquad |v|<r(u+2),                        \tag{5}
\]

and, whenever `u>0`,

\[
 u<r(v+2).                                        \tag{6}
\]

If `u,v` are not both nonnegative, (5), or (6) when `u>0>v`, gives
`u+v<2r`.  (If both are negative this is immediate.)  But

\[
H-(2+2r)=u_0+v_0-2r=(s-1)(1+r)>0,
\]

so this contradicts (4).

It remains to take `u,v>=0`.  First suppose `v>=u`.  If `u<=u_0`, (5)
gives

\[
u+v<(1+r)u+2r\le (1+r)u_0+2r=u_0+v_0.            \tag{7}
\]

If `u>u_0`, then `v>=u` and `uv<r` imply `u<sqrt(r)`, while

\[
u+v<u+\frac r u.
\]

The function `z+r/z` decreases on `(0,sqrt(r)]`.  Also `u_0<sqrt(r)`:
indeed `u_0^2<1/5<1/3<r`, using `7/5<sqrt(2)<2` and `t<5`.
Consequently

\[
u+v<u_0+\frac r{u_0}=u_0+r(1+s)=u_0+v_0.         \tag{8}
\]

If `u>=v`, the same argument with `u,v` interchanged uses (6) in place
of the second inequality in (5).  Thus in every case
`a+b=2+u+v<=2+u_0+v_0=H`, contradicting (4).  Therefore

\[
R(a,b)\ge C\quad\text{for all }a,b>0.             \tag{9}
\]

This is the requested exact positive-quadrant partition.  It uses four
explicit functions, not a numerical PEP or a bounded-box search.

## 4. Exact dimension-free upper certificate at the claimed schedule

Take

\[
h_1=s,\qquad h_2=1+v_0=\frac{3+t}{4}.
\]

For the samples indexed by `i,j in {*,0,1,2}`, put `g_i=nabla f(x_i)`
and

\[
I_{ij}=f_i-f_j-\langle g_j,x_i-x_j\rangle
       -\frac12\|g_i-g_j\|^2.
\]

Smooth convex interpolation gives `I_ij>=0` for every directed pair;
`x_*=g_*=0` and `f_*=0`.  Define the following six nonzero multipliers:

| `(i,j)` | `lambda_ij` |
|---|---:|
| `(*,0)` | `s r^2` |
| `(*,1)` | `(2+s) r^2` |
| `(*,2)` | `r` |
| `(0,1)` | `(1+s) r^2` |
| `(1,0)` | `r^2` |
| `(1,2)` | `1-r` |

They are all positive because `0<r<1`.  Direct expansion, using
`x_1=x_0-sg_0`, `x_2=x_1-(1+v_0)g_1`, and (1), gives the exact identity

\[
\begin{aligned}
C\|x_0\|^2-f_2
={}&\sum_{i,j}\lambda_{ij}I_{ij}\\
&+\left\|\frac r s x_0-rg_0-v_0g_1-\frac1s g_2\right\|^2.             \tag{10}
\end{aligned}
\]

For an independently checkable coefficient description, the function-value
coefficients in the sum on the right of (10) are `(0,0,-1)`.  In the Gram
basis `(x_0,g_0,g_1,g_2)`, its residual matrix is exactly `w w^T`, where

\[
w=(r/s,-r,-v_0,-1/s)^T.
\]

Thus (10) is a positive-semidefinite PEP dual certificate.  Since every term
on its right is nonnegative, `f_2<=C||x_0||^2` in every finite dimension.
The exact entrywise verification is implemented in
`evidence/exact_resolution_verify.py`.

## 5. Conclusion

Equation (9) gives the global lower bound for every positive ordered pair.
Equation (10) gives the matching upper bound at

\[
(L\eta_1,L\eta_2)=\left(\sqrt2,\frac{3+\sqrt{9+8\sqrt2}}4\right).
\]

Undoing the exact normalization proves

\[
\inf_{\eta_1,\eta_2>0}R_2^L(\eta_1,\eta_2)
=\frac1{5+4\sqrt2+\sqrt{9+8\sqrt2}},
\]

with attainment by the ordered schedule stated in `source.md`.  No uniqueness
claim is made.
