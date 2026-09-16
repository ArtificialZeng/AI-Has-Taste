# Citation and bibliography audit: accept

Job: `win-00060-p03-release-80160ca24233`  
Mathematical snapshot: `952ec68c27a7713fe1e32162ff743686ae874ef4d2b152c9b97f31d8681fc6f6`  
Manuscript snapshot: `d455837f7fd7b000aa22c7baa08bd4add8f334c66c868d2ae5da7382d38fafa9`  
PDF: `a40cd71a58b5b2a3bf59caf86025c9f0d1047b8e5582532da08a7c7370acaee5`

## Method and result

The required non-interactive two-pass procedure was used. Pass 1 read the
complete manuscript and froze eight externally sourced claim/citation pairs in
`audit/citation-claim-ledger.json`, without attempting verification. Pass 2
used only that frozen ledger and recorded exact source locations in
`audit/citation-verification.json`. All eight claims are verified (five exact,
three faithful paraphrases). There are no numerical errors, hallucinations,
misleading claims, missing sources, or unverifiable retained citations.
Subagents were not used because this job explicitly prohibited agents and
other workers.

## Per-reference audit

| Key | Primary record and source location | Nearby support | Action |
|---|---|---|---|
| `Padberg1989` | Manfred Padberg, Springer publisher page, Abstract and bibliographic record, https://link.springer.com/article/10.1007/BF01589101 | The Boolean quadric polytope results from linearizing the products in a quadratic zero-one form. | Title, author, 1989 date, volume 45, pp. 139--172, and DOI verified; retained. |
| `BurerLetchford2009` | Samuel Burer and Adam N. Letchford, SIAM publisher page, Abstract, https://epubs.siam.org/doi/10.1137/080729529 | The BoxQP convex sets studied there are explicitly related to the Boolean quadric polytope. | Title, authors, journal, volume/issue, pp. 1073--1089, year, and DOI verified; retained. |
| `ZhangWang2026` | Junyu Zhang and Guanyi Wang, arXiv:2609.03617v1 and checksum-bound local PDF; instance (5), Propositions 1--3, relaxation (9), Appendix A, Theorems 3--4 | Supplies the exact fixed instance, full BQP relaxation, original value zero, feasible `-1/100`, numerical `-0.0108`, and general-dimensional gap results. | arXiv title, authors, identifier, date/version, and every cited passage verified; retained. |
| `ZengEtAl2026` | Official SSRN record and Abstract, https://papers.ssrn.com/sol3/papers.cfm?abstract_id=7348478 | Supports only the nearby methods comparison: a finite-dimensional Hermitian positivity problem using exact rational/algebraic sign decisions and independent verification programs. | All five authors, title, 2026 date, DOI, and support verified; retained as a direct body-flow `\cite{ZengEtAl2026}`. |

No official record conflicts with the retained metadata. The available primary
pages did not expose a canonical BibTeX export whose field block differed from
the current entries, so no speculative replacement or key change was made.
There are no old-to-new key mappings and no unresolved metadata blockers.

## Coverage and user-library gate

The bibliography is not library-only. Padberg is the natural primary source
for the Boolean-quadric lift; Burer--Letchford is the primary BoxQP connection;
Zhang--Wang is both the problem-origin and closest-comparison source; and row 29
of the active user library supports a narrow verification-method comparison.
The exact certificate is self-contained and separately accepted in
`audit/math.json`, so it imports no uncited external theorem. Four references
are therefore sufficient for the actual dependencies, without padding.

The active 49-record first-sheet registry and workbook were read and their
SHA-256 hashes independently checked. Row 29 is the one genuinely relevant
library entry. A second library item would not support another natural claim.
The fresh attempt binding is recorded in
`audit/user-bibliography-selection.json` with citation attempt 3 and launch ID
`6e92c27c-c947-4645-b14e-a82cefc667e7`.

## Mechanical checks

The canonical bibliography is `manuscript/references.bib`. The skill checker
reports four cited keys, four BibTeX keys, no missing or unused entries, and
exact agreement with `main.aux`. The converged `main.log` and `main.blg` contain
no undefined citation/reference, database miss, duplicate entry, BibTeX
warning, LaTeX error, overfull box, or underfull box.

Verdict: **accept**.
