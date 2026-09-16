## 新WIN-1-20｜车道合并计数在中心窗口的统一二项渐近式

- **精确定义**：令
  \[
  E_{m,k}=\frac{G_{m,k}}{\binom{2m-1}{k}},\qquad
  G_{m,k}=\begin{cases}
  \displaystyle\sum_{i=0}^{k}\binom{2m-1}{i},&k<m,\\[4pt]
  \displaystyle\sum_{i=0}^{2m-2-k}\binom{2m-1}{i}
  +(k-m+1)\binom{2m}{k+1},&k\ge m,
  \end{cases}
  \]
  其中 \(m\ge1\)、\(0\le k\le2m-1\)，上限为负的和取 0。这是原模型的期望空隙。
- **精确问题**：令 \(k=m+\lfloor x\sqrt m\rfloor\)、\(\delta_m(x)=\lfloor x\sqrt m\rfloor-x\sqrt m\)。求显式函数 \(F_0,F_1\)，并证明对每个固定 \(A>0\)，一致地对 \(|x|\le A\)，
  \[
  E_{m,k}=\sqrt m\,F_0(x)+F_1(x,\delta_m(x))+O_A(m^{-1/2}).
  \]
- **开放依据**：原文已有精确计数和部分渐近估计，§8 第 2 问明确要求改进 \(k\) 接近 \(m\) 时的近似。本题冻结为含取整修正及统一误差的二项展开。[Insko–Johnson–Sullivan，Corollary 7.2、§8](https://ecajournal.haifa.ac.il/Volume2026/ECA2026_S2A9.pdf)。
- **AI 入口与验收**：把二项和转为二项分布尾概率，结合 Stirling 展开与连续性修正；特别处理 \(x=0\) 两侧拼接。完整成果必须给出两个函数及统一误差证明，不能仅拟合一条曲线。
