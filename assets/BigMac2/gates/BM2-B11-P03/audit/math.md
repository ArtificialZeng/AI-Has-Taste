# Fresh mathematical audit

## Frozen scope reviewed

I reviewed the claim frozen by snapshot digest
`34fc7c533f472c12c11c2e62b9890097b62bc171f4bd1d4168075cea194b9ae6`:
under the independent-row convention,

\[
H=\langle(12),(34)\rangle\leq S_4,
\qquad K_{(2,2)}=X^4/H,
\]

and the asserted product is

\[
K_{(2,2)}\times K_{(2,2)}\cong
2K_{(2,2)}\mathbin{\coprod}K_{(1,1,1,1)}.
\]

All six hashes in `audit/snapshot.json` were recomputed and match the frozen
files.  Running `evidence/s4_certificate.py` without writing into the project
produced SHA-256
`49c3629f84c0369b1ebdf469fca48d2277201f9f2aecd0a3c717fa5a57ec7f8b`,
the frozen certificate hash.

## Reconstruction of the decisive argument

A species concentrated on four-element sets is determined by its associated
\(S_4\)-set.  Pointwise Cartesian product gives the diagonal action on
\(S_4/H\times S_4/H\), whose transitive orbits are indexed by
\(H\backslash S_4/H\), with stabilizer
\(H\cap gHg^{-1}\) for the orbit represented by \(g\).

The two transpositions in \(H\) are \((12)\) and \((34)\).  Hence a normalizer
element must preserve the unordered block system
\(\{\{1,2\},\{3,4\}\}\), and every permutation preserving that block system
does normalize \(H\).  Thus \(|N_{S_4}(H)|=8\).  Because \(H\) is normal in
its normalizer and has index two there, the normalizer is the union of two
size-four double cosets, represented by \(e\) and \((13)(24)\).  Both
intersections are \(H\).

For \(r=(23)\),

\[
rHr^{-1}=\langle(13),(24)\rangle,
\qquad H\cap rHr^{-1}=1.
\]

Consequently \(|HrH|=|H|^2=16\).  This double coset is disjoint from the
normalizer: if \(h_1rh_2\) normalized \(H\), then, since both \(h_i\) do,
\(r\) would normalize \(H\), which it does not.  Its size equals the entire
complement of the order-eight normalizer.  Therefore these three double cosets
are exhaustive and have intersection stabilizers \(H,1,H\).  It follows that

\[
S_4/H\times S_4/H\cong S_4/H\sqcup S_4/1\sqcup S_4/H,
\]

which proves the claimed natural species isomorphism and coefficient vector
\((0,0,2,0,1)\).

## Independent checks actually performed

I used a separate in-memory exact enumeration, not importing the submitted
certificate code, to construct the six right cosets of \(H\) and all 36
ordered pairs, then computed their diagonal \(S_4\)-orbits directly.  The
orbit sizes were \(6,6,24\); their stabilizer orders were \(4,4,1\).  Each
order-four stabilizer had cycle-type profile one identity, two transpositions,
and one double transposition, hence was conjugate to \(H\).  Automatic
double-coset enumeration independently returned
\((|HgH|,|H\cap gHg^{-1}|)=(4,4),(4,4),(16,1)\).

The five stabilizers defining the displayed species are pairwise
nonconjugate: their orders distinguish all pairs except \(C_4\) and
\(C_2^2\), which are nonisomorphic.  Transitive finite \(S_4\)-sets form the
additive basis of the Burnside group, so there is no integral relation among
these five species and the coefficient vector is unique.  Independently, the
displayed fixed-point matrix is triangular up to its single lower entry and
has determinant \(384\neq0\), which gives the same conclusion for this list.

For cycle indices I recomputed from the elements of \(H\)

\[
Z_H=\tfrac14p_1^4+\tfrac12p_2p_1^2+\tfrac14p_2^2.
\]

Using the exact internal-product rule gives coefficients
\(3/2,1,1/2\) on \(p_1^4,p_2p_1^2,p_2^2\), respectively, exactly those of
\(2Z_H+p_1^4\).  The five submitted cycle-index columns have determinant
\(1/24\neq0\), so their integral relation module is also zero.

## Scope and contribution assessment

The immutable source asks precisely for this independent-row \((2,2)\) case,
including completeness of the subgroup-poset/double-coset calculation and a
uniqueness or nonuniqueness determination.  The proof settles that full scope;
it does not replace the requested species statement by only a character or
cycle-index computation.  The nearest prior machinery identified in the
frozen problem statement is the general double-coset formula, whereas the
finite normalizer and intersection computation above supplies the requested
case.  The argument is self-contained and makes no novelty or priority claim,
so it does not depend on an unverified external theorem beyond elementary
finite-group facts reconstructed here.

I found no missing case, degenerate-domain issue, denominator, unjustified
limiting step, or mismatch between the computational statement and the frozen
claim.  There is no unresolved mathematical gap in the exact submitted scope.

## Verdict

**Accept.**  Scope, correctness, exact evidence, uniqueness, and the stated
contribution all pass for the frozen `resolution-paper` claim.
