# Claim ledger

Frozen claim list: 2026-08-29 09:55 CST (before the decisive exact
factorization was computed).  “Not found” below is limited to the databases
and queries recorded in `search_log.md`.

| ID | Claim | Status | Source | Location | Confidence | Consequence |
|---|---|---|---|---|---|---|
| C01 | Rivin's paper is arXiv:2508.14901, authored by Igor Rivin, with only v1 submitted 2025-07-31 in the arXiv history. | exact metadata, verified | [arXiv record](https://arxiv.org/abs/2508.14901) | abstract page, submission history | high | Fixes the version under audit. |
| C02 | Over \(\mathbb F_2\), the paper reports 5,304 nonexpressible matrices among 20,160 invertible binary \(4\times4\) matrices. | author theorem; count not independently reproduced here | Rivin, arXiv:2508.14901v1 | Theorem 4, PDF p. 3 | high as attribution; unverified as computation | Background only; not used in the rational certificate. |
| C03 | The displayed matrix is exactly the paper's “simplest counterexample” over \(\mathbb F_2\). | exact transcription, verified | Rivin, arXiv:2508.14901v1 | Example 5, PDF p. 3 | high | Confirms that the audited matrix was not mistranscribed. |
| C04 | The paper states that all 5,304 examples remain counterexamples over \(\mathbb Z\). | author theorem; proof text has an unresolved coverage concern | Rivin, arXiv:2508.14901v1 | Theorem 6, PDF p. 3 | medium | Must not be strengthened to \(\mathbb Q\) or \(\mathbb R\). Not used here. |
| C05 | For \(\mathbb R\), the paper offers numerical optimization evidence, not an analytic infeasibility proof, and lists analytic proof as open. | exact, verified | Rivin, arXiv:2508.14901v1 | §4.3 and Open Problem 7.1(4), pp. 3, 7 | high | Makes an exact rational factorization materially relevant. |
| C06 | No later arXiv version, indexed citing paper, correction, or independent published resolution was found in the recorded searches as of 2026-08-29. | database-limited negative result | arXiv, Semantic Scholar, OpenAlex, Crossref, web queries | `search_log.md` | medium | Supports only a qualified novelty statement, never proof of novelty. |
| C07 | The displayed matrix is expressible over \(\mathbb Q\) as a Hadamard product of two rank-two matrices. | exact new result, independently certified | local serialized certificates and two standard-library verifiers | `certificates/`, `verifier/`, `proof/exact_disproof.md` | very high | Disproves \((C_M)\) over \(\mathbb Q\), hence over \(\mathbb R\). |
| C08 | The present certificate does not decide whether every invertible real \(4\times4\) matrix is rank-(2,2) Hadamard expressible. | exact logical limitation | formal statement and proof | `problem/formal_statement.md` | certain | Prevents overclaiming the universal problem. |
