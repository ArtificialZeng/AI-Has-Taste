# bigMac-00025-p03 — F3^2 cross-part rainbow near-perfect matching

## Immutable source statement

Let `G=F_3^2` under addition.  For every partition
\[
G=A\mathbin{\dot\cup}B,\qquad \{|A|,|B|\}=\{4,5\},
\]
decide whether there always exist four pairwise vertex-disjoint cross edges
`{a_i,b_i}`, with `a_i in A` and `b_i in B` after possibly swapping the names
of the parts, such that the multiset
\[
\{\,a_i-b_i,b_i-a_i:1\le i\le4\,\}
\]
is exactly `G\{0}`.

An affirmative result must cover every partition.  A negative result must give
one explicit partition and a complete exact no-matching certificate.  No claim
about larger groups is included.

## Source and status boundary

- Primary source: arXiv:2601.12250v3, *Paley-type matrices and
  1-factorizations of complete graphs*, Problem 1.6 and the paragraph following
  Theorem 1.7.
- Local primary PDF: `batches/literature/bigMac-25/2601.12250v3.pdf`, SHA-256
  `96a8cc209a1c1c82228698d903553c07c608de768b3e27a1fdab3c085a40d260`.
- That paper proves the same-part analogue for all odd-order finite abelian
  groups and the relevant cross-part Paley statement for prime cyclic groups,
  while identifying the general cross-part analogue as outside its method.
  The present smallest noncyclic layer is status-uncertain.

