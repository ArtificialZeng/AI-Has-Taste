# Source statement

# 2. Barker 的 A321614 十阶递推：从“验证到 5000”升级为“对所有 \(n\) 的定理”

## 精确问题

OEIS A321614 计数 \(4\times2n\) 棋盘上达到最大数量 \(2n\) 的互不攻击 king placements，并按矩形对称群取自由计数。

Colin Barker 在 2018 年根据很短的初始序列猜测一个显式十阶线性递推：

\[
\begin{aligned}
a(n)= {}&12a(n-1)-54a(n-2)+98a(n-3)+17a(n-4)-346a(n-5)\\
&+505a(n-6)-210a(n-7)-120a(n-8)+126a(n-9)-27a(n-10).
\end{aligned}
\]

2026 年已有独立计算把该递推验证到 \(n=5000\)，但“验证很多项”仍不是一个 **全 \(n\) 数学证明**。

## 为什么特别容易

这是固定宽度棋盘问题，本质上有有限状态 transfer matrix。

真正目标不是再算一百万项，而是证明：

\[
\boxed{\text{生成函数的最小多项式 / 有效状态子空间恰好导出上述十阶递推。}}
\]

有限状态一旦正确构造，这类证明通常可以变成精确整数线性代数。

## AI 攻击路线

1. 独立重建 row/column 状态自动机；
2. Burnside 分别处理 identity、horizontal flip、vertical flip、\(180^\circ\) rotation；
3. 构造精确 transfer matrices；
4. 求可达且可观测的最小子空间；
5. 求 minimal polynomial；
6. 证明四个 Burnside 分支合并后的分母正是 Barker 给出的分母；
7. 用 Cayley–Hamilton 得到全 \(n\) 递推。

## 成功标准

最终证明必须是有限整数 / 有理矩阵等式，而不是“验证到 \(N\)”。

## 来源

- OEIS A321614  
  https://oeis.org/A321614
- 当前计算审计页面  
  https://api.scinet.pub/p/456c1f41-44f3-4eee-87dd-e34b50e0c451

---
