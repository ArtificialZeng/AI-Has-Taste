# Research-pass source comparison

Job: primary-20260914-chern-logconcavity-research-5a27c3ef60f2.
Inspected 2026-09-14. This is bounded source comparison, not a priority
guarantee or a fresh full-registry search.

The live [primary HTML](https://arxiv.org/html/2605.25271v1) and
[version history](https://arxiv.org/abs/2605.25271) were opened. The history
lists only v1, 24 May 2026. Local Sections 3 and 5 were read with TeX math
preserved: equation (3.3), Lemma 3.5, Theorems 3.6--3.7, equation (5.2),
Lemma 5.3, and Theorem 5.4 supply the relevant definitions and methods.
The exact capture hash agrees with source.md's primary-source provenance.

The nearest proved statements are j=0 and j=1 log-concavity, and j=2
positivity. Section 4 was also inspected: it develops approximate
residual recurrences and the lower-mode operator basis, culminating in
the exact positivity argument in Section 5. It asserts no log-concavity
theorem for the present residual. The source already supplies the lower-mode recurrence and
the trace/Abel method. Those are not contributions of this pass. Its
Figure 1 labels a j=2 log-concavity result, while the formal theorem,
proof, and introduction use j=1; this priority caveat remains. The
proposed theorem concerns a different, explicitly defined polynomial
R_k, the sum of the four lower-mode terms in (5.2). The source proves
their positivity, not the log-concavity of their sum.

The live [Shivam Patel contribution](https://mathdb.com/p/374934/rank-two-binomial-positivity-conjecture-for-schur-coefficien)
was read through its final induction and attribution. It claims all-j
positivity/support, not log-concavity of R_k or B. Its all-index recurrence
and positivity proof are prior claims, not this pass's new theorem or
an independently accepted resolution. The present proof uses the
original source's admissible j=0,1 formulas, so does not depend on the
correctness of that all-index claim.

Current queries included the arXiv identifier with log-concavity and j=2,
the author names with log-concavity, and combinations of binomial,
log-concavity, residual, Chern, recurrence, and forcing. Search results
led to the source, mirrors, MathDB, or mathematically unrelated uses of
residual. No equivalent theorem for this explicit R_k family was found
in the inspected primary source and this bounded search on this date.
No assertion of worldwide novelty follows from that negative search.

Both local handoffs were enumerated and read. The newly supplied
`literature/dedup-evidence-handoff-20260914.md` appeared during this pass;
the focused/broader JSON receipts and desktop screen were then read.
The focused neighbors concern a q,t Gaussian-binomial Schur difference
and monomial additive spanning in Sym^3(C^4); their objects and quantifiers
differ from Newton coefficients of a rank-two Chern polynomial.
The broader receipt includes weighted-bond Schur log-concavity, Chern
configuration algebras, minimal-submanifold problems and a conic count;
none of the displayed statements is the proposed R_k theorem.

The receipts report screening 2,883 Excel rows and 684 registry rows,
but the complete underlying corpora were not searched again here.
The inaccessible target-conversation history remains an explicit gap.
These supplied receipts support only comparison with their displayed
neighbors and do not retroactively change triage's access record.

Proposed value: an infinite-family log-concavity theorem for the natural
forcing polynomial in the first unresolved Schur-mode recurrence,
together with a precise remaining mixed inequality. Its proof extends
the source's certificate method from 17 to 41 prefixes. This is an
auxiliary result, not a new general method or a proof for j=2. Whether
that mathematical increment is sufficient for a result note is a
substantive question for the fresh referee.
