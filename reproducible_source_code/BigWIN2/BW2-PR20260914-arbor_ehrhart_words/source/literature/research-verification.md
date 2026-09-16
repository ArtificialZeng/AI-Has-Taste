# Research-pass literature and scope check

Date: 2026-09-14 (UTC). Job:
`primary-20260914-arbor-ehrhart-words-research-9e9070b093b6`.
The only enumerated handoff was `literature/outer-intake-handoff.md`.
Its mathematical leads were independently checked as below. This file
records bounded comparison, not an exhaustive priority or open-status claim.

## Decisive primary sources

1. Athanasiadis, Xiao and Yan,
   [Lattice point enumeration of some arbor polytopes, v1](https://arxiv.org/html/2603.11654v1).
   The introduction defines exactly the descendant-union inequalities of
   `source.md`. Theorem 1.5 is the singleton-leaf octopus case. Section 4
   obtains its binomial-content formula and uses the multiset-word generating
   function. Conjecture 5.2, printed p.13, is exactly the frozen all-arbor
   statement. Its adjacent paragraph says even the linear-arbor case of
   this statistic was unclear there. I read the corresponding local PDF
   page again with `pdftotext -f 13 -l 13`, and checked matching live HTML.
   The live abstract-page history still lists only v1 (12 March 2026).
   Full copied primary PDF: `evidence/external/2603.11654v1.pdf`; its existing
   extracted text is `evidence/external/2603.11654v1.txt`.

2. Athanasiadis and Chapoton,
   [Polytopes and posets associated to preorders, v1](https://arxiv.org/html/2605.26916v1).
   Conjecture 4.4, p.12, extends the target to preorders; it reports tests
   through size 7. Proposition 4.5, pp.12–13, assumes a minimum vertex and
   uses modified ascents with an initial sentinel. Remark 7.3, p.19,
   explicitly supplies the binomial-sum reformulation conditional on the
   conjecture. These passages were checked in the local text and live HTML.
   Its Theorem 1.5 is Ehrhart–zeta duality, a distinct already proved formula.
   The live history lists only v1 (26 May 2026).
   Full copied primary PDF: `evidence/external/2605.26916v1.pdf`; text:
   `evidence/external/2605.26916v1.txt`.

## Additional primary comparisons

- Chapoton,
  [On posets and polytopes attached to arbors, v2](https://arxiv.org/html/2503.04247v2),
  Lemma 1.2 and Section 2.1, especially Proposition 2.1, equation (8).
  The height-counting F recurrence is already present. With his root size
  r=b and child coefficient W_s=r_s, equation (8) is precisely our upper
  truncation recurrence (F). Neither that recurrence nor the elementary
  Vandermonde identity is claimed as a new contribution. The inspected
  statement and proof compute F; they do not identify it with the weighted
  lower-truncation G polynomial of research-proof.md. Appendix B's two
  displayed summation lemmas were also screened, without a full-paper audit.

- Athanasiadis,
  [Lattice point enumeration of polytopes associated to integer compositions, v3](https://arxiv.org/html/2510.23903v3),
  Theorem 1.3, Section 4, and Proposition 4.2, equation (15). Its statistic
  counts strict ascents with w_0=1. This is the known linear-arbor
  interpretation cited by May Proposition 4.5, not a stated proof of the
  ordinary non-descent identity. I first inspected v1, where this result is
  Proposition 3.2, then checked the live history and v3 (24 January 2026).

- Liu and Tang,
  [Proofs of four generating function conjectures for arbor polytopes, v1](https://arxiv.org/html/2605.08968v1),
  introduction's definition before Figure 2 and Theorem 3.1 with its first
  proof. The family has a singleton root and singleton leaves. The four
  formulas concern that family and reuse Chapoton's height recurrence;
  they do not state the full-arbor Ehrhart–word identity.

- Dai et al.,
  [Counting Lattice Points in Minkowski Sums of Cross Polytopes, v2](https://arxiv.org/html/2608.16037v2),
  introduction, Theorems 1.2/1.3, and paragraph identifying their consequence
  as May Conjecture 5.4. The support enumerator is the h-star polynomial
  of a different root polytope. This proves support duality, not our
  counting-series identity. Existing primary HTML copy:
  `evidence/external/2608.16037v2.html`.

- Xue Yan,
  [Variations of colored multiset Eulerian polynomials and applications, v2](https://arxiv.org/html/2608.15682v2),
  Corollaries 5.1–5.4 and definitions in Sections 5.2–5.3. Corollary 5.3
  recovers the known modified-ascent composition formula. Corollary 5.4
  concerns R_tau=Q_tau+Delta-1, with an auxiliary letter and a sentinel;
  its binomial factors also differ. It does not state our formula for
  Q_tau. The history was checked after initially reading v1; v2 is dated
  20 August 2026. This is a newly inspected nearby lead in this pass.

- Menon,
  [Gamma-positivity for octopuses: a bijective proof, v1](https://arxiv.org/html/2608.13247v1),
  introduction and Proposition 3.4. Its polynomial counts support sizes of
  undilated lattice points, including lopsided octopuses. This is another
  newly inspected neighboring result with a different predicate.

## What is and is not claimed

The proposed contribution is the polynomial intertwining
G_v(y)=y^{N_v}(1+y)^{mN_v}F_v((1+y)^{-1}) at every subtree, and its proof
of the all-arbor binomial formula and hence March Conjecture 5.2. The
recursion, binomial-sum reformulation, multiset-word identity, octopus theorem,
and modified-ascent interpretations receive no novelty claim.

Live searches included exact identifiers with conjecture/proof terms,
"arbor polytopes" with "non-descents", "arbor" with "Ehrhart" and
"truncation", and the cited-paper titles. Many broad results were irrelevant;
aggregator snippets were discovery leads only. No equivalent proof was
found in the primary passages inspected on this date. Uninspected portions,
unindexed work, and subsequent versions remain outside this comparison.

The two supplied Excel entries in `literature/intake-dedup.json`
(`legacy-b08-p02` and `win2::legacy-b08-p02`) were read in full. They are
copies of a support-real-rootedness target. The three supplied registry
neighbors concern support factorization, inversion, or a support exponential
formula. Their displayed predicates differ from the present theorem.
I did not independently scan the full 2,883/701 databases or a live
conversation registry, and make no such deduplication claim.

Shell downloads of five additional comparator PDFs failed with
`Operation not permitted`; the browser supplied their primary HTML for
the comparisons above. No unavailable PDF is listed as an existing file.
The decisive March/May primary PDFs and texts were already copied inside
`evidence/external/`, checked locally, and are included in the candidate
evidence. The download failure has no mathematical implication.
