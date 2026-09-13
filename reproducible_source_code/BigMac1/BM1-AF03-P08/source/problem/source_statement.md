# Source statement

# 8. Kazhdan–Lusztig \(R\)-polynomial 的 \(q\)-Fibonacci product formula：首个未验证 \(n=10\)

令
\[
v_n=34\cdots n\,12.
\]
对于
\[
e\le\sigma_1\le\sigma_2\le v_n
\]
的 Bruhat interval，研究
\[
\widetilde R_{\sigma_1,\sigma_2}(q).
\]

Chen–Fan–Guo–Zhong 猜测它总可写成
\[
\boxed{
\widetilde R_{\sigma_1,\sigma_2}(q)
=
q^{g(\sigma_1,\sigma_2)}
\prod_iF_{h_i(\sigma_1,\sigma_2)}(q^{-2}),
}
\]
其中 \(F_j\) 是论文定义的 \(q\)-Fibonacci polynomials。

该猜想在原始工作中已验证
\[
n\le9,
\]
一般情形仍开放，所以首个未验证：
\[
\boxed{n=10}.
\]

## AI 反例优先路线

对每个 pair：
1. 用 KL recurrence exact 计算 \(\widetilde R(q)\)；
2. 除去最大 \(q\)-power；
3. exact factorization；
4. 检查每个 factor 是否来自允许的 \(q\)-Fibonacci family。

若失败，一个
\[
(\sigma_1,\sigma_2)
\]
和一条 exact polynomial 就是反例。

若全部成立，应从 reduced words、heaps、Bruhat interval decomposition 中找“独立 Fibonacci blocks”的结构解释。

## 来源

William Y. C. Chen, Neil J. Y. Fan, Peter L. Guo, Michael X. X. Zhong, *A Class of Kazhdan-Lusztig R-Polynomials and q-Fibonacci Numbers*  
https://arxiv.org/abs/1312.2170

---
