# Source statement

# 2. STS(15) 的 Pasch-switch 商图：确定 79 点连通分量的直径

## 定义

15 点 Steiner triple system \(STS(15)\) 是一个 triples 集合，使每一对点恰好出现在一个 block 中。

已知 \(STS(15)\) 一共有：

\[
80
\]

个同构类。

一个 Pasch switch 把

\[
abc,\ ade,\ fbd,\ fce
\]

替换为

\[
abd,\ ace,\ fbc,\ fde.
\]

构造商图：

- 顶点 = 80 个 \(STS(15)\) 同构类；
- 若两类可由一次 Pasch switch 相连，则加边。

## 已知边界

公开文献/近期审计已经知道：

- 唯一 anti-Pasch class 是 isolated vertex；
- 其余
  \[
  79
  \]
  个 classes 构成一个 connected component；
- 但没有找到这个 79 点分量直径的公开精确值。

## 为什么极适合 AI

数学宇宙只有：

\[
80\text{ 个顶点}.
\]

任务完全有限：

1. 重建 80 个 canonical representatives；
2. 对每个 system 枚举所有 Pasch configurations；
3. switch；
4. canonicalize；
5. 建完整 quotient graph；
6. BFS all-pairs shortest paths。

## 严格成功证书

输出：

- 80 个 canonical representatives；
- quotient edge list；
- 79+1 component 验证；
- 直径 \(D\)；
- 一对距离恰为 \(D\) 的顶点；
- 独立 BFS verifier。

## 注意

这属于“**精确有限科研目标**”，不是著名历史猜想。正式投稿前要对设计理论数据库与 STS(15) 计算文献做一次更强的优先权查重。

## 来源

- TheoremDB reviewed status  
  https://theoremdb.org/statements/sts15-pasch-switch-graph
- Small STS(15) classification / Pasch-switch literature
