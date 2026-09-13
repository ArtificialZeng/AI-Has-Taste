# Source statement

# 13. Sherman–Morrison + iterative refinement：最终是否必然后向稳定？

## 猜想

对 rank-one updated system

\[
(A+uv^\top)x=b,
\]

Sherman–Morrison formula 本身可能数值不稳定。

Hashemi–Nakatsukasa 2025 证明 iterative refinement 可在合理条件下稳定，并根据实验提出更强猜想：

若

\[
\kappa_2(A),\quad\kappa_2(A+uv^\top)
\]

都安全地低于 \(\epsilon_M^{-1}\)，那么固定精度 iterative refinement 最终应产生 backward-stable solution。

## 为什么值得用 AI 反例优先

这是一个浮点算法猜想，最危险情况往往在 **2×2 或 3×3** 就能出现。

可以把 IEEE-like rounding 抽象成

\[
\operatorname{fl}(a\circ b)=(a\circ b)(1+\delta),\quad |\delta|\le u
\]

并让 SMT / interval arithmetic 搜索误差符号的 adversarial trajectory。

## 两种成功

### 反例
给出小矩阵 \(A,u,v,b\) 和精确浮点格式，使：
- 两个 condition numbers 合规；
- refinement 仍不进入 backward-stable regime。

### 正面
证明误差 recurrence

\[
\eta_{k+1}\le q\eta_k+C u
\]

且 \(q<1\)，从而最终稳定。

## 来源

- Hashemi & Nakatsukasa, *Instability of the Sherman-Morrison formula and stabilization by iterative refinement*  
  https://arxiv.org/abs/2510.01696

---
