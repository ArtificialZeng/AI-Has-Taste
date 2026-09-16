# Fresh mathematical referee report

## Frozen scope

- **Candidate kind:** `result-note`.
- **Original status:** `unresolved`.
- **Claim reviewed:** no 3-out-of-5 admissible element of the free group
  \(F_5\) has reduced length at most 18, so \(L(3,5)\ge 20\); the displayed
  length-26 word gives \(L(3,5)\le 26\).
- **Snapshot:** `95cd9fcb261ad6fe4df05945af76955e312cda7ba75fce350ac973bbca29f6cf`.

The candidate explicitly leaves the original exact-minimum problem unresolved.
The audit below assesses the stated subsidiary result and does not reinterpret it
as a resolution of the original problem.

## Reconstruction of the lower-bound argument

Every generator must occur in an admissible word.  If generator \(g\) were
absent, choose two other generators \(a,b\).  Retaining the triple
\(\{a,b,g\}\) would give exactly the same projected word as retaining the pair
\(\{a,b\}\), whereas admissibility requires the former to be nonidentity and
the latter to be identity.

For each generator \(g\), retain a pair containing \(g\).  Since that pair
projection is the identity, its exponent sum in \(g\), and hence the exponent
sum of \(g\) in the original word, is zero.  Thus each unsigned occurrence
count is a positive even integer.  Consequently a candidate has even length at
least 10.  The positive-even partitions into five sorted parts at lengths
10, 12, 14, 16, and 18 number respectively 1, 1, 2, 3, and 5, giving exactly
the twelve patterns frozen in the snapshot.

It is enough that the CNFs retain cyclically reduced representatives.  Indeed,
if any admissible element of length at most 18 existed, choose one of minimum
length.  If its reduced representative began with \(a\) and ended with
\(a^{-1}\), it would have the form \(aua^{-1}\).  Every deletion maps this to
\(\pi(a)\pi(u)\pi(a)^{-1}\), so identity versus nonidentity is exactly the same
for \(u\); this would give a shorter admissible element, a contradiction.
Hence a shortest counterexample is cyclically reduced.  Its generators can be
relabelled so their counts are sorted, it can be rotated to an occurrence of a
least-count generator and that generator labelled 1, and independent generator
inversions make first occurrences positive.  Within every equal-count block,
the remaining labels can be assigned in first-occurrence order.  These steps
give `x[0,+1]`, the tie-block ordering clauses, first-occurrence sign clauses,
and `x[L-1,-1] = false` used by the encoder.  Thus no incomplete symmetry
quotient is being used.

For a retained set \(R\), the encoding's variable \(E_R(i,j)\) is equivalent
to the projection of the half-open interval \([i,j)\) freely reducing to the
identity.  If the first letter is not retained it is skipped.  Otherwise, in
any identity reduction it cancels with a later inverse letter at a position
\(k\), with both the intervening projected word and the suffix reducing to the
identity.  Conversely, those two empty reductions followed by that
cancellation empty the whole interval.  Induction on interval width proves the
grammar equivalence.  I separately checked the Tseitin definitions in
`search_exact_sat.py`: relevance is an exact disjunction under the one-hot
letter constraint; the match variable is true exactly when positions \(i,k\)
hold retained inverse letters; conjunction and disjunction helpers encode both
directions.  The final clauses require emptiness for all ten retained pairs and
nonemptiness for all ten retained triples.  Adjacent inverse input letters are
forbidden, and the sequential counters impose exactly half positive and half
negative occurrences for every fixed count.

Therefore satisfiability of one of the twelve CNFs would produce a canonical
shortest admissible word in the corresponding case.  Conversely, the
normalization above maps any hypothetical shortest word of length at most 18
to a model of one of them.

## Checks actually performed

1. I recomputed SHA-256 for `claim.json`, `source.md`, `problem.md`, and every
   snapshot-listed evidence file.  All matched `audit/snapshot.json`.
2. I ran `evidence/audit_exact_encoding.py` afresh.  It independently
   enumerated the 1+1+2+3+5 patterns, regenerated every archived CNF clause for
   clause with matching variable and clause counts, and compared the interval
   grammar with ordinary stack reduction on all 335,923 words of length at
   most 7 over two retained generators and one ignored generator.  Every check
   passed.
3. I ran `evidence/check_drup.py` afresh with MiniSat 2.2 propagation on all
   twelve archived CNF/DRUP pairs.  Every learned-clause addition was RUP, and
   every proof contained a RUP-checked empty-clause addition.  Ignoring proof
   deletions is sound here: retained earlier learned clauses have already been
   shown to follow from the base CNF, so using them can only add entailed
   consequences.  This fresh replay establishes UNSAT independently of the
   stored solver-status fields.
4. I inspected the separate frozen `drat-trim` audit and its full replay log.
   All twelve archived pairs are hash-bound to the snapshot, returned exit code
   zero, and contain exactly one `s VERIFIED` marker.  I also inspected the
   Glucose3 reproduction script and report; they record byte-identical CNF and
   proof reproduction for all twelve cases.  These provenance checks are
   corroborative; the lower-bound conclusion already follows from the fresh
   RUP replay and the audited encoding.
5. I ran `evidence/verify_upper26.py` afresh.  The word is freely reduced of
   length 26, all ten size-three deletions reduce to the identity, and all ten
   size-two deletions have nonempty reduced residuals.

These checks exclude the only possible lengths below 20: lengths below 10 are
ruled out by positive even occurrence counts, and lengths 10, 12, 14, 16, and
18 by the exhaustive certified cases.  Hence \(L(3,5)\ge 20\); the verified
word gives \(L(3,5)\le 26\).

## Source comparison and contribution

The frozen primary PDF proves the zero-exponent/parity fact in Section 6 and
lists exact 3-out-of-5 as the next small open minimum in Section 8.  The frozen
source record reports only an author-repository search through length 16 and
correctly treats its log as prior computational evidence rather than a
standalone certificate.  Against that nearest result, the candidate supplies
a proved-complete, replayable exclusion through length 18 and narrows the exact
value to \(20,22,24,\) or \(26\).  This is a nonroutine and useful finite lower
bound: it advances the next unresolved frontier and supplies independently
checkable certificates rather than merely another heuristic search log.

The literature comparison is expressly bounded by the frozen screen and is
not evidence of worldwide priority.  The candidate makes no exhaustive
priority claim, so this limitation is stated honestly and does not enlarge its
mathematical scope.

## Remaining gap and verdict

The exact value of \(L(3,5)\) remains unresolved; lengths 20, 22, and 24 have
not been excluded, and no construction shorter than 26 is certified here.
That is the disclosed gap of the original problem, not a gap in the submitted
subsidiary theorem.

**Verdict: accept.**  The exact frozen `result-note` scope, its mathematical
correctness/evidence, and its contribution all pass review.
