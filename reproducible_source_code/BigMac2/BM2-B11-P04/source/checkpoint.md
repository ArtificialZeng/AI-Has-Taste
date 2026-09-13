# Checkpoint

## Research-pass result

- Research job: `bigMac-00011-p04-research-5c12a1076ce8`.
- `source.md` remains byte-for-byte unchanged, with SHA-256
  `20d6e08ccd3dccfb2c3b6ddee861164a4968fef522bebf968feaa334ff2bbc4f`.
- The full exact derivation is in `evidence/rederivation.md`; its deterministic
  algebra/rational checks are in `evidence/verify_symbolic.py`. Running
  `python evidence/verify_symbolic.py` returned
  `all exact symbolic and rational checks passed` under SymPy 1.13.3.

## Decisive evidence

Put \(x=\sqrt p\), \(A=x\cosh x-\sinh x\), and
\(B=A+q\sinh x\). Substituting source equation (57) into (D6) and (D8),
after commuting the finite volume average with parameter differentiation,
gives exact formulas for all five raw moments and simplifies to

\[
 \operatorname{Cov}(T,L)=
 \frac{3\{\xi_1(p)+q\xi_2(p)\}}{4x^6B^2}.
\]

Here \(A>0\), \(B>0\), \(\xi_1=4x^2A^2>0\), while exact coefficient
collection gives

\[
 \xi_2(x^2)=-\sum_{n\ge5}
 \frac{2^{2n-3}(2n-1)(2n-6)(2n-8)}{(2n)!}x^{2n}<0.
\]

Consequently the complete zero set in the positive quadrant is the analytic
graph \(q=q_0(p)=-\xi_1(p)/\xi_2(p)\). The covariance is positive below,
zero on, and negative above this graph. Both variances are finite because
\(T\le\delta\) and \(L\le\widehat\ell\), and strictly positive because each
variable is proved nonconstant in `evidence/rederivation.md`; hence the
Pearson-correlation sign equivalence is valid everywhere in the open quadrant.

An exact counterexample is \((p,q)=(1,200)\). Writing \(y=e^2\), its numerator
satisfies \(2yN=8-200(y^2-4y-25)\). The positive exponential series proves
\(y>7389/1000\), and monotonicity gives
\(y^2-4y-25>41321/10^6>1/25\), so \(N<0\) exactly. The frozen universal
positivity assertion is therefore disproved.

## Obstacles and next test

No mathematical gap is presently known. No broad novelty claim is made; the
nearest source remains the frozen 2026 preprint identified in `problem.md`.
One initial all-at-once `trigsimp` check was computationally slow; factoring
the same exact identity first completed in 1.6 seconds and changed no claim.

**Completed referee test:** a fresh referee independently differentiated (57),
verified the five moment formulas and covariance identity (5), rederived the
general Taylor coefficient in (8), and checked the strict-variance and exact
\((1,200)\) witness arguments against the frozen probability space.

## Referee and manuscript

- The fresh audit in audit/math.md accepted the full resolution-paper scope at
  snapshot digest
  7032172b209dfedee38fe1c802525ed47d607bca80262387017f426f5113d081.
- Writing job bigMac-00011-p04-write-ef336393b8b2 produced
  manuscript/main.tex, manuscript/references.bib, and the four-page draft
  manuscript/main.pdf.
- The manuscript freeze gate passed: manuscript digest
  84002f0977d6ab3eb4b3635f035a9c7abe45a768b9353d1b0f705a3199bbb1d8
  and PDF digest
  35665e8331dce8129d62ea8b66c88da8669115f5e094b2613c38294004b646df.
- Clean build command: cd manuscript && latexmk -pdf
  -interaction=nonstopmode -halt-on-error main.tex. The final log has no
  undefined citation/reference, overfull box, package warning, or LaTeX
  warning. All PDF fonts are embedded, and all four rendered pages were
  visually inspected.
- Both exact verification scripts pass. The immutable source.md still has
  SHA-256 20d6e08ccd3dccfb2c3b6ddee861164a4968fef522bebf968feaa334ff2bbc4f.
- Ye's metadata was checked against the official arXiv record. The single
  genuinely relevant entry available in literature/user_bibliography_check.md
  is cited only for its delimited methodological parallel; the manuscript
  explicitly says it supplies no diffusion-specific support.

## Release audit

- Release job `bigMac-00011-p04-release-0ac2fee38be9` completed fresh
  citation, build, and rendered-page reviews bound to the frozen manuscript
  and PDF digests above.
- Ye's metadata, model normalization, Appendix-F formulas, and explored-range
  positivity statement were verified against the official arXiv record and
  full HTML. The Zeng paper's registered metadata and narrow abstract-level
  methodological relevance were verified; its newly deposited SSRN landing
  page and full text were not directly accessible in this fresh context, so
  `audit/citations.json` records the permitted citation-access limitation.
- The existing nonempty build log is warning-free and digest-bound. All fonts
  are embedded, text extraction is nonempty, and pages 1--4 were rendered and
  visually inspected without clipping, overlap, or illegibility.
- `source.md` remains unchanged at SHA-256
  `20d6e08ccd3dccfb2c3b6ddee861164a4968fef522bebf968feaa334ff2bbc4f`.

No mathematical, build, or visual obstacle remains; no broad priority claim is
made.

**Next test:** the supervisor should run `release_gate.py publish` on the
project after the fresh release gate check succeeds.
