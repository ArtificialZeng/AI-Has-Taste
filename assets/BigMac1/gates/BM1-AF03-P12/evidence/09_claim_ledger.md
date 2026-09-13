# Claim ledger

Claim list frozen for Gate 1 on 2026-08-29 (Asia/Shanghai), before accepting
any discovery result.  “Not found” below is database- and query-relative, not
an assertion of nonexistence.

| ID | Claim | Type | Status | Primary source | Location | Confidence | Consequence |
|---|---|---|---|---|---|---:|---|
| L01 | The cited paper is a 2026 Semigroup Forum article by Bruce E. Sagan and Chenchen Zhao, DOI 10.1007/s00233-026-10652-4. | exact metadata | verified | Springer version of record | article header/About this article | 100% | fixes bibliography and publication status |
| L02 | Knuth equivalence satisfies \(v\equiv w\iff P(v)=P(w)\). | exact theorem | verified | Sagan--Zhao, citing Knuth (1970) | p. 243 / online lines 72--75 | 99% | legitimizes the tableau decision procedure |
| L03 | Stable, \(K\)-stable, and strongly stable mean respectively eventual equality, equality from the named bound, and \(K=1\). | exact definition | verified | Sagan--Zhao | p. 243 / online lines 82--85 | 100% | fixes target quantifiers |
| L04 | Words consisting only of 1s and 2s are strongly stable. | paraphrase of theorem | verified | Sagan--Zhao | Theorem 2.13 | 100% | known \(m=2\) baseline |
| L05 | Every permutation in \(\mathfrak S_m\) is \(m\)-stable. | exact theorem | verified | Sagan--Zhao | Theorem 3.7 | 100% | covers length-3 3-packed words |
| L06 | \(m\)-packed means \(\max u=m\) and every integer in \([m]\) occurs in \(u\). | exact definition | verified | Sagan--Zhao | paragraph preceding Conjecture 3.8 | 100% | rules out letters \(>3\) in the target \(u\) |
| L07 | The proposed packed-word assertion is Conjecture **3.8**, not Conjecture 4.6, in the version-of-record PDF.  The Springer HTML currently mislabels it 4.6; PDF Conjecture 4.6 is a different log-concavity conjecture. | exact numbering/web observation | verified/corrected | Sagan--Zhao official PDF and Springer HTML | Conjecture 3.8, journal p. 256; Conjecture 4.6, p. 261 | 100% | corrects source prompt without changing endpoint |
| L08 | The authors tested all \(m=3,4\) packed \(u\) of length at most 8, with \(C'(u^k)=C(u^k)\cap[m]^l\), \(l\le10\), and adjacent equality for \(m\le k\le14\). | author report | verified as reported; the fixed project's \(m=3\) component independently reproduced | Sagan--Zhao; `experiments/breaker/runs/baseline/` | paragraph preceding Conjecture 3.8, p. 255; sealed run | 100% as report and finite reproduction | defines and closes the relevant published computational baseline |
| L09 | Sagan--Wilson conjectured every word is stable. | exact prior claim | verified through original citation and Sagan--Zhao restatement | Sagan--Wilson (2025), Conj. 7.2; Sagan--Zhao intro | cited locations | 98% | places T3 inside the larger conjecture |
| L10 | No later public proof/counterexample of the 3-packed case was located as of 2026-08-29. | bounded negative search | Gate 1, pre-release pass 2, and post-full-DAG pass 3 completed | arXiv/title/phrase/DOI/citation/code searches recorded in search log | search log and independent report | 92% within stated search scope | permits a carefully qualified novelty claim; does not prove global nonexistence |
| L11 | Public code exists for older Sagan--Wilson stability experiments, but the committed notebook does not visibly implement the full 2026 Sagan--Zhao grid. | exact repository fact plus code-audit inference | verified | Sagan--Wilson GitHub, commit `0e35eaa4b715f192e6284777828f6531db5ccc23` | `Stability Conjectures.ipynb` | 95% | 2026 baseline must be independently reimplemented |
| L12 | Defant (2026) proves bounded-row and evacuation conjectures, not packed-word stability. | exact scope claim | verified | arXiv:2605.19979v3 | Section 4, Theorems 4.3 and 4.7 | 98% | does not close T3 |
| L13 | Oberwolfach Report 2/2026 recorded stability as an open problem at the January 2026 workshop. | exact historical report | verified | DOI 10.4171/OWR/2026/2 | report p. 143 | 98% | corroborates the frontier as of January 2026 only |

## Theorem frontier after pass 1

- Proved: alphabet size 1 and 2 (strong stability); permutations
  (\(m\)-stability); the decreasing permutation (strong stability).
- Open in the cited version: general \(m\)-packed words, hence non-permutation
  3-packed words of length at least 4.
- Published finite evidence: the exact truncated regime in L08 only.
- Current project endpoint: the unbounded assertion (T3), including arbitrary
  word length, arbitrary centralizer witness length, and arbitrary positive
  letters in the witness.
