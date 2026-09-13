# Fresh mathematical referee report

## Frozen scope and materials

I reviewed the exact resolution-paper claim frozen in claim.json: for the
displayed rational map \(C_{18}\), every Fatou component is contained in a
basin of one of the nineteen roots. I used only the frozen statement and
interpretation, the two listed proof/certificate files, and the listed local
copy of arXiv:2609.02884v1. The SHA-256 values of claim.json and all five
listed evidence files agree with audit/snapshot.json, whose digest is
d0ca5ba0df04480ff06cbbca2b1700e66cf8802807299148fe8ab62fa9a77803.

## Reconstruction and exact checks

Write \(F=C_{18}\), let

\[
q(t)=\frac{t(12654t^2+684t-306)}{2(19t+1)^3},
\qquad t_0=\frac{17}{703},
\]

and put \(Q(x)=xq(x^{18})\). If \(\lambda=e^{\pi i/18}\) and \(k\) is odd,
direct substitution gives \(F(\lambda^k x)=\lambda^kQ(x)\). The free critical
points are exactly \(\lambda^k t_0^{1/18}\) for the eighteen odd residue
classes \(k\bmod 36\), so it suffices to follow the real \(Q\)-orbit.

I independently recomputed the rational identities and inequalities, rather
than relying only on the supplied script. Exact symbolic/rational arithmetic
gave

\[
q(t_0)=-\frac{10693}{9747},\qquad
\frac{16}{125}<t_1=t_0q(t_0)^{18}<\frac{13}{100},
\qquad -\frac1{50}<q(t_1)<0,
\]

and hence

\[
0<t_2=t_1q(t_1)^{18}
 <\frac{13}{100}\left(\frac1{50}\right)^{18}<\frac1{100}.
\]

The two printed integer cross-product gaps in the certificate were also
reproduced exactly. I checked the identities

\[
q(t)+1=\frac{P(t)}{(19t+1)^3},\qquad
P(t)=13186t^3+1425t^2-96t+1,
\]

and

\[
q(t)-1=-\frac{532t^3+741t^2+210t+1}{(19t+1)^3}.
\]

For \(g(t)=6593t^2+475t-16\), \(P'(t)=6g(t)\), \(g\) is increasing
on \([0,\infty)\), and

\[
g(1/100)=-\frac{105907}{10000}<0,\quad
P(1/100)=\frac{97843}{500000}>0,\quad
P(1/70)=-\frac{1808}{42875}<0.
\]

Thus \(P\) stays positive on \([0,1/100]\), while its smallest positive
root \(t_*\) exists in \((1/100,1/70)\). For \(0<t<t_*\), the two identities
above imply \(-1<q(t)<1\). The real interval \(0<|x|^{18}<t_*\) is forward
invariant under \(Q\), and \(|Q(x)|<|x|\) there. If the decreasing sequence
\(|Q^m(x)|\) had a positive limit \(L\), continuity would give
\(L=L|q(L^{18})|<L\), a contradiction. Hence \(Q^m(x)\to0\). Since
\(t_2<t_*\), every free critical point of \(F\) is therefore in the full
basin \(B(0)\). The denominator is positive throughout the real threshold
argument, so no pole or division-by-zero case is hidden in it.

I also ran the supplied exact verifier successfully. As a separate symbolic
check, differentiation and cancellation gave

\[
F'(z)=\frac{18\cdot19\,z^{18}(z^{18}-1)^2(703z^{18}+17)}
              {2(19z^{18}-1)^4}.
\]

The reduced numerator and denominator of \(F\) have degrees \(55\) and \(54\)
and gcd \(1\). The critical multiplicities are \(18\) at \(0\), \(2\) at
each of the eighteen roots of unity, \(1\) at each of the eighteen free
critical points, and \(2\) at each of the eighteen triple poles. Their sum is

\[
18+18\cdot2+18+18\cdot2=108=2\deg(F)-2,
\]

so the list is complete, including the possible pole and infinity cases.
The multiplier at infinity in the coordinate \(w=1/z\) is \(361/333>1\),
so infinity is repelling and the poles, which map to infinity, lie in the
Julia set.

## Fatou-component closure

The source's Lemma 2.4 says that an immediate attracting or parabolic basin
contains a critical point. No listed critical orbit can support a non-root
attracting or parabolic cycle: root critical points are fixed roots, free
critical points tend to \(0\), and pole critical points land at the repelling
fixed point infinity. Thus every attracting or parabolic periodic Fatou
component is associated with one of the nineteen root cycles.

For rotation domains, Lemma 2.4 places the whole boundary in the closure of
the postcritical set. The latter is a finite union of convergent free-critical
orbits (all lying in \(B(0)\), with sole limit \(0\)), fixed root orbits, and
the finite pole/infinity orbits. Consequently its intersection with the Julia
set is finite. A Siegel disk or Herman ring cannot have finite boundary: if a
domain on the sphere had finite boundary, connectedness of the sphere minus
that finite set forces the domain to be the complement of its boundary; such
a punctured sphere is neither a disk nor a finite-modulus annulus of the
required type. Hence no rotation domain exists.

Sullivan's no-wandering-domain theorem, quoted on PDF p. 5 of the supplied
source, makes every Fatou component periodic or preperiodic. The same pages
give the exhaustive four-type classification of periodic components. The
preceding exclusions therefore force every eventual periodic component to be
the immediate basin of a root. Pulling back along the finite preperiod sends
every point in the original component to that same root basin, which proves
the frozen componentwise quantifier, not merely critical-orbit convergence.

## Source comparison and scope assessment

The supplied paper's Theorem D (PDF p. 3) covers only \(n\le16\) or odd \(n\).
Its concluding question (PDF p. 27) asks about even \(n\ge18\), and its \(n=18\)
table entry (PDF p. 28) is numerical. Thus the frozen source does not already
contain this exact \(n=18\) resolution. The submitted proof replaces that
numerical entry with exact capture and supplies the global Fatou-component
closure. This is a nontrivial resolution of the entire frozen original claim;
it makes no assertion for other \(n\), Julia topology, or convergence speed.
Priority beyond the frozen supplied literature is not certified by this
review, but no broader priority claim is needed for the mathematical verdict.

I specifically attacked empty/degenerate domains, poles and infinity,
critical-list completeness, the sign and first-positive-root arguments, the
contraction limit, preperiodic components, parabolic cycles, and both types of
rotation domains. I found no unresolved mathematical gap or scope mismatch.

## Verdict

**Accept.** The exact frozen resolution-paper claim is proved at full scope,
the evidence is reproducible, and the contribution relative to the supplied
nearest result is substantive.
