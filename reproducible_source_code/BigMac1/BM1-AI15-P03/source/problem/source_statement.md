# Source statement

# 3. A383733：严格证明零点集恰为 \(\{7,8,12,16\}\)

## 精确问题

令 \(a(n)\) 为 chorded cycle \(C_n^{(3)}\) 的 proper 3-colorings 数。现有精确 / 模素数计算已检查到 \(n=3000\)，只发现

\[
a(n)=0
\iff
n\in\{7,8,12,16\}.
\]

问题是把“3000 以内成立”提升成

\[
\boxed{\forall n\ge6,\quad a(n)=0\iff n\in\{7,8,12,16\}.}
\]

## 为什么 AI 友好

- odd branch 已有闭式；
- even branch 已知来自 54-state transfer matrix；
- 两个偶数同余类的序列已有低阶线性递推（约 34/35 阶）；
- 因而剩下的是一个典型“线性递推序列最终正性”问题。

## 两条可能很短的证明

### 路线 A：构造性

直接为所有足够大的 \(n\bmod m\) 给出周期 3-coloring pattern，再有限检查小例外。

### 路线 B：谱分解

对递推特征多项式：
1. 严格隔离所有根；
2. 证明唯一正主导根；
3. 对其余根给出模上界；
4. 得到显式 \(N_0\)，使 \(a(n)>0\) 对 \(n>N_0\) 恒成立；
5. 对 \(n\le N_0\) 精确检查。

## 来源

- OEIS A383733  
  https://oeis.org/A383733
- 当前问题页  
  https://api.scinet.pub/p/69d6d14f-32c0-4de4-933e-9d4b4ab99e2a

---
