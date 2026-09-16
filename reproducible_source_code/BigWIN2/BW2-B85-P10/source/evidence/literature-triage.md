# Literature triage evidence

Retrieval date: 2026-09-11.  Original retrieval job provenance:
`win-00085-p10-triage-d3832cab6298`.  The arXiv record, v1 HTML at the cited
theorem/remark, and targeted exact/equivalent searches were rechecked live by
`win-00085-p10-triage-a175262e65a9` on the same date.  The record still listed
only v1 (submitted 2026-05-04), and the recheck found no primary paper claiming
to settle Remark 3.4.  This remains negative-search evidence, not proof of
priority or completeness.

Research pass 3 (`win-00085-p10-research-831e68f0827d`) again opened the live
arXiv abstract and v1 HTML on 2026-09-11.  The abstract history still listed
only v1; HTML Theorem 3.3 still assumed every `a_i>=1`, and Remark 3.4 still
stated the zero-leg extension only as a belief.  Fresh exact-phrase and
equivalent-keyword searches for log-concavity of caterpillar domination
polynomials returned that paper but no primary source resolving the remark or
the specific `T(p,0,0,q)` family.  This is a bounded recheck, not a claim of
exhaustive priority.

## Inspected primary source

- Alina Du, Steven Heilman, and Greta Panova, *Trees and Graphs with Non
  Log-concave Dominating Set Sequence via AI Tools*, arXiv:2605.02193v1.
  Abstract record: https://arxiv.org/abs/2605.02193 ; inspectable HTML:
  https://arxiv.org/html/2605.02193v1 .  The arXiv record lists submission on
  2026-05-04 and only version v1 as of retrieval.
- Definition and claim context: HTML lines 56--70 define dominating sets,
  `d_j`, and log-concavity.  Section 3.2, lines 232--238 (PDF p.6), defines
  `T(a_1,...,a_k)` and states Theorem 3.3 only under `a_i >= 1` for every `i`.
  Lines 240--255 give the factorization proof and explicitly use `a_i >= 1`.
- Remark 3.4, HTML lines 256--258 (PDF p.7), says the authors *believe* that
  caterpillars with some `a_i=0` also have log-concave domination
  polynomials.  It supplies neither a proof nor a numbered conjecture.

## Search scope and status

Exact-title, exact-assertion, and equivalent-keyword searches were run against
arXiv and DOI-indexed primary literature for `caterpillar`, `domination
polynomial`/`dominating set sequence`, `log-concave`, and `zero legs`/`legless`.
They recovered the paper above and no later primary resolution of Remark 3.4.
That negative search result is not proof of priority.  The source status is
therefore **open-supported (provisional)** by the authors' explicit Remark 3.4;
any eventual novelty claim still requires a broader current literature audit.
