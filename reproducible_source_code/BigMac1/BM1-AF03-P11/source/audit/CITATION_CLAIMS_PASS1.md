# Citation audit Pass 1: frozen claim extraction

Document: `paper/main.tex`

Mode: search verification for external claims; exact local-certificate
verification for claims that are new results of this project.

No verification is recorded in this file.  The following list is frozen for
Pass 2.

| ID | Claim | Type | Location |
|---|---|---|---|
| CC01 | Zhang conjectured `|M_{2n}|=(n+1)|M_{2n-1}|`. | Attribution | Abstract; Introduction, Eq. (1) |
| CC02 | Zhang reported computational verification for `n<=6`. | Attribution + statistic | Abstract; Introduction |
| CC03 | The length-13 and length-14 skeleton spaces have exactly 1,235,520 and 2,162,160 elements. | Statistic | Abstract; Section 4; Table 1 |
| CC04 | The certified counts are `|M_13|=47,265,120` and `|M_14|=378,120,960`. | Statistic + existence | Abstract; Theorem 1.1; Table 1 |
| CC05 | Deleting the last entry and standardizing is eight-to-one from `M_14` to `M_13`. | Existence + comparative ratio | Abstract; Introduction; Proposition 5.1 |
| CC06 | Berlow introduced generalized maps `s_T` and proved the periodic points of `s_{123,132}` are exactly the half-decreasing permutations. | Attribution | Introduction; Definitions |
| CC07 | Zhang proved `ord_{s_{123,132}}(S_N)=2 floor((N-1)/2)` and defined the minimally-sorted sets used here. | Attribution | Introduction; Definitions |
| CC08 | The present result is the first parameter relation beyond the source paper's reported range `n<=6`. | Ranking + temporal-context inference | Introduction |
| CC09 | The large-label factorization identity `kappa_m o s = F_m o kappa_m` holds. | Existence (new lemma) | Lemma 3.1 |
| CC10 | Every qualifying skeleton has `(N-m)!` labelled lifts, so `|M_N|=|Q_N|(N-m)!`. | Statistic + existence (new corollary) | Corollary 3.2 |
| CC11 | The exact enumeration independently reproduces every relation for `n<=6`. | Existence | Section 4; Table 1 |
| CC12 | Two discovery enumerators with distinct generation/evaluation routes agree for every length 1 through 14. | Statistic + existence | Section 4 |
| CC13 | The no-import verifier regenerates all skeletons, rejects malformed inputs, and checks `Q_14={wL:w in Q_13}`. | Existence | Section 4; Eq. (2) |
| CC14 | No Lean, Coq, Isabelle, or other proof assistant was used. | Existence/negative process fact | Limitations and reproducibility |
