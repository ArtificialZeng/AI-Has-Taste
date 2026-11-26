# Proof audit

Status of current manuscript (`paper/main.tex`, `proof/star_pack_crt_tier2_proof.md`):
**passed for mathematical soundness and exact zero-float certification** (2026-11-26).

Terminal status: **`partial theorem`** (the full Agoh--Giuga conjecture remains open; no interactive proof assistant such as Lean/Coq/Isabelle was used).

## Independent adversarial reconstruction & bugs caught and fixed

Every theorem in the manuscript was reconstructed from definitions and subjected to adversarial boundary testing before finalizing:

1. **Lemma 2.1 & Theorem 2.2 (Star-Pack Reciprocal Dominance & Exact Extremal Normal-Set Theorem):**
   - Verified exhaustiveness and disjointness of the 7-leaf partition over all $2^5 = 32$ truth assignments of $\{3, 5, 7, 23, 83\}$.
   - Independently audited every star $A_c = \{c\} \sqcup T_c$ on every leaf with exact balanced-tree `Fraction` sums.
   - **Discrepancy corrected from earlier round framing:** Preliminary notes cited a 14-leaf bound of $338{,}033$ at $N=\{7\}$. Independent reconstruction proved every normal set in $N=\{7\}, F=\{3,5\}$ satisfies $\max(S) \ge 457{,}679$, while our sharper 7-leaf max-capacity Star-Pack proves the **exact attained minimum** outside Leaf 2 ($N=\{5,7,23,83\}, F=\{3\}$) is **$352{,}757$**, uniquely achieved at Leaf 3's 100%-normal greedy set $L^{(3)}$ ($|L^{(3)}|=8{,}880$).
   - Verified Lemma 2.1 never requires normality on $S_{>B}$, hence rigorously implies $j_d = 8{,}135$ for all $d \ge 27{,}692$ in Borwein--Maitland--Skerritt (2013) without settling intermediate relaxed depths $d \in [312, 27{,}691]$.
   - Verified non-uniqueness of $|S| = 8{,}135$ via explicit normal witness $L' = (L \setminus \{321{,}053\}) \cup \{321{,}073\}$.

2. **Theorem 3.1 (Mod-16 & Mod-8 Congruences) & Theorem 3.3 ($a \ge 2$ Splitting):**
   - Verified $+8$ invariance in $(\mathbb{Z}/16\mathbb{Z})^\times$ and $(1-4)^k \equiv 1 - 4k \pmod{16}$ ($4^2 \equiv 0 \pmod{16}$) both algebraically and exhaustively over all residue-count tuples mod 8.
   - Properly attributed the odd-Giuga mod-8 congruence $m - a \equiv 1 \pmod 8$ to Mavrotheris (Aug 2026, DOI `10.5281/zenodo.22085830`).
   - Verified exact integer checks $321{,}053^{10{,}000} > 10^{55{,}065}$, $321{,}053^{1{,}053} > 10^{5{,}798}$, and primality of $1{,}284{,}211$.

3. **Lemma 4.1 & Theorem 4.2 (Forced-Prime CRT + 2D Lattice Tier 2 Bounds):**
   - **Soundness gap caught and closed in Part 3 (`dp2`):** Using single-option `(1, |T_c|, cap[c])` transitions alone could miss strictly smaller leaf counts $1 \le |W_c| < |T_c|$. Fixed by applying a suffix-minimum over $k$ (`dp_sound[ds][k] = min_{k' >= k} dp[ds][k']`), computing a dynamic exact fractional-knapsack upper bound $K_{\mathrm{ub}}$, and verifying soundness against randomized partial-subset enumeration in `tests/test_agoh_giuga_tier2.py`.
   - **Disjointness guard added in Part 4d (`dm = 27`):** Explicitly asserted `p < L[-m0_hi_eff]` and `c < L[-m0_hi_A]` at every branch so omitted/forced primes are guaranteed disjoint from the top $m_0$ primes of $L$.
   - **Zero-float Lagrangian checks (`dm = 35` and `dm >= 43`):** Replaced all floating-point logarithms with exact integer power inequalities $c^v B^{v(|T|-1)-u} \le (\prod T)^v$ and $P_{\mathrm{top}}^{1000} B^{a_{1000}} \ge 10^{1000(D-1-40729)}$.
   - **AST audit & tamper tests:** Confirmed syntactically via `ast` that `src/verify_agoh_giuga_certificate.py` contains zero floating-point constructs, and confirmed fail-closed rejection on schema, digest, leaf-partition, lattice-witness, and interval-gap tampering.
   - **Strengthened dichotomies:** Per-rank reciprocal bounds $x_j < jB/(j - \Delta m - B\cdot\mathrm{gap}_L)$ raised the certified largest-prime dichotomies to $P(n) > 10^{3{,}685}$ ($\omega = 8{,}138$) and $P(n) > 10^{103}$ ($\omega = 8{,}146$).

4. **Theorem 5.1 ($r = 2$ Giant-Prime Structural Barrier):**
   - **Boundary error caught and fixed:** Preliminary notes stated $P_1 P_2 < t_0(N_0)^3 M_0^2$. Boundary evaluation at $d_1 = x_+$ (corresponding to $d_1 = P_2 - 1$) showed $P_1 P_2$ exceeds $t_0(N_0)^3 M_0^2$ by $\Theta(M_0)$. Proved the exact unconditional strict inequality $P_1 P_2 < t_0(N_0)^3 M_0^2 + t_0(N_0)^2 M_0$, verified strictly at $d_1 = x_+$ across $(N_0, M_0)$, and proved via exact integer arithmetic that $t_0(3)^3 + 10^{-5} < 0.4523$, establishing $P_1 P_2 < 0.4523 M_0^2$ for all $M_0 \ge 10^5$.

Historical note: Earlier August 2026 audits (`audit/GEMINI_REVIEW.md`, `audit/IMPROVED_BOUND_PROOF_AUDIT.md`) are retained for provenance; the current manuscript supersedes both and does not depend on any external computational bound.
