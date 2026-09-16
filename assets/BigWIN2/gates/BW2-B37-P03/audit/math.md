# Fresh mathematical referee report

## Frozen scope

I reviewed the claim frozen by snapshot
`65cc4fb76286022f584f70287404e0d6762c09afc264c84294460137eadd8852`.
It is a full-scope negative answer to the immutable source: it excludes every
tuple in \(\mathbb Q^{18}\), without imposing distinctness, nonzero
coordinates, or interval restrictions. The claim therefore has the correct
scope for a `resolution-paper` with original status `disproved`.

## Reconstruction of the decisive argument

Assume that a solution exists and write \(x_j=a_j/D\), where \(D>0\), all
\(a_j\) are integers, and \(\gcd(D,a_1,\ldots,a_{18})=1\). Clearing
denominators gives

\[
 S_2=9D^2,\qquad S_4=27D^4/4,\qquad S_6=45D^6/8,
 \quad S_r=\sum_{j=1}^{18}a_j^r.
\]

The denominator \(D\) must be even: if it were odd, the equality
\(4S_4=27D^4\) would equate a multiple of four with an odd integer. Write
\(D=2^k d\), with \(k\geq1\) and \(d\) odd. Primitivity then implies that
at least one \(a_j\) is odd.

For each odd \(a\), define \(p(a)\pmod4\) by
\(a^2\equiv1+8p(a)\pmod{32}\). Direct multiplication gives

\[
 a^4\equiv1+16p(a),\qquad a^6\equiv1-8p(a)\pmod{32}.
\]

Let \(O\) count the odd numerators, let
\(P=\sum_{a_j\text{ odd}}p(a_j)\pmod4\), and let \(E\) and \(F\) count
the numerators of 2-adic valuation exactly one and exactly two. Classifying
each numerator by its 2-adic valuation yields

\[
\begin{aligned}
 S_2&\equiv O+8P+4E+16F,\\
 S_4&\equiv O+16P+16E,\\
 S_6&\equiv O-8P
\end{aligned}\pmod{32}.
\]

If \(k=1\), the right sides of the three cleared identities are
\((4,12,8)\pmod{32}\). Reducing the fourth-power identity modulo 16 gives
\(O\equiv12\pmod{16}\). Since \(1\leq O\leq18\), this forces \(O=12\).
The sixth-power identity modulo 8 instead gives \(O\equiv0\pmod8\), a
contradiction.

If \(k\geq2\), both \(S_4\) and \(S_6\) vanish modulo 32. The fourth-power
identity modulo 16 gives \(O=16\). The sixth-power congruence then gives
\(P\equiv2\pmod4\), and the fourth-power congruence makes \(E\) odd.
Only two numerators are even, so \(E=1\); the remaining even numerator has
valuation two or at least three, hence \(F\in\{0,1\}\). Therefore
\(S_2\equiv4+16F\in\{4,20\}\pmod{32}\). But the cleared second-moment
identity gives \(S_2\equiv16\pmod{32}\) when \(k=2\), and
\(S_2\equiv0\pmod{32}\) when \(k\geq3\). This is the required
contradiction in every remaining case.

## Checks performed

I checked every residue identity above directly, including the dependence of
the target residues on \(k\) and the endpoint count \(1\leq O\leq18\). I
also ran the submitted exhaustive dynamic program and separately recomputed
the 18-coordinate reachable states modulo 32 without importing it. Both
computations produced 520 compressed states and excluded the primitive targets
\((4,12,8)\), \((16,0,0)\), and \((0,0,0)\). This computation corroborates
the proof but is not needed for its validity.

The supplementary unit-circle-pair observation is also correct: in a
primitive integer Pythagorean triple the hypotenuse is odd, so each
\((ab)^2\) has an odd reduced denominator; a finite sum retains odd reduced
denominator and cannot equal \(9/8\). This supplement is strictly separated
from the full-scope obstruction and is not used to infer the main result.

## Source comparison and limitations

The frozen `problem.md` reports only background on real Chebyshev-type
quadrature and an unverified supplied claim about the analogous 17-variable
system. Neither settles the rational 18-variable problem. No external source
is used in the proof, and the candidate expressly makes no novelty or priority
claim. Thus the limited literature evidence does not create an unsupported
mathematical dependency in the submitted scope.

I found no unresolved gap, hidden restriction, division by zero, limiting
argument, or reliance on a computational search in the proof. The primitive
common-denominator reduction covers zero coordinates, repeated coordinates,
arbitrary signs, and all rational denominators.

## Verdict

**Accept.** The elementary 2-adic argument proves the exact frozen claim and
therefore disproves the original existence statement in its full stated scope.
