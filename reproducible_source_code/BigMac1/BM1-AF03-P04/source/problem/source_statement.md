# Source statement

# 4. Monomial bialgebras：transitive-CYBE Conjecture 1.4 的 \(n=5\)

Berenstein–Greenstein–Li 定义 \(n\times n\) matrix \(a=(a_{ij})\) 为 transitive，如果
\[
a_{ik}\in\{a_{ij},a_{jk}\}
\]
对所有 \(i,j,k\) 成立。

设
\[
r=\{r(c)\}_{c\in C}
\]
是 transitive CYBE 的任意解族。Conjecture 1.4 断言
\[
\boxed{
a\text{ transitive}
\Longrightarrow
r(a)\text{ solves ordinary CYBE}.
}
\]

论文明确说明一般 \(C\) 下已经验证
\[
n\le4.
\]
因此首个开放小参数是
\[
\boxed{n=5}.
\]

## 为什么 AI 友好

对固定 \(n=5\)，问题可以压成：
- transitive array 的有限 combinatorial types；
- CYBE residual 的 symbolic commutator expansion；
- transitive-CYBE relations 下的 normal-form reduction。

### Prover
无同构生成 5×5 transitive arrays，quotient color relabeling 与 index permutations，对每类把 residual 化简为 0。

### Breaker
寻找：
- 一个 5×5 transitive array；
- 一个有限维 Lie algebra；
- 一组 exact \(r(c)\) 满足 transitive CYBE；
- 但普通 CYBE residual 非零。

若反例存在，最终证书可以全是有理 structure constants。

## 来源

Arkady Berenstein, Jacob Greenstein, Jian-Rong Li, *Monomial bialgebras*  
https://arxiv.org/abs/2602.02342

---
