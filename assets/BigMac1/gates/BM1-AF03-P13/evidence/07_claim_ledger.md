# Claim ledger — Gate 1 frozen claim list

Frozen: 2026-08-29 (Asia/Shanghai).  “Not found” below is bounded by the
databases and queries recorded in `search_log.md`; it is not a proof of
nonexistence.

| ID | Claim | Class | Status | Primary source / location | Confidence | Consequence |
|---|---|---|---|---|---:|---|
| C01 | A generalized snake word \(\varepsilon w_1\cdots w_m\) has length \(m\), and \(|P(\mathbf w)|=2m+4\). | exact | verified | arXiv:2411.18695v2, Defs. 2.1–2.2; source `revision2/sections/preliminaries.tex:6–30` | 100% | Fixes all dimension and disk parameters. |
| C02 | For length \(m\), \(\prod_{j=1}^{m+3}(t+j)\mid L\) and \(L(t)=L(-m-4-t)\). | exact | verified | Lee–Vindas-Mel\'endez–Wang, Thm. 2.9; v2 source `preliminaries.tex:300–339` | 100% | Gives center \(-(m+4)/2\) and known roots. |
| C03 | arXiv v1 Conj. 5.1 contains the \(h^*\)-real-rootedness and Ehrhart-root disk claims and reports verification through word length 9. | exact/author report | verified as written | arXiv:2411.18695v1, `sections/h_polynomials.tex:544–554` | 100% for text; no certificate supplied | Establishes the claimed baseline only as an author report until reproduced. |
| C04 | The literal v1 Conj. 5.1 display is internally inconsistent (length \(n+1\), positive disk center, negative stated axis). | exact | verified | same lines 547–552, compared with Def. 2.1 and Thm. 2.9 | 100% | Requires the explicit repaired statement in `problem/formal_statement.md`. |
| C05 | The current arXiv version is v2 dated 2026-02-27; it retains Section 5, Conjecture 5.1, and the sentence reporting verification through length 9. | exact | verified | arXiv version history; v2 TeX source `revision2/sections/h_polynomials.tex` and pp. 28--29 of the v2 PDF | 100% | The conjecture and the author-reported baseline remain in the accepted revision. |
| C06 | The paper has journal DOI 10.1016/j.disc.2026.115072, Discrete Mathematics 349(9), article 115072 (2026). | exact metadata | verified | Crossref DOI record; eScholarship author manuscript | 100% | Use journal metadata and the retained v2 conjecture text. |
| C07 | Braun–Jal prove \(h^*(\mathcal O(P(\mathbf w));z)\) real-rooted for every generalized snake word. | exact | verified | arXiv:2607.00922v1, Thm. 4.1 and abstract | 100% | Conj. 5.1(1) is closed and is outside this project. |
| C08 | At Gate 1, no public proof or counterexample to the corrected Ehrhart disk claim / length-10 endpoint was located. | bounded negative search | not found at Gate 1 | arXiv, Crossref, OpenAlex, Semantic Scholar, Google-style web queries in `search_log.md` | 85% | Permitted new finite research and triggered a result-fingerprint novelty pass. |
| C09 | A public code repository or source-supplied computation certificate for the length-9 claim exists. | unverified | not found | arXiv “Code, Data, Media”, source archives, GitHub/web queries | 85% | We must reproduce the baseline independently. |
| C10 | Complementing every \(L/R\) preserves the Ehrhart polynomial. | exact | verified | Lee–Vindas-Mel\'endez–Wang, Remark 2.8 (v2 source lines 294–296) | 100% | Complement quotient is sound after verifier rechecks it. |
| C11 | Reversal of a generalized snake word preserves the Ehrhart polynomial. | proposed inference | unverified at lock | no statement located in cited source | 40% | Do not quotient reversal until exactly proved/tested. |
| C12 | Length 10 is the first case beyond the authors’ **reported** baseline. | inference about the report | verified relative to C03 | v1/v2 report through length 9 plus Definition 2.1 | 100% | Defines the requested finite endpoint \((F10)\), but does not certify the reported baseline. |

## Post-lock exact-result updates

| ID | Claim | Class | Status | Exact evidence | Confidence | Consequence |
|---|---|---|---|---|---:|---|
| C13 | The length-10 word \(\varepsilon LRLRLRLRLR\) violates the corrected disk \(|t+7|\le6\). | exact new result | independently certified | rational Rouch\'e certificate `experiments/breaker_counterexample_certificate.json`; reconstructing verifier `discovery/breaker_verify_counterexample.py`; separate order-ideal/Routh verifier `audit/independent_routh_verifier.py` | 100% conditional only on ordinary integer arithmetic and Rouch\'e/Routh theorems | Disproves the requested finite universal statement \((F10)\), hence the corrected general conjecture. |
| C14 | The length-9 regular word \(\varepsilon LRLRLRLRL\) already violates \(|t+13/2|\le11/2\). | exact new result / baseline correction | independently certified | rational Rouch\'e certificate `experiments/breaker_length9_counterexample_certificate.json` and no-import reconstructing verifier `discovery/breaker_length9_verify_counterexample.py`; independent order-ideal discovery agrees | 100% conditional only on ordinary integer arithmetic and Rouch\'e's theorem | The authors' unaccompanied “verified through length 9” report is false under the user-adopted natural repair. |
| C15 | The full, unquotiented exact length-10 scan has 1024 records and flags six words in two complement/reversal orbits; a single regular-snake witness suffices for disproof. | exact finite computation | certified as a search record; not needed for the theorem | `experiments/breaker_length10_exact.jsonl` and `experiments/breaker_length10_summary.json`; the witness is separately reconstructed from definitions | 100% for serialized records and witness | Search breadth does not replace the witness proof; it documents how the candidate was found. |
| C16 | Result-specific public searches locate no earlier occurrence of either witness word together with its Ehrhart factor, isolating disk, or distinctive coefficients. | bounded negative novelty search | not found | second-pass queries in `search_log.md` and referee log | 90% | Supports bounded novelty wording only; it is not proof of priority. |

## NOVELTY_LOCK decision

`NOVELTY_LOCK = PASS_WITH_STATEMENT_REPAIR` for the corrected finite endpoint
\((F10)\).  The lock does **not** assert global novelty.  It records that the
only located later mathematical result, Braun--Jal, closes the \(h^*\) half and
does not state an Ehrhart-root disk result.  The accepted v2 manuscript retains
the conjecture and the unsupported computational baseline.  The required
post-result fingerprint search found no earlier matching counterexample; all
novelty language remains explicitly database- and date-bounded.
