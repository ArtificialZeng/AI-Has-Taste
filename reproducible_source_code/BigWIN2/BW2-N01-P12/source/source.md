## 新WIN-1-12｜\(2\times4\times3\) 非退化超矩阵的全部受限计数

- **精确定义**：取弱递减非负整数三元组 \(\lambda,\mu\)，满足 \(\mu_i\le\lambda_i\)、\(\lambda_i\le4-i\)、\(\mu_i\le3-i\)。考虑 \(\mathbb F_q\) 上两个 \(4\times3\) 切片 \(A,B\)，规定
  \[
  A_{ij}=0\ (i>4-\lambda_j),\qquad
  B_{ij}=0\ (i>4-\mu_j).
  \]
  非退化指相应边界格式超行列式非零。
- **待证命题**：对每个上述零位置形状及每个素数幂 \(q\)，非退化数组个数为
  \[
  q^9(q-1)^6
  \prod_{i=1}^{3}[5-i-\lambda_i]_q
  \prod_{i=1}^{3}[4-i-\mu_i]_q,
  \qquad[r]_q=1+\cdots+q^{r-1}.
  \]
- **开放依据**：原文 Conjecture 3.1 已证明 \(k=2\) 及若干特殊形状；本题完整处理 \(k=3\) 中尚未覆盖的形状。[Koprowski–Lewis，Conjecture 3.1、Theorem 4.1](https://ecajournal.haifa.ac.il/Volume2027/ECA2027_S2A3.pdf)。
- **AI 入口与验收**：利用原文的轨道求和式，将每个形状化成至多 \(|S_4\times S_3|=144\) 项的符号计算，逐一核验多项式恒等式。有限域抽样只能辅助；全部形状的符号证书才能覆盖所有 \(q\)。

