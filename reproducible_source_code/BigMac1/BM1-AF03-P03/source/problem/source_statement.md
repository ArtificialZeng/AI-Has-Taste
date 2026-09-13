# Source statement

# 3. \((1,2)\)-bosonic-fermionic coinvariant ring：Conjecture 3.2 的首个开放维数 \(n=5\)

John Lentfer 在 2025 年提出候选 monomial basis
\[
B_n^{(1,2)}
\]
用于 coinvariant ring \(R_n^{(1,2)}\)。Conjecture 3.2 断言
\[
\boxed{
B_n^{(1,2)}\text{ 是 }R_n^{(1,2)}\text{ 的 basis}.
}
\]

作者已经证明候选集合大小为
\[
|B_n^{(1,2)}|=2^{n-1}n!,
\]
并明确写道猜想已验证至
\[
n\le4.
\]

因此第一未验证维数：
\[
\boxed{n=5}.
\]
候选基只有
\[
2^4\cdot5!=1920
\]
个 monomials。

## AI 路线

1. 精确实现 supercommutative algebra；
2. 复现 \(n=3,4\)；
3. 构造正次数 \(S_n\)-invariant ideal；
4. 按 multidegree 分块；
5. Gröbner basis / standard monomial computation；
6. 检查候选 1920 个 monomials 是否恰为标准单项式。

反例可以是：
- 一个 exact linear dependency；
- 一个缺失的 quotient class；
- 某个 graded dimension 与候选不符。

若 \(n=5\) 成立，让 AI 从 initial ideal 中猜一般 \(n\) 的递推结构，争取由有限验证升级到一般证明。

## 来源

John Lentfer, *A conjectural basis for the \((1,2)\)-bosonic-fermionic coinvariant ring*, Algebraic Combinatorics 8 (2025), 711–743.  
https://alco.centre-mersenne.org/articles/10.5802/alco.424/

---
