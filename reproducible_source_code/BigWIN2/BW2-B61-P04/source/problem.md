# Precise reading and triage

Provenance: `win-00061-p04-triage-2602d0cdede1` (triage, 2026-09-07).
The verbatim frozen statement is `source.md`; it remains controlling if this
interpretation differs from it.

## Mathematical statement

For each rational prime \(\ell\ne5\), let \(U(\ell)\) be the assertion

\[
 \forall A,B/\mathbb F _5\text{ elliptic},\qquad
 Q_\ell(A)\cong Q_\ell(B)\Longrightarrow
 A\sim_{\mathbb F _5}B,
\]

where

* \(A[\ell](\overline{\mathbb F}_5)\cong\mathbb F_\ell^2\) is the geometric
  \(\ell\)-torsion and \(\pi_{A,\ell}\) is the restriction of the
  \(5\)-power Frobenius;
* \(Q_\ell(A)=Q(A[\ell](\overline{\mathbb F}_5),\pi_{A,\ell})\) has underlying
  set \(A[\ell](\overline{\mathbb F}_5)\) and, following Definition 2.4 of
  arXiv:2609.02278v1, operation
  \(x*y=\pi_{A,\ell}(x)+(1-\pi_{A,\ell})(y)\);
* \(\cong\) means an abstract quandle isomorphism, not an assumed linear map;
  Corollary 4.3 of the cited paper is what makes it equivalent here to
  similarity of the two Frobenius operators over \(\mathbb F_\ell\);
* \(A\sim_{\mathbb F _5}B\) means that an isogeny over \(\mathbb F _5\)
  exists.

The requested integer is
\[
 \min\{\ell:\ell\text{ is a rational prime},\ \ell\ne5,\ U(\ell)\}.
\]
The quantifiers include every elliptic curve over \(\mathbb F _5\), including
ordinary and supersingular isogeny classes; the same single \(\ell\) must work
for every ordered pair. “Least” therefore requires treating the smaller
eligible primes individually. For a curve \(A\), put
\[
 a_A=6-\#A(\mathbb F _5),\qquad P_A(T)=T^2-a_AT+5.
\]
Then \(|a_A|\le4\), and equality of \(P_A\) (equivalently of \(a_A\)) is the
\(\mathbb F _5\)-isogeny criterion. A counterexample certificate must still
establish similarity, hence the rational canonical form, rather than infer it
only from equality of characteristic polynomials modulo \(\ell\).

## Nearest prior result and proposed delta

The inspected primary source is WonTae Hwang, *Frobenius Alexander quandles,
knot colorings, and isogeny classes of abelian varieties over finite fields*,
arXiv:2609.02278v1, submitted 2026-09-02, inspected at
<https://arxiv.org/html/2609.02278v1> on 2026-09-07. Definition 2.4 fixes the
operation; Corollary 4.3 identifies quandle isomorphism with Frobenius
similarity; Corollary 4.5 proves \(U(\ell)\) when \(\ell>4\sqrt5\), hence for
\(\ell=11\); Example 4.9 gives a failure of \(U(3)\). The frozen source
misattributes this arXiv item to Yuta Taniguchi; the official arXiv record and
paper give WonTae Hwang. This correction does not alter the mathematical claim.

The exact \(\mathbb F _5\) sharpness question for \(\ell=2,7\) is not answered
in the inspected paper. It is best classified at intake as a **new question**
adjacent to that paper, not as a verified historical open problem. Exact-title,
exact-assertion, and equivalent-language searches on 2026-09-07 found no other
primary source resolving this finite delta; that limited search is not a
priority or openness claim.

Proposed contribution: nearest result = Hwang's sufficient bound and
\(\ell=3\) example; delta = settle \(\ell=2,7\) and thereby decide sharpness at
\(11\); verification = enumerate points on explicit nonsingular curves, compute
the integral Frobenius polynomials, and compute the invariant factors/minimal
polynomials of Frobenius modulo each prime.

## Cheapest discriminating screen (not yet an audited resolution)

Similarity modulo \(\ell\) forces \(a_A\equiv a_B\pmod\ell\). Since the trace
interval has diameter \(8\), this already proves equality of traces for
\(\ell\ge11\). The two unresolved small-prime screens have explicit leads:

* For \(\ell=7\), traces \(-4\) and \(3\) are congruent. The curves
  \(y^2=x^3+3x\) and \(y^2=x^3+4x+2\) have screened point counts \(10\) and
  \(3\). Their common reduced polynomial is \(T^2-3T+5\), whose discriminant
  is \(3\), a nonsquare in \(\mathbb F _7\); hence both candidate Frobenius
  matrices have the same irreducible companion rational canonical form.
* For \(\ell=2\), the curves \(y^2=x^3+3x\) and \(y^2=x^3+1\) have screened
  point counts \(10\) and \(6\), hence traces \(-4\) and \(0\). Each defining
  cubic has exactly one root in \(\mathbb F _5\), so Frobenius on \(E[2]\) is
  nonidentity with characteristic polynomial \((T+1)^2\); both therefore have
  the nonsemisimple companion/Jordan rational canonical form.

These leads, together with Example 4.9 at \(3\), make a bounded exact-certificate
research pass plausible. They are triage calculations, not an accepted proof.
