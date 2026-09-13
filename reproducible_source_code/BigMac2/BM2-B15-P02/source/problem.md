# Precise problem statement

## Frozen original claim

The immutable input is [`source.md`](source.md), whose SHA-256 at triage was
`3e003968a6991322c7ad79fac1cf58c3f36107f2bb5344109cf871bbfce585be`.
Its mathematical claim, reproduced without alteration, is:

> 对 Delta>log(2)，令 q=2 exp(-Delta)/(1+2 exp(-Delta))，
> P(X=1)=P(X=-1)=q/2，P(X=0)=1-q；令
> kappa_j(q)=(d^j/dz^j) log(1-q+q cosh z)|_{z=0}。
> 定义 m_*(Delta)=min{m integer>=2 : (-1)^(m+1) kappa_(2m)(q)<0}。
> 证明或反驳
> lim_{epsilon downarrow 0} sqrt(epsilon) m_*(log(2)+epsilon)=pi^2/(4 sqrt(2))。
> 等价候选是令 a=arcosh(exp(Delta)/2) 后 a m_*(Delta)->pi^2/4。
> 这里 m_* 是半阶指标，真正 cumulant 阶数为 2m_*；零值不算首次严格失效。

## Precise interpretation

All logarithms are natural. For each real
\(\Delta\in(\log 2,\infty)\), set
\[
 q=q(\Delta):=\frac{2e^{-\Delta}}{1+2e^{-\Delta}}
              =\frac{2}{e^\Delta+2}\in(0,\tfrac12).
\]
Let \(X=X_\Delta\) be the real random variable with
\[
 \mathbb P(X=1)=\mathbb P(X=-1)=q/2,
 \qquad \mathbb P(X=0)=1-q.
\]
Its moment-generating function is
\(M_q(z)=\mathbb E(e^{zX})=1-q+q\cosh z\).  Let
\(K_q(z)=\log M_q(z)\) denote the unique analytic germ at \(z=0\) with
\(K_q(0)=0\); thus no global choice of logarithm is involved.  For every
integer \(j\geq 1\), define the cumulant
\[
 \kappa_j(q):=K_q^{(j)}(0).
\]
(Symmetry gives \(\kappa_{2r+1}(q)=0\), but odd cumulants play no role.)

For integers \(m\geq2\), put
\[
 S_m(\Delta):=(-1)^{m+1}\kappa_{2m}(q(\Delta)).
\]
The first strict sign failure is
\[
 m_*(\Delta):=\min\{m\in\mathbb Z:m\geq2, S_m(\Delta)<0\}.
\]
Equality \(S_m(\Delta)=0\) is not a failure.  The definition requires the
set to be nonempty; the supplied source reports a prior existence result for
every \(\Delta>\log2\).  In a self-contained resolution, that existence must
either be cited from a checked theorem or proved as part of the argument.

The frozen target is the single assertion
\[
 \boxed{\displaystyle
 \lim_{\varepsilon\downarrow0}
 \sqrt{\varepsilon}\,m_*(\log2+\varepsilon)
 =\frac{\pi^2}{4\sqrt2}.}
\]
Here the limit ranges over all real \(\varepsilon>0\) tending to zero; the
integer-valued minimum is evaluated separately at each such parameter.  A
proof must therefore control the sign for every earlier integer
\(2\leq m<m_*(\Delta)\), not merely exhibit a subsequence of failing orders.
A disproof may establish a different limit, nonexistence of the limit, or a
parameter sequence incompatible with the displayed constant, using rigorous
error/sign control.

## Equivalent normalization

With \(\Delta=\log2+\varepsilon\), define
\[
 a(\Delta):=\operatorname{arcosh}(e^\Delta/2)
            =\operatorname{arcosh}(e^\varepsilon)>0.
\]
Since
\[
 \frac{a(\log2+\varepsilon)}{\sqrt\varepsilon}\longrightarrow\sqrt2,
\]
the frozen target is equivalent (and only in the same limit
\(\Delta\downarrow\log2\)) to
\[
 a(\Delta)m_*(\Delta)\longrightarrow\frac{\pi^2}{4}.
\]
The index \(m_*\) is a half-order index: the corresponding cumulant order is
\(2m_*\).

## Scope and status at intake

- The parameter boundary \(\Delta=\log2\) (equivalently \(q=1/2\)) is not in
  the domain; only the one-sided critical limit is asserted.
- The problem concerns the one-variable cumulants above.  It asserts no
  monotonicity of \(m_*\), no convergence rate, and no extension to
  distinct-vertex or general-graph Ursell functions.
- Fixed-\(\Delta\), high-order asymptotics alone do not justify the required
  joint regime \(\Delta\downarrow\log2\), \(m\to\infty\).
- Intake status remains `new-question / status-uncertain`, not a verified open
  problem.  The nearest prior result reported by the supplied source is
  Shengchun Yu, *A note on Ursell functions for the Blume--Capel model*,
  arXiv:2609.04610v1, especially Proposition 4 and equations (8)--(9): it is
  reported to prove existence of some failing even order for fixed
  \(\Delta>\log2\) and to identify the relevant zeros, but not this uniform
  first-failure asymptotic.  This triage job did not independently audit that
  paper, so those statements are literature leads rather than verified
  evidence here.

