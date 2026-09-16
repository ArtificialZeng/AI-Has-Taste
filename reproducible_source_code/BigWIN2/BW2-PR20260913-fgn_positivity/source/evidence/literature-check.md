# Triage source and duplication check

Retrieval/inspection date: 2026-09-13, Asia/Shanghai.
Job: primary-20260913-fgn-positivity-triage-00acd6d3f130.

## Primary source inspection

1. Mishura, Ralchenko and Schilling, *Analytical and Computational Problems
Related to Fractional Gaussian Noise*, arXiv:2209.02501v1, 2022;
https://arxiv.org/pdf/2209.02501v1 and https://arxiv.org/abs/2209.02501.
Inspected the conjecture and system at printed pp.2–4, the n=3/n=4 passages
at pp.7–10, and Proposition 2.17 at pp.13–14. Conjecture (A) is exactly
one-sided finite predictor positivity. Proposition 2.11 establishes the
n=4 outer coefficient signs/order; Remark 2.12 gives only numerical support
for the middle sign. Proposition 2.17's last weighted-sum implication needs
an additional sign argument for an unconditional all-n conclusion; see
triage-math.md. This does not establish falsity of its statement.

Local bytes: literature/fgn-2022-analytical.pdf, copied unchanged to
evidence/external/fgn-2022-analytical.pdf. SHA256:
dd8610375cc3dffe0d10872c6ad8c061a9dd5c89c273d73ca196d393c7642b2f.
Relevant extracts: 2022-pp7-10.txt and 2022-pp13-15.txt.

2. Bodnarchuk, Mishura and Ralchenko, *Fractional Gaussian Noise: Projections,
Prediction, Norms*, Fractal Fract. 9 (2025), 428;
https://doi.org/10.3390/fractalfract9070428,
https://osuva.uwasa.fi/bitstreams/ba17e604-877b-4de0-b940-2ac4cae74a92/download,
and preprint metadata https://arxiv.org/abs/2408.09188.
Inspected printed pp.3–8 of the retained journal PDF. Conjecture 3 repeats
the universal assertion. Equation (8) is the six-term exponential sum.
Proposition 1, pp.5–6, states its positivity: Step 1 treats H<H0,
Step 2 an unspecified neighborhood of 1, and Step 3 invokes a graph for
the full interval. The authors explicitly say overlap of the analytic
intervals was not established. Proposition 2 proves next-last positivity
conditionally on all coefficients of the previous row being positive.
Remark 4, p.8, specifically identifies Gamma_5^4 as the next analytic difficulty.

Local bytes: literature/fgn-2025-projections.pdf, copied unchanged to
evidence/external/fgn-2025-projections.pdf. SHA256:
1a8f2eaf5f1e8be7830a6630ea9172d87543f1576542d0aa5cbbe3ca4072790f.
Relevant extract: 2025-pp3-8.txt. Direct journal-page opening returned an
access error/429; the complete supplied primary PDF was readable and
search-indexed journal text independently agreed with the inspected passage.

3. Chunhao Cai, *Second-order PACF asymptotics and discrimination between
fractional Gaussian noise and FARIMA(0,d,0)*, arXiv:2605.31416v1;
https://arxiv.org/html/2605.31416v1.
Inspected the introduction and main theorem statements 2.1–2.3 in live
primary HTML. They concern the asymptotic partial autocorrelation coefficient
and its second-order difference from FARIMA, not all finite predictor
coefficients. In particular the inspected statements do not settle this
source claim or the n=5 penultimate sign. No audit of that paper's proofs
was undertaken, and it is not a dependency of the triage algebra.

## Bounded search coverage and limits

Live searches included exact paper titles and combinations of:
`fractional Gaussian noise positivity 2026`,
`fractional Gaussian noise prediction coefficients positive proof`,
`fractional Gaussian noise positivity proof coefficients 2025 2026`,
`fractional Gaussian noise Descartes`, and
`fractional Gaussian noise positivity n = 5`.
No later all-coefficient resolution or equivalent n=5 certificate was located
in the inspected primary material. This is not an exhaustive search or a
priority claim. Source status is open-supported in this bounded sense.

The zero-count lemma is standard. Searches identified G. J. O. Jameson,
*Counting zeros of generalised polynomials: Descartes' rule of signs and
Laguerre's extensions*, Mathematical Gazette 90 (2006), 223–234,
DOI https://doi.org/10.1017/S0025557200179628. Opening the original article
failed; its exact theorem text is therefore not represented as inspected.
The argument in triage-math.md supplies a self-contained proof of the
precise lemma used and claims no novelty for that lemma.

## Handoff and local semantic comparison

Enumerated literature/*handoff*.md: the only match was
literature/outer-intake-handoff.md. Read it, outer-dedup.md, and the four
stored original statements in outer-dedup-full.md. Those concern Gaussian
tail extrema, MIMO sample separation, woven exponentials, and permutation
X-rays. Their objects and quantifiers do not match stationary fGn one-sided
prediction. The 2,883-description historical search remains a supervisor
report; this worker did not rescan those full Excel payloads.

A fresh read-only scan of the live native registry found 652 JSONL records,
SHA256 cd744206df630610e5d419b54780703ee605a7f4f37adf9976e0f36610171ecc.
Searches for fractional Gaussian/Brownian, fGn, Hurst and the two arXiv IDs
returned only this project's own newly added record. Thus the handoff's
650-record snapshot is historical; the own-record match is registration,
not a second research project. Keyword absence alone does not prove semantic
uniqueness. No browser-conversation comparison or worldwide novelty is claimed.

The previous next test has been changed on evidence: the n=4 global sign
now has a short argument, whereas the remaining n=5 cofactor has 18 raw
sign variations. Repeating the n=4 search or assuming its three-zero count
automatically transfers would be uninformative.
