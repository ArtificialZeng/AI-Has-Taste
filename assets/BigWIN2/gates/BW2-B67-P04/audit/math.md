# Fresh mathematical referee report

## Scope and binding

I reviewed the exact frozen `resolution-paper` claim with original status
`proved`, bound to snapshot
`9e8fed4b82f286146f9e6fe8fa75f1048a79e6ce1f5b28176f9f18f9979241f9`.
The reviewed mathematical scope is the full family
\(S=\{2,5,c\}\), \(c>5\), \(c\ne7\), including the two previously
unsettled residue classes \(c\equiv0,4\pmod 7\). The hashes of the inspected
frozen source, interpretation, claim, proof, verifier, verification record,
and source PDF agree with their entries in `audit/snapshot.json`. In
accordance with the referee-job restriction, I did not read `checkpoint.md`.

## Reconstruction of the mex proof

Let \(A=0011021\). The proof's finite-certification reduction is correct.
If a proposed word has a prefix of length \(q\), followed by a block \(P\)
of length \(p=c+2\), it suffices to check:

1. the initial range \(0\le n<c\);
2. the transient range \(c\le n<c+q\); and
3. for every residue \(r\pmod p\),
   \[
   P_r=\operatorname{mex}\{P_{r-5},P_{r-2},P_{r+2}\}.
   \]

Indeed, for \(n\ge c+q\) all three predecessors lie in the periodic tail,
and \(n-c=n+2-p\). Thus the last displayed cyclic rule is exactly the game
recurrence. Forward uniqueness of mex then proves the entire one-sided word.

For \(n<c\), direct calculation gives `00110` at \(n=0,\ldots,4\), then
`21` at \(n=5,6\). Thereafter the two-move recurrence is the seven-row
calculation for \(A\); I recomputed every row, including the legal-move
boundary at 5. In the \(c=7K+4\) family, the four initial letters of the
following block `0011223` agree with the needed continuation of \(A\), so
the same argument covers the entire range below \(c\).

For \(c=7K+4\), I recomputed the cyclic seams of
\(P=021021A^K\), the complete exceptional \(K=1\) transient, the common
first fourteen transient rows for \(K\ge2\), and the final seven rows. The
unlisted middle ranges reduce exactly to the base seven-row table: in the
transient middle the current phase is \(i\equiv m-2\pmod7\), and the three
predecessor phases are \(i-5,i-2,i+2\). The stated empty-range conventions
make the \(K=1\) and \(K=2\) boundaries exhaustive without overlap.

For \(c=7K\), I likewise recomputed both cyclic seams of
\(P=1A^{K-1}02102102\), the first fourteen and final eight transient rows,
and the seven-row reduction on the middle range. For \(K=2\), the two
cyclic seam tables are adjacent and exhaustive and the transient middle is
empty, so the smallest allowed parameter is covered. Every displayed
current digit is the mex of the displayed predecessor set. These checks
establish, uniformly in the parameters,
\[
g_{7K+4}=A^K0011223(021021A^K)^\infty \quad(K\ge1)
\]
and
\[
g_{7K}=A^K32203103(1A^{K-1}02102102)^\infty \quad(K\ge2).
\]

As arithmetic cross-checks, I ran the frozen exact verifier successfully for
\(K=1,\ldots,1000\) in the first family and \(K=2,\ldots,1000\) in the
second. I also used a separately written in-session exact recurrence check
on 245 boundary and spread-out cases, including \(K=10000\), checking every
cyclic tail row, primitivity, and the preperiod-boundary mismatch. These
finite computations support but are not used in place of the symbolic range
partition above.

## Exact period and preperiod

The minimality argument is valid. For \(021021A^K\), the cyclic gaps between
successive occurrences of the digit 2 are \(3,7^K,3\); for
\(1A^{K-1}02102102\), they are, up to rotation, \(7^{K-1},3^3\). Each cyclic
gap word has one nonempty run of 3-gaps and one of 7-gaps. If either period
block were a proper power, its cyclic 2-gap word would repeat the gap word of
one factor and would have at least two runs of each present gap size. Hence
both blocks are primitive, including the boundary cases \(K=1\) and \(K=2\),
so their right-infinite repetitions have least periods \(p=7K+6=c+2\) and
\(p=7K+2=c+2\), respectively.

At the preceding index \(q-1\), the transient letter is 3 in both families.
The same phase one period later is 1 for \(c=7K+4\) and 2 for \(c=7K\).
If periodicity began at any \(q'<q\) with positive period \(d\), its
restriction to the tail would force \(p\mid d\). Periodicity at \(q-1\)
would then equate the stated unequal letters. Therefore the exact minimal
preperiods are \(q=7K+7=c+3\) and \(q=7K+8=c+8\), both positive.

## Source comparison and full-shape scope

I checked the cited statements directly in the frozen arXiv v1 PDF. For
\((a,b)=(2,5)\), one has \(a+b=7\), \(\delta=3\), \(\eta=1\), and
\(\epsilon=1\). Lemma 14 gives the inert angles \(\{2,5\}\). Theorem 57
gives the \(c+a\) angles \(\{\delta-a,b\}=\{1,5\}\), with angle 5 already
in the inert class. Substituting these parameters into Theorem 28 gives
\(C_{2,5}=\{3,6\}\) for the new \(c+b\) angles. Theorem 32 therefore proves
pure periodicity at exactly \(1,2,3,5,6\pmod7\), with least periods as
stated in the evidence. The only remaining angles are 0 and 4. The value
\(c=7\) is the excluded additive case; the only smaller admissible boundary,
\(c=6\), is in the proved angle-6 zone. Also
\(\gcd(2,5,c)=1\) automatically, so no primitive-case hypothesis is lost.

Thus the two uniform word theorems cover every member of both remaining
angle classes and, together with the source theorem, prove Conjecture 50 on
the entire frozen shape. The exact parameterized words and their minimality
are a substantive strengthening of mere positive-preperiod assertions. The
frozen primary source itself marks these angle classes as conjectural and
does not contain these word formulas. The evidence makes only a bounded
arXiv-search statement and no broad priority claim; this verdict likewise
does not certify priority beyond the precise comparison with the cited v1
source.

## Verdict

**Accept.** The candidate matches the frozen full scope, the universal mex
proof is correct at all parameter and seam boundaries, the period and
preperiod minimality proofs are sound, and the checked source results cover
exactly the complementary residue classes. I found no mathematical gap that
requires revision.
