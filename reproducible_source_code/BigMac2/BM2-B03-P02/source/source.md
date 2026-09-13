## DM03-02 七原子矩问题的首批未覆盖有限支撑情形

一个有限 moment system 是三元组 $(p_i,t_i,z_i)_{i=1}^s$，其中 $p_i>0$、$\sum_i p_i=1$、$t_i\in\mathbb C$ 且 $|t_i|=1$、$z_i\in\mathbb C$，并满足

$$\sum_i p_it_i=\sum_i p_iz_i=\sum_i p_i\overline{t_i}z_i=0.$$

令 $E=\sum_i p_i|z_i|^2$。对任意概率向量 $q=(q_i)$，设

$$\mu=\sum_iq_it_i,\qquad \nu=\sum_iq_iz_i,\qquad \lambda=\sum_iq_i\overline{t_i}z_i,$$

并在 $|\mu|<1$ 时由

$$\begin{pmatrix}1&\mu\\ \overline\mu&1\end{pmatrix}\binom ab=\binom\nu\lambda$$

定义 $C(q)=|a|^2+|b|^2$。证明或反驳下列两个断言：

1. 若 $s\le5$，则存在 $|\operatorname{supp}q|\le3$、$|\mu|<1$ 的 $q$ 使 $C(q)\le5E/8$；
2. 若 $s\le6$，则存在 $|\operatorname{supp}q|\le4$、$|\mu|<1$ 的 $q$ 使 $C(q)\le E/4$。

若只能完成其中一个断言，必须明确冻结为局部结果。

来源与范围：Guangjian Zhang, *Exact Recovery Thresholds for Weighted Data Selection in Vector-Valued Linear Regression*, arXiv:2608.30254v1，Section 7，尤其 Lemmas 7.2--7.6、Theorem 7.7、Conjecture 7.8 与 Proposition 7.9。完整猜想无损归约到至多七原子；来源已覆盖三点预算的至多四原子、四点预算的至多五原子及若干特殊类。本题是两个预算的首批遗漏有限支撑层，不得冒充完整 Conjecture 7.8。
