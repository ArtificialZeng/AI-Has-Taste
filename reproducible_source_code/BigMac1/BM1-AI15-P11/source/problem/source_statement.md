# Source statement

# 11. Erdős #993：树的 independent-set sequence 是否总是单峰？

## 猜想

对树 \(T\)，令

\[
i_k(T)=\#\{\text{size-}k\text{ independent sets of }T\}.
\]

猜测序列

\[
i_0(T),i_1(T),\ldots,i_{\alpha(T)}(T)
\]

总是 unimodal。

注意：更强的 log-concavity 已经被 2023–2025 年的反例推翻，但所有这些树的序列仍是 unimodal。

2026 年完整枚举已经把树和森林的无反例范围推进到 30 个顶点，因此若反例存在，必须有更大的核心。

## 为什么 AI 比纯枚举更适合

独立多项式对 rooted tree 满足极简单 DP：

\[
I_T(x)=I_{T-v}(x)+xI_{T-N[v]}(x).
\]

因此可以训练 / 搜索树结构，直接最大化“单峰违反度”：

\[
\max_{k<\ell<m}\min(i_k-i_\ell,\ i_m-i_\ell).
\]

AI 不必枚举所有树，而可用：
- subtree mutation；
- grammar search；
- PatternBoost；
- symbolic construction；
- 从已知 non-log-concave families 放大参数。

## 反例证书

一棵 tree edge list + 精确系数序列即可。

## 来源

- Erdős #993  
  https://www.erdosproblems.com/993
- 当前计算状态  
  https://api.scinet.pub/p/8383c81d-e6c5-406d-aa40-43e383f3d57f

---
