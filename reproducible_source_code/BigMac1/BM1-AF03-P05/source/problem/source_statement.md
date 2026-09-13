# Source statement

# 5. 稀疏补图的 \(q(G)=2\) 猜想：首个新阶 \(n=9\)

对 graph \(G\)，令 \(S(G)\) 为所有与 \(G\) 具有指定 off-diagonal zero/nonzero pattern 的 real symmetric matrices。定义
\[
q(G)=\min_{A\in S(G)}\#\{\text{distinct eigenvalues of }A\}.
\]

Barrett–Fallat–Furst–Nasserasr–Rooney–Tait 猜测：
\[
\boxed{
e(\overline G)\le n-3
\Longrightarrow q(G)=2.
}
\]

论文证明：
- 若 \(\overline G\) bipartite，则成立；
- 许多特殊 family 成立；
- 并记录 \(n=7,8\) 已验证。

所以自然下一阶为
\[
\boxed{n=9},
\]
此时只需考虑
\[
e(\overline G)\le6,
\]
而 bipartite complements 已全部排除。

## AI 路线

\(q(G)=2\) 时可经 affine normalization 搜索 symmetric orthogonal/involutory realization：
\[
A=A^\top,\qquad A^2=I,
\]
同时满足 \(G\) 的零模式。

1. graph6 无同构生成所有 non-bipartite \(H=\overline G\) 且 \(|E(H)|\le6\)；
2. 对每个 \(G\) 求 rational/algebraic realization；
3. exact 验证 \(A^2=I\) 与 pattern。

若某个图无解，必须用 Gröbner、real radical、Positivstellensatz 或 CAD 给出不可行证书，不能以数值求解失败代替反例。

## 来源

Wayne Barrett et al., *Graphs with Bipartite Complement that Admit Two Distinct Eigenvalues*, Electronic Journal of Linear Algebra 42 (2026), 146–161.  
https://journals.uwyo.edu/index.php/ela/article/view/9443

---
