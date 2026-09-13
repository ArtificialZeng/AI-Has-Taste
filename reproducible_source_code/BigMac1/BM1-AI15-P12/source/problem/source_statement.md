# Source statement

# 12. rank-\(\le2\) 矩阵的 Marcus permanent inequality

## 问题

设 \(T\) 是 \(n\times n\) 矩阵且

\[
\operatorname{rank}(T)\le2.
\]

Marcus 提出的一个开放 permanent 不等式为

\[
\operatorname{per}
\begin{pmatrix}
T&T\\
T&T
\end{pmatrix}
\le
\binom{2n}{n}\operatorname{per}(T)^2.
\]

正元素等若干情形已有结果，但一般符号 / 复数情形仍开放。

## AI 友好的实际切法

不要直接攻击所有 \(n\)。

先强制项目目标为：

\[
n=3\quad\text{或}\quad n=4
\]

的任意实 rank-2 矩阵，先搜索反例；若没有，再符号证明这个首批小阶情形。

rank-2 可参数化为

\[
T=uv^\top+xy^\top,
\]

永久式于是变成低次数多项式。

## 路线

- quotient 掉行列尺度；
- 随机 / adversarial 参数优化；
- exact rational reconstruction；
- symbolic expansion；
- SOS / CAD / cylindrical algebraic decomposition。

## 来源

- MathDB 条目及原始论文入口  
  https://mathdb.com/p/351542/permanent-inequality-for-rank-at-most-two-matrices

---
