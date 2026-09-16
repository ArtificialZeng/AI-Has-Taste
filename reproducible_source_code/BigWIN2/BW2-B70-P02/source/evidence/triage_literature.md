# Triage literature and source check

Retrieval date: 2026-09-08.  This is a bounded source-status check, not a
claim of exhaustive priority.

## Primary source inspected

- Yi-Qiu Mao and Zhi-Yi Wu, *On the spectrality of the non-homogeneous
  golden-mean self-similar measure*, arXiv:2609.04701v1 (2026-09-04),
  <https://arxiv.org/abs/2609.04701v1> and
  <https://arxiv.org/html/2609.04701v1>.
- Official HTML lines 60--84 define the two-map Hutchinson measure and the
  golden-mean parameter.  Lines 233--266 give
  `F(xi)=p F(xi/2)+p^2 exp(-pi i xi) F(xi/4)` and its 2-by-2 matrix product.
- Proposition 3.3, official HTML lines 297--360, proves no zero on
  `[-1.08,1.08]`.
- Section 4.3, lines 562--589, reports a double-precision scan of
  `[1,10^7]`, including the two smallest reported `|q|` valleys at
  `6580077.19160276` and `5065070.60771886`.
- The Remark at line 590 explicitly says the numerical work is not a formal
  proof and leaves a rigorous computer-assisted verification for future work.
  Thus the frozen finite zero-free assertion is not proved by this source.

## Search coverage and status

Exact-title, exact-phrase (`"golden-mean self-similar measure"`), recurrence,
and parameter-pair searches restricted to arXiv were run on 2026-09-08.  They
surfaced the Mao--Wu preprint but no separate paper asserting a rigorous
zero-free result for this measure through `10^7`.  Broader results returned by
the search concern Fourier decay of general self-similar measures, not this
finite zero-free assertion.  Search results and snippets are only leads; this
limited negative search does not establish novelty or priority.

Source-status assessment: **open-supported** for the precise formal upgrade.
The source itself supplies the unresolved rigorous-verification gap.  The
nearest verified result is its Proposition 3.3; the proposed delta is complete
certification of `[1.08,10^7]` (and hence the symmetric closed interval), with
a replayable directed-rounding certificate and proved terminal-scale error.

No `literature/*handoff*.md` files were present at triage time.

## Cheapest feasibility probe

`evidence/triage_valley_probe.py` was run with python-flint 0.9.0 at 256-bit
precision and recursion depth 120.  Using only the functional equation and the
rigorous support bound `supp(mu) subset [0,2/3]`, it certified:

- at `x=6580077.19160276`,
  `|F(x)| = [7.4405748550999934e-11 +/- 6.92e-28]` and
  `|q(x)| = [4.0667417888497602e-7 +/- 5.55e-24]`; the Lipschitz bound
  certifies `F != 0` for `|t-x| <= 1e-11`;
- at `x=5065070.60771886`,
  `|F(x)| = [3.3299030407100328e-11 +/- 3.24e-28]` and
  `|q(x)| = [4.4338980224214795e-7 +/- 4.29e-24]`; it certifies `F != 0`
  for `|t-x| <= 5e-12`.

These are rigorous but microscopic local checks around the exact printed
decimals.  They neither certify the complete source refinement cells nor any
substantial portion of `[1.08,10^7]`; they are evidence that an available
directed-rounding implementation can resolve values at the hardest reported
locations without losing all precision.

