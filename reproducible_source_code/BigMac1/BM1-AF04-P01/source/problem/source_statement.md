# Source statement

# 1. A278992：从已知指数生成函数严格推出四阶 D-finite 递推

## 问题

OEIS A278992 计数 **simple chord-labeled chord diagrams with \(n\) chords**。

其指数生成函数已经明确给出：

\[
F(t)
=
(1+\sqrt{1-2t})(1-2t)^{-1/2}
\exp(-1-t+\sqrt{1-2t})
-(2-t)e^{-t}.
\]

但截至 2026-08-29，OEIS 仍把下式标为：

> **Conjecture D-finite with recurrence**

\[
\begin{aligned}
0={}&(-n+2)a(n)
+(2n^2-8n+7)a(n-1)\\
&+(6n^2-18n+11)a(n-2)\\
&+(n-1)(6n-11)a(n-3)\\
&+2(n-1)(n-2)a(n-4).
\end{aligned}
\]

## 为什么特别适合 AI

这是最典型的：

\[
\boxed{
\text{显式 EGF}
\Longrightarrow
\text{线性微分方程}
\Longrightarrow
\text{系数递推}
}
\]

问题。

强模型可以直接：

1. 令
   \[
   s=\sqrt{1-2t}
   \]
   消去代数函数；
2. 为第一项构造 annihilating differential operator；
3. 与 \((2-t)e^{-t}\) 的 annihilator 合并；
4. 得到 \(F(t)\) 的多项式系数 ODE；
5. 对
   \[
   F(t)=\sum_{n\ge0}a_n\frac{t^n}{n!}
   \]
   抽取系数；
6. 精确核对初值与起始 index。

## 成功标准

不能只是“验证前十万项”。

必须给出：

- ODE；
- 符号恒等式；
- ODE → recurrence 的严格系数转换；
- 所需初值。

如果发现 OEIS 递推有 index shift 或少量边界修正，也同样是有价值的澄清结果。

## 评价

- **AI 成功形态：极好**
- **数学影响力：中低**
- **适合作为科研 skill 的快速闭环测试**

## 来源

- OEIS A278992  
  https://oeis.org/A278992
- Krasko–Omelchenko, *Enumeration of Chord Diagrams without Loops and Parallel Chords*  
  https://arxiv.org/abs/1601.05073
