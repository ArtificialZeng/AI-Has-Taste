# Source statement

# 10. Lotka–Volterra tree-systems：首个未验证阶 \(n=9\)

某类 homogeneous Lotka–Volterra systems 与 trees 一一对应。van der Kamp 猜测：
\[
\boxed{
T_1\not\cong T_2
\Longrightarrow
LV(T_1)\not\sim LV(T_2),
}
\]
即非同构 trees 对应的 tree-systems 不会通过允许的 linear transformation 变成等价系统。

正式论文明确：
\[
\boxed{n<9\text{ 已验证。}}
\]
所以
\[
\boxed{n=9}
\]
是首个未验证阶。

## AI 路线

9-vertex unlabeled trees 的数量很小，可以完整处理。

### Breaker
寻找非同构 \(T_1,T_2\) 与可逆矩阵 \(M\)、参数重映射，使两个 LV vector fields 等价。

### Prover
给每个 tree-system 计算 preserved invariants：
- Darboux polynomial incidence；
- hypergraph structure；
- Jacobian / spectral data；
- rational integrals；
- parameter incidence lattice。

如果找到一个 invariant 能重构 tree，就有希望直接推一般 \(n\)。

## 来源

Peter H. van der Kamp, *Hypergraphs and Lotka-Volterra Systems with Linear Darboux Polynomials*, Journal of Dynamics and Differential Equations (2025).  
https://link.springer.com/article/10.1007/s10884-025-10446-2

---
