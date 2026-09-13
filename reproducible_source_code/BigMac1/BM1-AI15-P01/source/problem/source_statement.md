# Source statement

# 1. \(4\times4\) 实矩阵 rank-\((2,2)\) Hadamard 分解：认证现成候选反例

## 精确问题

问是否所有满秩 \(4\times4\) 实矩阵 \(M\) 都可以表示成

\[
M=A\circ B,\qquad \operatorname{rank}(A)\le2,\quad \operatorname{rank}(B)\le2,
\]

其中 \(\circ\) 表示逐元素 Hadamard 乘积。

Igor Rivin 在 2025 年对 \(\mathbb F_2\) 完整搜索，找到了 5304 个反例；这些反例也被验证在整数域 \(\mathbb Z\) 上不可分解。但对 **实数域 \(\mathbb R\)**，论文只给出了强数值证据，并未给出严格实代数不可行性证明。

论文中一个最小候选为

\[
M=
\begin{pmatrix}
1&1&1&1\\
1&1&1&0\\
0&1&0&0\\
1&0&0&0
\end{pmatrix}.
\]

## 为什么这是本清单第一名

这里几乎不存在“找候选”的问题：候选已经明确。

AI 真正需要解决的是：

\[
\boxed{\nexists A,B\in\mathbb R^{4\times4}:
A\circ B=M,\ 
\operatorname{rank}A\le2,\ 
\operatorname{rank}B\le2}
\]

或反过来真的找到一个实分解，推翻现有数值猜测。

这可以写成有限多项式方程 / 不等式系统。rank \(\le2\) 等价于全部 \(3\times3\) minors 为零；矩阵零元又强迫相应的 \(a_{ij}b_{ij}=0\)，因此可按零模式分支。

## AI 攻击路线

1. 枚举 0 元位置处 \(a_{ij}=0\) 或 \(b_{ij}=0\) 的有限分支；
2. 对 1 元位置用尺度自由度消变量；
3. 加入所有 \(3\times3\) minors；
4. Gröbner basis / resultant 消元；
5. real radical / CAD / Positivstellensatz；
6. 如果得到数值近解，尝试 PSLQ / algebraic reconstruction；
7. 用第二个 CAS 独立复核。

## 严格成功标准

- **反证分解存在性**：给出每个零模式分支的实不可行证书；
- **推翻候选**：给出显式代数数或有理数 \(A,B\)，逐项检查 \(A\circ B=M\) 及 rank；
- 不能把“优化器找不到”写成证明。

## 发表价值

若给出第一个严格的 \(\mathbb R\) 反例认证，适合矩阵论、计算代数、代数几何交叉期刊；结果本身非常干净。

## 来源

- Igor Rivin, *Computational Resolution of Hadamard Product Factorization for \(4\times4\) Matrices*, arXiv:2508.14901  
  https://arxiv.org/abs/2508.14901

---
