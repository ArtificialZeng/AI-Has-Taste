## 新WIN-1-19｜二次取余集合的归一化大小是否不收敛？

- **精确定义**：对正整数 \(n\)，令
  \[
  S_0(n)=\{1,\ldots,\lfloor n/2\rfloor\},\qquad
  S_{j+1}(n)=\{n\bmod k:k\in S_j(n),\ k>0\},
  \quad s_j(n)=|S_j(n)|.
  \]
- **待证命题**：\(s_2(n)/n\) 在 \(n\to\infty\) 时没有极限。
- **开放依据**：原文证明一次取余的归一化计数收敛，并对迭代情况给出上下界；Problem 2 提出从 \(j=2\) 开始不收敛。本题只攻第一层。[Baraskar–Vukusic，§7 Problem 2](https://cs.uwaterloo.ca/journals/JIS/VOL29/Vukusic/vukusic2.pdf)。
- **AI 入口与验收**：先按模 6、模 30 的剩余类分组实验，寻找两类分离的子序列。充分证书是 \(n_r,m_r\to\infty\) 及 \(\alpha<\beta\)，满足 \(\limsup_r s_2(n_r)/n_r\le\alpha<\beta\le\liminf_r s_2(m_r)/m_r\)。数值散点本身不证明不收敛。

