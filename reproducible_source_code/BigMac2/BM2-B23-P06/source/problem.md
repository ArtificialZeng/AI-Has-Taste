# 精确问题表述

## 冻结对象

本文件只解释 `source.md` 中冻结的有限分类任务，不改变其量词或把它扩张为普遍分类。

对整数 \(n\ge 1\)，定义严格真因子集
\[
D_n:=\{d\in\mathbb Z_{>0}:d\mid n,\ d<n\}.
\]
给定 \(D\subseteq D_n\)，令 \(G(n,D)=ICG_n(D)\) 为顶点集
\(\mathbb Z/n\mathbb Z\) 上的简单无向图。不同顶点 \(x,y\) 相邻，当且仅当
\[
\gcd(\widetilde x-\widetilde y,n)\in D,
\]
其中 \(\widetilde x,\widetilde y\) 是任意整数代表，`gcd` 取非负最大公因数。此条件与代表的选择无关；对 \(x\ne y\)，该最大公因数必在 \(D_n\) 中。排除 \(x=y\) 明确禁止自环，条件关于 \(x,y\) 对称。

有限图 \(G\) 称为 **perfect**，若对它的每个诱导子图 \(H\) 都有
\(\chi(H)=\omega(H)\)。等价地（Strong Perfect Graph Theorem），\(G\) 不含长度
\(2k+1\ge5\) 的诱导圈（odd hole），并且 \(\overline G\) 也不含这样的诱导圈
（亦即 \(G\) 不含 odd antihole）。

## 精确量词与待产出对象

须对
\[
\forall n\in\mathbb Z\ (1\le n\le64),\qquad
\forall D\subseteq D_n
\]
精确确定布尔值
\[
P(n,D):=\mathbf 1\{G(n,D)\text{ is perfect}\}.
\]
换言之，待分类集合是
\[
\mathcal P_{\le64}:=\{(n,D):1\le n\le64,\ D\subseteq D_n,
\ G(n,D)\text{ is perfect}\}.
\]
因为 \(|D_n|=\tau(n)-1\)，完整输入域共有
\(\sum_{n=1}^{64}2^{\tau(n)-1}=4197\) 个有序对 \((n,D)\)；任何一个都不能遗漏。
“将全部正例压缩”解释为：除逐项判定外，还须用可人工核查的因子格条件、覆盖整个输入域的有限参数族，或无歧义的完整表格表示 \(\mathcal P_{\le64}\)。这是一项有限分类请求，并非预先断言某张尚未产生的表为真。

## 边界情形与对称性

- \(n=1\) 时 \(D_1=\varnothing\)，唯一输入给出单顶点图 \(K_1\)。
- 对每个 \(n\)，\(D=\varnothing\) 给出无边图，\(D=D_n\) 给出完全图；两者均在量词内且均 perfect。
- 对所有输入，\(\overline{G(n,D)}=G(n,D_n\setminus D)\)。因此补图配对可用于核验，但不能用来删除任一输入。
- 不连通图、完全图、补图及其他退化情形全部保留；题目没有连通性假设。

## 完成标准与证书语义

对判为 imperfect 的每个等价类，必须给出图或其补图中的奇数长度至少五的顶点序列，并以精确邻接关系验证它是诱导圈。对判为 perfect 的每个等价类，必须给出可独立重放的 Berge/perfectness 证书、带证明的完整结构分解，或经审计的穷尽算法及其覆盖证明。浮点谱证据或软件返回的裸布尔值不构成证书。按乘法单位对 \(D\) 或见证去冗余只是一种表示压缩；它不得改变对全部 4197 个输入的覆盖义务。

## 范围、来源状态与拟议增量

冻结任务仅涉及 \(n\le64\)，不蕴含任何 \(n>64\) 的结论，也不解决所有 integral circulant graphs 的 perfectness 分类。`source.md` 报告的最近背景是：Basic, *On uniquely colorable Cayley graphs*, arXiv:2609.03184v1 的 §2 给出 integral circulant 对象，§5 将一般 perfect integral circulant 分类列为开放方向，并指出 unitary 情形 \(D=\{1\}\) 已有分类。该有限层本身是否已有公开 census、以及是否新颖，当前均未核实，故来源状态保持 `status-uncertain`；不得称其为已知开放问题或新结果。

拟议贡献可表为：最近背景是已分类的 unitary 子族及尚未完成的一般分类；拟议增量是 \(n\le64\) 的完整、压缩且有精确证书的有限层；首个有界验证路线是先覆盖 \(n\le32\) 的全部 539 个 \((n,D)\)，提取 odd-hole/antihole 见证，并检验 perfect 正例能否由可证明的标准结构覆盖。若公开一手来源已有同等 census，或正例无法获得可审计的覆盖证书，则该拟议增量应停放。
