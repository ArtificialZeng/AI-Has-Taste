# Five-cycle colored Gaussian model: first odd MLT cell

## Immutable source statement

Let (G_5) be the colored cycle on vertex set ℕ/5ℕ, with edges {(i,i+1)} modulo 5. All five vertices have one common vertex color, and the five edges have pairwise distinct colors. Determine whether

\[
\operatorname{mlt}(G_5)=1.
\]

Here `mlt` is the maximum-likelihood threshold of the colored Gaussian graphical model in Definition 2.13 of the source. Equivalently, using Theorem 3.4 and the notation of the source, prove that for Lebesgue-almost-every (x\in\mathbb R^5) there is no nonzero matrix (K\in L_{G_5}\cap\operatorname{PSD}(5)) with (Kx=0), or disprove this by an exact positive-measure obstruction.

## Quantifiers and scope

- The graph and coloring are fixed exactly as above.
- The claim is an almost-everywhere statement over real (x\in\mathbb R^5), not merely a finite or floating-point observation.
- A disproof must establish failure on a positive-measure set; one isolated exceptional vector does not refute an almost-sure assertion.
- The edge-color condition is explicit. Conjecture 3.27 abbreviates it, but it immediately follows Proposition 3.26, whose family has all edges differently colored.

## Primary source and nearest result

- Kaie Kubjas and Olga Kuznetsova, *Colored Gaussian Graphical Models: Maximum Likelihood Thresholds, Algebraic Geometry, and Persistent Homology*, arXiv:2609.02382v1 (2026), https://arxiv.org/abs/2609.02382.
- Local primary PDF: `batches/inbox/bigWin-55-materials/2609.02382.pdf`.
- SHA-256: `29727f7143ce6a7a92cf15dc80882e74590b7a3de66c42b50c31a4d94737e48d`.
- Locators: Definition 2.13, PDF p.5; Theorem 3.4, PDF p.7; Proposition 3.25 and Proposition 3.26, PDF pp.12–13; Conjecture 3.27, PDF p.13.
- Nearest theorem: Proposition 3.26 proves `gcr(G)=2` for this all-distinct-edge family and proves `mlt(G)=1` when the cycle length is even. Proposition 3.25 proves only `wmlt(G)=1`. The source reports computational support, not a proof, for odd length.

## Proposed contribution boundary

Resolve only the first untreated odd case (m=5). Do not report a theorem for every odd cycle unless a complete proof genuinely supports that stronger quantifier. A useful exact partial result may instead isolate and prove the decisive semialgebraic criterion for (m=5), provided a fresh referee accepts its mathematical value.

## Cheapest decisive test and certificates

Write the generic (5\times6) linear kernel system for the six color parameters, eliminate symbolically, and determine whether its nonzero solutions can be positive semidefinite on a positive-measure set of (x). Acceptable evidence includes exact maximal minors, exact principal-minor inequalities, a CAD or equivalent exact semialgebraic decomposition with replay instructions, and adversarial tests of degenerate strata. A fast disproof route is a rational transverse pair ((x,K)) with (K\succeq0), (Kx=0), and positive definiteness on (x^\perp), together with the argument that the obstruction persists on an open set.

## Provenance

Prepared on 2026-09-07 from the primary arXiv PDF during the authorized primary-literature fallback because the confirmed Chrome target tab could not be attached. This file freezes the statement; later mathematical clarification must be recorded separately and must not silently weaken it.
