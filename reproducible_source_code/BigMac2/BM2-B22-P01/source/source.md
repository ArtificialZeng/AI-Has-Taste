# bigMac-00022-p01 — immutable source

> 冻结日期：2026-09-09。此文件是问题入口的不可变来源记录；研究中的推导、失败与更正应写入后续 problem/checkpoint 文件，不回写本文件。

## 一手来源与本地证据

- Yi Du, *When a Relaxed PEP Is Exact: The Sharp Queried-Gradient Rate of Nesterov's Fast Gradient Method*，arXiv:2608.26719v1 [math.OC]，2026-08-27，18 页。
- 本地 PDF：`/Users/mac/4prove-or-disprove-math/batches/literature/bigMac-22/2608.26719v1.pdf`
- 本地 PDF SHA-256（以 `shasum -a 256` 实读）：`34ce307c547848e4f6c36604190195e67e7f59c3db20d7e842093ad313eef2fd`

## 原题（论文中的定义与开放范围）

令 `F_{0,L}(R^d)` 为 `R^d` 上凸、可微且梯度为 `L`-Lipschitz 的函数类。论文研究如下 FGM（论文 (FGM)，第 2 页）：

```text
y_0=x_0,  t_0=1,
y_{k+1}=x_k-(1/L)∇f(x_k),
t_{k+1}=(1+sqrt(1+4t_k^2))/2,
x_{k+1}=y_{k+1}+((t_k-1)/t_{k+1})(y_{k+1}-y_k).
```

这里 horizon `N` 执行 `N` 次更新，并在 `x_0,...,x_N` 查询梯度。论文式 (7)（第 3 页）定义

```text
W_N(L,R,d)
 := sup { min_{0≤k≤N} ||∇f(x_k)||^2 :
          f∈F_{0,L}(R^d), x_*∈argmin f, ||x_0-x_*||≤R }.
```

论文第 3 页的 Scope 明说：`N=1` 由 Proposition 8.1 解决，而 `2≤N≤6` 的五个有限分支仍缺解析刻画。本文冻结其中最小分支 `N=2`。

## 冻结的拟研究命题（不是论文已陈述的闭式猜想）

固定

```text
t_1=(1+sqrt(5))/2,
t_2=(1+sqrt(7+2sqrt(5)))/2,
beta=(t_1-1)/t_2
     =(sqrt(5)-1)/(1+sqrt(7+2sqrt(5))),
c_2=1/(3+beta).
```

猜想：对所有 `L>0`、`R≥0`、整数 `d≥1`，

```text
W_2(L,R,d)=c_2^2 L^2 R^2.
```

其中

```text
c_2^2 = 0.0928513193578614102140718294340... .
```

量词包括 `R=0` 的退化边界，也包括任意维数；不得把固定维度或浮点 PEP 最优值冒充该命题。

## 当前严格边界

论文 Theorem 2.1（第 4 页）对所有 `N≥1,L>0,R≥0,d≥1` 给出

```text
W_N(L,R,d) ≤ L^2 R^2/S_N,
S_N=Σ_{k=0}^N t_k^2.
```

下述精确一维 projection-envelope 构造给出本题下界，故当前有严格分离的解析夹逼

```text
c_2^2 L^2R^2 ≤ W_2(L,R,d) ≤ L^2R^2/S_2,
c_2^2 < 1/S_2.
```

归一化后：

```text
0.0928513193578614... ≤ W_2(1,1,d)
                     ≤ 0.1186296604458931... .
```

论文 Table 1（第 13 页）的 dimension-unrestricted exact-interpolation PEP 浮点值为 `0.0928513212`，报告 primal-dual gap `3.4e-9`。论文明确说明这些数值及 gap 不是严格 enclosure 或解析证书，`2≤N≤6` 仍是数值状态；它与 `c_2^2` 相差约 `1.84e-9`，只能算提出闭式的线索，不能算证明。Theorem 7.2（第 12 页）只解决 `N≥7`（先在 `d≥N-4`，再等距嵌入到更高维），不能用于宣布 `N=2` 已解。Proposition 8.1（第 13–14 页）证明的是 `W_1=L^2R^2/4`。

## 最小非平凡精确下界证书

先取 `L=R=1`，任选单位向量 `e`，令线段 `K=[0,c_2e]`，并定义 Moreau/projection envelope

```text
f(x)=max_{g∈K} { <x,g>-(1/2)||g||^2 }.
```

则 `f∈F_{0,1}(R^d)`，`∇f(x)=Proj_K(x)`。取 `x_*=0,x_0=e`。直接代入 FGM 得

```text
x_1=(1-c_2)e,
x_2=(1-(2+beta)c_2)e=c_2e,
∇f(x_0)=∇f(x_1)=∇f(x_2)=c_2e,
```

其中最后一行用到 `c_2<1/2`。因此 `min_{0≤k≤2}||∇f(x_k)||^2=c_2^2`。平移、缩放

```text
f_{L,R}(x)=L R^2 f((x-x_*)/R)
```

并把该一维构造嵌入任意 `d≥1`，即得 `c_2^2L^2R^2` 的全量词下界；`R=0` 单独直接为零。

## 与来源的差异及潜在小贡献

- 论文提出并数值研究整个 `2≤N≤6` 开放带，但没有给出上述 `c_2` 闭式，也没有声称 Table 1 的 `N=2` 数值已严格确定。
- 本项目只冻结 `N=2`，并把一维精确下界和待找的 exact PEP dual 配成一个可证伪的单点问题。
- 若能给出目标恰为 `c_2^2` 的精确对偶证书，便解析解决论文未解带的第一个格点；若最优值不同，给出精确插值反例同样是决定性贡献。
- 不研究 post-gradient 点 `y_k` 的准则；论文指出它与 queried-gradient `x_k` 准则不同。

## 首个最快决定性测试：exact PEP dual

归一化 `L=R=1`，建立包含 `x_0,g_0,g_1,g_2` 与相应函数值的完整 smooth-convex exact-interpolation PEP；用上面下界构造的活跃约束猜测对偶乘子。在代数数域

```text
Q(sqrt(5), sqrt(7+2sqrt(5)))
```

中求解目标恰为 `c_2^2` 的对偶恒等式，并精确核验：

1. 所有乘子非负；
2. 对偶 slack 矩阵正半定（可用精确主子式、特征多项式与 Sturm 隔离）；
3. 恒等式覆盖完整插值约束、FGM 更新和 `||x_0-x_*||≤1`；
4. 下界 construction 的 projection 区间与全部等式精确成立。

若直接的 cocoercivity/Cauchy 组合能像 Proposition 8.1 一样给出同一恒等式，也可作为更短证书。浮点 SDP、采样或小 primal-dual gap 均不是完成标准。

## 快速否证与停机条件

- 任何满足完整 smooth-convex 插值不等式、FGM 递推和初始半径约束的精确 Gram/function-value 数据，只要能证明
  `min(||g_0||^2,||g_1||^2,||g_2||^2)>c_2^2`，就反驳冻结等式。
- 反例必须给出有理或代数数 PSD/插值证书；仅比 `0.0928513212` 更大的浮点输出不算反例。
- 若 exact PEP 得到不同代数值，应冻结新值及其 primal/dual 证书，而不是把误差吸收到本猜想。
- 不得把 relaxed 上界 `1/S_2` 当成真实最优值；论文 `N=1` 已展示 relaxed bound 可非紧。

## 开放状态

截至该 v1 论文及本地筛选证据，`N=2` 的解析 queried-gradient 常数仍开放；上式是由一维精确 witness 与数值 PEP 对齐所提出的新闭式猜想，不是论文定理。
