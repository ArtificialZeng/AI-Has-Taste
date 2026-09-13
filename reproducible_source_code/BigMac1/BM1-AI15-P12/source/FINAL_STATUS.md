# Final status: `PARTIAL_THEOREM`

Date: 2026-08-29.  `original_prompt_complete = true`.

## Certified theorem

For every real `3 x 3` matrix `T` with `rank(T) <= 2`,

\[
\operatorname{per}\!\begin{pmatrix}T&T\\T&T\end{pmatrix}
\le 20\operatorname{per}(T)^2.
\]

Equality holds if and only if at least one of the following holds:

1. `rank(T) <= 1`;
2. `T` has a zero row or a zero column;
3. `T` has rank two and, after independent row and column permutations,
   contains a `2 x 2` all-zero submatrix.

The proof does not divide by `per(T)` and includes zero-permanent rank-two
equality cases.

## Decisive evidence

The projective normal-form proof gives two explicit integer-coefficient SOS
identities.  `certificates/n3_sos_certificate.json` serializes them.  A pure
standard-library verifier reconstructs both the `3!` and `6!` permanent sums
from the definition; an independent SymPy verifier reaches the same zero
remainders.  The verifiers bind the canonical certificate hash, require the
exact nested key schema, reject duplicate keys and non-finite JSON values,
and fail closed on `badhash`, `extra`, `drop`, and `tamper` mutations.

Separate builder and referee derivations prove the binary-form reduction and
audit every boundary/equality case.  In particular, the final independent
referee report reconstructs from definitions the rank-two factor maps, the
PGL2 and row-scaling reduction for all three row-line multiplicity strata,
the points at infinity, and the zero set of both SOS identities.  The exact
certificate SHA-256 is
`b239bd925f6daac67ab3b2f914fb39e67387d4351af1fc23baa9265c832e74f0`.

Clean one-command reproduction:

```bash
bash scripts/reproduce_clean.sh
```

The runner enforces CPython `3.13.5`, installs hash-locked
`SymPy==1.13.3`/`mpmath==1.3.0` in a fresh temporary environment, executes
the positive and negative verifier suites, all independent equality and
referee checks, the retained breaker reconstruction, and a clean LaTeX build.
Every check passes exactly.

## Novelty and source disposition

The original formula and real setting were checked against Marcus's arXiv
paper and DOI record.  A fresh second novelty audit froze the exact matrix
theorem, its equality classification, and the equivalent split-real
binary-cubic inequality before searching MathDB, arXiv, Crossref, DOI and
forward-citation records.  No prior occurrence was found in the dated
databases and queries recorded in `literature/novelty_recheck_n3.md`.  This
is a bounded search result, not proof of global novelty or absence from
unindexed literature.

## Limits

- `n=4` is not decided: a genuine projective cross-ratio and its collision
  strata remain open.
- The all-order real Marcus conjecture is not decided.
- Ordinary `<=` is not defined for arbitrary complex permanents; no complex
  absolute-value variant is asserted.
- The n=3/n=4 numerical and finite searches are falsification diagnostics,
  not universal certificates.

## Release audit

Citation audit, exact proof/referee audit, fail-closed mutation audit, pinned
clean reproduction, clean LaTeX build, static-source audit, second novelty
search, and page-by-page inspection of the six-page PDF all pass.  The
release manifest binds the manuscript, PDF, proof ledger, and exact
certificates by SHA-256.

No proof assistant was used.  No external submission was performed.

## Post-timeout recovery

At the user's request, Gates 1--6 were re-entered on 2026-08-29 after service
timeouts.  Primary sources, exact certificates, independent role reports,
clean build, citation consistency, every PDF page, and the release manifest
were rechecked.  `audit/RECOVERY_AUDIT.md` records the commands and outcomes.
The mathematical endpoint and limitations were unchanged.
