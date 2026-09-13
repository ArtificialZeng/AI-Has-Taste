# Proof dependency graph

## Main result

Up to
\[
S\longmapsto a+uS\qquad(a\in\mathbb Z/105\mathbb Z,\;u\in(\mathbb Z/105\mathbb Z)^\times),
\]
there are exactly two inclusion-minimal vanishing subsets of weight 20:

\[
\begin{aligned}
S_{20,1}={}&\{0,1,3,9,11,24,26,30,41,42,45,46,61,63,71,72,76,84,87,93\},\\
S_{20,2}={}&\{0,1,3,11,12,16,24,33,41,42,45,46,54,63,71,75,76,84,86,87\}.
\end{aligned}
\]

Together with the seven previously recorded orbits, these are exactly the nine
minimal affine orbits of weight at most 20.

## Dependencies

1. **Cyclotomic criterion.** For a subset \(S\), put
   \(P_S(X)=\sum_{s\in S}X^s\). Since \(\zeta\) is primitive of degree
   \(\varphi(105)=48\),
   \[
   P_S(\zeta)=0\Longleftrightarrow \Phi_{105}\mid P_S
   \Longleftrightarrow P_S\bmod\Phi_{105}=0.
   \]
   This gives a 48 by 105 integer matrix with SHA-256
   `669ac026c32d1396ec85f4a7348a848918221d9a9c19598428011eefcfcc2744`.

2. **Affine invariance and normalization.** Translation multiplies the sum
   by \(\zeta^a\), and multiplication by a unit is a Galois automorphism.
   Both preserve vanishing and inclusion-minimality. Every nonempty orbit has
   a translate containing 0.

3. **Seven-fiber lemma.** Let \(\alpha=\zeta_7\), \(\beta=\zeta_{15}\).
   Then \(\zeta_{105}=\alpha\beta^{-2}\), because
   \(1/7-2/15=1/105\). For \(i\in\mathbb Z/7\mathbb Z\), define
   \[
   M_i=\{-2s\bmod15:s\in S,\ s\equiv i\pmod7\},\qquad
   F_i=\sum_{j\in M_i}\beta^j.
   \]
   Hence \(P_S(\zeta)=\sum_{i=0}^6\alpha^iF_i\). The cyclotomic fields of
   coprime conductors 7 and 15 are linearly disjoint, so \(\alpha\) has
   minimal polynomial \(1+T+\cdots+T^6\) over \(\mathbb Q(\beta)\).
   Consequently \(P_S(\zeta)=0\) iff \(F_0=\cdots=F_6\).
   The map \(s\mapsto(s\bmod7,-2s\bmod15)\) is bijective, so no subset data
   are lost.

4. **Finite exhaustive proposition.** Reducing the \(2^{15}=32,768\) fiber
   masks modulo
   \[
   \Phi_{15}(X)=X^8-X^7+X^5-X^4+X^3-X+1
   \]
   gives 14,221 distinct exact integer vectors. Enumerating all seven-tuples
   of equal-valued masks with exponent 0 selected and total weight at most 20
   produces exactly 1,209,813 tuples. Every tuple contains one of 1,331 affine
   images of the nine displayed representatives; the unblocked count is 0.
   Stream digests are `620fbdb4...f908ccca` and `11f1684b...497ea50`.

5. **Validity and minimality of blockers.** The standard-library verifier
   reconstructs \(\Phi_{105}\), proves exact vanishing of every representative,
   and uses meet-in-the-middle integer subset sums to reject every nonempty
   proper zero-sum subset. It checks orbit sizes
   \(35,21,15,105,105,315,210,210,315\), stabilizers, canonicality, and
   pairwise orbit disjointness.

6. **Completeness.** Let \(S\ne\varnothing\) be minimal, vanishing, and have
   \(|S|\le20\). Translate it so \(0\in S\). By step 3 it occurs in the
   finite enumeration of step 4, so it contains a listed blocker \(B\).
   Step 5 says \(B\) is a nonempty vanishing subset. Minimality forces
   \(S=B\). Conversely step 5 proves every listed representative is minimal.
   Selecting the records of weight 20 yields precisely the two sets above.

## Endpoint and degenerate cases

- The empty set is excluded by definition and by the normalization \(0\in S\).
- Subsets have distinct exponents; repeated roots and multiplicities are not in
  the theorem.
- Weight 20 is included. No assertion is made about weights at least 21.
- No numerical tolerance or floating-point equality occurs in the proof.
