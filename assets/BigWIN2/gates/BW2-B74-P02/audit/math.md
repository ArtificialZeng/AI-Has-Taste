# Fresh mathematical referee report

Referee job: `win-00074-p02-referee-58c2401b6eff`  
Frozen snapshot: `31509399c6759126af316eda93228c498c0964e40d7927a2f74d111d66dba244`

## Scope and integrity

I reviewed the exact `resolution-paper` claim frozen in `claim.json`: for every
field \(K\) and every integer \(c\ge 2\),
\[
v(I_c)=2,\qquad v(\overline{I_c})=\left\lceil\frac c2\right\rceil,
\quad I_c=(x^2,y^2,z^c,xyz),
\]
together with all three asserted endpoint regimes. I did not replace this with
a finite-range or otherwise weaker statement.

I recomputed the SHA-256 digest of each of the eight frozen files. Every file
matched `audit/snapshot.json`, and the canonical digest of its file mapping was
the snapshot digest printed above. In particular, `source.md` retained digest
`1d3e86e773c0cff8e1d4cf1ab82845ff365401ba6a6d9caf6edc554a7a15af15`.

## Reconstruction of the decisive proof

Write
\[
w(a,b,d)=c(a+b)+2d.
\]
The three pure-power exponent vectors \((2,0,0),(0,2,0),(0,0,c)\)
lie on \(w=2c\). Their convex hull plus the nonnegative orthant is exactly
\(\{w\ge 2c\}\): if \(u\ge0\) and \(S=w(u)\ge2c\), then
\((2c/S)u\) is a convex combination of those three vectors and the remaining
vector \((1-2c/S)u\) is nonnegative. The fourth exponent \((1,1,1)\)
has weight \(2c+2\), so it does not change this Newton polyhedron.

The dossier also proves the lattice criterion directly, which avoids relying
on an unstated monomial-integral-closure theorem. For a nonzero polynomial
\(f\), let \(\nu(f)\) be the minimum \(w\)-weight of its terms. Weighted
initial forms in the domain \(K[x,y,z]\) give
\(\nu(fg)=\nu(f)+\nu(g)\). Every member of \(I_c^i\) has weight at least
\(2ci\). If an integral equation for \(f\) had \(\nu(f)<2c\), its term
\(f^n\) would have strictly smaller weight than every other term
\(a_i f^{n-i}\), so its nonzero initial form could not cancel. Thus every
term of every \(f\in\overline{I_c}\) has weight at least \(2c\).

Conversely, for \(m=x^ay^bz^d\) of integer weight
\(S=c(a+b)+2d\ge2c\), the product
\[
(x^2)^{ca}(y^2)^{cb}(z^c)^{2d}
\]
uses exactly \(S\) generators and divides \(m^S\), coordinate by coordinate;
the three exponent differences are
\(a(S-2c),b(S-2c),d(S-2c)\). Hence \(m^S\in I_c^S\), so \(m\) is
integral over \(I_c\). Since integral closure is an ideal, these two
directions establish, over every field,
\[
\overline{I_c}=(x^ay^bz^d: c(a+b)+2d\ge2c). \tag{1}
\]

Both ideals contain a power of each variable and are proper, hence are
\(\mathfrak m=(x,y,z)\)-primary. Their only associated prime is
\(\mathfrak m\), so their v-numbers are the least total degrees of nonzero
socle classes. For a monomial ideal, membership is termwise; consequently a
homogeneous nonmonomial cannot create a lower-degree socle class by
cancellation, and it suffices to classify socle monomials.

For \(I_c\), a standard monomial \(x^ay^bz^d\) has
\(a,b\le1\), \(d\le c-1\), and not \(a=b=1,d\ge1\). Direct divisibility
after multiplication by \(x,y,z\) gives exactly the exponent triples
\[
(1,1,0),\quad(1,0,c-1),\quad(0,1,c-1).
\]
Their degrees are \(2,c,c\), proving \(v(I_c)=2\).

For (1), a standard monomial of weight \(W\) is in the socle exactly when
\[
W<2c,\qquad W+c\ge2c,\qquad W+2\ge2c.
\]
Because \(2c-2\ge c\) for every allowed \(c\), this is precisely
\(2c-2\le W<2c\). If \(s=a+b\), the upper bound forces \(s\le1\).
For \(s=0\), the sole integer solution is \(d=c-1\). For \(s=1\), the
condition is \(c-2\le2d<c\), whose sole solution is
\(d=\lceil c/2\rceil-1\). Thus the complete socle list is
\[
(0,0,c-1),\quad
(1,0,\lceil c/2\rceil-1),\quad
(0,1,\lceil c/2\rceil-1).
\]
The degrees are \(c-1,\lceil c/2\rceil,\lceil c/2\rceil\), and
\(c-1\ge\lceil c/2\rceil\) for \(c\ge2\). This proves the second formula.

Substitution now gives \((v(I_c),v(\overline{I_c}))=(2,1)\) at \(c=2\),
\((2,2)\) at \(c=3,4\), and second component greater than 2 exactly for
\(c\ge5\). Hence every endpoint in the frozen claim follows.

## Adversarial and computational checks

I specifically checked the smallest value \(c=2\), where
\(2c-2=c\) and where the inequality used in the socle reduction is only an
equality. The closure is then \(\mathfrak m^2\), so its least socle degree is
indeed 1. I also checked that the power exponent \(S\) in the integrality
certificate is always a positive integer; that no division or limiting
argument depends on the field; and that weighted initial forms remain
nonzero in every characteristic because a polynomial ring over a field is a
domain. Empty domains, extra associated primes, nonmonomial cancellation, and
unproved interchange of limits do not occur.

Rerunning `evidence/triage_enumerate.py` reproduced the frozen output digest
`5f877d2dad81d01b3fbb99f8174566f337069e2c7bdceac3260f193cae11d7ee`.
I also used a fresh checker, separate from that script, which attached the
explicit \(S\)-th-power certificate above to each positive closure-membership
decision and used the separating weight for each negative decision. Exhaustive
standard-box enumeration for every \(2\le c\le200\) returned exactly the two
symbolic socle lists above. This computation is corroboration; the preceding
argument, not the finite range, proves the universal quantifier.

## Source comparison and contribution

I inspected the supplied primary PDF itself. Its definition of the v-number
agrees with the frozen reading. Theorem 3.2 is a comparison theorem for
monomial ideals in two variables. Example 3.3 treats precisely the isolated
case \(c=5\), lists
\((x^2,xy,y^2,xz^3,yz^3,z^5)\) as the integral closure, and computes the
v-numbers 2 and 3. Formula (1) specializes to exactly that list and those
values. The supplied paper does not state the all-parameter classification.

Relative to that nearest supplied result, the frozen candidate adds a genuine
infinite classification, a complete symbolic socle description, and the exact
first reversal and equality regimes. It is neither merely the known \(c=5\)
calculation nor an arbitrary toy restriction. The associated literature search
record is explicitly limited and does not establish priority; the candidate's
contribution statement likewise makes no priority claim. That limitation does
not undermine the correctness or the precise delta verified here.

## Verdict

**Accept.** The proof settles the original statement in its full frozen scope,
including every field, every integer \(c\ge2\), and all endpoints. The
mathematical argument is self-contained, the exact finite check agrees with it,
and the stated contribution is supported relative to the supplied primary
source. I found no unresolved mathematical gap requiring revision.
