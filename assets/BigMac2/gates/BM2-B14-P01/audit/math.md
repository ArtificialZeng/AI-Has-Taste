# Fresh mathematical referee report

Referee job: `bigMac-00014-p01-referee-1b4392cafd87`  
Frozen snapshot: `64359d3012d06c12d1f42fca723c4b98cccde9ccf428bdb15ce924eab88e8b70`

## Scope and input integrity

I reviewed the exact `resolution-paper` claim frozen in `claim.json`, against
the immutable statement in `source.md` and its interpretation in `problem.md`.
I recomputed every SHA-256 entry in `audit/snapshot.json` and its canonical
mapping digest; all entries and the snapshot digest match. The claim addresses
the full loops-allowed binary row/column-sum-two model for every integer
\(N\ge2\), not the zero-diagonal or shifted models.

## Reconstruction of the exact argument

For a fixed matrix \(A\), its row-column bipartite graph is a disjoint union
of even cycles of lengths \(2k\), \(k\ge2\). Each component has exactly two
alternating perfect matchings. Hence, if \(c(A)\) is the number of components,
there are exactly \(2^{c(A)}\) ordered decompositions \(A=P+R\) into disjoint
permutation matrices. With \(Q=P^{-1}R\), disjointness is equivalent to \(Q\)
having no fixed point, and a bipartite component of length \(2k\) gives one
\(k\)-cycle of \(Q\). Thus \(c(Q)=c(A)\).

Let \(Z_N=\sum_{q:c_1(q)=0}2^{-c(q)}\). Choosing \(P\) uniformly and,
independently, \(Q\) with probability \(2^{-c(Q)}/Z_N\), the mass of any
particular \(A\) is
\[
  2^{c(A)}\frac{2^{-c(A)}}{N!Z_N}=\frac1{N!Z_N}.
\]
This proves uniformity directly, rather than assuming the coefficient identity
from the cited representation. It also proves the required normalization.

Conjugating the permutation matrix of \(Q\) puts it into cycle blocks \(C_k\).
Since the eigenvalues of \(C_k\) are the \(k\)-th roots of unity,
\(\det(I+C_k)=1-(-1)^k\). Because \(P\) is invertible,
\(A=P(I+Q)\) is invertible exactly when all cycles of \(Q\) are odd. Under the
fixed-point-free condition, the allowed lengths are precisely \(3,5,7,\ldots\).
This checks both directions of the determinant reduction, including the even
cycle obstruction.

For cycle multiplicities \((m_k)\), the number of permutations is
\(N!/\prod k^{m_k}m_k!\). Weighting every cycle by \(1/2\) therefore gives
\[
 \frac1{N!}\sum_q2^{-c(q)}
 =[z^N]\exp\!\left(\frac12\sum_{k\in L}\frac{z^k}{k}\right).
\]
Taking \(L=\{2,3,\ldots\}\) gives
\(D=e^{-z/2}(1-z)^{-1/2}\); taking
\(L=\{3,5,7,\ldots\}\) gives
\(H=e^{-z/2}(1+z)^{1/4}(1-z)^{-1/4}\). Consequently
\[
 p_N=\frac{[z^N]H}{[z^N]D},\qquad
 |\mathcal M_{N,2}|=(N!)^2[z^N]D,
\]
and the analogous invertible count is \((N!)^2[z^N]H\). Positivity of the
denominator follows independently from the positive weight of an \(N\)-cycle.

The small cases and strict inequalities are also complete: odd lengths at least
three cannot sum to 2 or 4, while 3 itself is allowed, so
\(p_2=p_4=0\) and \(p_3=1\). For every \(N\ge5\), an allowed odd-cycle
decomposition exists (one \(N\)-cycle for odd \(N\), and \(3+(N-3)\) for even
\(N\ge6\)); a forbidden decomposition also exists (one even \(N\)-cycle for
even \(N\), and \(2+(N-2)\) for odd \(N\)). Hence \(0<p_N<1\).

## Independent finite checks

I independently enumerated matrices by choosing the two occupied columns in
each row, filtered by column sums, and evaluated determinants by fraction-free
elimination for \(2\le N\le5\). The resulting (total, invertible) counts were
\((1,0),(6,6),(90,0),(2040,1440)\), giving
\(0,1,0,12/17\). A separate direct sum over cycle multiplicities reproduced
the asserted coefficient counts. These agree with, but do not substitute for,
the all-\(N\) proof.

## Reconstruction of the two-singularity asymptotic

For fixed nonintegral \(\beta\),
\[
 [z^N](1-z)^\beta=
 \frac{N^{-\beta-1}}{\Gamma(-\beta)}
 \left(1+\frac{\beta(\beta+1)}{2N}+O(N^{-2})\right).
\]
At \(z=1\), the analytic multipliers of \(D\) and \(H\) have respective
linear coefficients \(1/2\) and \(3/8\). At \(z=-1\), the multiplier of
\(H\) has linear coefficient \(-3/8\). Combining each linear term with the
gamma-ratio correction gives relative corrections
\(-3/8,-3/8,5/8\), respectively. Thus, with
\[
 a=\frac{e^{-1/2}2^{1/4}}{\Gamma(1/4)},\quad
 b=\frac{e^{1/2}2^{-1/4}}{\Gamma(-1/4)},\quad
 c=\frac{e^{-1/2}}{\sqrt\pi},
\]
one obtains
\[
 [z^N]D=cN^{-1/2}(1-3/(8N)+O(N^{-2})),
\]
\[
 [z^N]H=aN^{-3/4}(1-3/(8N))
 +(-1)^NbN^{-5/4}(1+5/(8N))+O(N^{-11/4}).
\]

The remainder argument is sufficient: subtracting the first four local
fractional-power terms leaves boundary behavior of orders \(7/2\) for \(D\),
and \(15/4\) and \(17/4\) for \(H\) at \(1\) and \(-1\). The global remainders
are therefore \(C^3\) on the unit circle, so three Fourier integrations by
parts give coefficient \(O(N^{-3})\); the explicitly omitted degree-two terms
give the stated, sometimes larger, bounds. There are no other unit-circle
singularities.

Upon division, the \(-3/(8N)\) nonoscillating corrections cancel, while the
oscillating relative correction becomes \(5/8+3/8=1\). Since
\(\Gamma(-1/4)=-4\Gamma(3/4)\), the result is exactly
\[
 p_N=\frac{2^{1/4}\sqrt\pi}{\Gamma(1/4)}N^{-1/4}
 +(-1)^{N+1}\frac{e\sqrt\pi}{2^{9/4}\Gamma(3/4)}
   (N^{-3/4}+N^{-7/4})+O(N^{-9/4}).
\]
This sign-checks and includes the requested contribution from \(z=-1\), and
it supplies a rigorous error term stronger than the requested leading
equivalent.

## Source comparison, limitations, and verdict

The frozen comparison record attributes the conditional Ewens representation
to He--Huang and the cycle determinant criterion to Li--Lin--Rodman, and it
does not claim those ingredients as new. Its proposed delta is limited to the
uniform all-\(N\) probability count and parity-sensitive asymptotic. The
snapshot does not include the external primary PDFs, so I did not independently
re-audit their texts in this evidence-bounded pass. This is not a correctness
gap because every mathematical ingredient used in the resolution is proved in
the frozen dossier, and the literature language expressly avoids a priority
claim.

**Verdict: accept.** The proof resolves the frozen original problem at its full
scope; the exact identity, exceptional sizes, determinant equivalence, both
dominant singularities, constants, signs, division, and error control all pass.
No substantive revision or unresolved mathematical gap was found.
