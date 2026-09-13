# bigMac-00015-p01 — 有限域原始求逆映射的精确 joint ANF leap

领域：有限域、Boolean algebraic normal form、表示复杂度。
来源状态：new-question / status-uncertain；下述等式是外层监督器提出的待验精化，不是来源已宣称的定理或已认证开放问题。

精确命题：对每个整数 n>=2、每个 F_2 上首一不可约 n 次多项式 p，
取 F=F_2[t]/(p)，以 E=(1,t,...,t^(n-1)) 为坐标基。令 J_n 为 F 的求逆
坐标映射，约定 J_n(0)=0。对全部 P in F_2^(n*n) 和 u in F_2^n（包括奇异 P），
定义 G(P,u)=adj(P) J_n(Pu)。在 n^2+n 个 Boolean 变量的唯一 multilinear ANF 中，
令 A(G) 是非零向量系数的 monomial support 集合。定义
L(G)=min_{A_1,...,A_s ordering A(G)} max_j |A_j minus union_{i<j} A_i|。
证明或反驳 L(G)=n。不得把定义域缩成 GL_n；不得静默把量词改为某个固定 p。

一手来源：Zheng Zhang and Na Zhang, Representation Redundancy and Structural Complexity
in Finite-Field Inversion, arXiv:2609.04583v1,
https://arxiv.org/abs/2609.04583v1 。
本地完整 PDF：batches/literature/bigMac-15/2609.04583v1.pdf。
已检查定位：Definition 11 / Proposition 12 p.11；Definition 14 p.12；
Theorem 17 pp.14–15；Table 1 p.17。
已知边界：来源证明 G 的每个 support monomial degree>=n，因而 L(G)>=n；
另有 deg(G)<=3(n-1)。来源给 n=3,4 的精确表，其 L=n，不能据此推一般 n。

拟研究差异与价值：把已知线性下界升级为全维精确结构量，并给可显式复核的
support ordering。若只是原文直接推论或无实质结构收益，登记重发现，不强行成文。
最小例：n=2 的完整 Boolean truth table 仅 2^6 个点，须先核验。
最便宜决定性测试：先精确算 n=2 和不同低次 p 的 ANF；再检查最小 degree-n
support 是否可覆盖全部必要变量并形成每步至多 n 个新变量的证书。系数须用
XOR_{C subset A} G(1_C) 或独立等价精确算法验证。
最快否证：找一个具体 n,p，使可证明最优 leap>n；找不到 ordering 不是反例。
AI 适配：稀疏 support、有限域精确运算与符号证书；不要启动大 truth table brute force。
历史区别：registry 既有 F-set 和 Laurent ring 条目不涉及此 Boolean joint-support 对象；
未发现等价题。一般有序基的扩展仅可单列为附加主张。
