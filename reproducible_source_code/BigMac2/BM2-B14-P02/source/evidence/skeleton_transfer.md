# Pathwise refresh-skeleton transfer

## Statement proved

Assume the hypotheses and notation frozen in `source.md` and `problem.md`.
In particular, fix one \(\rho\in[0,1)\), put \(q=1-\rho>0\), take iid
\(Y_0,Y_1,\ldots\sim\pi\) independently of iid
\(B_1,B_2,\ldots\sim\operatorname{Bernoulli}(q)\), and set
\[
 M_n=\sum_{t=1}^n B_t,\qquad X_n=Y_{M_n}.
\]
For the loop-deleted directed and undirected simple graphs, normalized by the
observed range, all four fixed-degree limits and all four iterated asymptotics
in `problem.md` hold almost surely. In particular, no factor depending on
\(\rho\) remains.

## Source theorem used

For an iid sample of length \(N\) from \(\pi\), write
\(\widehat r^{\to}_{N,k},\widehat r^{\mathrm u}_{N,k}\) and
\(\widehat r^{\to}_{N,k+},\widehat r^{\mathrm u}_{N,k+}\) for the four
loop-deleted degree statistics, each divided by the iid observed range.
Proposition 2 of the designated Xie--Zhou source gives, for every fixed
\(k\ge1\), almost surely,
\[
 \widehat r^{a}_{N,k}\longrightarrow r_k^a,
 \qquad
 \widehat r^{a}_{N,k+}\longrightarrow r_{k+}^a
 \quad(N\to\infty),\qquad a\in\{\to,\mathrm u\}.
\]
Theorem 1 of that source gives
\[
 r_{k+}^{\to}\sim\pi_k^\gamma,\qquad
 r_{k+}^{\mathrm u}\sim2^\gamma\pi_k^\gamma,
 \qquad
 r_k^{\to}\sim\frac{\pi_k^\gamma}{k},\qquad
 r_k^{\mathrm u}\sim\frac{2^\gamma\pi_k^\gamma}{k}.
\]
These are precisely the deterministic limits defined in `problem.md`.

## Lemma (exact skeleton identity)

For every realization and every integer \(n\ge0\), put
\(N_n=M_n+1\). The vertex set and both loop-deleted edge sets of the
sticky-refresh sample through clock time \(n\) equal those of the iid sample
\(Y_0,\ldots,Y_{N_n-1}\):
\[
 V_n=\{Y_0,\ldots,Y_{M_n}\},
\]
\[
 E_n^{\to}
 =\{(Y_{j-1},Y_j):1\le j\le M_n,\ Y_{j-1}\ne Y_j\},
\]
\[
 E_n^{\mathrm u}
 =\{\{Y_{j-1},Y_j\}:1\le j\le M_n,\ Y_{j-1}\ne Y_j\}.
\]

**Proof.** If \(B_t=0\), then \(M_t=M_{t-1}\), so
\((X_{t-1},X_t)\) is a self-loop and is deleted. If \(B_t=1\) and this
is the \(j\)-th refresh, then \(M_{t-1}=j-1\), \(M_t=j\), and the clock
transition is \((Y_{j-1},Y_j)\). As \(t\) runs through the refresh times
up to \(n\), \(j\) runs once through \(1,\ldots,M_n\). A refresh that
redraws the same label produces a self-loop on both sides and is deleted on
both sides. Finally, because \(M_t\) starts at zero and increases one at a
time, the clock sample has visited exactly the displayed skeleton labels.
Suppressing repeated edges therefore gives the asserted set identities. \(\square\)

Consequently every vertex has exactly the same directed and undirected
loop-deleted degree in the two graphs, and their range denominators are
identical. There is one convention to check in the directed source statistic:
its numerator ranges over the labels seen before the final iid observation,
whereas `problem.md` ranges over the full vertex set. If the final skeleton
label was seen before, it already belongs to the source's numerator domain.
If it is new, it has no outgoing transition and hence out-degree zero. Thus
for every \(k\ge1\), both the degree-\(k\) and degree-at-least-\(k\) directed
numerators agree exactly. Hence, pathwise,
\[
 r_{n,k}^{\rho,a}=\widehat r_{N_n,k}^{a},\qquad
 r_{n,k+}^{\rho,a}=\widehat r_{N_n,k+}^{a},
 \quad a\in\{\to,\mathrm u\},\quad k\ge1.
\]

## Transfer along the random sample size

By the strong law,
\[
 \frac{M_n}{n}\longrightarrow q>0
 \quad\text{almost surely},
\]
so \(N_n=M_n+1\to\infty\) almost surely. Take the countable intersection
over \(k\ge1\) and the four source convergence events; it still has
probability one. On its intersection with the preceding strong-law event,
ordinary pathwise convergence along the integer subsequence \(N_n\) gives,
simultaneously for every fixed \(k\ge1\),
\[
 r_{n,k}^{\rho,\to}\to r_k^{\to},\qquad
 r_{n,k}^{\rho,\mathrm u}\to r_k^{\mathrm u},
\]
\[
 r_{n,k+}^{\rho,\to}\to r_{k+}^{\to},\qquad
 r_{n,k+}^{\rho,\mathrm u}\to r_{k+}^{\mathrm u}.
\]
This is a pathwise subsequence argument; independence between \(N_n\) and
the iid-limit event is not needed (although it is available in the stated
construction).

Only after these inner limits have been taken, the source asymptotics give
the four requested ratios explicitly:
\[
 \lim_{k\to\infty}
 \frac{\displaystyle\lim_{n\to\infty}r_{n,k+}^{\rho,\to}}
      {\pi_k^\gamma}=1,
 \qquad
 \lim_{k\to\infty}
 \frac{\displaystyle\lim_{n\to\infty}r_{n,k+}^{\rho,\mathrm u}}
      {2^\gamma\pi_k^\gamma}=1,
\]
\[
 \lim_{k\to\infty}
 \frac{\displaystyle\lim_{n\to\infty}r_{n,k}^{\rho,\to}}
      {\pi_k^\gamma/k}=1,
 \qquad
 \lim_{k\to\infty}
 \frac{\displaystyle\lim_{n\to\infty}r_{n,k}^{\rho,\mathrm u}}
      {2^\gamma\pi_k^\gamma/k}=1.
\]
It follows as well that the undirected-to-directed amplitude ratio tends to
\(2^\gamma\) for both tails and local masses. Since
\(\pi_k^\gamma/k\in RV_{-2}\), the two local limiting laws have exponent
two. No simultaneous \(k=k(n)\) limit and no uniformity in
\(\rho\uparrow1\) has been used or asserted.

## Audit conclusion

The exact graph identity handles both types of self-loop (a non-refresh and a
refresh that repeats its label), the directed terminal vertex, the observed
range normalization, and all four positive-degree statistics. The random
index diverges for every fixed \(\rho<1\), so the source's full-sequence iid
limits transfer without a rate estimate or an interchange of limits. No
mathematical gap relative to the frozen claim is known. External novelty is
not asserted and remains a separate literature question.
