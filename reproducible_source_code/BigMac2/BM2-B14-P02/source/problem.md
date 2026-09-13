# Precise problem reading

## Frozen source and source status

The immutable statement is `source.md` (SHA-256
`acde4095c880fb75747d10f4c9d37ebfd2aa609713f0e06131ba150036348c04`).
The designated primary source is Xie--Zhou, *Universal Exponent-Two Degree
Laws in Range-Renewal Networks*, arXiv:2609.05290v1. Its Theorem 1 proves the
iid formulas below, Proposition 2 transfers them to loop-deleted graphs, and
the discussion asks broadly about dependent symbol sequences. The particular
sticky-refresh chain is not stated there. Thus the iid theorem is the nearest
prior result; the status of this exact specialization is `status-uncertain`
until a wider literature check, and no novelty claim is made here.

## Data and quantifiers

Let \(\pi=(\pi_i)_{i\ge1}\) be a nonincreasing sequence with \(\pi_i>0\) and
\(\sum_i\pi_i=1\). Fix \(0<\gamma<1\) and assume
\(\pi_k\in RV_{-1/\gamma}\), meaning
\[
  \frac{\pi_{\lceil tx\rceil}}{\pi_{\lceil x\rceil}}
  \longrightarrow t^{-1/\gamma}\qquad(x\to\infty)
\]
for every fixed \(t>0\). Independently fix a **constant**
\(\rho\in[0,1)\), and put \(q=1-\rho>0\).

On one probability space take iid \(Y_0,Y_1,\ldots\sim\pi\) and iid
\(B_1,B_2,\ldots\sim\operatorname{Bernoulli}(q)\), with the two sequences
independent. Define
\[
 M_0=0,\qquad M_n=\sum_{t=1}^n B_t,\qquad X_n=Y_{M_n}.
\]
Equivalently, \(X_0\sim\pi\) and
\[
 \Pr(X_t=y\mid X_{t-1}=x)=\rho\,\mathbf1_{\{x=y\}}+q\pi_y.
\]
Thus a refresh redraw may itself return the current symbol.

## Loop-deleted simple graphs and normalization

For integer \(n\ge0\), let
\[
 V_n=\{X_0,\ldots,X_n\},\qquad R_n=\#V_n.
\]
Repeated edges are suppressed by using edge sets, and all self-loops are
deleted:
\[
 E_n^{\to}=\{(X_{t-1},X_t):1\le t\le n,\ X_{t-1}\ne X_t\},
\]
\[
 E_n^{\mathrm u}=\{\{X_{t-1},X_t\}:1\le t\le n,\ X_{t-1}\ne X_t\}.
\]
For \(x\in V_n\), define
\[
 D_n^{\to}(x)=\#\{y:(x,y)\in E_n^{\to}\},\qquad
 D_n^{\mathrm u}(x)=\#\{y:\{x,y\}\in E_n^{\mathrm u}\}.
\]
For every integer \(k\ge1\), the normalized local masses and tails are
\[
 r_{n,k}^{\rho,\to}=\frac1{R_n}\#\{x\in V_n:D_n^{\to}(x)=k\},\quad
 r_{n,k+}^{\rho,\to}=\frac1{R_n}\#\{x\in V_n:D_n^{\to}(x)\ge k\},
\]
with \(r_{n,k}^{\rho,\mathrm u}\) and \(r_{n,k+}^{\rho,\mathrm u}\) defined
analogously. Counting all of \(V_n\), rather than excluding a possibly new
last symbol as in the source's directed convention, makes no difference for
\(k\ge1\), since that symbol has out-degree zero.

To name the deterministic iid limits, let \(K_m\) be the number of distinct
values in \(m\) iid draws from \(\pi\), and set
\[
 s_\ell(\gamma)=\frac{\gamma\Gamma(\ell-\gamma)}
 {\Gamma(1-\gamma)\Gamma(\ell+1)},\qquad
 r_k^{\to}=\sum_{\ell\ge1}s_\ell(\gamma)\Pr(K_\ell=k),
\]
\[
 r_k^{\mathrm u}=\sum_{\ell\ge1}s_\ell(\gamma)\Pr(K_{2\ell}=k),
 \qquad r_{k+}^{a}=\sum_{j\ge k}r_j^a\quad(a\in\{\to,\mathrm u\}).
\]
These are also the source's loop-deleted limiting laws.

## Claim to prove or disprove

For **each fixed** \(\rho\in[0,1)\), on an event of probability one, for
every fixed integer \(k\ge1\), first let clock time \(n\to\infty\):
\[
 r_{n,k}^{\rho,\to}\to r_k^{\to},\quad
 r_{n,k}^{\rho,\mathrm u}\to r_k^{\mathrm u},\quad
 r_{n,k+}^{\rho,\to}\to r_{k+}^{\to},\quad
 r_{n,k+}^{\rho,\mathrm u}\to r_{k+}^{\mathrm u}.
\]
Only after these fixed-\(k\) limits, let \(k\to\infty\). The four asserted
asymptotics are
\[
 r_{k+}^{\to}\sim\pi_k^\gamma,
 \qquad r_{k+}^{\mathrm u}\sim2^\gamma\pi_k^\gamma,
\]
\[
 r_k^{\to}\sim\frac{\pi_k^\gamma}{k},
 \qquad r_k^{\mathrm u}\sim\frac{2^\gamma\pi_k^\gamma}{k}.
\]
Equivalently, each corresponding iterated ratio (inner limit in \(n\), then
outer limit in \(k\)) equals one. In particular, "amplitude ratio
\(2^\gamma\)" is read, consistently with the source theorem, as
undirected divided by directed. No simultaneous regime \(k=k(n)\), no
uniform limit as \(\rho\uparrow1\), and no finite-time rate is claimed.

## Cheapest decisive reduction and permitted scope

At every non-refresh step the only transition is a discarded self-loop. At
the \(j\)-th refresh the transition is \((Y_{j-1},Y_j)\). Hence, pathwise,
\[
 V_n=\{Y_0,\ldots,Y_{M_n}\},
\]
and both loop-deleted simple edge sets at clock time \(n\) equal those of the
iid skeleton \(Y_0,\ldots,Y_{M_n}\). Since \(M_n/n\to q>0\) almost surely,
the clock-time statistics are iid statistics along an almost surely diverging
random subsequence. This is the proposed transfer route to audit. It predicts
no residual \(\rho\)-factor under the source normalization by \(R_n\).
(A normalization by deterministic \(\alpha(n)\), which is not the claim,
would retain the ordinary sampling-rate factor through
\(\alpha(qn)/\alpha(n)\to q^\gamma\).)

The permitted target is a complete proof that this identity plus the source's
loop-deleted iid theorem transfers all four iterated limits, or an exact
endpoint/normalization obstruction showing which displayed formula fails.
