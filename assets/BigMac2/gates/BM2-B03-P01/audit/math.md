# Fresh mathematical referee report

## Frozen scope and verdict

I reviewed the exact `resolution-paper` claim frozen in `claim.json`, against
the original statement in `source.md` and its quantified reading in
`problem.md`.  The candidate resolves the whole original conjunction: it
establishes the limit for every fixed admissible pair \((q,R)\), proves the
upper bound \(1/3\), and proves both directions of the asserted equality
classification.  No restriction of the original scope is needed.

**Verdict: accept.**  The proof is complete at the stated scope.  The supplied
literature supports the comparison made with Korsky's general-set result; the
candidate appropriately makes no claim of priority or journal acceptance.

The audit is bound to snapshot
`f6645e17ef0677c1caa881429b8de75fbb9db2c4b2f4ed0fd99027c5555af0f1`.
I recomputed the SHA-256 hashes of `claim.json` and every enumerated evidence
file, and all six values agree with `audit/snapshot.json`.

## Reconstruction of the decisive argument

Let \(G=\mathbb Z/q\mathbb Z\), let \(r=|R|>0\), and set
\[
T=T_q(R)=\#\{(u,v)\in G^2:u,u+v,u+3v\in R\}.
\]
Here \(q\) and \(R\) are fixed before \(N\) tends to infinity.

First, counting each selected residue class in \([1,N]\) gives
\[
|A_N|=\frac rqN+O_q(1).
\]
For fixed \((u,v)\in G^2\), consider positive dilations with
\(x\equiv u\pmod q\) and \(d\equiv v\pmod q\).  Put
\(m=\lfloor(N-1)/3\rfloor\).  The interval constraints reduce exactly to
\(1\le d\le m\) and \(1\le x\le N-3d\); the middle point is then
automatically in \([1,N]\).  For a fixed admissible \(d\), the number of
possible \(x\)'s is
\[
\frac{N-3d}{q}+O(1).
\]
In any fixed residue class modulo \(q\),
\[
\#\{1\le d\le m:d\equiv v\pmod q\}=\frac mq+O_q(1),
\quad
\sum_{\substack{1\le d\le m\\d\equiv v\ (q)}}d
=\frac{m^2}{2q}+O_q(m).
\]
Consequently the positive-dilation count for this residue pair is
\[
C^+_{u,v}(N)=\frac{N^2}{6q^2}+O_q(N).
\]

For negative dilations, write \(e=-d\ge1\).  The interval constraints reduce
to \(1+3e\le x\le N\), and \(e\equiv-v\pmod q\).  The same residue-class sum
therefore gives
\[
C^-_{u,v}(N)=\frac{N^2}{6q^2}+O_q(N).
\]
This treatment genuinely excludes the integer \(d=0\), while retaining
nonzero dilations with \(d\equiv0\pmod q\).  Summing the two estimates over
the exactly \(T\) residue pairs satisfying the three membership conditions
yields
\[
M(A_N)=\frac{T}{3q^2}N^2+O_q(N).
\]
Since \(r>0\), division by the squared size asymptotic proves existence of the
limit and the exact formula
\[
L(q,R)=\frac{T_q(R)}{3r^2}.
\]

It remains to determine \(T\).  The change of variables
\((u,v)\mapsto(a,b)=(u,u+v)\) is a bijection on \(G^2\), and
\(u+3v=3b-2a\).  Thus
\[
T_q(R)=\#\{(a,b)\in R^2:3b-2a\in R\}\le r^2.
\]
This proves \(L(q,R)\le1/3\), and equality is equivalent to
\[
3b-2a\in R\qquad\text{for every }a,b\in R. \tag{1}
\]

Assume (1), choose \(c\in R\), and translate to \(S=R-c\).  Then \(0\in S\)
and
\[
3y-2x\in S\qquad(x,y\in S). \tag{2}
\]
Putting \(x=0\) and \(y=0\), respectively, gives
\(3S\subseteq S\) and \(-2S\subseteq S\).  Because \(2\) and \(3\) are
units modulo \(q\), both multiplication maps are injective on the finite
group, hence
\(3S=S=-2S\).  Given \(s,t\in S\), choose \(y,x\in S\) with
\(3y=s\) and \(-2x=t\); (2) then gives \(s+t\in S\).  A finite subset of a
group containing zero and closed under addition contains additive inverses
(for an element of order \(k\), its inverse is its \((k-1)\)-fold sum).
Therefore \(S\le G\), so \(R=c+S\) is a subgroup coset.

Conversely, if \(R=c+H\) with \(H\le G\), then for
\(a=c+h_1\) and \(b=c+h_2\),
\[
3b-2a=c+(3h_2-2h_1)\in c+H.
\]
Hence every pair in \(R^2\) is counted, \(T=r^2\), and the limit is exactly
\(1/3\).  This completes both directions without appealing to an unstated
classification lemma.

## Quantifier and edge-case audit

- The error constants may depend on the fixed \(q\), which is exactly the
  quantified scope; no uniform-in-\(q\) assertion is used.
- Positive and negative dilations are counted separately and together give
  the required signed, ordered convention.
- The residue \(v=0\) is included in \(T\), as it must be: it represents
  nonzero multiples of \(q\) in the main term.  The forbidden integer
  dilation \(d=0\) is absent from both triangles.
- The intermediate point lies between the two extreme points in each signed
  triangle, so no interval constraint was dropped.
- Nonemptiness of \(R\) makes the denominator nonzero for all sufficiently
  large \(N\).  Singleton residue sets and the full group are both covered
  and correctly occur among the equality cases.
- The hypothesis \(\gcd(q,6)=1\) is used precisely where the proof needs
  multiplication by \(2\) and \(3\) to be invertible.  No conclusion outside
  that hypothesis is asserted.

## Independent checks and source comparison

As a non-proof cross-check, I independently enumerated every nonempty subset
for \(q=5,7,11,13,17\) (141,467 subsets in total).  In every case
\(T_q(R)\le |R|^2\), and equality occurred exactly for the enumerated subgroup
cosets.  I also checked every subgroup coset and 20,000 deterministic random
nonempty subsets for each composite admissible modulus
\(q=25,35,49,55,65\), with the same result.  Direct integer enumeration for
several non-coset, singleton, and full-group examples at
\(N=100,250,500\) approached the stated modular limiting coefficients.  These
computations corroborate but are not used to prove the theorem.

The supplied Korsky PDF defines positive and signed affine-copy counts in
(1.1)--(1.2), identifies the \(\{0,1,3\}\) equation in (1.15), gives the
interval coefficient \(1/3\) in (1.17), and proves the general finite-set
upper coefficient \(47/122\) in Theorem 1.4 and (1.19)--(1.20).  A full-text
check of that supplied paper found residue-class methods but no statement of
the present fixed-periodic subgroup-coset classification.  Thus the frozen
problem's claimed delta from the cited result is accurately scoped.  The
supplied user-bibliography note explicitly treats its two entries as
methodological context only; neither is needed in the proof.  This audit does
not elevate that bounded comparison into a claim of exhaustive priority, and
the candidate itself makes no novelty or acceptance claim.

There is no unresolved mathematical gap in the frozen claim.
