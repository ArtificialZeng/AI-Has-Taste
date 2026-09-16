# Fresh citation and bibliography audit

## Binding and method

- Release job: `win-00056-p04-release-abe5976d40e2`.
- Accepted evidence snapshot: `f400278043022a78b6fad23f832e57d2593a690342ae64738ccd6469b18597d0`.
- Manuscript snapshot: `3c292282824e1a08f3f7b44f03ed335c4190af52c4d10103b823c287b44ae897`.
- PDF SHA-256: `0fa9bf6381c47f17b4ce7fc472f9ca5b4070beac99e2ad8bc8d8d9683836f1cf`.
- Verification mode and date: search verification, 2026-09-07.
- Audit architecture: pass 1 extracted and froze the claim/citation surface in
  `audit/citation-claim-ledger.md`; pass 2 below uses those fixed claim IDs and
  does not re-extract claims.
- Per-reference checking was performed serially because this release job
  expressly prohibited agents and background workers.

All publication inputs listed by `publication.json` were inspected:
`manuscript/main.tex` and `manuscript/references.bib`.  The TeX source has four
distinct citation keys and six ordinary body-flow citation commands.  There are
no custom citation macros.  The canonical bibliography has exactly those four
entries; no source key, BibTeX key, or auxiliary-file key is missing or unused.

## Pass 2: fixed-claim verification

| ID | Status | Confidence | Exact support and limitation |
|---|---|---|---|
| C01 | Verified | paraphrase | The SIAM publisher record identifies Daykin--Frankl, the 1983 article, DOI, volume, pages, and an abstract saying that it discusses conjectured inequalities for all subsets of a finite set.  Duffus--Howard--Leader, Introduction/Conjecture 1, gives the exact convex-family inequality and attributes it to Daykin and Frankl; Williams v1, p.1, independently gives the same attribution and formula. |
| C02 | Verified | exact | Duffus--Howard--Leader, Introduction and Theorem 7, explicitly state that the conjecture is verified for initial segments of the binary order.  Its abstract and sections 2--6 substantiate the broader description of related width results for downsets. |
| C03 | Verified | exact | Williams v1, PDF p.2, Theorem 1 and Lemma 2 state the full product inequality and the exact two-layer reduction used by the manuscript. |
| C04 | Verified | exact | Williams v1, PDF p.3, uses `C` in both sorting bullets without defining it and says that the second output follows by “hourglass symmetry.”  No later arXiv version was shown by the official record on the search date; the locally inspected file is explicitly v1. |
| C05 | Verified | exact | Williams p.3 fixes the rules being interpreted.  The frozen certificate `evidence/inferred-sorting-failure.json` and the displayed three-chain substitution reproduce the failed first output.  This verifies only failure of that explicitly identified interpretation, not failure of the lemma. |
| C06 | Verified | exact | The displayed antichains and two horizontal chain covers prove both section widths are exactly 2.  Direct inspection of the five-point downset gives width 2, hence equality.  The frozen certificate records the same values. |
| C07 | Verified | exact | Summing the per-order `convex_subsets` counts in `evidence/exhaustive-through-5.json` gives exactly 180,102.  Its counterexample field is null, and its frozen verifier and method scope are explicit.  This is finite evidence only. |
| C08 | Verified | exact | A linear extension of any finite poset relabels its elements increasingly, so its relation occurs among naturally labelled transitive closures.  This justifies isomorphism-class coverage, not a claim of one representative per class. |
| C09 | Verified | exact | Summing the per-order pair counts in `evidence/component-repair-through-5.json` gives exactly 1,684,785; its failure field is null and its checked-condition list is exactly legality, both output antichains, and cardinality preservation.  This is finite evidence only. |
| C10 | Verified | exact | The DOI-specific Crossref capture in `literature/crossref-ssrn-7385118.md` records HTTP 200, Crossref status `ok`, message-type `work`, and a deposited abstract containing both “All arithmetic is integral” and “independent evaluators are supplied for both endpoints.”  Its required SHA-256 was independently recomputed.  The inaccessible SSRN full text is not used. |
| C11 | Verified | exact | Neither the deposited abstract nor its metadata discusses Daykin--Frankl, the repaired lemma, or this project's census.  The manuscript states this limitation immediately and uses the source only for the abstract-level methodological comparison. |

No numerical error, hallucination, misleading citation, missing citation, or
unsupported strengthening of the accepted statement was found in the frozen
claim set.  In particular, the manuscript consistently separates the universal
proof from finite computation and separates the source-step counterexample from
the truth of the lemma.

## Bibliographic records and nearby-claim support

| Key | Current title and verified primary record | Needed for | Action |
|---|---|---|---|
| `DaykinFrankl1983` | *Inequalities for Subsets of a Set and KLYM Posets*, David E. Daykin and Peter Frankl, *SIAM Journal on Algebraic and Discrete Methods* 4(1), 67--69 (1983), DOI `10.1137/0604009`; publisher record: `https://epubs.siam.org/doi/10.1137/0604009` | Original problem and attribution | Metadata verified; retained; no key change. |
| `DuffusHowardLeader2019` | *The Width of Downsets*, Dwight Duffus, David Howard, Imre Leader, *European Journal of Combinatorics* 79, 46--59 (2019), DOI `10.1016/j.ejc.2018.11.005`; publisher record and author manuscript/arXiv `1710.05714` inspected | Closest established special case and related downset results; also exact restatement of the original conjecture | Metadata and claimed theorem verified; retained; no key change. |
| `Williams2026` | *Confirmation of the Daykin--Frankl Conjecture*, Kada Kálmán Williams, arXiv:`2609.03087v1` (2026); official record `https://arxiv.org/abs/2609.03087` and frozen local PDF inspected | Exact theorem/lemma being repaired and exact defective sorting passage | Metadata and all cited locators verified; retained; no key change. |
| `Zeng2026SSRN7385118` | *Certified Bounds for the Number of Unlabeled Posets on 17 Points*, Zijian Zeng, SSRN preprint (2026), DOI `10.2139/ssrn.7385118`; DOI-specific Crossref metadata/abstract capture inspected | Narrow, explicitly limited methodological comparison for proof-oriented exact finite-poset computation | Metadata/abstract scope verified; retained; no key change. |

The bibliography is not user-library-only: the three natural non-library primary
sources cover problem origin, closest prior theorem, and the exact proof under
repair.  The single selected library paper is genuinely relevant only to the
secondary computational-method sentence; selecting another library entry would
pad the bibliography.  The elementary central-binomial width of the Boolean
lattice and the self-contained comparison-graph construction need no further
dependency citation.  No retained source is decorative.

The active registry SHA-256 is
`67477dfa5d2f3dfcb5a9123fd79975af80968b43058ff32c774143c2f26112d4`,
and its source workbook SHA-256 is
`93cd3aa74e2deac375e7e54b3a640cb457c186b0a8e90fa2c0afe7024f59a427`.
The attempt-specific binding and row-35 selection are recorded in
`audit/user-bibliography-selection.json`.

## Mechanical consistency and conclusion

`check_bib_keys.py manuscript/main.tex --aux manuscript/main.aux` reports four
cited keys, four bibliography keys, zero missing files or keys, zero unused
entries, and exact TeX/aux agreement.  The converged `main.log` and `main.blg`
contain no undefined citation/reference, missing database entry, repeated entry,
BibTeX warning, LaTeX error, fatal stop, runaway argument, or layout warning.

Verdict: **accept**.  Four distinct references (six citation occurrences) were
verified; no `.tex` or `.bib` correction and no citation-key replacement was
needed.  The only access limitation is the SSRN full text, which is immaterial to
the deliberately abstract-only claim and is expressly disclosed.
