# win-00071-p01 — Real stability for the all-one odd-length 2-bridge family

## Immutable primary-source record

- Primary source: Kotaro Shoji, *On the Mahler measure and root distribution of the Q-polynomial of links*, arXiv:2609.05200v1 [math.GT], 4 September 2026.
- Official abstract: <https://arxiv.org/abs/2609.05200v1>.
- Official PDF: <https://arxiv.org/pdf/2609.05200v1>.
- Definitions: Q-polynomial skein definition on printed p.3; real stable on Definition 4.2, printed p.9.
- Nearest theorem: Proposition 4.3, printed pp.9–11. Source-stated gap: Remark 4.5, printed p.11.
- Access record: official arXiv text and PDF were inspected on 2026-09-08. The PDF is archived as `bigWin-71-materials/2609.05200.pdf`, SHA256 `cb26a6a18b50faf3bfce151a7c760bd6f96a9b1c99ff797c335923dad4dc8610`.

## Frozen assertion

For every positive integer \(n\), let \(L_n\) be the 2-bridge link denoted in Shoji's convention by a continued fraction with exactly \(2n+1\) entries, every entry equal to \(1\). Prove or disprove that its Q-polynomial \(Q_{L_n}(x)\) is real stable: after removal of any Laurent monomial factor, all zeros are real.

The universal quantifier is inherited from the “analogue of Proposition 4.3” wording in Remark 4.5. The statement does not concern arbitrary odd entries, arbitrary signs, or arbitrary 2-bridge links.

## Nearest result and precise delta

Proposition 4.3 proves real stability for the corresponding all-one family with exactly \(2n\) entries. Remark 4.5 reports checks for several small \(n\) in the \(2n+1\)-entry analogue and says a complete proof is not known there.

The proposed delta is exactly that odd-length analogue. A result must audit whether its recurrence and initial data are genuinely different from the even case; a mere relabeling of Proposition 4.3 is not new.

## Cheapest decisive attack

Derive the odd subsequence exactly from the source's skein/transfer recurrence, retaining all initial conditions and Laurent factors. Clear only monomial factors. For \(1\le n\le20\), use exact Sturm sequences to compare the number of real roots with the polynomial degree. In parallel, seek the closed trigonometric form after \(x=2\cos\theta-1\) and a complete sign-interlacing grid analogous to Proposition 4.3.

Any exact Sturm deficit supplies the smallest counterexample and should stop the universal proof route. A proof requires an argument for every \(n\), not numerical roots or finitely many Sturm counts.

## Failure and novelty risks

- Do not confuse the frequency \(2n+1\) appearing inside the even-family trigonometric formula with the number of continued-fraction entries in Remark 4.5.
- The odd-family recurrence may make the result a short nearby corollary. If so, state the exact method/value delta and perform a current literature check before publication.
- Source v1 establishes only that its authors did not supply a proof; it does not establish global novelty by itself.

## Semantic boundary

No registered project used arXiv:2609.05200, this all-one odd-length family, or Q-polynomial real stability. Historical continued-fraction and knot entries, if any, have different invariants and quantifiers.
