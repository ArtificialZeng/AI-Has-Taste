# Verification report

**PASS — all 25 fixed claims and all seven retained citation keys verified.**

Release job `newwin-00001-p18-release-ecb3e56853b6`; citation attempt 2; launch `4d1f8672-f643-46f1-a0ca-d3a703cd0153`.
Completed 2026-09-12T11:40:37.346664+00:00. Mode: fresh primary-source search and manual passage review,
combined with the accepted mathematical evidence and exact package checks.
No agents or other Codex processes were used, as the user expressly prohibited them.

## Two-stage review and exact scope

Stage 1 read the complete manuscript and froze the 25 claims and direct citation
pairs in `audit/citation-extraction-initial.json`. After the justified official
BibTeX replacement and synchronized preprint attribution, the final extraction
was frozen in `audit/citation-extraction-final.json` and the canonical ledger.
Stage 2 verified the fixed claims sequentially against original source locators,
with no new claim extraction during verification. The seven-key ledger union
equals the ordinary body citation set exactly. Comments, inert macros,
hidden conditionals, verbatim material and nocite do not supply coverage.

The accepted theorem remains the complete original fixed-P classification:
ordinary recurrence iff the word is zero iff Q belongs to P F_p[P]. The body
preserves all primes, n=0, and arbitrary finite Laurent support. It does not
claim a solution for other degenerate P, higher prime powers, or exhaustive
priority. Primary comparisons retain their actual characteristic and
recurrence hypotheses. Mathematical acceptance remains the frozen referee's;
this release review checks the manuscript's fidelity to that scope.

## Citation coverage and source audit

| Key | Claims | Verified primary source | Exact source locations | Why retained |
|---|---|---|---|---|
| Kohen2026 | C02, C07, C08 | [A Linear Representation for Constant Term Sequences mod p^a with Applications to Uniform Recurrence](https://cs.uwaterloo.ca/journals/JIS/VOL29/Kohen/kohen9.pdf) | Theorem 14, printed/PDF page 9, browser-extracted lines 673–682; Definition 18 and Proposition 19, printed/PDF page 11, lines 848–857 | Problem origin, exact recurrence convention, and closest general density/recurrence results. |
| RowlandZeilberger2014 | C05 | [A Case Study in Meta-AUTOMATION: AUTOMATIC Generation of Congruence AUTOMATA For Combinatorial Sequences](https://arxiv.org/pdf/1311.4776) | Author-submitted arXiv v1, 19 November 2013; record journal-reference and related-DOI fields; The Present Method: Using Constant Terms, preprint page 3, lines 94–105 | Foundational automatic representation for the class being studied; no claim that an automaton was computed here. |
| Kohen2025 | C06 | [Uniform Recurrence in the Motzkin Numbers and Related Sequences mod p](https://www.combinatorics.org/ojs/index.php/eljc/article/download/v32i2p44/pdf/) | Publisher PDF first-page author/title/date and DOI footer; Proposition 15, printed/PDF page 9, lines 593–599; proof continues on page 10 | Closest earlier result and precise boundary of its applicability. |
| Gessel2016 | C11, C12 | [Lagrange Inversion](https://arxiv.org/pdf/1609.05988) | Section 1.1, preprint page 1, lines 26–30: coefficient domain contains Q; Theorem 4.1.1 and proof, preprint pages 22–23, lines 2826–2871 | Nontrivial formal-residue method and its characteristic restriction. |
| Zeng_2026 | C14 | [Generic Characteristic-Zero Equivalence Between Derivative Bézout Inversion and Multipoint Evaluation](https://www.preprints.org/manuscript/202608.2160) | Publisher title/author/version/posted-date fields; Section 6, Proposition 6.1 and proof, publisher HTML lines 283–292 | Exact library match explaining why derivative data lose the constant coefficient retained by the quotient relation. |
| ByszewskiKonieczny2020 | C15 | [Automatic Sequences and Generalised Polynomials](https://www.cambridge.org/core/services/aop-cambridge-core/content/view/89086F399E83E464032E523A6DD2BEAB/S0008414X19000038a.pdf/automatic_sequences_and_generalised_polynomials.pdf) | Definition 3.11, printed page 411/PDF page 20, lines 1526–1535; Theorem 3.13, printed page 412/PDF page 21, lines 1554–1573 | Closest structural finite-sums context and the reason a stronger local argument is supplied. |
| LaugierSaikia2012 | C23 | [A New Proof of Lucas' Theorem](https://nntdm.net/papers/nntdm-18/NNTDM-18-4-01-06.pdf) | Publisher PDF page 1, title/author/volume/year/pages and Theorem 1.1, lines 0–42 | Verification technique used by the exact computational supplement. |

The bibliography is adequate for the actual claims: problem origin and closest
prior results, the formal-residue method, finite-sums context, and the exact
Lucas verification method all have natural primary citations in body flow.
Six works are genuinely outside the active user library, as checked against
all 49 registry identities; renaming the selected library key did not change
its identity. Row 14 is the single gate-bound library selection because it
matches the precise quotient family and information-loss comparison. No
unrelated second item was inserted. None of the seven retained works is used
only decoratively. Registry metadata were leads, not claim evidence.

Source-specific scope checks include: Gessel's coefficient domain contains Q,
so the manuscript proves its own characteristic-p extension; Zeng's splitting
statement assumes algebraic closure, but only its displayed Bezout identity is
used over F_p(t); Byszewski–Konieczny permit stage-dependent IPS shifts and do
not supply the fixed-translate obstruction; Kohen's positive-index condition
and zero-word exception are both retained. No arithmetic complexity result is
attributed to the selected preprint.

## Exact DOI recovery and bibliography changes

The exact supplied `literature/doi-recovery-evidence-20260912.md` has SHA-256
`248c9f41d770b5de7fc6b37af3948991084b2a30d6e530ba1a02771640ddee83`.
It was independently read and audited, and its linked JSON and BibTeX capture
hashes were recomputed. The official [Crossref work endpoint](https://api.crossref.org/works/10.20944/preprints202608.2160.v1)
is recorded in that evidence. Its saved response has status `ok`, message type
`work`, source `Crossref`, and matches the active row's DOI, sole author Zijian
Zeng, title, posted/issued 2026-08-31, and version-1 resource URL. Its deposited
type is `posted-content`, subtype `preprint`. The note records the transport
provenance; it does not provide response headers. A fresh ordinary WSL curl
request failed with exit 7, which does not erase the valid saved response.
The publisher's actual Proposition 6.1 and proof were also freshly inspected.
The record certifies neither peer review nor release acceptance.

`manuscript/references.bib` now contains the official transformation block
verbatim, including its original key and whitespace. The only key mapping is
`Zeng2026` → `Zeng_2026`. The sole body use was synchronized and explicitly
described as a preprint; the six other verified entries were retained.
There are no unresolved metadata or source-support blockers.

The official export uses `@article` without a journal field. BibTeX therefore
emits the single understood warning `empty journal in Zeng_2026`. No journal
name was fabricated or peer-review status inferred. The rendered reference
contains author, title, August 2026 and the exact versioned DOI; the body
identifies its preprint status. The unchanged official block is preserved in
`literature/crossref-2026082160v1-20260912.bib` and the precise patch is in
`audit/release-changes.patch`.

## Every fixed claim

All locations below are one-based lines of `manuscript/main.tex`.

| Claim | Lines | Direct citation / evidence | Verification |
|---|---|---|---|
| C01 | 31–41 | Accepted proof / exact evidence | The abstract preserves the accepted all-prime/all-Laurent-Q three-way classification; only the fixed example of Question 20 is resolved. |
| C02 | 52–56 | Kohen2026 | Kohen Definition 18 explicitly equates recurrence with infinitely many later returns without bounded gaps; indexing from zero is included. |
| C03 | 58–65 | Accepted proof / exact evidence | All three items agree with claim.json and the accepted proof, including n=0 and Q=P F(P). |
| C04 | 67–71 | Accepted proof / exact evidence | The normal-form argument yields the K-span of positive powers of P, not the Laurent-ring ideal. All finite positive/negative exponents and p=2 remain included. |
| C05 | 73–75 | RowlandZeilberger2014 | The Rowland–Zeilberger construction and its degree-bounded state finiteness prove the attributed automatic representation modulo prime powers. |
| C06 | 75–77 | Kohen2025 | The source Proposition 15 displays the symmetric trinomial and explicitly assumes p>2; the manuscript attributes only that scope. |
| C07 | 78–81 | Kohen2026 | Kohen Theorem 14 states density-one zeros and expressly exempts the zero sequence from the non-uniform-recurrence conclusion. |
| C08 | 81–85 | Kohen2026 | Kohen Proposition 19 requires n_0>0 with nonzero unweighted constant term. Question 20 explicitly lists this completely degenerate P. |
| C09 | 87–92 | Accepted proof / exact evidence | The comparison is bounded to the inspected primary results and the date of review, with no universal priority claim. Those results do not supply the stated fixed-P kernel/ordinary-recurrence classification. |
| C10 | 108–112 | Accepted proof / exact evidence | The recurrence a_(j+1)=p*a_j+1 gives Y=z(1+Y^p); its leading term z makes it the inverse of x/(1+x^p), as in the frozen proof. |
| C11 | 118–133 | Gessel2016 | Gessel Section 1.1 assumes a domain containing Q; Theorem 4.1.1 is the cited change-of-variable formula. The manuscript supplies its own integral-lift reduction to characteristic p. |
| C12 | 114–145 | Gessel2016 | The residue derivation matches the accepted proof: f_prime=(1+x^p)^(-1) in characteristic p, giving [z^n]Y^r=[x^0]P^n*x^r without division in F_p. |
| C13 | 147–205 | Accepted proof / exact evidence | The quotient is the Laurent ring, free over K[t]; the shift operator has triangular monic images of all degrees. This gives image K[Y] and kernel P K[P], including negative monomials and cancellations. |
| C14 | 208–214 | Zeng_2026 | Publisher Proposition 6.1 and its proof give the normalized pair independent of d. For c=-t over F_p(t) the identity is direct; no splitting claim or characteristic-zero complexity conclusion is transferred. Official captured DOI metadata independently agree. |
| C15 | 224–230 | ByszewskiKonieczny2020 | Definition 3.11 permits stage-dependent shifts, Theorem 3.13 gives the arid-or-IPS alternative, and the following discussion forbids substitution by a fixed translated IP set. The paper proves its required stronger local statements. |
| C16 | 232–244 | Accepted proof / exact evidence | Returning the prefix through a+T_m at a positive position t_(m+1)>T_m duplicates every old subset sum. This is ordinary recurrence, with no bounded-gap assumption. |
| C17 | 253–285 | Accepted proof / exact evidence | Disjoint positive block sums divisible by successive p-powers produce D+1 separated digit blocks. The same index excludes every offset r=0,...,D; D=0 and p=2 are covered. |
| C18 | 287–304 | Accepted proof / exact evidence | Each nonzero coefficient comes from some Y^r. Multiplying an exponent sum by p-1 and adding r yields a sum of r p-powers; carrying lowers digit sum. Cancellations can only shrink support. |
| C19 | 306–316 | Accepted proof / exact evidence | The main proof combines the accepted kernel, return-set and digit-support lemmas in the same scope. No finite computation is used to prove the infinite implication. |
| C20 | 320–324 | Accepted proof / exact evidence | Phi(1)=1, Phi(P)=0 and Phi(x)=Y give the three boundary examples; a_(j+1)-a_j=p^j gives exactly p,p^2,p^3,... as successive gaps. |
| C21 | 326–331 | Accepted proof / exact evidence | The recursion multiplies length by 6 and number of ones by 2. Copies of every fixed W_m recur arbitrarily late; the stated prefix upper bound gives zero density. |
| C22 | 335–345 | Accepted proof / exact evidence | The binomial formula follows from x^(-n)(1+x^p)^n. The condition (n-e)/p in {0,...,n} includes integrality and every boundary case. |
| C23 | 346–349 | LaugierSaikia2012 | Theorem 1.1 gives the actual Lucas digit product implemented in lucas(); the negative-monomial recurrence follows from the displayed Laurent identity. |
| C24 | 349–352 | Accepted proof / exact evidence | Fresh execution reproduced all results byte for byte. Counts are exactly 7*33*1025=236775 and 7*33*129=29799, with the stated prime, exponent and index ranges. |
| C25 | 354–367 | Accepted proof / exact evidence | Fresh independent-program replay reproduced 10*49*1025=502250 comparisons, 10*6=60 kernel matrices, and 207 digit certificates with 635 blocks and 635 offset checks. Degree/family coverage is explicitly finite in the supplement; it is not an infinite recurrence certificate. |

There are 25 verified claims, zero numerical errors, zero unverified claims,
zero misleading attributions and zero hallucinations. C09 is a bounded
comparison, and C14 includes an explicitly checked algebraic specialization;
their conservative classification is interpretation. Method and AI-assistance
disclosures were checked separately against the actual code and frozen review
record. Distinct contexts are not described as statistical independence or
external peer review.

## Mechanical, dependency, and visual checks

The canonical TeX uses only the canonical `references.bib`; all eight sorted
publication source files were inspected. The FLS dependency record contains
no omitted project-authored citation source. Standard TeX packages are system
dependencies. Both standalone supplement programs were executed as unchanged
copies under `audit/supplement-replay`; all three generated result/certificate
files were byte-identical to the publication inputs. Frozen mathematical
files and the publication supplement remained unchanged.

Clean `latexmk -C` followed by `latexmk -pdf -interaction=nonstopmode
-halt-on-error -outdir=build main.tex` succeeded. The final key checker found
seven TeX keys, seven BibTeX entries, seven AUX keys, no missing or unused
keys, no duplicate entry, and no undefined citation/reference. There are no
TeX overfull/underfull boxes or fatal diagnostics; the one export-related
BibTeX warning is documented above. Every final 120-DPI rendered page 1–6
was actually viewed in this context, including every bibliography entry.
No clipping, overlap, missing glyph, broken link label, or illegibility was
observed. Build and visual details are in their respective reports.

The hook-compatible `validate_selection` function passed for this exact
attempt and launch. Each selected `verified_at` is the actual UTC date
2026-09-12, and its compact citation sentence matches the masked TeX lines.
The configured `pre_publish_hook` was not invoked. The runner owns the
post-worker prepublication hook and publish step.

Manuscript digest: `260f9e3032adc94ed40a9d4684bb3542d018ea567b648eaa5f628dbf55afdcf4`.
PDF digest: `b3635986e7c3be508b7917c1a6d04675ff0cbd3674b388c0aae4fe3c87004b72`.
These release checks are process and source-support evidence, not a new
mathematical proof or a guarantee of priority.
