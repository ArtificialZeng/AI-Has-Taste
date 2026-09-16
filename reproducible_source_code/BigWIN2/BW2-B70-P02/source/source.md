# win-00070-p02 — A certified zero-free interval for the golden-mean Fourier transform

## Immutable primary-source record

- Primary source: Yi-Qiu Mao and Zhi-Yi Wu, *On the spectrality of the non-homogeneous golden-mean self-similar measure*, arXiv:2609.04701v1 [math.CA], 4 September 2026.
- Official abstract: <https://arxiv.org/abs/2609.04701v1>.
- Official HTML: <https://arxiv.org/html/2609.04701v1>.
- Parameters and recurrence: HTML 60–84 and 231–260; rigorous baseline: Proposition 3.3, HTML 297–360; numerical scan: §4.3, HTML 562–589; explicit non-proof/future-work statement: HTML 590.
- Access record: official arXiv HTML was read directly on 2026-09-08. The official PDF is archived as batch material.

## Frozen assertion

Let \(\mu=\mu^p_{1/2,1/4}\) be the self-similar probability measure determined by
\[
\mu(E)=p\,\mu((x\mapsto x/2)^{-1}E)
 +(1-p)\,\mu((x\mapsto(x+2)/4)^{-1}E),
\]
where
\[
p=2^{-\log_2\varphi}=\frac{\sqrt5-1}{2},
\qquad 1-p=p^2,
\qquad \varphi=\frac{1+\sqrt5}{2}.
\]
For
\[
F(\xi)=\widehat\mu(\xi)=\int e^{-2\pi i\xi x}\,d\mu(x),
\]
prove or disprove
\[
F(\xi)\ne0\qquad\text{for every real }|\xi|\le10^7.
\]

An acceptable proof may be computer-assisted only if it emits a deterministic, independently replayable certificate with directed rounding and a proved truncation/tail bound. One exact real zero, isolated away from numerical error, disproves the statement.

## Nearest result and precise delta

Proposition 3.3 proves zero-freeness only on \([-1.08,1.08]\). The source then scans \([1,10^7]\) in double precision and reports no zero, with the ten deepest valleys listed in Table 1. Its final Remark explicitly says the computation is not a formal proof and that rigorous verification would require a computer-assisted proof.

The delta is exactly to certify the finite interval already investigated by the source. It does not assert \(F\) is zero-free on all of \(\mathbb R\), and it does not by itself prove non-spectrality.

## Cheapest decisive attack

Use the exact functional equation
\[
F(\xi)=pF(\xi/2)+p^2e^{-\pi i\xi}F(\xi/4)
\]
and its \(2\times2\) matrix product. First perform a go/no-go calculation with at least 128-bit ball arithmetic on neighborhoods of the two smallest reported \(|q|\) valleys,
\(6580077.19160276\) and \(5065070.60771886\). Prove an enclosure that separates \(F\) from zero there.

If that succeeds, cover \([1.08,10^7]\) by adaptive rational intervals. For each leaf interval, certify that either the enclosure of \(\Re F\) or of \(\Im F\) excludes 0, using rigorous Taylor models or complex balls, the finite matrix recursion, and a uniform analytic tail bound. Store the covering tree, arithmetic precision, library/version, rounding mode, and a small independent verifier. Symmetry \(F(-\xi)=\overline{F(\xi)}\) then covers the negative half.

## Failure risks

- Double precision, sampled grids, quadratic interpolation, and plots are not proofs.
- An interval evaluation that overestimates through dependency may fail to separate zero; this is an algorithmic limitation, not evidence of a zero.
- The denominator in the Riccati quotient must be certified nonzero before using \(q=F(\xi)/F(\xi/2)\).
- The source's empirical third-derivative bound and empirical lower bound for \(|F|\) cannot be imported as rigorous constants.
- A certificate covering fewer than all points of \([1.08,10^7]\) is only a bounded partial result.

## Semantic boundary

No registry entry was found for arXiv:2609.04701 or the golden-mean Fourier transform. The project is a finite rigorous upgrade of a source-stated numerical observation, not a renamed form of another spectral-measure project.
