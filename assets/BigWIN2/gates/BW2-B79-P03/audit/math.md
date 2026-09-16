# Fresh mathematical referee report

## Verdict

**Accept.** The frozen `resolution-paper` claim is correct at its stated scope. It proves both parts of the immutable assertion: the explicit family satisfies the relevant source-side parameter and BDD promises for all sufficiently large (n), and the stated (N=n^8) covariance test separates its joint sample law from every fixed legal discrete-MIMO law with the claimed uniform negligible error bound. No weakening of the original family or of its quantifiers is needed.

I reviewed the exact statement in `claim.json`, the immutable statement and interpretation, the proof in `evidence/finite_sample_separator.md`, and the cited Dean--Goldsmith and Li PDFs. The hashes of all frozen inputs agree with `audit/snapshot.json` (digest `71cb4c86fc33451424485a0b8d9495aa4e425cf029d346856d6018b998017a51`).

## Reconstruction of the source promises and sample law

For (L=A=I_n), the lattice and its dual are both (mathbb Z^n), (lambda_1(L)=1), and the least eigenvalue parameter in Dean--Goldsmith Lemma 7 is (1). Dean--Goldsmith Claim 2 gives

\[
\eta_{2^{-n}}(\mathbb Z^n)\leq \sqrt n,
\]

so (r=n^2>\sqrt2\eta_{2^{-n}}(L)) eventually (indeed for (n\geq2)). The other main parameter inequality is

\[
\frac{m\alpha}{k^2}=\frac{3n^5/2}{n^4}=\frac32n>\sqrt n.
\]

The imposed lower bound on (M) is the source's constellation-size bound and implies (M\geq2) eventually. Also (0<\alpha=1/2<1), (k,r,m>0), the independent error after the scaling in Equation (19) has scale (k\alpha/r=1/2\leq\alpha), and (\|\delta\|=1/4<r). The exact discrete Gaussian required here is also efficiently samplable for this explicit orthogonal lattice; in particular, its width (r=n^2) is well above the large-width sampling regime invoked by Claim 1.

With (F(n)=2^{n\log\log n/\log n}), one has (F(n)/n^C\to\infty) for every fixed (C). Hence the Lemma 7 distance ceiling becomes

\[
\frac{M\alpha}{k^2r\sqrt2}=\frac{M}{2\sqrt2\,n^6}
  >\frac{3}{2\sqrt2}\frac{F(n)}n\longrightarrow\infty.
\]

Thus (d_0=3/8) is below that ceiling for all sufficiently large (n). The target (y=2M\mathbf1+e_1/4) lies at distance (1/4<d_0) from (c=2M\mathbf1\in\mathbb Z^n). Coordinatewise nearest-integer inspection shows that (c) is the unique closest lattice vector, consistently with (d_0<\lambda_1(L)/2=1/2).

Finally, substituting (A=I_n) and (k=r=n^2) into Dean--Goldsmith Equation (19) gives exactly

\[
a=v\sim D_{\mathbb Z^n,n^2},\qquad
b=2\sum_{j=1}^n a_j+\frac{a_1}{4M}+e,
\quad e\sim\nu_{1/2}.
\]

Thus the proof audits the actual frozen constructor rather than a modified distribution. The fact that (c\notin[0,M)^n) and that the offset is nonzero is the intended source mismatch, not a failure of the BDD input promises.

## Independent check of the finite-sample argument

Let (Z\sim D_{\mathbb Z,r}), (r=n^2), and (V=\mathbb E Z^2). Completing the square and applying Poisson summation shows

\[
\mathbb E e^{tZ}\leq e^{r^2t^2/(4\pi)},
\qquad
\Pr(|Z|>u)\leq2e^{-\pi u^2/r^2}.
\]

The elementary mass count on the integers with (r/2\leq |z|\leq r), together with (\rho_r(\mathbb Z)\leq1+r\leq2r), gives the stated lower bound

\[
V\geq e^{-\pi}r^2/8.
\]

These estimates validate the truncation calculation used for the empirical covariance. With (T=rn), (N=n^8), and

\[
C=N^{-1}\sum_{i=1}^N a_i a_i^T,
\]

the coordinate tail union bound is (2n^9e^{-\pi n^2}). The truncation bias is at most (6r^2n^2e^{-\pi n^2}\leq V/(100n)) for (n\geq3). Hoeffding's inequality at deviation (V/(100n)), followed by a union bound over the (n^2) entries, gives the second term

\[
2n^2\exp\!\left(-e^{-2\pi}n^2/1{,}280{,}000\right).
\]

Every entry of (C-VI_n) is consequently at most (V/(50n)) in absolute value. Since this matrix is symmetric, its operator norm is at most its maximum absolute row sum, hence at most (V/50). This checks both the constants and the passage from entrywise control to the event used later.

Write (\mathbf1=(1,\ldots,1)^T), (X_i=\langle a_i,\mathbf1\rangle), and (D=\sum_iX_i^2=N\mathbf1^TC\mathbf1). On the covariance event,

\[
D\geq(49/50)NVn>0,
\]

so the proof never divides by an uncontrolled random denominator. For a legal secret (t=s/M\in[0,1)^n), the noiseless empirical slope obeys, simultaneously for all such (t),

\[
R_Q=\frac{\mathbf1^TCt}{\mathbf1^TC\mathbf1}
\leq\frac{51}{49}.
\]

For the constructed law,

\[
R_P=2+\frac1{4M}\frac{\mathbf1^TCe_1}{\mathbf1^TC\mathbf1},
\]

and operator-norm control gives

\[
\left|\frac{\mathbf1^TCe_1}{\mathbf1^TC\mathbf1}\right|
\leq\frac{50+\sqrt n}{49n}\leq1,
\]

whence (R_P\geq7/4). Thus both hypotheses have a deterministic margin at least (1/4) from the threshold (3/2) on the same public-sample event.

Conditional on the public samples, the noise contribution to the slope is exactly Gaussian with variance (\gamma^2/(2\pi D)), with (0<\gamma\leq1/2) under either hypothesis. A two-sided Gaussian bound at distance (1/4) is therefore at most

\[
2e^{-\pi D/4}
\leq2\exp\!\left(-49\pi e^{-\pi}n^{13}/1600\right).
\]

Adding the covariance-event failure probability yields exactly the three-term error bound in `claim.json`. Each term is negligible. The estimate is independent of the admissible (M), simultaneous over the full constellation through (\|s/M\|_2\leq\sqrt n), and monotone in every (0<\beta\leq1/2). The stipulated (D=0) convention is correct for every legal sample set and, for the constructed law, (D=0) is already contained in the covariance failure event. This resolves the zero-denominator, composite-hypothesis, and uniformity issues explicitly.

## Source comparison, attacks, and scope

Dean--Goldsmith Definition/Equation (14) and Lemma 7/Equation (19) support the normalization used above. Li Proposition 5.1 establishes only exact non-membership in the legal discrete-MIMO family when the coefficient is outside the constellation or the offset is nonzero. Li Remark 5.3 expressly leaves statistical detectability dependent on the instance and observes that a large (M) does not suppress the coefficient-reduction term. The frozen result supplies the missing stronger statement for one fully explicit admissible family: a single polynomial-time, polynomial-sample test with a constant population separation and uniform negligible finite-sample error.

I specifically attacked the arbitrary-(M) quantifier, secrets on the constellation boundary, (\beta\downarrow0), the unbounded discrete-Gaussian coordinates, empirical cross-covariances, a possibly zero or small denominator, a negative constructed correction term, and the distinction between ratios of expectations and the empirical ratio. The covariance event and conditional-noise calculation cover all of these cases. The proof does not infer a general MIMO attack or repair the invalid general reduction, and the claim makes neither assertion. It also uses the limited source comparison honestly rather than asserting priority.

There are no unresolved mathematical gaps within the frozen scope. The finite cutoff at which the distance ceiling exceeds (3/8) need not be numerically optimized because the claim is explicitly asymptotic. The contribution is a complete resolution of the immutable explicit-family assertion, not merely Li's exact-distribution mismatch.
