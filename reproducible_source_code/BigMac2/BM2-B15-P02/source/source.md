# bigMac-00015-p02 — Blume–Capel 首次 Ursell 符号失效阶数的临界渐近

领域：概率、Ursell functions、生成函数零点、渐近分析。
来源状态：new-question / status-uncertain；下面的常数是待反驳或证明的监督器候选，
不是一手来源已经证明的结论。

精确命题：对 Delta>log(2)，令 q=2 exp(-Delta)/(1+2 exp(-Delta))，
P(X=1)=P(X=-1)=q/2，P(X=0)=1-q；令
kappa_j(q)=(d^j/dz^j) log(1-q+q cosh z)|_{z=0}。
定义 m_*(Delta)=min{m integer>=2 : (-1)^(m+1) kappa_(2m)(q)<0}。
证明或反驳
lim_{epsilon downarrow 0} sqrt(epsilon) m_*(log(2)+epsilon)=pi^2/(4 sqrt(2))。
等价候选是令 a=arcosh(exp(Delta)/2) 后 a m_*(Delta)->pi^2/4。
这里 m_* 是半阶指标，真正 cumulant 阶数为 2m_*；零值不算首次严格失效。

一手来源：Shengchun Yu, A note on Ursell functions for the Blume-Capel model,
arXiv:2609.04610v1, https://arxiv.org/abs/2609.04610v1 。
本地 PDF：batches/literature/bigMac-15/2609.04610v1.pdf。
已检查定位：Section 4 p.4 的定义与 kappa_2,kappa_4,kappa_6；
Proposition 4 / equations (8),(9) p.5。
已知边界：来源证明每个 Delta>log2 均存在某个失效偶阶，并确定零点
+/-a+(2l+1)pi i；最近四零点给固定 Delta 的高阶渐近。
来源所读正文没有给 Delta downarrow log2 时的第一个失效阶数的统一渐近。

拟研究差异与价值：定量描述临界边界附近要到多高阶才观察到严格符号失效；
既要证明存在失效，也要排除全部更早阶，不能只沿某个子序列找到负值。
最便宜决定性测试：用有理 q<1/2 的 exact moment-cumulant recursion 检查前几阶，
再独立重算最近零点导出的相位和候选常数。首个小例：q<1/3 时 m_*=2；
q=1/3 的 kappa_4=0 必须另查，不可当严格失效。
决定性证明证书：带参数一致误差的零点和或等价精确表达，加上对所有更早 m 的符号控制。
只有 fixed-Delta 的 O(error) 不足以交换临界极限和阶数极限。
最快否证：常数、半阶规范化或最早阶出现不符；浮点取消误差必须用精确/区间验证排除。
历史区别：已登记 Pearson random walk、occupancy 及 dependence 课题均无相同 cumulant
或临界量词。有限星图的 distinct-vertex 推广如有，只能作为附属推论，
不能声称已求全部图的最小反例规模。
