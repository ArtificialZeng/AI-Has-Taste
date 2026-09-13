# Claim ledger — NOVELTY_LOCK

冻结时间：**2026-08-29（Asia/Shanghai）**。下列 13 项是检索前冻结的有限主张集合；检索结论只覆盖 `search_log.md` 记载的来源和查询。“未发现”不等于不存在。

分类约定：`exact` = 来源逐字或等价的精确陈述；`paraphrase` = 忠实转述；`inference` = 本项目从来源推出；`author report` = 作者/计算仓库报告、尚未由本 Gate 独立重放；`unverified` = 尚无可依赖证据。

| ID | Frozen claim | Class | Status at lock | Primary evidence and location | Confidence | Consequence |
|---|---|---|---|---|---|---|
| C01 | 对本题的 $n\ge 6$，$C_n^{(3)}$ 的顶点集是 $\mathbb Z/n\mathbb Z$，边为无向简单边 $\{i,i+1\}$、$\{i,i+3\}$，偶数 $n$ 时再加 $\{i,i+n/2\}$；$a(n)$ 数的是到一个带标号三色集合的所有 proper maps，不要求满射。 | exact + formal clarification | **verified** | [OEIS A383733](https://oeis.org/A383733), COMMENTS/Maple code；Lopez-Bonilla et al., DOI [10.9734/jamcs/2025/v40i102060](https://doi.org/10.9734/jamcs/2025/v40i102060), Definition 1.1, pp. 80–81. | high | 所有证明和 verifier 必须按这个 literal edge set；重复边（尤其 $n=6$）只保留一次。 |
| C02 | OEIS A383733 的 offset 是 6，已公布 $n=6,\ldots,20$ 的 15 项；其零项恰在 $7,8,12,16$，且 $a(20)=120$。 | exact | **verified as database record** | [OEIS text record](https://oeis.org/search?fmt=text&q=id:A383733), `%S`, `%O`；[OEIS table](https://oeis.org/A383733/list). b-file SHA-256 `f88fe3991ada3aa6e5df90be8c10822b6b2f4460d5a55d3dd344855a4e66ed3d`. | high | 给出最小回归基线，并直接否定 OEIS 自身的“4 的倍数反复为零”评论。 |
| C03 | 对奇数 $n$，有闭式 $a(n)=L_n+2\cos(2\pi n/3)+2s_n+2$，其中 $(s_0,s_1,s_2)=(3,-1,1)$、$s_{n+3}=-s_{n+2}-s_n$；对应 12-state transfer matrix 的特征多项式为 $(\lambda-1)^2(\lambda^2-\lambda-1)(\lambda^2+\lambda+1)(\lambda^3+\lambda^2+1)^2$。 | exact | **published theorem** | Lopez-Bonilla et al., DOI [10.9734/jamcs/2025/v40i102060](https://doi.org/10.9734/jamcs/2025/v40i102060), Theorem 3.4 and Corollary 3.1, pp. 83–85；较早 [arXiv:2509.05845v1](https://arxiv.org/abs/2509.05845), Theorem 3.4. | high for statement; medium-high for printed derivation | 奇数支可化为显式代数根支配。期刊版 Newton-sum 推导附近有排字/公式错误，但其最终递推与逐根恒等式一致，最终证明应自行重建而非照抄。 |
| C04 | 奇数支的全体零点恰为 $\{7\}$。 | inference | **not found as a completed published proof** | 期刊文只证明“充分大奇数为正”（Corollary 5.1(ii)）并给闭式；[SciNet finding](https://api.scinet.pub/f/a760d2f8-717e-4d44-b3b9-86f30957a285), Claim 2 明标为 inference 且说未 formalized。 | medium-high that it is open in the searched record | 仍需显式根界/整数递推不等式加有限核验；不能把渐近式本身当作零点分类证明。 |
| C05 | 朴素 54-state paired-window matrix 的普通 trace 并不计数偶数支；需要额外的全局 seam/track-swap 闭合。 | exact + author report | **published failure; corrected mechanism reported in executable artifact** | DOI paper, Definition 3.1 and Theorem 3.6, pp. 86–88：54 个兼容状态且 $P(C_{2m}^{(3)},3)\ne\mathrm{tr}(\widehat A^m)$。固定提交 `b873c297…` 的 `a383733.py` 构造 54-state 矩阵 $M$ 与 seam indicator $S$，实现 $a(2m)=\sum_{i,j}(M^{m-3})_{ij}S_{ij}=\mathrm{tr}(M^{m-3}S^{\mathsf T})$（$m\ge4$）。 | high for published failure; medium-high for artifact until independent bijection audit | 任一谱证明都必须包含 seam functional/置换，不能使用 arXiv v1 的无 seam trace 等式；正确公式是 matrix-power linear functional，而非 ordinary trace。 |
| C06 | 偶数计数序列满足某个有限阶常系数线性递推。 | exact claim | **published, but cited proof should not be used without repair** | DOI paper, Theorem 3.7, pp. 88–89，声称阶 $d\le54$。同文 Remark 3.2 已指出朴素闭合失败，而 Lemma 3.2 只适用于与长度无关的 fixed offsets；Theorem 3.7 从“需额外 phase information”仍断言状态数不超过 54，论证未给出具体正确 automaton。SciNet artifact 提供可执行 54-state seam construction。 | medium | 递推存在性应从已序列化的正确 transfer-with-seam 重新证明；不要仅引用期刊 Theorem 3.7 的存在性段落。 |
| C07 | 正式期刊文计算到 $n=57$，并把最终零点问题留作猜想。 | exact | **verified, with internal contradiction** | DOI paper, Table 2 and Conjecture 6.3, pp. 91–93. Table 2 给 $a(11)=66$，但 Conjecture 6.3 却列出零点 $\{4,5,7,8,11,12,16\}$；$4,5$ 又在本题 $n\ge6$ 域外。 | high | 该猜想列表不可引用为证据；在本题域内，表格支持到 57 的 $\{7,8,12,16\}$，但仍只是有限计算。 |
| C08 | $6\le n\le3000$ 的零点恰为 $\{7,8,12,16\}$：到 400 为 bigint exact，401–3000 用两个素数的非零剩余认证。 | author report | **public finite-result artifact; not independently replayed in Gate 1** | [SciNet finding a760d2f8](https://api.scinet.pub/f/a760d2f8-717e-4d44-b3b9-86f30957a285), Claims 1/4；[GitHub commit b873c297…](https://github.com/scinet-ai/math-combinatorics/commit/b873c297e21bcd6ac973f1190a82a857010f8556), README/results. SciNet 标记 “awaiting independent review”。 | medium-high | 是本项目 discovery 基线，不是全体定理；Gate 4/5 应从固定输入独立重放。 |
| C09 | 两个偶数同余支 $n\equiv0\pmod4$、$n\equiv2\pmod4$ 的“最小递推阶”分别为 34、35。 | author report | **computational evidence, not a characteristic-zero minimality theorem** | [SciNet finding](https://api.scinet.pub/f/a760d2f8-717e-4d44-b3b9-86f30957a285), Claim 6；固定 artifact 的 `results/deep_analysis.json` 只保存 $K=54$、两个素数、BM 阶 `[34,34]`/`[35,35]` 与共同零候选，没有保存 BM 系数、特征/最小多项式或 Hankel minor。DOI paper earlier 猜测整偶支阶 $\le20$，与此模素数数据不相容。 | medium | 两素数一致不自动证明有理数域上的最小性。经独立重建的非零模 $p$ Hankel minor 可给有理数域阶数下界；上界 34/35 仍需精确递推系数与全程验证。 |
| C10 | 已有公开证明 $\forall n\ge6,\ a(n)=0\iff n\in\{7,8,12,16\}$。 | unverified | **not found; NOVELTY_LOCK remains open** | 截止冻结时，[SciNet problem](https://api.scinet.pub/p/69d6d14f-32c0-4de4-933e-9d4b4ab99e2a) 状态 `ACTIVE`、只有上述有限计算 finding、`Verification pending`；OEIS、arXiv、Crossref/OpenAlex 和精确短语检索未发现全体证明。 | medium-high within recorded search scope | 本题若得到完整可审计证明，在已检索范围内具有新颖性；发布前必须做第二次 novelty search。 |
| C11 | OEIS 评论“$n=8,12,16,\ldots$ 的 4 倍数反复为零”是正确规律。 | exact quotation | **refuted** | [OEIS A383733](https://oeis.org/A383733), COMMENTS 同时给出该评论；同一条目的末项 $a(20)=120$，且 DOI paper Table 2 也给 120。 | high | 不得把 OEIS 评论当定理；它是本项目必须显式纠正的附近错误强化。 |
| C12 | Skolem–Mahler–Lech 直接由检查到 3000 排除无限零点等差数列。 | inference | **false inference** | DOI paper 仅说明 LRS 的零点集是有限集与有限多个完整等差数列之并；[SciNet problem](https://api.scinet.pub/p/69d6d14f-32c0-4de4-933e-9d4b4ab99e2a) 也只说 3000 以内结果令其“不可信”，并要求严格证明。 | high | 有限前缀覆盖许多小模数不排除首项/模数很大的进程；SML 不能替代主导根界或构造。 |
| C13 | 论文 Definition 1.1 与 OEIS 本题的 $n=6$ 端点完全一致。 | exact comparison | **needs explicit correction** | DOI paper Definition 1.1 要求 $1<k<n/2$，对 $k=3,n=6$ 不成立；但同文 Theorem 3.6(c) 和 OEIS 都实际定义并计算 $C_6^{(3)}=K_{3,3}$、$a(6)=42$。 | high | 本项目应以用户/OEIS 的 literal edge-set 定义覆盖所有 $n\ge6$，并单独说明 $n=6$ 的 chord 与 diameter 重合。 |

## Theorem frontier at the lock

- **可直接作为已知输入：** literal graph definition；OEIS 的 15 项；正式论文的奇数闭式及 12-state 特征多项式；朴素 54-state trace 闭合失败。
- **仅为有限/计算证据：** $n\le3000$ 的零点核查；偶数两支 BM 阶 34/35；track-swap seam 代码实现，均须在 Gate 4/5 独立重建。
- **真正未解决端点：** 全体偶数正性（除 $8,12,16$）；完整零点集；若走谱路线，还缺精确特征/最小多项式、根隔离、系数界和显式阈值。
- **附近错误陈述：** OEIS 的“所有后续 4 倍数反复为零”；arXiv v1 的无 seam 偶数 trace；期刊 Conjecture 6.3 把 11 错列为零点并混入域外 4,5；“查到 3000 + SML 即足够”。

## NOVELTY_LOCK decision

截至 **2026-08-29**，在 `search_log.md` 明列的 OEIS、arXiv、DOI/Crossref、OpenAlex、SciNet、GitHub artifact 与精确网页查询范围内，**没有发现**本题全称命题的既有证明或反例。最强公开邻近结果是：正式论文给出奇数闭式并将偶数端点留作猜想；SciNet artifact 把零点集严格/模素数地推进到 $n=3000$，但明确把全体结论另立为 active problem。

## Post-result recheck

完成显式块构造后，以最终定理措辞、精确零点集以及块
`A=01`, `B=21202` 再检索一次（见 `search_log.md`, S08）。结果仍未发现
既有全称证明或反例。故本项目只作如下有界新颖性陈述：**在截至
2026-08-29 记录的数据库与查询范围内，本全称证明未见先例。**
