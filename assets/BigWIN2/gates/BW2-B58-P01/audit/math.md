# Fresh mathematical referee report

## Frozen scope and integrity

I reviewed the exact universal identity in `claim.json`, with the definitions
and quantifiers fixed by `source.md` and `problem.md`.  The SHA-256 hashes of
the claim and all four evidence files agree with `audit/snapshot.json`; the
snapshot digest is
`7d8416c18a7d29194eafb7c8e35f72f293055bbb4a80ee38363c8f220f5857ac`.
The submitted scope is the full original claim, not a restriction or a
subsidiary result.

## Reconstruction of the decisive argument

Let \(\eta\) be an integer-valued probability law supported in an interval
\([L,H]\) of length at most three, and let
\(\mu=\sum_{r\geq0}T_{2r}\eta\).  Write \(F(x)=\mu(( -\infty,x])\).
For every \(x\geq H-2\), each progression \(h,h+2,h+4,\ldots\) places
exactly one rung, with its base mass, in \((x,x+2]\).  Summing over the base
law gives
\[
F(x+2)=F(x)+1.
\]
The analogous identity for open lower rays also holds.  Moreover
\(F(H-2)\leq1\): a rung with index at least one is at least
\(L+2\geq H-1\), so only base mass can occur at or below \(H-2\).
Consequently, for every \(s>1\), the generalized quantile
\(q=\lambda(s)\) is strictly above \(H-2\).  Applying both the open and
closed distribution identities at \(q\) transports the two defining
quantile inequalities exactly, including at atoms, and yields
\[
\lambda(s+1)=\lambda(s)+2 \qquad(s>1).
\]

It remains to identify the additive constant in a unit quantile block.  Let
\(A\) and \(B\) be the quantile pushforwards of Lebesgue measure on
\((0,1]\) and \((1,2]\), respectively.  Quantile periodicity gives
\(\mu=A+\sum_{j\geq0}T_{2j}B\), while the ladder construction gives
\(\mu=\eta+T_2\mu\).  Subtraction is legitimate on bounded sets and leaves
the finite-measure identity
\[
\eta=A+B-T_2A.
\]
Since both \(A\) and \(B\) have mass one, taking first moments gives
\(\int x\,dB=m+2\), where \(m=\int x\,d\eta\).  Thus, for
\(D(s)=K(s+1)-K(s)\), one has \(D(1)=m+2\).  Integrating the quantile-shift
identity over equal-length end pieces gives \(D(s)-D(1)=2(s-1)\) first on
\([1,2]\), and unit translation extends it to all \(s\geq1\).  Hence
\[
K(s+1)-K(s)=2s+m \qquad(s\geq1).
\]

For the submitted application, the nonconstant part
\[
p(z)=2\mathbf 1_{z<\alpha_v}-\mathbf 1_{z<v}
\]
has oscillation at most two because the intervals \([0,\alpha_v)\) and
\([0,v)\) are nested.  Adding \(\mathbf 1_{y>\beta_v}\) increases
oscillation by at most one.  Thus the integer-valued distribution of
\(h_v(y)\) has support oscillation at most three for every \(v\), including
all parameter breakpoints.

The map \(y\mapsto(1/2-y)\bmod1\) preserves Lebesgue measure.  With
\(q=\lfloor20v\rfloor\), \(a=\{20v\}\),
\(r=\lfloor41v\rfloor\), and \(b=\{41v\}\), direct integration gives
\[
\int_0^1h_v(y)\,dy=2q-r+2a-v+(1-b)=1-2v.
\]
Applying the ladder formula at \(s=j+v\), for every integer \(j\geq1\),
therefore gives
\[
K_v(j+1+v)-K_v(j+v)=2(j+v)+1-2v=2j+1.
\]
Summation from \(j=1\) to \(n-1\), together with the tautological case
\(n=1\), proves the frozen identity for every stated \(v\) and \(n\).

## Adversarial and exact checks performed

I checked the threshold \(s=1\), positive-mass ties, strict/open versus
closed distribution functions, the endpoint \(v=0\), coincident interval
endpoints, and floor/fractional-part breakpoints.  None creates a missing
case: endpoint values in \(y\) are null, whereas breakpoint values of \(v\)
remain covered by the uniform oscillation and mean identities.

As a corroborative check rather than a substitute for the proof, I used a
fresh exact-rational implementation of the interval decomposition and
lowest-mass integral.  It verified the identity for \(1\leq n\leq8\) at
\(v=0,1/82,1/41,1/40,1/20,1/2,19/20,40/41,81/82,999/1000\).  A separate
finite check covered all 56 probability laws with denominator-five weights
on four consecutive integer levels and verified the ladder increment at
all half-integer \(s\in[1,5]\).

## Source comparison and contribution

The supplied primary PDF states this identity as Lemma 6.6.  Its proof says
that ladder ordering is constant on the later breakpoint partition and
calls the result an exact finite verification; it does not provide the
cell ledger or a checker there.  The submitted proof has a materially
different and reusable mechanism: support oscillation at most three forces
the quantile shift after the first unit of mass, and one first-moment
calculation fixes every unit-block cost.  It therefore supplies a uniform,
breakpoint-free closure of the exact claim and explains why enumeration is
unnecessary.  This is a substantive proof benefit over the nearest supplied
result.  The candidate makes no unsupported priority claim.

## Verdict

**Accept.**  The proof settles the frozen original statement in its full
scope.  I found no unresolved mathematical gap, scope mismatch, or
contribution defect in the evidence reviewed.
