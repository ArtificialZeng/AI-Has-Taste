# Precise problem statement

## Frozen source and notation

The immutable original wording is in `source.md`. Its mathematical reading is
as follows.

For every positive integer \(N\), write
\[
[N]=\{1,2,\ldots,N\}.
\]
A **feasible set** at \(N\) is a (non-multiset) subset \(A\subseteq[N]\) such
that
\[
\forall x,y,z\in A,\quad
\bigl(x,y,z\text{ pairwise distinct}\bigr)
\Longrightarrow
\neg\bigl(
\gcd(x,y)=\gcd(x,z)=\gcd(y,z)
\bigr).
\]
Here \(\gcd\) is the usual positive greatest common divisor. Equivalently, no
three-element subset of \(A\) has one common value on all three pairwise-GCDs.
Because the condition is symmetric, treating triples as ordered or unordered
does not change feasibility.

Define
\[
f_3(N)=\max\{|A|:A\subseteq[N]\text{ is feasible at }N\}.
\]
The maximum exists because \([N]\) is finite. The subscript \(3\) refers to the
forbidden triple; it is not an exponent and introduces no additional parameter.

## Quantified target and scope

Determine the unique integer \(k\) for which \(f_3(127)=k\). This is a finite,
exact extremal problem: only subsets of \([127]\) and triples of distinct
members are in scope. No asymptotic statement, classification of all extremal
sets, or value at any other \(N\) is required.

The source supplies the lead that Zijian Zeng, *The Exact Value of a
Pairwise-GCD Sunflower-Free Function At 126*, DOI
`10.2139/ssrn.7395458`, proves \(f_3(126)=16\). If that theorem uses the same
definition, then inclusion \([126]\subset[127]\) gives
\(f_3(127)\geq16\). Conversely, deleting \(127\) from a feasible subset of
\([127]\) leaves a feasible subset of \([126]\), giving
\(f_3(127)\leq f_3(126)+1=17\). Thus the advertised reduction is the exact
dichotomy \(f_3(127)\in\{16,17\}\), conditional on validating the cited
\(N=126\) theorem and its definition.

A resolution by \(17\) requires an explicit set \(A\subseteq[127]\) with
\(|A|=17\) and an exact verification of its \(\binom{17}{3}=680\) triples. A
resolution by \(16\) requires a complete exclusion of every feasible
17-element subset, together with the lower bound (for example, a verified
16-element witness or the validated \(N=126\) result).

## Nearest prior result and validation status

The cited SSRN item is the only supplied prior-result lead. The project contains
a workbook-derived abstract and BibTeX record in
`literature/user-library-record.md` and `literature/source.bib`, but no copy of
the paper or its certificates. The supplied abstract defines \(f_3(N)\) exactly
as above, states \(f_3(126)=16\), describes an explicit lower bound and a
Boolean/DRAT upper bound, and says the result concerns only the stated finite
value; it does not mention \(N=127\). This is evidence that the bibliography
lead is aligned with the problem, not verification of the paper's formal text.

On 2026-09-06, research pass 2 repeated exact-title, DOI, SSRN-ID,
author/title, and repository searches. They found no inspectable primary copy;
the SSRN landing page returned HTTP 403 to the available reader, direct
command-line retrieval could not connect, and the local bibliography cache had
only the workbook-derived record. Consequently, the paper's formal definition,
theorems, tables, and any computational data at \(N=127\) remain independently
unverified. This access failure does not affect the direct proof below, but it
blocks a novelty claim and paper-specific assertions beyond the supplied
abstract. Details are in `evidence/pass2-audit.md`.

The proposed contribution is: nearest lead \(f_3(126)=16\); delta, determine
which of \(16,17\) is \(f_3(127)\); verification route, either an exact
17-element certificate checked over all triples or a proof-producing exhaustive
exclusion of size \(17\), after validating the lead.

## Research-pass candidate (pending fresh referee)

Research pass 1 produced a direct, paper-independent candidate resolution
\(f_3(127)=16\). A 16-element witness was checked from the definition, and the
nonexistence of a 17-element feasible set was encoded in CNF and certified by a
DRAT proof accepted by `drat-trim`. Details and hashes are in
`evidence/computation.md`. This is a researcher handoff, not yet a referee
acceptance or a novelty claim. Research pass 2 reran the witness check,
byte-for-byte CNF regeneration, and DRAT verification successfully; see
`evidence/pass2-audit.md`. The cited SSRN paper remained inaccessible.
