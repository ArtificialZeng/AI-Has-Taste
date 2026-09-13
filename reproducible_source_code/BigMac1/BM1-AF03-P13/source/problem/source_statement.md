# Source statement

# 13. Generalized snake posets：只攻击仍开放的 Ehrhart 根位置猜想

原论文 Conjecture 5.1 有两部分：
1. \(h^*\)-polynomial roots 全部 real and negative；
2. Ehrhart polynomial roots 位于一个指定圆盘。

**第 1 部分已在 2026 年 7 月被 Braun–Jal 证明，不能再当开放问题。**

仍开放的是第 2 部分。

对 generalized snake word \(w\)，其 Ehrhart polynomial
\[
L(\mathcal O(P(w));t)
\]
具有已证明的对称轴
\[
\operatorname{Re}z=-\frac{n+4}{2}.
\]

猜想所有根位于以该对称轴中心点
\[
-\frac{n+4}{2}
\]
为中心、半径
\[
\frac{n+2}{2}
\]
的圆盘。

作者验证所有 snake words：
\[
\boxed{\text{length}\le9}.
\]

所以自然下一层：
\[
\boxed{\text{length }10}.
\]

## AI 路线

1. 枚举 length-10 generalized snake words，quotient reversal/complement symmetry；
2. exact 计算 Ehrhart polynomial；
3. algebraic root isolation；
4. 对每个 root 严格验证圆盘不等式。

一个越界 algebraic root 就是反例。

正面一般路线：利用已证明 symmetry 与新的 \(h^*\)-real-rootedness，研究 Ehrhart transform 是否保持某种 root disk。

## 来源

Eon Lee, Andrés R. Vindas-Meléndez, Zhi Wang, *Generalized snake posets, order polytopes, and lattice-point enumeration*  
https://arxiv.org/abs/2411.18695

已解决的 \(h^*\) 部分：  
Benjamin Braun, Aryaman Jal, *Order polytopes of generalized snake posets are \(h^*\)-real-rooted*  
https://arxiv.org/abs/2607.00922

---
