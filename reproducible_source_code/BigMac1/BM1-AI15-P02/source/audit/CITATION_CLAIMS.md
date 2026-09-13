# Citation-check Pass 1: frozen claim extraction

Mode: search verification for external claims; exact-artifact verification for
new mathematical claims. Document: `paper/main.tex` as frozen before Pass 2.
No verification was performed while preparing this list.

| ID | Extracted claim | Type | Location |
|---|---|---|---|
| CC01 | “OEIS A321614 counts maximum `2n` nonattacking king placements on a `4 x 2n` board modulo the generic rectangle symmetries.” | Attribution + existence | Abstract; Introduction paragraph 1 |
| CC02 | “Colin Barker contributed the displayed rational generating function and order-ten recurrence as conjectures in 2018.” | Attribution + temporal | Abstract; Introduction paragraph 1 |
| CC03 | “The published OEIS data contain 22 terms and stop at `n=21`.” | Statistic | Introduction paragraph 1 |
| CC04 | “Wilf used forced `2 x 2` cell occupancy for fixed-width maximum king placements and proved a general fixed-height asymptotic theorem.” | Attribution + existence | Introduction paragraph 2 |
| CC05 | “The labeled height-four identity branch is OEIS A061593.” | Attribution + existence | Introduction paragraph 2 |
| CC06 | “A 2026 SciNet computation reproduced the 22 terms, verified the recurrence through `n=5000`, and explicitly did not prove all `n`.” | Attribution + statistic + temporal | Introduction paragraph 3 |
| CC07 | “The maximum number of nonattacking kings on `4 x 2n` is exactly `2n`.” | Statistic + existence | Section 2 |
| CC08 | “Equality in the packing bound yields exactly twelve two-column states and a bijection with paths in the displayed transfer graph.” | Statistic + existence | Section 2 |
| CC09 | “The three geometric operations induce the displayed state involutions and transfer reversal identities.” | Existence | Section 3 |
| CC10 | “The horizontal fixed branch is `H_n=n+1`.” | Statistic | Section 3 |
| CC11 | “The reversal fixed-path formulas, including the counts 3/0 and 7/2 for middle-edge/center vectors, are exact.” | Statistic + existence | Section 3 |
| CC12 | “The displayed integer rows satisfy `Z(y)(I-yT)=D_0(y)1^T` coefficientwise.” | Existence | Section 4, equation (4.1) |
| CC13 | “The identity, horizontal, vertical and half-turn generating functions are the four displayed rational functions.” | Existence | Sections 3–4 |
| CC14 | “Burnside averaging gives Barker's displayed rational generating function.” | Existence | Theorem 5.1 |
| CC15 | “The five displayed remainders are exact and prove `gcd(N,D)=1`.” | Statistic + existence | Proof of Theorem 5.1 |
| CC16 | “The expanded denominator gives the displayed recurrence for every `n>=10`, and degree ten is minimal.” | Existence | Section 5 after Theorem 5.1 |
| CC17 | “At `n=2`, the four-operation fixed counts are `(79,3,3,7)` and give 23 orbits; full `D4` gives extra counts `3,3,7,7` and 14 orbits.” | Statistic | Section 6 |
| CC18 | “Changing only `a(2)` from 23 to 14 makes the recurrence fail at `n=10,11,12`.” | Statistic | Section 6 |
| CC19 | “The compact and 68-dimensional verifiers reconstruct the claimed exact objects; the latter checks 68 observable zeros and a Bezout identity.” | Existence + statistic | Section 7 |
| CC20 | “The decisive computations use exact standard-library arithmetic, no randomness/floating inference/external CAS/proof assistant, and three independent audit roles were used.” | Existence | Section 7 disclosure |

This list is immutable for Pass 2. Any later manuscript change that adds a
covered factual claim invalidates this audit and requires a new extraction.
