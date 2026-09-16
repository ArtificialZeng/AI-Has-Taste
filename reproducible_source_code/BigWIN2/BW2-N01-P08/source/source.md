## 新WIN-1-08｜Fuss–Catalan 路径：固定峰数后的 NNE 多项式是否实根？

- **精确定义**：取整数 \(m\ge2,n\ge1\)。考虑从 \((0,0)\) 到 \((n,mn)\)、使用北步 \(N\) 与东步 \(E\)、始终满足 \(y\ge mx\) 的路径。峰为连续片段 \(NE\)，\(\operatorname{nne}(D)\) 为连续片段 \(NNE\) 的出现次数。定义
  \[
  W^{(m)}_{n,k}(t)=
  \sum_{D:\,\#NE(D)=k}t^{\operatorname{nne}(D)},\qquad1\le k\le n.
  \]
- **待证命题**：每个 \(W^{(m)}_{n,k}(t)\) 都只有实零点。
- **开放依据**：普通 Dyck 路径的相应结果已有证明；Alexandersson 在其维护的页面中仍将 Fuss–Catalan 推广列为猜测。本题明确固定了矩形方向和连续片段计数约定。[Alexandersson，NNE 猜测及已知边界](https://www.symmetricfunctions.com/realRootedCatalan.htm)。
- **AI 入口与验收**：以高度、峰数和末尾两步为状态计算整数系数；用 Sturm 序列精确判根。一个确有非实根的多项式即可否证；正向可寻找保实根递推或正交多项式表达。

