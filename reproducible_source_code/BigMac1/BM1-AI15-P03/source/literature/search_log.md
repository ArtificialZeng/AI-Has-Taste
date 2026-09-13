# Search log — NOVELTY_LOCK 2026-08-29

检索日期均为 **2026-08-29（Asia/Shanghai）**。只记录会影响 C01–C13 的查询。结论中的 “not found” 仅指下列数据库、URL 与查询；发布前必须重复检索。

## S00 — workflow and frozen questions

- 完整读取 `/Users/mac/.codex/skills/prove-or-disprove-math/references/research-workflow.md`，依其两遍法先冻结 C01–C13，再搜证据。
- 冻结问题：精确定义/端点；OEIS 数据；奇数闭式与全奇数零点；偶数 transfer/递推；已知有限范围；全称命题是否已经解决；来源中的冲突或更正。

## S01 — OEIS primary sequence record

- URLs:
  - <https://oeis.org/A383733>
  - <https://oeis.org/search?fmt=text&q=id:A383733>
  - <https://oeis.org/A383733/list>
  - <https://oeis.org/history?seq=A383733>
  - <https://oeis.org/A383733/b383733.txt>
- Located: offset 6；15 项 (n=6\ldots20)；literal edge construction；(a(20)=120)；entry comment nevertheless asserts recurring zeros at multiples of four；references to arXiv and DOI paper；entry revision #24 dated 2025-11-13.
- Integrity: fetched b-file SHA-256 = `f88fe3991ada3aa6e5df90be8c10822b6b2f4460d5a55d3dd344855a4e66ed3d`，与 SciNet artifact 报告一致。
- Conclusion: supports C01, C02, C11, C13；OEIS is a database record, not a proof of terms beyond its b-file.

## S02 — original arXiv paper

- URLs:
  - <https://arxiv.org/abs/2509.05845>
  - <https://arxiv.org/html/2509.05845v1>
- Metadata: Rogelio N. Lopez-Bonilla, Julian Allagan, Shawn M. Langley, Angel J. Clinton, “Golden Ratio Growth and Phase Transitions in Chromatic Counts of Circular Chord Graphs,” arXiv:2509.05845v1 [math.CO], submitted 2025-09-06, 13 pp.
- Located: Definition 1.1；odd closed form and spectral factorization (Theorem 3.4)；counts through 35；claim of a paired-window trace for even (n) (Theorem 3.5)；SML discussion.
- Version warning: this v1 claims the naive even trace is exact, while the later DOI paper explicitly proves that construction fails. For the even branch, v1 is superseded and must not be relied on.
- Conclusion: supports historical provenance of C03, but C05 requires the corrected journal version/artifact.

## S03 — DOI and final journal version

- DOI: <https://doi.org/10.9734/jamcs/2025/v40i102060>.
- Crossref singleton query: <https://api.crossref.org/works/10.9734%2Fjamcs%2F2025%2Fv40i102060>.
- Crossref metadata returned: “Chromatic Polynomials of \(C^{(3)}_n\) Graphs: Lucas Sequences, ϕ\(^n\) Asymptotics and Linear Recurrence Existence,” *Journal of Advances in Mathematics and Computer Science* 40(10), 79–98, published 2025-11-01, DOI as above.
- Publisher landing/PDF was Cloudflare-blocked (HTTP 403 in direct `curl`); final DOI-stamped author-uploaded text was inspected at <https://www.researchgate.net/publication/397141446_Chromatic_Polynomials_of_C3_n_Graphs_Lucas_Sequences_phn_Asymptotics_and_Linear_Recurrence_Existence>. The publisher’s under-review file at <https://files.sdiarticle5.com/wp-content/uploads/2025/10/Ms_JAMCS_146917.pdf> was used only as a cross-check, not for publication metadata.
- Relevant locations in final version:
  - Definition 1.1, pp. 80–81: graph definition and restrictive (1<k<n/2).
  - Theorem 3.4 / Corollary 3.1, pp. 83–85: 12-state odd matrix, characteristic polynomial, exact closed form.
  - Definition 3.1 / Theorem 3.6 / Remark 3.2, pp. 86–88: 54 compatible pairs, naive paired trace failure, global closure mismatch.
  - Theorem 3.7 / Remark 3.3, pp. 88–89: asserted recurrence existence/order (\le54), explicit recurrence still open.
  - Table 2 and Conjectures 6.1–6.3, pp. 91–93: computations through 57 and even-case conjectures.
- Internal audit findings:
  - Table 2 has (a(11)=66), but Conjecture 6.3 lists 11 as a zero and also includes domain-external 4,5.
  - It correctly says the naive 54-state trace fails, then asserts a corrected representation has no more than 54 states even if extra phase information is needed; no explicit corrected automaton is supplied. The fixed-offset lemma does not directly cover the length-dependent diameter offset.
  - The printed Newton-sum paragraph contains a coefficient inconsistency, although the stated (s_{n+3}=-s_{n+2}-s_n) follows directly by summing the root equation and is consistent with the table.
- Conclusion: strongest formal source for C03, C05–C07, C13; its even recurrence proof and zero-set conjecture require independent reconstruction.

## S04 — SciNet problem and finite finding

- Problem: <https://api.scinet.pub/p/69d6d14f-32c0-4de4-933e-9d4b4ab99e2a>.
- Finding: <https://api.scinet.pub/f/a760d2f8-717e-4d44-b3b9-86f30957a285>.
- Problem state seen: `ACTIVE`; posed 2026-07-28; one investigation; “Verification pending”; no completed all-(n) proof listed.
- Finding reports:
  - definition-level check of the 15 OEIS terms;
  - exact counts to 400 and nonzero mod each of 1048573, 1047551 through 3000;
  - odd formula checked to 201;
  - branch BM orders 8/34/35;
  - exact-zero-set all (n) explicitly left as companion problem.
- Provenance label: the site labels the (n\le3000) item as data/code, but also says “awaiting independent review”; the all-odd zero statement is explicitly an `inference` and “not formalized here.”
- Conclusion: supports C04, C08–C10, C12 as an author/computational report, not a substitute for Gate 4/5 verification.

## S05 — public computational artifact

- Repository directory: <https://github.com/scinet-ai/math-combinatorics/tree/main/a383733>.
- Pinned commit: <https://github.com/scinet-ai/math-combinatorics/commit/b873c297e21bcd6ac973f1190a82a857010f8556>.
- GitHub API confirmed commit SHA `b873c297e21bcd6ac973f1190a82a857010f8556`, author timestamp 2026-07-28T04:12:09Z, message reporting the (n=3000) result and orders 8/34/35.
- README states: 18-state odd transfer；54-state pair transfer with track-swap seam for even (n)；two-prime sweeps；exact BM；reproduction commands. Files named `a383733.py`, `deep_analysis.py`, `data/`, `results/` are public.
- This Gate inspected provenance and claims only; it did **not** count artifact execution as independent mathematical verification.
- Conclusion: source for C05, C08, C09; exactification/audit must pin serialized inputs and replay separately.

## S06 — broad exact-phrase web queries

Queries (general web index):

1. `"A383733" zero set proof`
2. `"A383733" "7, 8, 12, 16"`
3. `"C_n^{(3)}" 3-colorings zero set`
4. `"Chromatic Polynomials of C_n^(3) Graphs"`
5. `site:github.com A383733`
6. `site:arxiv.org A383733`
7. `site:doi.org A383733`
8. `"zero set" "circular chord" graph coloring`

Results relevant to the frozen claims: OEIS A383733; the arXiv/DOI papers; SciNet problem/finding; the SciNet GitHub artifact; a 2026 preprint “Quartic Equimodular Curves and Spectral Reductions in Prism-Derived Chromatic Polynomials” that only cites the 2025 DOI paper and does not treat this zero set. No independent all-(n) proof or counterexample appeared.

## S07 — formal metadata/database sweep

- Crossref exact DOI singleton: see S03.
- Crossref title query `query.title=Chromatic Polynomials of C_n^(3) Graphs`, 10 results: the fuzzy ranking did not surface the paper, so the direct DOI lookup is the authoritative metadata check.
- OpenAlex query `search=A383733`, `per-page=20`: count 1, only <https://openalex.org/W4414755767> = arXiv:2509.05845, cited-by count 0 at access.
- OpenAlex title/concept query `search=Chromatic Polynomials of C n 3 Graphs Lucas Sequences Asymptotics Linear Recurrence Existence`, `per-page=20`: located <https://openalex.org/W4415759050>, DOI 10.9734/jamcs/2025/v40i102060, cited-by count 0 at access; no resolving paper among returned records.
- OEIS history showed no post-2025 mathematical update to the sequence content; the visible entry remains revision #24 (2025-11-13).
- Conclusion: within these formal records, the DOI paper remains the publication frontier and has no indexed citing resolution.

## Locked novelty conclusion

`NOVELTY_LOCK = OPEN_PROBLEM_NOT_PREVIOUSLY_RESOLVED_IN_RECORDED_SEARCH_SCOPE`.

The lock does **not** certify global novelty. Before any “new/publishable” claim, repeat S01, S04, S06, S07 with the final theorem wording and search for later versions, corrections, citations, and independent repositories.

## S08 — post-result novelty recheck

- Recheck date: **2026-08-29 (Asia/Shanghai)**, after the elementary block
  construction and exact obstruction proof had been fixed.
- Exact web queries:
  1. `"A383733" "zero set" proof`
  2. `"A383733" "7, 8, 12, 16"`
  3. `"21202" "chorded cycle" coloring`
  4. `"C_n^(3)" 3-colorable 16 20`
- Direct records revisited:
  [OEIS A383733](https://oeis.org/A383733),
  [SciNet active problem](https://api.scinet.pub/p/69d6d14f-32c0-4de4-933e-9d4b4ab99e2a),
  [SciNet finite finding](https://api.scinet.pub/f/a760d2f8-717e-4d44-b3b9-86f30957a285),
  [journal DOI record](https://doi.org/10.9734/jamcs/2025/v40i102060), and
  [arXiv:2509.05845](https://arxiv.org/abs/2509.05845).
- Results: the searches returned the same OEIS entry, DOI/arXiv paper, SciNet
  finite computation, and unrelated uses of similar notation.  No occurrence
  of the final blocks `A=01`, `B=21202`, no proof of the exact all-order zero
  set, and no counterexample was found.  The SciNet problem remained `ACTIVE`
  and explicitly described the all-order classification as the requested
  endpoint; its linked finding still stopped at 3000.
- Bounded conclusion:
  `SECOND_NOVELTY_SEARCH_PASS = NO_PRIOR_ALL_N_PROOF_FOUND_IN_RECORDED_SCOPE`.
  This is a search-scope statement, not a guarantee of global priority.

## S09 — seam-correct automaton, exact recurrence data, and eventual positivity follow-up

- Access date: **2026-08-29 (Asia/Shanghai)**. Narrow queries:
  1. `"A383733" seam transfer matrix`
  2. `"A383733" minimal polynomial recurrence`
  3. `"paired-window" "track-swap" coloring`
  4. `"C_n^(3)" "eventual positivity" coloring`
- Primary/current records revisited:
  [OEIS A383733 text record](https://oeis.org/search?fmt=text&q=id:A383733),
  [arXiv:2509.05845v1](https://arxiv.org/abs/2509.05845),
  [journal DOI 10.9734/jamcs/2025/v40i102060](https://doi.org/10.9734/jamcs/2025/v40i102060),
  [SciNet active problem](https://api.scinet.pub/p/69d6d14f-32c0-4de4-933e-9d4b4ab99e2a),
  [SciNet finite finding](https://api.scinet.pub/f/a760d2f8-717e-4d44-b3b9-86f30957a285), and
  [pinned GitHub artifact](https://github.com/scinet-ai/math-combinatorics/tree/b873c297e21bcd6ac973f1190a82a857010f8556/a383733).
- **Published theorem / record.** The final DOI paper, unlike arXiv v1, proves that the naive 54-state ordinary-trace construction fails (Theorem 3.6) and gives only an existential even-branch recurrence statement (Theorem 3.7); it contains no explicit corrected matrix, recurrence coefficients, characteristic/minimal polynomial, root isolation, or even-branch positivity threshold. OEIS likewise says that an explicit minimal polynomial/recurrence remains open. The arXiv record still has only v1, so its uncorrected even ordinary-trace assertion is not a later solution.
- **Executable author report.** At commit `b873c297e21bcd6ac973f1190a82a857010f8556`, `a383733.py` defines six diameter-compatible color pairs and 54 legal three-pair windows. Its transition matrix $M$ shifts a window and enforces the two trackwise cycle and offset-3 conditions. A separate Boolean seam matrix $S$ swaps both tracks on wrapped start pairs and checks the four wrap constraints. The implemented identity is
  $$a(2m)=\sum_{i,j}(M^{m-3})_{ij}S_{ij}
          =\operatorname{tr}(M^{m-3}S^{\mathsf T}),\qquad m\ge4,$$
  with smaller $m$ handled from the literal graph definition. This is a matrix-power linear functional, not `tr(M^m)`. The repository self-test compares it with definition-level enumeration only for even $8\le n\le28$; the all-$m$ bijection remains to be reconstructed in the independent proof/verifier.
- **What is and is not serialized.** The pinned tree contains only `README.md`, `a383733.py`, `deep_analysis.py`, two input records, and three JSON result files. `results/deep_analysis.json` stores exactly
  $K=54$, $m_{\max}=1500$, primes $1048573,1047551$, BM orders $[34,34]$ and $[35,35]$, and joint modular zero candidates $[8,12,16]$. It does **not** store either modular BM coefficient list, a rational/integer recurrence, $\chi_M$, a minimal polynomial, a nonzero Hankel minor, eigenvalues, isolating intervals, dominant coefficients, or a positivity bound.
- **Minimality distinction.** Agreement of BM orders at two primes is evidence, not a characteristic-zero minimality proof. Once independently reconstructed, a displayed nonzero Hankel minor modulo one prime could certify a lower bound on the rational Hankel rank. To certify exact orders 34/35 one still needs matching exact recurrences (upper bounds) verified for the matrix-power functional, not merely a probabilistic “wrong-order accident” estimate.
- **Eventual positivity distinction.** The DOI/arXiv source gives odd asymptotic positivity but no explicit odd threshold. For the even residue branches it gives conjectures only. The SciNet problem proposes a dominant-root proof as a route; neither its finding nor the pinned code supplies a characteristic polynomial, root separation, coefficient bound, or explicit $N_0$. The focused web queries returned only these known records plus unrelated eventual-positive semigroup literature.
- **Freshness check.** GitHub’s current commit history for path `a383733` has exactly the single 2026-07-28 commit above; current `main` has the same content Git blob IDs as the pinned tree. The SciNet problem remains `ACTIVE`. No later seam-correct publication, exact minimal polynomial, exact recurrence certificate, or eventual-even-positivity proof was found in this recorded follow-up scope.
- Bounded conclusion:
  `S09_RESULT = CORRECT_SEAM_FORMULA_FOUND_ONLY_AS_EXECUTABLE_AUTHOR_REPORT; NO_EXACT_SPECTRAL_OR_EVENTUAL_POSITIVITY_CERTIFICATE_FOUND`.
