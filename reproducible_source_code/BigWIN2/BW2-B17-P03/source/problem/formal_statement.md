# Formal statement

## Corrected definition

For every integer \(n\ge 1\), let \(L_n\) be the least integer \(x\) for
which there exist integers \(d\ge1\) and a set
\(V\subseteq\{2,3,\ldots,x-d\}\) with \(|V|=n\), such that the multiset
\((v,v+d)_{v\in V}\) consists of \(2n\) distinct integers and
\[
 \gcd(a,b)=1
 \quad\text{for every two distinct }a,b\in
 S(d,V):=\bigcup_{v\in V}\{v,v+d\}.
\]
The interval is an integer interval; in particular it is empty if \(x-d<2\).
The target is the single finite cell \(L_{41}\), not the asymptotic Erdős--
Straus sumset problem from which this two-row auxiliary quantity arose.

## Theorem to be certified

\[
\boxed{L_{41}=529}.
\]

More explicitly:

1. at \(x=529\), \(d=42\) and the 41-element set recorded in
   `certificate/witness.json` satisfy the definition;
2. at \(x=528\), no integer \(d\ge1\) and no 41-element \(V\) satisfy it.

Monotonicity in \(x\) then proves minimality.

## Quantifiers and finite reduction

For the negative assertion it is enough to check \(1\le d\le526\), since
\(V\subseteq[2,528-d]\) must be nonempty.  If \(n\ge2\), an odd \(d\)
would put one even integer in every pair \(\{v,v+d\}\), producing at least
two distinct even members of \(S(d,V)\), contrary to pairwise coprimality.
Thus only the 263 even values \(d=2,4,\ldots,526\) remain.

For fixed \((x,d)\), retain precisely the integers \(v\in[2,x-d]\) with
\(\gcd(v,v+d)=1\).  Make two retained vertices adjacent exactly when their
two pairs together are four distinct pairwise-coprime integers.  A feasible
set \(V\) of size 41 is exactly a 41-clique.  Equivalently, attach to \(v\)
the set of prime divisors of \(v(v+d)\); feasibility is exactly selection of
41 pairwise-disjoint prime-support sets.

## Normalizations

There is no scaling normalization: scaling by an integer greater than one
destroys coprimality.  Column order is immaterial, so \(V\) is a set.  The
two rows may be interchanged, and the positive gap convention fixes their
order.  The source's recommendation to examine even gaps is a consequence,
not an additional hypothesis.

## Edge cases

All entries are at least 2, so every entry has a nonempty prime support.
Repeated endpoints are forbidden explicitly and also detected by the direct
gcd verifier.  No floating-point comparison or decimal threshold occurs in
this problem.  The source claims \(L_{37}=463,L_{38}=487,L_{39}=491,L_{40}=509\)
are contextual prior computational results, not assumptions in the proof of
the theorem above.

## Repairs and provenance status (cutoff 2026-09-01)

The source omitted explicit integrality of \(x,d,v\) and used real-interval
notation; these are repaired above.  It also presented the values through
\(L_{40}\) and the phrase “completely determined” without supplying evidence.
The values are corroborated by the 2026-08-12 public working report and its
described verification bundle, but that report labels them computational-only.
No primary or official record located by the searches in
`literature/search_log.md` reports \(L_{41}\); this is a bounded search claim,
not proof of global novelty.
