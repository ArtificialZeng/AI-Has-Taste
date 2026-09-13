# Source statement

# 7. K-Knuth shape-interval Conjecture 7.6：首个未验证字母规模 \(n=8\)

对一个 straight increasing tableaux 的 K-Knuth equivalence class，令出现的 shapes 构成集合 \(\Sigma\)。

Conjecture 7.6 断言：
若
\[
\lambda_i,\lambda_j\in\Sigma,\qquad \lambda_i\subseteq\lambda_j,
\]
那么 Young lattice interval 中所有
\[
\lambda_i\subseteq\mu\subseteq\lambda_j
\]
也都属于 \(\Sigma\)。

即
\[
\boxed{
\lambda_i,\lambda_j\in\Sigma
\Longrightarrow
[\lambda_i,\lambda_j]\subseteq\Sigma.
}
\]

原论文明确：
\[
\boxed{\text{已验证 K-Knuth classes on }[n]\text{ for }n\le7.}
\]
所以首个未验证 alphabet size：
\[
\boxed{n=8}.
\]

## AI 路线

1. 生成所有 increasing tableaux over \([8]\)；
2. 构造 K-Knuth class；
3. 收集 shape set；
4. 对 comparable pair 检查 interval completeness。

反例证书很短：
- 两个已出现 shape；
- 一个缺失的中间 shape；
- class 的 canonical representative / equivalence proof。

若 \(n=8\) 全部通过，再从数据中猜 local shape-filling lemma，争取一般证明。

## 来源

Christian Gaetz et al., *K-Knuth Equivalence for Increasing Tableaux*, Electronic Journal of Combinatorics 23(1) (2016), P1.40.  
https://www.combinatorics.org/ojs/index.php/eljc/article/view/v23i1p40

---
