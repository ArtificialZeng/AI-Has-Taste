# Fresh mathematical referee report

## Frozen scope and verdict

I reviewed the exact `result-note` claim frozen in `claim.json`: for the
self-similar measure and Fourier transform specified in `source.md` and
`problem.md`,

\[
F(\xi)\ne 0\qquad\text{whenever}\qquad 27/25\le |\xi|\le 1024.
\]

The original assertion through \(10^7\) remains unresolved.  My verdict on
the frozen subsidiary claim and its stated contribution is **accept**.

## Evidence integrity and review boundary

All files enumerated by `audit/snapshot.json` had the frozen SHA-256 values.
In particular, the certificate digest was
`3a83ce8c86d526ea5070bc407555355c6328d1c4f33add5d3123e257d0da0b21`,
and the snapshot digest was
`c4b516d765be407403ec58acafbfa542e2fb29722862fb1ea97a687a5425743f`.
The immutable `source.md` retained digest
`1d7fe134dedec418a06b3155598b70295df9a6fe07b651280df0e66ab0fadee3`.
I assessed only this frozen snapshot and did not import an owner verdict or
silently change the claimed range.

## Reconstruction of the decisive argument

The two contractions map \([0,2/3]\) into itself, so the invariant measure is
supported there.  With \(A=4\pi/3\), this gives, for real \(t\),

\[
 |F(t)-1|\le A|t|,
 \qquad |F^{(n)}(t)|\le A^n\quad(n=1,2,3).
\]

These follow directly from
\(|e^{-2\pi i t y}-1|\le 2\pi |t|y\) and
\(0\le y\le2/3\); they are analytic enclosures, not sampled estimates.
The invariance identity gives

\[
 F(x)=pF(x/2)+p^2e^{-\pi i x}F(x/4),
\]

and differentiating it yields exactly the recurrence implemented for orders
zero through three.  At recursion depth 120, the preceding support bounds
enclose the terminal values and derivatives.  Outward-rounded Arb operations
then propagate inclusions back to \(F(x)\), \(F(x/2)\), and their derivatives.
There is therefore no unbounded or empirical truncation term hidden at the
terminal scale.

On every accepted real interval \(I=[a,b]\), the complex enclosure of
\(F(I/2)\) excludes zero.  Thus

\[
q(x)=F(x)/F(x/2)
\]

is well defined and three times differentiable throughout that entire closed
interval.  The quotient jets are obtained by valid Taylor-series division.
Let \(m=(a+b)/2\), \(h=(b-a)/2\), and let \(P(s)\) interpolate the three
certified values of \(q\) at \(a,m,b\), with \(x=m+hs\).  Applying the scalar
Lagrange remainder separately to the real and imaginary components gives

\[
 |q(m+hs)-P(s)|_{\rm component}
 \le \sup_I |q'''|_{\rm component}\,
       \frac{h^3}{9\sqrt3},\qquad -1\le s\le1,
\]

because \(\max_{[-1,1]}|s(s^2-1)|=2/(3\sqrt3)\).  The serialized dyadic
covers of \([-1,1]\) prove that \(|P(s)|\) is strictly larger than the
Euclidean norm of these two componentwise errors.  Direct complex-ball
separation handles 11,360 polynomial segments; certified monotonicity of
\(|P|^2\), followed by the minimizing endpoint check, handles 23 increasing
and 13 decreasing segments.  Hence \(q\), and therefore \(F\), is nonzero on
each leaf.

The 8,184 exact initial cells are adjacent and cover
\([27/25,1024]\), including both endpoints.  Exact midpoint bisection produces
11,224 accepted leaves, again with exact adjacency; there are no sampled gaps.
Finally, positivity and reality of the measure give
\(F(-x)=\overline{F(x)}\), proving the stated absolute-value version.

## Checks actually performed

I inspected both evaluator recurrences, the quotient differentiation, the
interpolation constant, the exact partition logic, and all serialized-proof
checks.  I then ran
`python3 evidence/verify_research_taylor_cover_1024.py
evidence/research_taylor_cover_1024_certificate.json` from a fresh referee
session.  The stored-proof audit checked all 8,184 cells, 11,224 leaves, and
11,396 polynomial segments.  The separate Taylor-coefficient recurrence then
recomputed every leaf at 320-bit precision and depth 128.  It completed with
exit status zero, the same 11,396 accepted segments, maximum polynomial-cover
depth 7, and the frozen certificate digest.

As an additional aggregate scan of every leaf, I recomputed the stored strict
margins.  The smallest lower bound for an interval denominator was
\(1.3651341245973564\times10^{-5}\), and the smallest certified quadratic
distance minus remainder norm was
\(3.5487297055146311\times10^{-5}\); no nonpositive margin occurred.  I also
checked the first endpoint \(27/25\), the final endpoint 1024, dyadic leaf
alignment, empty/degenerate interval risks, and the implication from a
nonzero quotient to a nonzero numerator.  No division by an enclosure
containing zero occurs.

Both computational paths use Arb via python-flint, so the replay is not a
cross-library formalization.  This is disclosed in the evidence and does not
undermine the proof: the decisive operations are outward-rounded inclusions,
the analytic terminal bounds are proved above, and the second recurrence uses
higher precision and greater depth rather than trusting stored success flags.

## Source comparison, contribution, and remaining gap

The frozen source record identifies Mao--Wu Proposition 3.3 as proving only
\([-1.08,1.08]\), followed by a double-precision scan to \(10^7\) that the
authors explicitly do not present as a formal proof.  Relative to that nearest
identified result, the present gap-free certificate extends the rigorous
positive range from 1.08 to 1024, nearly three orders of magnitude, with a
replayable exact-rational cover.  This is a nonroutine and useful subsidiary
theorem rather than a toy finite sample.  The snapshot's literature statement
supports this comparison but, appropriately, does not establish an absolute
priority guarantee beyond the searched sources.

Nothing in the certificate covers \(1024<|\xi|\le10^7\).  The note therefore
must continue to state that the original problem is unresolved.  This is an
honest limitation already present in the frozen statement and contribution,
not a defect in the subsidiary theorem.

## Explicit verdict

**Accept.**  The exact frozen scope is correct, the directed-rounding
certificate is gap-free and independently replayable at higher precision, and
the contribution is nontrivial relative to the nearest result identified in
the frozen source record.
