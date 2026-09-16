## 新WIN-1-16｜五个不同素因子的奇本原非亏数：小分量界

- **精确定义**：\(\sigma(n)\) 为正因子和。称 \(n\) 为本原非亏数，若 \(\sigma(n)\ge2n\)，且每个真因子 \(d\mid n\) 都满足 \(\sigma(d)<2d\)。设
  \[
  n=\prod_{i=1}^{5}p_i^{a_i},\quad
  3\le p_1<\cdots<p_5,\quad a_i\ge1,\quad
  R=\prod_{i=1}^{5}p_i.
  \]
- **待证命题**：每个这样的 \(n\) 都满足 \(\min_i p_i^{a_i+1}<2R\)。
- **开放依据**：原文 Conjecture 1 提出一般界；Lemma 4 已处理奇数且不同素因子数为 3 或 4 的情形，偶数也另有结果。本题冻结为五素因子的下一层。[Zelinsky，Conjecture 1、Lemma 4](https://cs.uwaterloo.ca/journals/JIS/VOL29/Zelinsky/zel14.pdf)。
- **AI 入口与验收**：利用 \(\prod p_i/(p_i-1)>2\) 限制素数分支，再用 \(\sigma(n/p_i)<2n/p_i\) 限制指数。目标是带严格剪枝依据的穷尽证明；反例给出因子分解和全部五个素数商的精确检查。

