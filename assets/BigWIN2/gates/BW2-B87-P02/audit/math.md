# Fresh mathematical referee report

**Referee job:** `win-00087-p02-referee-0902fffef46f`  
**Frozen snapshot:** `1d08f3df43e1804951f4ef07917eb35239993893581ade36d6b108daa2c3830a`  
**Candidate scope:** the full `resolution-paper` statement in `claim.json`, with
`original_status` equal to `proved`.

## Integrity and scope

I recomputed all six file hashes in `audit/snapshot.json` and the canonical
digest of its `files` mapping. They agree with the frozen snapshot. In
particular, `source.md` has SHA-256
`e35a48b0af43111912b741dda755076b278d6e25947d6b2e88a6f3965b815c87`.
I assessed the exact universal statement for every prime (p\ge 11) and every
(3\le \ell\le(p-3)/2), including ordered-pair equivalence, the two endpoint
families, the converse, and uniqueness. I did not replace it by a small-prime
or normalized-only claim.

## Reconstruction of the decisive argument

Let the two missing restricted sums be the distinct residues (s,t). Under
the simultaneous affine map (z\mapsto uz+v), sums transform by
(w\mapsto uw+2v), while the inequality between the summands is preserved.
Taking (u=2/(t-s)) and (2v=-us) is legitimate because (p) is odd and
(s\ne t), and sends the unordered missing set to ({0,2}).

For a normalized pair, write (C=\mathbb F_p\setminus A). If (y\in
B\setminus\{0\}), then (-y\ne y), so missingness of zero forces
(-y\in C). Likewise, if (y\in B\setminus\{1\}), then (2-y\ne y),
so missingness of two forces (2-y\in C). Hence

\[
U(B)=((-B)\setminus\{0\})\cup((2-B)\setminus\{1\})\subseteq C,
\qquad |U(B)|\le \ell.
\]

Put (X=-B). Translation by (2) is one cycle on the additive group of
(\mathbb F_p). If (X) has (r) maximal cyclic (+2)-runs, then

\[
|X\cup(X+2)|=\ell+r.
\]

Passing to
(V=(X\setminus\{0\})\cup((X+2)\setminus\{1\})) removes zero exactly when
zero is a run start and removes one exactly when (-1) is a run end. With
the corresponding indicators (\delta_0,\delta_1), the exact count is

\[
|V|=\ell+r-\delta_0-\delta_1.
\]

Thus (|V|\le\ell) permits at most two runs. With one run, at least one of
the two exceptional endpoints occurs; with two runs, both occur and lie on
different runs. They cannot lie on one run of length (m\le\ell), because
that would give (p\mid 2m-1), whereas
(1\le2m-1\le2\ell-1\le p-4). Consequently, for unique (a,b\ge0) with
(a+b=\ell),

\[
X=\{2j:0\le j<a\}\cup\{-1-2j:0\le j<b\}.
\]

Directly shifting these two runs gives

\[
V=\{2j:1\le j\le a\}\cup\{-1-2j:0\le j<b\}.
\]

The pieces cannot meet: an intersection would imply
(p\mid 2(i+j)+1), while
(3\le2(i+j)+1\le2\ell-1\le p-4). Thus (|V|=\ell).
Since (V=U(B)\subseteq C) and (|C|=\ell), equality follows. Negating
(X) gives precisely (B_{a,b}), and (C=C_{a,b}). This establishes the
universal classification without importing an order on the field.

## Converse and endpoint checks

The same odd-integer collision bounds show separately that both displayed
pieces of (B_{a,b}), and both displayed pieces of (C_{a,b}), are
disjoint; hence the asserted cardinalities are correct. The identity
(U(B_{a,b})=C_{a,b}) rules out allowed representations of both zero and
two, including the exceptional equal-summand possibilities (y=0) and
(y=1).

When (a,b>0), residues outside (C_{a,b}\cup\{0\}) are represented with
the element (0\in B). The positive-even elements (2i\in C) other than
two are represented as ((2i-1)+1), and the negative-odd elements are
represented as ((-2j-2)+1). I checked all membership and unequal-summand
conditions modulo (p). In particular, the apparently parity-based
comparisons are rectified by (2\ell\le p-3): the relevant same-sign
integer representatives have absolute value below (p), and every
cross-sign collision would force a nonzero integer of absolute value below
(p) to be divisible by (p).

For (a=\ell,b=0), the only elements not already represented using zero are
(2i) with (2\le i\le\ell). With (j=\ell-i+1), the representation

\[
2i=2(\ell+1)+(-2j)
\]

has its first summand outside (C), since (2\ell+2\le p-1), and the two
summands are not congruent: their positive even difference is below (2p)
and hence is neither the odd number (p) nor (2p). The map
(z\mapsto1-z) supplies the case (a=0,b=\ell). Therefore the displayed
restricted sumset is exactly (\mathbb F_p\setminus\{0,2\}) in every case.

## Affine uniqueness

Any affine map between two displayed pairs must preserve their missing-sum
set. Thus

\[
\{2v,2u+2v\}=\{0,2\},
\]

which gives only ((u,v)=(1,0)) or ((-1,1)). The identity preserves the
unique two-run lengths, while (z\mapsto1-z) sends
((B_{a,b},C_{a,b})) to ((B_{b,a},C_{b,a})). Hence the parameters agree
exactly up to swapping, and the (\ell+1) decompositions have
(\lfloor\ell/2\rfloor+1) affine classes.

## Falsification and computational checks

I specifically tested the smallest allowed (\ell), the maximal allowed
(\ell), (a=0), (b=0), possible coincidence of the two exceptional run
endpoints, modular collisions in every displayed union, and equality of the
two restricted summands. There is no division by zero, limiting argument,
compactness step, cited theorem, or circular dependence in the proof.

I reran the supplied exact normalized enumerator. It passed all 16 legal
((p,\ell)) cases for (p=11,13,17,19), with no (B) having
(|U(B)|<\ell). As a separate check, I exhaustively enumerated all
unnormalized pairs ((B,C)) at (p=11), rather than filtering first through
(U(B)). For (\ell=3), all 220 critical pairs equal the union of the full
affine orbits of the representatives; for (\ell=4), the corresponding
count is 275. In each case all 55 unordered missing-sum sets occur uniformly
(four and five normalized pairs per missing set, respectively). These finite
checks corroborate, but are not used in place of, the universal run proof.

## Source comparison and limitation

The frozen source and interpretation describe Li--Liang's one boundary
example and results in a different cardinality range, and report that full
overlap checking against Liu--Qian was unavailable. The submitted proof is
self-contained and invokes none of those inverse theorems. The claim also
expressly makes no priority or novelty assertion. Accordingly the unresolved
literature-overlap question does not create a gap in the mathematical
resolution of the frozen statement; this verdict does not certify novelty or
publication priority.

## Verdict

**Accept.** The argument proves every quantified part of the exact frozen
classification, including normalization, the forced inclusion, both endpoint
corrections, modular no-wrap, the converse, and affine uniqueness. I found no
unresolved mathematical gap in the submitted scope.
