# Source statement

# 15. Type \(D_9\) absolute order 的 normalized flow

Gaetz–Gao 研究 finite complex reflection groups 的 absolute order \(\operatorname{Abs}(W)\) 与 Sperner property。除 Type \(D_n\) 外，相关 strong Sperner 结果已建立。

他们留下 normalized-flow conjecture：
\[
\boxed{
\operatorname{Abs}(D_n)
\text{ admits a normalized flow}.
}
\]

公开状态记录为已计算验证
\[
n\le8,
\]
因此首个未验证：
\[
\boxed{D_9}.
\]

## 为什么可以机器认证

normalized flow 本质是 cover edges 上的非负 rational variables
\[
f(x,y)\ge0
\]
满足指定 rank-flow conservation / normalization equations，因此是 rational LP feasibility。

直接展开 \(D_9\) 很大，必须利用：
- signed permutation cycle types；
- conjugacy/orbit quotient；
- edge-orbit variables；
- rank symmetry。

### 若 feasible
输出 exact rational orbit flows，lifting 后独立检查所有 flow equations。

### 若 infeasible
输出 Farkas dual certificate，严格反驳该 \(D_9\) 实例。

更重要的是从 \(D_9\) orbit solution 中找 \(D_n\to D_{n+1}\) 的递推模式。

## 来源

Christian Gaetz, Yibo Gao, *On the Sperner property for the absolute order on complex reflection groups*, Algebraic Combinatorics 3 (2020), 791–800.  
https://arxiv.org/abs/1903.02033

---
