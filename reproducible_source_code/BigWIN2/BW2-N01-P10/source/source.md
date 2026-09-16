## 新WIN-1-10｜Schur 形状 \((2,2)\) 的单项式多重集能否恢复整数分拆？

- **精确定义**：对正整数分拆 \(\lambda=(\lambda_1,\ldots,\lambda_\ell)\)，\(\ell\ge2\)，在 Schur 多项式 \(s_{(2,2)}(x_1,\ldots,x_\ell)\) 的展开中，将各单项式代入 \(x_i=\lambda_i\)。系数为 \(r\) 的单项式重复保留 \(r\) 次，所得数值多重集记为 \(\mathcal S_{22}(\lambda)\)。
- **待证命题**：对每个 \(N\)，若 \(\lambda,\mu\vdash N\) 且 \(\mathcal S_{22}(\lambda)=\mathcal S_{22}(\mu)\)，则 \(\lambda=\mu\)。两分拆总和相同是必要的题设。
- **开放依据**：原文证明形状 \((2,1)\) 的单射性，并在 Conjecture 6.2 提出一般两行形状问题；本题选取 \((2,2)\)。[Thomas–Tung，Theorem 1.4、Conjecture 6.2](https://ecajournal.haifa.ac.il/Volume2027/ECA2027_S2A4.pdf)。
- **AI 入口与验收**：用半标准 Young 表生成多重集，按总和分桶找碰撞；正向先恢复最大部件，再使用原文的恢复引理。反例是两个同总和分拆及完全一致的多重集。

