# NEON-P01 — Star-Pack Dominance and Forced-Prime CRT Lower Bounds for the Agoh–Giuga Conjecture

[Final PDF / 最终稿](../../../pdfs/Neon/NEON-P01_Star_Pack_Dominance_and_Forced_Prime_CRT_Lower_Bounds_for_the_Agoh_Giuga_Conjecture.pdf) · [LaTeX entry / 入口](source/manuscript/main.tex) · [Evidence / 复现材料](source/evidence/)

Collection / 合集: Neon (Gemini 4 Neon). First obtained / 首次得到: 2026-11-26. Archived / 入库: 2026-11-27.

## Result / 结论

The Agoh–Giuga conjecture (Giuga, 1950; Agoh, 1995) asserts that no composite integer $n$ satisfies $\sum_{j=1}^{n-1} j^{n-1} \equiv -1 \pmod n$, equivalently that no composite integer is simultaneously a Giuga number and a Carmichael number. The full conjecture remains open. The strongest prior published computational bound (Borwein, Maitland, and Skerritt, 2013) spent ten days and 120 GB of storage trimming normal-set trees to depth 311 to establish $\omega(n) \ge 4{,}771$ and $n > 10^{19{,}907}$, while noting that normal-set pruning can never exceed the $8{,}135$-prime threshold of the greedy normal set $L = L_{27,692}$.

- **Exact Extremal Normal-Set Theorem (Theorem 2.2):** Via a 4-line *Star-Pack Reciprocal Dominance Lemma* and a 7-leaf partition of the odd primes, every finite normal set $S \subset \mathbb{P}_{\mathrm{odd}}$ with $\sum_{p \in S} 1/p > 1$ satisfies $|S| \ge 8{,}135$ (not uniquely attained), $\max(S) \ge 321{,}053$ (equality iff $S = L$), and $\prod_{p \in S} p \ge P(L)$ ($40{,}733$ decimal digits, equality iff $S = L$). This exhausts the Borwein–Maitland–Skerritt algorithm ($j_d = 8{,}135$ for all $d \ge 27{,}692$) with zero external large-scale computation, and establishes the sharp outside-Leaf-2 minimum $\max(S) \ge 352{,}757$ (uniquely attained at Leaf 3's $8{,}880$-element greedy normal set).
- **Elementary mod-16 congruence and $a \ge 2$ splitting (Theorems 3.1 & 3.3):** Gives a 10-line elementary proof of $m - a \equiv 1 \pmod 8$ (independently proved for odd Giuga numbers via unimodular lattices by Mavrotheris, Aug 2026) together with its exact mod-16 refinement, and a purely elementary 3-line bound for Giuga value $a \ge 2$: $\omega(n) \ge 329{,}188$, $P(n) \ge 1{,}284{,}211$, and $\ge 1{,}808{,}611$ decimal digits (no analytic number theory required).
- **Breaking past the normal-set ceiling (Theorem 4.2):** Coupling forced-prime CRT congruences $X \equiv C_F Y \pmod{M_F}$ with sound suffix-minimum 2D integer knapsacks, linear forcing cascades, zero-float Lagrangian star inequalities, and 846 exact 2D lattice witnesses establishes unconditionally:
  $$\omega(n) \ge 8{,}138, \qquad P(n) \ge 326{,}057, \qquad n \ge 10^{40{,}921} \;(\ge 40{,}922 \text{ decimal digits}),$$
  with sharp dichotomies at the smallest prime-factor counts ($\omega(n) = 8{,}138 \implies \ge 51{,}798$ digits and $P(n) > 10^{3{,}685}$; $\omega(n) = 8{,}146 \implies \ge 41{,}895$ digits and $P(n) > 10^{103}$; $\omega(n) = 8{,}154 \implies \ge 41{,}128$ digits).
- **Sharp $r = 2$ giant-prime barrier (Theorem 5.1):** For $n = M_0 P_1 P_2$ ($a = 1$, $N_0 = M_0(1 - \sum_{p \mid M_0} 1/p)$), proves $N_0 \ge 3$ is odd and $P_1 P_2 < t_0(N_0)^3 M_0^2 + t_0(N_0)^2 M_0 < 0.4523 M_0^2$ ($M_0 \ge 10^5$), explaining why local CRT + 2D lattice refutation leaves $3 \le N_0 \lesssim 10^{17{,}704}$ open.

Agoh–Giuga 猜想（Giuga 1950；Agoh 1995）断言不存在合数 $n$ 满足 $\sum_{j=1}^{n-1} j^{n-1} \equiv -1 \pmod n$（等价于不存在同时为 Giuga 数和 Carmichael 数的合数）。完整猜想目前仍然开放。此前已发表的最强计算下界（Borwein–Maitland–Skerritt, 2013）耗时 10 天与 120 GB 存储将正规集搜索树剪枝至深度 311，证得 $\omega(n) \ge 4{,}771$ 与 $n > 10^{19{,}907}$，并指出纯正规集方法永远无法突破贪心正规集 $L = L_{27,692}$ 的 $8{,}135$ 素因子天花板。

- **正规集精确极值定理（Theorem 2.2）：** 通过 4 行 *Star-Pack 倒数支配引理* 与奇素数的 7 叶子划分，零外部计算依赖证明任意满足 $\sum_{p \in S} 1/p > 1$ 的有限奇素数正规集满足 $|S| \ge 8{,}135$（不唯一达到）、$\max(S) \ge 321{,}053$（当且仅当 $S = L$ 取等）与 $\prod_{p \in S} p \ge P(L)$（$40{,}733$ 位，当且仅当 $S = L$ 取等），彻底穷尽 Borwein–Maitland–Skerritt 算法（$j_d = 8{,}135, \forall d \ge 27{,}692$），并确定 Leaf 2 之外的精确极小最大素因子为 $352{,}757$。
- **初等模 16 同余与 $a \ge 2$ 纯初等分裂界（Theorems 3.1 & 3.3）：** 给出 $m - a \equiv 1 \pmod 8$（Mavrotheris 2026 年 8 月独立由幺模格证得）及其模 16 精确提升的 10 行初等证明；并给出 $a \ge 2$ 情形的 3 行纯初等界 $\omega(n) \ge 329{,}188$、$P(n) \ge 1{,}284{,}211$、位数 $\ge 1{,}808{,}611$（不依赖解析数论）。
- **突破正规集天花板的无条件 Tier 2 主定理（Theorem 4.2）：** 结合强迫素数 CRT 同余 $X \equiv C_F Y \pmod{M_F}$、完备后缀最小二维整数背包、线性强迫级联、零浮点 Lagrangian 星形不等式与 846 组精确二维格见证，无条件证得 $\omega(n) \ge 8{,}138$、$P(n) \ge 326{,}057$、$n \ge 10^{40{,}921}$（$\ge 40{,}922$ 位十进制数字），并给出小 $\omega(n)$ 时的剧烈二分跳跃（$\omega=8{,}138 \implies \ge 51{,}798$ 位且 $P(n) > 10^{3{,}685}$；$\omega=8{,}146 \implies \ge 41{,}895$ 位且 $P(n) > 10^{103}$；$\omega=8{,}154 \implies \ge 41{,}128$ 位）。
- **两枚巨素数补全的精确结构障碍（Theorem 5.1）：** 证明 $n = M_0 P_1 P_2$ 必满足 $N_0 \ge 3$ 为奇数且 $P_1 P_2 < t_0(N_0)^3 M_0^2 + t_0(N_0)^2 M_0 < 0.4523 M_0^2$（$M_0 \ge 10^5$），阐明为何仅靠局部 CRT + 二维格方法无法排除 $3 \le N_0 \lesssim 10^{17{,}704}$ 区间的两枚巨素数补全。

## Check it yourself / 自行验证

From `source/evidence/` (Python 3 standard library only; zero external dependencies, zero floating-point arithmetic in the verifier):

```sh
python3 src/verify_agoh_giuga_certificate.py certificates/agoh_giuga_tier2_certificate.json
python3 -m unittest tests/test_agoh_giuga_tier2.py -v
# Optional: regenerate the 2.68 MB exact certificate from scratch (~20 s):
python3 src/generate_agoh_giuga_certificate.py
```

| File | Purpose |
|---|---|
| `src/verify_agoh_giuga_certificate.py` | Standalone AST-audited 100% zero-float fail-closed verifier (~15 s, checks all 7 leaves, mod-16, $a \ge 2$, all 846 lattice witnesses, and Lagrangian star inequalities) |
| `src/generate_agoh_giuga_certificate.py` | Exact certificate generator (~20 s on CPython 3.13) |
| `certificates/agoh_giuga_tier2_certificate.json` | Serialized exact Tier 1 + Tier 2 JSON certificate (846 `(U, R)` witnesses) |
| `tests/test_agoh_giuga_tier2.py` | 11 unit, AST zero-float, DP2 soundness, $r=2$ boundary, and fail-closed tamper tests |
| `src/verify_improved_bound.py`, `experiments/improved_bound_certificate.json` | Regression verifier retained for test suite compatibility |
| `proof/star_pack_crt_tier2_proof.md`, `proof/gap_ledger.md` | Detailed proof notes and closed gap ledger |
| `audit/PROOF_AUDIT.md`, `audit/BIBLIOGRAPHY_AUDIT.md`, `audit/PDF_AUDIT.md` | Internal proof, primary-source bibliography, and 13-page visual PDF audit records |

## Scope and limitations / 范围与局限

- **Terminal status: `partial theorem`.** The full Agoh–Giuga conjecture remains open; Theorem 5.1 proves a concrete structural barrier explaining why local CRT + 2D lattice refutation cannot eliminate two-giant-prime completions on its own.
- Not externally peer reviewed; no interactive proof assistant (Lean, Coq, Isabelle) was used.
- Priority and novelty wording is bounded to literature indexed through October 2026 (including Mavrotheris, Aug 2026, DOI `10.5281/zenodo.22085830`, and López, Oct 2026, `arXiv:2610.09129v2`).
- External literature PDFs are cited, not reproduced.

本文稿处于 `partial theorem` 状态（完整 Agoh–Giuga 猜想仍未解决），未经外部同行评审，亦未使用 Lean/Coq/Isabelle 等交互式定理证明器；全部计算断言由经 AST 审计的零浮点标准库验证器确定性复算。外部文献仅作引用，不转载原文。

The proofs, algorithms, zero-float verifier, exact certificate, and manuscript were produced with **Gemini 4 Neon** under the author's direction.
证明、算法、零浮点验证器、精确证书与文稿均由 **Gemini 4 Neon** 在作者指导下完成。
