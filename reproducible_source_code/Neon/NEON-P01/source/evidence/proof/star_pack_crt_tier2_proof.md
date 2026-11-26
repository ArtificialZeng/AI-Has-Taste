# Star-Pack Dominance, Elementary Congruences, and Forced-Prime CRT Bounds for the Agoh--Giuga Conjecture

**Terminal status:** `partial theorem` (the full Agoh--Giuga conjecture remains open).
**Exact verification:** 100% zero-float standalone Python verifier [`src/verify_agoh_giuga_certificate.py`](../src/verify_agoh_giuga_certificate.py) checking [`certificates/agoh_giuga_tier2_certificate.json`](../certificates/agoh_giuga_tier2_certificate.json) (~15.6 seconds, 846 `(U, R)` 2D lattice refutation pairs, zero proof assistant used).

---

## 1. Preliminaries & Notation

A composite counterexample $n > 1$ to the Agoh--Giuga conjecture ($\sum_{j=1}^{n-1} j^{n-1} \equiv -1 \pmod n$) is an odd squarefree integer $n = \prod_{p \in S} p$ ($m = \omega(n) = |S| \ge 2$) satisfying, for every $p \in S$:
- **Giuga condition:** $p \mid (n/p - 1)$, equivalently $\sum_{p \in S} \frac{1}{p} - \frac{1}{n} = a$ for a positive integer $a \ge 1$ (the *value* of $n$);
- **Carmichael condition:** $(p - 1) \mid (n - 1)$ (Korselt's criterion).

In particular, $S$ is a **normal** set of odd primes: no distinct $p, q \in S$ satisfy $p \mid (q - 1)$.

Let $q_1 = 3, q_2 = 5, \dots$ be the odd primes in increasing order, and let $L = L_{27,692}$ denote the greedy normal set starting from $\{5, 7\}$ up to $B = q_{27,692} = 321{,}053$. Exact rational arithmetic verifies:
- $|L| = 8{,}135$, $\max(L) = 321{,}053$,
- $\sum_{p \in L} \frac{1}{p} > 1$ with $\operatorname{gap}_L = \sum_{p \in L} \frac{1}{p} - 1 \approx 9.185030 \times 10^{-7} < \frac{1}{321{,}053}$,
- $\sum_{p \in L \setminus \{321{,}053\}} \frac{1}{p} < 1$,
- $P(L) = \prod_{p \in L} p$ has exactly $40{,}733$ decimal digits ($135{,}311$ bits, binary SHA-256 `826dad79c2ef410c85a9bd4cb8f3b1ea01dddfabfec8363badc427ca9f4ea7bb`).

---

## 2. Star-Pack Reciprocal Dominance Lemma & Exact Extremal Normal-Set Theorem

### Lemma 1 (Star-Pack Reciprocal Dominance)
Let $N, F$ be disjoint finite sets of odd primes with $N$ normal, let $B \ge \max(N \cup F \cup \{3\})$, and let
$$U = \{p \in \mathbb{P}_{\mathrm{odd}} \cap [1, B] \setminus (N \cup F) : \forall r \in N,\; r \nmid (p - 1) \text{ and } p \nmid (r - 1)\}.$$
Suppose $U = \bigsqcup_{c \in C} A_c$ is partitioned into pairwise disjoint *stars* $A_c = \{c\} \cup T_c$ such that for every $c \in C$:
1. $c \mid (q - 1)$ (hence $q \ge 2c + 1 > c$) for all $q \in T_c$;
2. $\operatorname{cap}(c) := \frac{1}{c} - \sum_{q \in T_c} \frac{1}{q} > 0$.

Let $S$ be any finite set of odd primes such that $S_{\le B} := S \cap [1, B]$ is normal, $N \subseteq S_{\le B}$, $S_{\le B} \cap F = \emptyset$, and $\sum_{p \in S} \frac{1}{p} > 1$. (Notice: normality is **not** required among primes in $S_{>B} := S \cap (B, \infty)$!) Partition $C = M_0 \sqcup M_1 \sqcup M_+$ where $M_0 = \{c : S \cap A_c = \emptyset\}$, $M_1 = \{c : \emptyset \ne S \cap A_c \subseteq T_c\}$, $M_+ = \{c : c \in S\}$. Then:
1. For each $c \in C$, $\sum_{q \in S \cap A_c} \frac{1}{q} \le \frac{1}{c}$ (with strict inequality for $c \in M_0 \cup M_1$), so $\sum_{q \in S_{\le B}} \frac{1}{q} \le \sum_{p \in N \cup C} \frac{1}{p}$.
2. Let $\Sigma := \sum_{p \in N \cup C} \frac{1}{p}$. If $\Sigma \le 1$, then $S_{>B} \ne \emptyset$, $\max(S) > B$,
   $$|S_{>B}| \ge |M_0| + t, \qquad t := \lfloor B(1 - \Sigma) \rfloor + 1 \ge 1,$$
   $$|S| \ge |N \cup C| + t, \qquad \prod_{q \in S} q > \left(\prod_{p \in N \cup C} p\right) B^t.$$
3. If $\Sigma > 1$ and $\Sigma - 1 < \min\bigl(\frac{1}{B},\, \min_{c \in C} \operatorname{cap}(c)\bigr)$, then:
   - $|S_{>B}| \ge |M_0|$ unconditionally;
   - $|S| \ge |N \cup C|$;
   - $\max(S) \ge B$, with equality $\max(S) \le B$ iff $S = N \cup C$;
   - $\prod_{q \in S} q \ge \prod_{p \in N \cup C} p$, with equality iff $S = N \cup C$.

*Proof.* Because $S_{\le B}$ is normal and $c \mid (q-1)$ for all $q \in T_c$, no star $A_c$ contains both $c$ and an element of $T_c$, so $M_0, M_1, M_+$ partition $C$ and $\sum_{q \in S \cap A_c} \frac{1}{q} \le \frac{1}{c}$ holds for each $c$. Every $c \in M_0$ satisfies $1/c \ge 1/B$, and every $q \in S_{>B}$ satisfies $1/q < 1/B$. Thus
$$1 < \sum_{q \in S} \frac{1}{q} \le \Sigma - \sum_{c \in M_1} \operatorname{cap}(c) - \frac{|M_0|}{B} + \frac{|S_{>B}|}{B},$$
with strict inequality on the last term whenever $S_{>B} \ne \emptyset$. In case (2), $S_{>B} \ne \emptyset$ follows from $\Sigma \le 1$, yielding $|S_{>B}| > |M_0| + B(1 - \Sigma)$, so $|S_{>B}| \ge |M_0| + t$. Since $|S_{\le B}| \ge |N \cup C| - |M_0|$, we get $|S| \ge |N \cup C| + t$. Moreover, for each $c \in M_1$, $\prod_{q \in S \cap T_c} q \ge 2c + 1 > c$, and $\prod_{q \in S_{>B}} q > B^{|M_0| + t} \ge (\prod_{c \in M_0} c) B^t$, yielding the product bound. In case (3), if $S_{>B} = \emptyset$ and $S \ne N \cup C$, then some $c \in M_0 \cup M_1$ reduces the sum by at least $\min(1/B, \operatorname{cap}(c)) > \Sigma - 1$, contradicting $\sum 1/q > 1$. Otherwise $|S_{>B}| > |M_0| - B(\Sigma - 1) > |M_0| - 1$, hence $|S_{>B}| \ge |M_0|$, giving $|S| \ge |N \cup C|$ and $\prod_{q \in S} q > \prod_{p \in N \cup C} p$ whenever $S \ne N \cup C$. $\square$

### Theorem 1 (Exact Extremal Normal-Set Theorem & Exhaustion of BMS 2013)
Partition $2^{\mathbb{P}_{\mathrm{odd}}}$ into the **7 mutually exclusive, exhaustive leaves** by membership in $\{3, 5, 7, 23, 83\}$:
1. Leaf 1: $N=\{3\}, F=\emptyset$;
2. Leaf 2: $N=\{5, 7, 23, 83\}, F=\{3\}$;
3. Leaf 3: $N=\{5, 7, 23\}, F=\{3, 83\}$;
4. Leaf 4: $N=\{5, 7\}, F=\{3, 23\}$;
5. Leaf 5: $N=\{7\}, F=\{3, 5\}$;
6. Leaf 6: $N=\{5\}, F=\{3, 7\}$;
7. Leaf 7: $N=\emptyset, F=\{3, 5, 7\}$.

Applying max-capacity ascending Star-Pack at $B = 321{,}053$ (and at $B_{\mathrm{out}} = 352{,}756$ on the 6 non-Leaf-2 leaves, plus Leaf 3 at $352{,}757$) certifies with zero floating-point arithmetic:
1. For every finite normal set $S$ of odd primes with $\sum_{p \in S} \frac{1}{p} > 1$:
   - $|S| \ge 8{,}135$ (not uniquely attained: $L' = (L \setminus \{321{,}053\}) \cup \{321{,}073\}$ is normal with $|L'| = 8{,}135$ and $\sum_{p \in L'} 1/p > 1$);
   - $\max(S) \ge 321{,}053$, with equality iff $S = L$;
   - $\prod_{p \in S} p \ge P(L)$ ($40{,}733$ decimal digits), with equality iff $S = L$.
2. **Exhaustion of Borwein--Maitland--Skerritt (2013):** Because Lemma 1 never assumes normality on $S \cap [B, \infty)$ (and $1/q \le 1/B$ still gives $|S| > |L| - B(\Sigma - 1) > 8{,}134$), every relaxed completion $T_{27,692}(N)$ in BMS (2013) satisfies $j_{27,692}(N) \ge 8{,}135$, hence **$j_d = 8{,}135$ for all $d \ge 27{,}692$**. This settles the extremal lower-bound consequence of Borwein et al. (1996) Open Problem #5 without settling intermediate relaxed depths $d \in [312, 27691]$.
3. **Strict separation outside Leaf 2:** Every normal set $S$ with $\sum_{p \in S} 1/p > 1$ outside Leaf 2 satisfies $|S| \ge 8{,}846$, $\prod_{p \in S} p \ge 10^{44{,}627}$ ($\ge 44{,}628$ digits), and $\max(S) \ge 352{,}757$, where $352{,}757$ is the **exact attained minimum** outside Leaf 2, uniquely achieved at Leaf 3's greedy normal set $L^{(3)}$ ($|L^{(3)}| = 8{,}880$, 100% normal).
4. **Normality of Leaf 2 extension:** Max-capacity ascending Star-Pack on Leaf 2 has zero non-normal centers through $B_{\mathrm{out}} = 352{,}756$ ($|L_{338032}| = 8{,}512$, $|L_{352756}| = 8{,}855$).

---

## 3. Elementary Mod-8 / Mod-16 Congruences & Purely Elementary $a \ge 2$ Splitting

### Theorem 2 (Mod-16 and Mod-8 Congruences for Odd Weak Giuga Numbers)
Let $n = \prod_{p \in S} p$ be an odd squarefree integer with $p \mid (n/p - 1)$ for all $p \in S$, so $\sum_{p \in S} 1/p - 1/n = a \in \mathbb{Z}_{\ge 1}$. Let $c_k = \#\{p \in S : p \equiv k \pmod 8\}$ ($k \in \{1, 3, 5, 7\}$) and $r = c_3 + c_7 = \#\{p \in S : p \equiv 3 \pmod 4\}$. Then:
1. **Quadratic Reciprocity Signature:** $r \equiv 0 \text{ or } 1 \pmod 4$.
2. **Mod-16 Congruence:**
   $$m - a - 1 \equiv \begin{cases} 2r + 8c_3 \pmod{16} & \text{if } r \equiv 0 \pmod 4,\\ 2(r - 1) + 8c_5 \pmod{16} & \text{if } r \equiv 1 \pmod 4. \end{cases}$$
3. **Mod-8 Corollary (cf. Mavrotheris, Aug 2026):** $m - a \equiv 1 \pmod 8$. In particular, for $a = 1$, $m \equiv 2 \pmod 8$, which immediately lifts $|S| \ge 8{,}135$ to **$\omega(n) \ge 8{,}138$**.

*Proof.* (1) Taking Legendre symbols of $n/p \equiv 1 \pmod p$ and multiplying over all $p \in S$ yields $1 = \prod_{\{p,q\}} \left(\frac{p}{q}\right)\left(\frac{q}{p}\right) = (-1)^{\binom{r}{2}}$, so $r \equiv 0, 1 \pmod 4$. (2) In $(\mathbb{Z}/16\mathbb{Z})^\times$, $(p + 8)(p^{-1} + 8) \equiv 1 \pmod{16}$ for every odd $p$, so shifting any factor $p \mapsto p + 8$ shifts both $\sum p^{-1}$ and $n^{-1}$ by $+8 \pmod{16}$; thus $\sum p^{-1} - n^{-1} \pmod{16}$ depends only on $(c_1, c_3, c_5, c_7)$. Evaluating on representatives $\{1, 3, 5, 7\}$ using $11 \equiv 7 \cdot 13$, $7^2 \equiv 1$, and $13^k = (1 - 4)^k \equiv 1 - 4k \pmod{16}$ gives $n^{-1} \equiv 7^r(1 - 4(c_3 + c_5)) \pmod{16}$ and $\sum p^{-1} \equiv m + 10c_3 + 12c_5 + 6c_7 \pmod{16}$. Subtracting in the two cases $r \equiv 0, 1 \pmod 4$ yields the exact mod-16 formula, which reduces modulo $8$ to $m - a \equiv 1 \pmod 8$. $\square$

### Theorem 3 (Purely Elementary $a \ge 2$ Splitting Bound)
If $n$ is a composite Agoh--Giuga counterexample with $a \ge 2$, then:
$$\omega(n) \ge 329{,}188, \qquad P(n) \ge 1{,}284{,}211, \qquad n > 10^{1{,}808{,}610} \text{ ($\ge 1{,}808{,}611$ decimal digits).}$$

*Proof.* Order $S = \{p_1 < \dots < p_m\}$ and let $k$ be the least index with $\sum_{i=1}^k 1/p_i > 1$. By Theorem 1, $k \ge 8{,}135$, $p_k \ge 321{,}053$, and $\prod_{i=1}^k p_i \ge P(L) > 10^{40{,}732}$. By minimality of $k$, $\sum_{i=1}^k 1/p_i \le 1 + 1/p_k$, so the tail $S_2 = \{p_{k+1}, \dots, p_m\}$ satisfies $1 - 1/p_k < \sum_{p \in S_2} 1/p < |S_2|/p_k$, forcing $|S_2| \ge p_k \ge 321{,}053$. Hence $\omega(n) = k + |S_2| \ge 8{,}135 + 321{,}053 = 329{,}188$. Every prime $> 3$ is coprime to $6$, and since $321{,}053 \equiv 5 \pmod 6$, the $321{,}053$-rd integer $> 321{,}053$ coprime to $6$ is $321{,}053 + 6 \cdot 160{,}526 + 2 = 1{,}284{,}211$ (which is prime), so $P(n) \ge 1{,}284{,}211$. Finally, $n > P(L) \cdot 321{,}053^{321{,}053} = P(L) \cdot (321{,}053^{10{,}000})^{32} \cdot 321{,}053^{1{,}053} > 10^{40{,}732 + 32 \cdot 55{,}065 + 5{,}798} = 10^{1{,}808{,}610}$. $\square$

---

## 4. Breaking Past the Normal-Set Ceiling via Forced-Prime CRT & 2D Lattice Refutations

### Lemma 2 (Forced-Prime CRT & 2D Lattice Box Refutation)
Let $L_{\mathrm{base}} \subset \mathbb{P}_{\mathrm{odd}}$ be a finite normal set with product $P_{\mathrm{base}} = \prod_{p \in L_{\mathrm{base}}} p$. For any $a = 1$ counterexample $n = \prod_{p \in S} p$, write $Y = \prod_{p \in L_{\mathrm{base}} \setminus S} p$ and $X = \prod_{q \in S \setminus L_{\mathrm{base}}} q$, so $\gcd(X, Y) = 1$ and $Y n = P_{\mathrm{base}} X$. For any *forced* subset $F \subseteq S \cap L_{\mathrm{base}}$, normality of $L_{\mathrm{base}}$ guarantees that $\{p : p \in F\}$ and $\lambda(F) := \operatorname{lcm}_{p \in F}(p - 1)$ are pairwise coprime and $\gcd(P_{\mathrm{base}}, \lambda(F)) = 1$. The Giuga and Carmichael conditions at $p \in F$ combine by CRT into a unique congruence
$$X \equiv C_F Y \pmod{M_F}, \qquad M_F := \left(\prod_{p \in F} p\right) \lambda(F).$$
Suppose $(u, v) \in \mathbb{Z}^2 \setminus \{(0,0)\}$ satisfies $u \equiv C_F v \pmod{M_F}$. Then for any box $[1, R] \times [1, U]$:
- If $uv < 0$ and $|v| R + |u| U < M_F$, then no $(X, Y) \in [1, R] \times [1, U]$ satisfies $X \equiv C_F Y \pmod{M_F}$.
- If $uv > 0$, $|v| R < M_F$, $|u| U < M_F$, and $\max(|u|/g - R,\, |v|/g - U) > 0$ where $g = \gcd(|u|, |v|)$, then no coprime $(X, Y) \in [1, R] \times [1, U]$ satisfies $X \equiv C_F Y \pmod{M_F}$.

*Proof.* Since $u \equiv C_F v \pmod{M_F}$ and $X \equiv C_F Y \pmod{M_F}$, we have $vX - uY \equiv 0 \pmod{M_F}$. If $uv < 0$, then $0 < |v|X + |u|Y \le |v|R + |u|U < M_F$, impossible. If $uv > 0$, then $-M_F < -|u|U < vX - uY < |v|R < M_F$, forcing $vX = uY$; since $\gcd(X, Y) = 1$, this forces $(X, Y) = (|u|/g, |v|/g)$, which lies outside $[1, R] \times [1, U]$. $\square$

### Theorem 4 (Tier 2 Unconditional Bounds & Conditional Dichotomies)
Every composite counterexample $n$ to the Agoh--Giuga conjecture satisfies:
$$\omega(n) \ge 8{,}138, \qquad P(n) \ge 326{,}057, \qquad n \ge 10^{40{,}921} \text{ ($\ge 40{,}922$ decimal digits).}$$
Moreover, for the smallest admissible prime-factor counts ($a = 1$, $m = 8{,}135 + \Delta m \equiv 2 \pmod 8$):
- If $\omega(n) = 8{,}138$ ($\Delta m = 3$), then $n \ge 10^{51{,}797}$ ($\ge 51{,}798$ digits) and $P(n) > 10^{3{,}685}$.
- If $\omega(n) = 8{,}146$ ($\Delta m = 11$), then $n \ge 10^{41{,}894}$ ($\ge 41{,}895$ digits) and $P(n) > 10^{103}$.
- If $\omega(n) = 8{,}154$ ($\Delta m = 19$), then $n \ge 10^{41{,}127}$ ($\ge 41{,}128$ digits).

*Proof Outline (fully certified by `verify_agoh_giuga_certificate.py`):*
1. **Largest prime $P(n) \ge 326{,}057$:** By Theorems 1 and 3, any counterexample with $P(n) \le P_0 := 326{,}056$ must have $a = 1$ and lie in Leaf 2. On $L_{\mathrm{base}} = L_{326056}$ ($|L_0| = 8{,}254$, 100% normal), $S_{>P_0} = \emptyset$, so every omitted star $A_c$ pays exact reciprocal cost $\ge \operatorname{cap}_{P_0}(c)$ out of $\operatorname{gap}_0 = \sum_{p \in L_0} 1/p - 1$. Scaling by $D = 10^{12}$ (ceiling for $\operatorname{gap}_0$, floor for costs), a 2D integer knapsack `dp2[ds][k]` followed by a suffix-minimum over $k$ produces sound exact integer upper bounds $U(k)$ for every $k = |S \setminus L_0|$ (covering all partial leaf choices $W_c \subseteq T_c$). A 153-branch linear forcing cascade ($|F_0| = 104$ to $|F_{\mathrm{final}}| = 256$, skipping $p = 233$) coupled with $k$-bucketing refutes all $155$ `(U, R)` boxes via Lemma 2.
2. **Digits $\ge 40{,}922$:** By Theorems 1 and 3, any counterexample with $< 40{,}922$ digits must have $a = 1$ and lie in Leaf 2, so $\Delta m = m - 8{,}135 \in \{3, 11, 19, 27, 35\} \cup \{43, 51, \dots\}$.
   - For $\Delta m \in \{3, 11\}$: Star-Pack forcing + exact $S_4 = 10^{18}$ upper tail sums $T_F$ bound $d_{\max} \in \{161, 291\}$; a single `(U, R)` witness certifies digits ($\ge 51{,}798$ and $\ge 41{,}895$), and per-rank upper bounds $q_{(j)} < \frac{jB}{j - \Delta m - B \operatorname{gap}_L}$ ($j \ge \Delta m + 1$) certify $P(n) > 10^{3{,}685}$ and $P(n) > 10^{103}$.
   - For $\Delta m = 19$: 4 contiguous $m_0$-intervals covering $[0, 377]$ certify $\ge 41{,}128$ digits (4 `(U, R)` pairs).
   - For $\Delta m = 27$: 8 contiguous $m_0$-intervals covering $[0, 448]$ under $Q_{\lceil} = \lceil(10^{40{,}921} - 1)/P(L)\rceil$, each closed by a linear forcing cascade (683 `(U, R)` pairs total), certify $\ge 40{,}922$ digits.
   - For $\Delta m = 35$ and $\Delta m \ge 43$: Exact zero-float Lagrangian multipliers $A_{35} = 6{,}900$ (checked on all $1{,}171$ non-$F_{35}$ stars) and $A_{\mathrm{glob}} = 15{,}050 < B$ (checked on all $1{,}455$ stars) verify $\log_B(n / P(L)) > \Delta m - A(\operatorname{gap}_L + \Delta m/B)$, and exact integer power checks $P_{\mathrm{top}}^{1000} B^{a_{1000}} \ge 10^{1000(D - 1 - 40729)}$ certify $\ge 40{,}922$ digits ($\Delta m = 35$) and $\ge 40{,}959$ digits ($\Delta m \ge 43$). $\square$

---

## 5. Sharp $r = 2$ Giant-Prime Structural Barrier

### Theorem 5 ($r = 2$ Giant-Prime Barrier)
Suppose $n = M_0 P_1 P_2$ is an $a = 1$ Agoh--Giuga counterexample with $M_0 = \prod_{p \in S_0} p$ and two remaining primes $P_1 < P_2$. Set $N_0 := M_0\bigl(1 - \sum_{p \in S_0} 1/p\bigr) \in \mathbb{Z}$. Then:
1. $N_0 \ge 3$ is odd;
2. Setting $t_0(N_0) := \frac{1 + \sqrt{1 + 4N_0}}{2N_0}$, we have the unconditional strict upper bound
   $$P_1 P_2 < t_0(N_0)^3 M_0^2 + t_0(N_0)^2 M_0.$$
   For all $M_0 \ge 10^5$ (in particular for all counterexamples), $P_1 P_2 < 0.4523 M_0^2$.

*Proof.* From $1/P_1 + 1/P_2 - 1/(M_0 P_1 P_2) = N_0/M_0$, multiplying by $M_0 P_1 P_2$ gives $M_0(P_1 + P_2) - 1 = N_0 P_1 P_2$. Since $M_0, P_1, P_2$ are odd, $N_0$ is positive and odd; also $N_0 P_1 P_2 = M_0(P_1 + P_2) - 1 > M_0 P_2$ forces $d_1 := N_0 P_1 - M_0 > 0$, and similarly $d_2 := N_0 P_2 - M_0 > d_1 > 0$, with $d_1 d_2 = M_0^2 - N_0$. Moreover, $M_0 P_1 - 1 = d_1 P_2 \equiv d_1 \pmod{P_2 - 1}$, so the Carmichael condition $(P_2 - 1) \mid (M_0 P_1 - 1)$ forces $(P_2 - 1) \mid d_1$, hence $d_1 \ge P_2 - 1$. If $N_0 = 1$, then $d_1 < d_2 = P_2 - M_0 < P_2 - 1$, contradiction; hence $N_0 \ge 3$.

Rewriting $N_0(d_1 + 1) \ge N_0 P_2 = M_0 + (M_0^2 - N_0)/d_1$ gives $f(d_1) := N_0 d_1^2 - (M_0 - N_0) d_1 - (M_0^2 - N_0) \ge 0$, so $d_1 \ge x_+$ (the unique positive root of $f$). Since $N_0 \ge 3$ and $M_0 > N_0$, $f(\sqrt{M_0^2 - N_0}) > 0$ so $x_+ < \sqrt{M_0^2 - N_0}$. Because $P_1 P_2 = \bigl(2M_0^2 - N_0 + M_0(d_1 + (M_0^2 - N_0)/d_1)\bigr)/N_0^2$ decreases on $(0, \sqrt{M_0^2 - N_0}]$, we obtain
$$P_1 P_2 \le \frac{(M_0 + x_+)(M_0 + (M_0^2 - N_0)/x_+)}{N_0^2} = \frac{(M_0 + x_+)(x_+ + 1)}{N_0}.$$
Evaluating $f(t_0 M_0) = N_0(t_0 M_0 + 1) > 0$ (where $N_0 t_0^2 = t_0 + 1$) shows $x_+ < t_0 M_0$, so
$$P_1 P_2 < \frac{(1 + t_0) M_0 (t_0 M_0 + 1)}{N_0} = t_0^3 M_0^2 + t_0^2 M_0.$$
For $N_0 \ge 3$, $t_0 \le \frac{1 + \sqrt{13}}{6}$, and exact integer verification confirms $t_0(3)^3 + 10^{-5} < 0.4523$. $\square$

*Barrier implication:* Even if all $8{,}135$ primes of $L$ were forced, $M_L = P(L)\lambda(L)$ has $54{,}909$ decimal digits, whereas $M_0^2 \approx P(L)^2 \approx 10^{81{,}464}$. Thus the CRT + 2D lattice inequality $P_1 P_2 < M_L$ leaves the massive window $3 \le N_0 \lesssim 10^{17{,}704}$ consistent with $M_L < P_1 P_2 < t_0(N_0)^3 M_0^2 + t_0(N_0)^2 M_0$. Ruling out giant-prime completions therefore requires genuinely new global arithmetic structure beyond local CRT moduli.
