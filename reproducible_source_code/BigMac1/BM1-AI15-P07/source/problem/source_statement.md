# Source statement

# 7. Erdős–Szekeres #699：二项式系数的公共“大”素因子

## 猜想

对

\[
1\le i<j\le \frac n2
\]

是否总存在素数 \(p\ge i\)，使

\[
p\mid
\gcd\!\left(\binom ni,\binom nj\right)?
\]

这是一个**单个有限反例即可终结**的数论猜想。

截至 2026 年已有大规模计算验证到 \(n\le100000\)，没有找到 weak-form 反例；更强的 \(p>i\) 版本则已有少数反例。

## 为什么仍适合 AI

Kummer 定理把

\[
p\mid\binom nk
\]

转成 base-\(p\) 加法进位条件。AI 可以不是机械继续扫描，而是分析：

- 哪类 \((n,i)\) 只有极少个 \(p\ge i\) 因子；
- 如何选 \(j\) 同时避开这些素数；
- 强版本反例的结构是否能“变形”为弱版本反例。

## 最短反例证书

只需：

\[
(n,i,j)
\]

加上两个二项式系数 gcd 的完整素因子分解，并证明所有公共素因子都 \(<i\)。

## 来源

- DeepMind Formal Conjectures issue（状态 open）  
  https://github.com/google-deepmind/formal-conjectures/issues/887
- 2026 计算验证至 \(10^5\) 的记录可作为 baseline，而不是证明。

---
