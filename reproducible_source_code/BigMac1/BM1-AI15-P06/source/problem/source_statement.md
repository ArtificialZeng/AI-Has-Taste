# Source statement

# 6. Kusner 的 taxicab 等距集猜想：首个开放维数 \(n=5\)

## 精确问题

在 \(\mathbb R^n\) 的 \(\ell_1\) 距离

\[
\|x-y\|_1=\sum_{j=1}^n|x_j-y_j|
\]

下，令 \(e(\ell_1^n)\) 为最大 equilateral set 大小。

Kusner 猜测：

\[
e(\ell_1^n)=2n.
\]

目前只证明到 \(n\le4\)，所以第一个开放参数就是

\[
\boxed{e(\ell_1^5)=10?}
\]

等价地：能否找到 11 个 \(\mathbb R^5\) 中的点，使任意两点 \(\ell_1\) 距离完全相同？

## 为什么适合 AI

\(\ell_1\) 的绝对值可由差值符号模式线性化。

固定所有

\[
\operatorname{sgn}(x_{ri}-x_{si})
\]

之后，55 条等距条件变成线性方程 / 不等式。因此整个问题可化为有限 sign-pattern feasibility。

## 反例路线

搜索 11 个有理点。若找到，验证只需逐对算 55 个有理距离。

## 正面路线

- 超平面排列 / oriented matroid 约化；
- SAT 枚举 coordinate order types；
- 每个分支 LP infeasibility；
- Farkas lemma 给短对偶证书。

## 来源

- 2026 新文再次确认 \(p=1\) 只知到 \(n\le4\)：相关问题页  
  https://api.scinet.pub/p/74491319-9bc4-4067-8f7a-ba824d8dc6c4

---
