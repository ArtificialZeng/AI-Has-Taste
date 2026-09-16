# Precise problem statement

## Frozen source and interpretation

The immutable statement is `source.md` (SHA-256
`c5347a30addb4e76d3aacf32e67f81ac4d7ccea80c81d3fece59dd366c4f6e70`).
This file fixes its mathematical reading; it does not replace or amend the
source.

Let (I=\{1,2,3,4,5\}), and let

\[
F_5=\langle x_1,x_2,x_3,x_4,x_5\rangle
\]

be the free group with identity (e).  For (g\in F_5), let
(\ell(g)) be the number of letters in the unique freely reduced word over
(\{x_i^{\pm1}:i\in I\}) representing (g).  Thus the optimization is over
free-group elements, and length always means reduced word length.

For every (S\subseteq I), define the deletion homomorphism
(\pi_S:F_5\to F_5) by

\[
\pi_S(x_i)=\begin{cases}e,&i\in S,\\x_i,&i\notin S.\end{cases}
\]

Call (g\in F_5) *3-out-of-5 admissible* if

1. (g\ne e);
2. for every (S\subseteq I) with (|S|=3), (\pi_S(g)=e); and
3. for every (T\subseteq I) with (|T|=2), (\pi_T(g)\ne e).

All quantifiers range over the ten subsets of the indicated size; equality is
equality in the free group after free reduction.  The requested integer is

\[
L(3,5)=\min\{\ell(g):g\in F_5\text{ is 3-out-of-5 admissible}\}.
\]

The two boundary layers are equivalent to the full picture-hanging condition.
If (|U|\ge3), choose a three-set (S\subseteq U); then (\pi_U) factors as
a further deletion after (\pi_S), so (\pi_U(g)=e).  If (|U|<2) and
(\pi_U(g)=e), extend (U) to a two-set (T); further deletion would give
(\pi_T(g)=e), contradicting condition 3.  In particular condition 3 also
implies (g\ne e), although condition 1 is retained verbatim.

## Scope and contribution target

The primary target is the exact integer (L(3,5)).  An explicit word gives
only an upper bound unless every shorter length is excluded by a proved
analytic argument or a complete, independently checkable enumeration.
Classification of minimizers under generator permutations, independent
generator inversions, word reversal/inversion, and cyclic rotation is optional
secondary output and cannot replace optimality.

The nearest primary result is Tom Verhoeff, *The k-out-of-n picture-hanging
puzzle: shorter solutions for small k and n-k*, arXiv:2605.27617v1, Section 8,
which explicitly identifies 3-out-of-5 as the next exact-minimum case.  Section
6 proves that every solution for (k<n) has zero exponent sum in every
generator, hence even length.  Proposition 15 combines a 3-out-of-4 solution
of length 8 with a 2-out-of-4 solution of length 16 to give length at most 34
before junction cancellation.  The associated repository's `runs/runs.md` at
commit `c501b3d6df0fc4eaaf7932d440087d336cc863dd` reports an exhaustive search
with no solution at even lengths through 16, but its log is not by itself an
independently checkable optimality certificate.

A triage computation found and independently checked the freely reduced
length-26 word

\[
\begin{split}
(&x_1,x_2,x_3,x_4,x_1^{-1},x_2^{-1},x_3^{-1},x_4^{-1},x_5,
x_2,x_1,x_4,x_3,x_4^{-1},x_3^{-1},x_2^{-1},x_1^{-1},\\
&x_3,x_4,x_1,x_2,x_4^{-1},x_3^{-1},x_2^{-1},x_1^{-1},x_5^{-1}).
\end{split}
\]

It is Proposition 15 with four letters cancelled at the junction.  The
standalone verifier `evidence/verify_upper26.py` checks all ten three-deletions
and all ten two-deletions without importing the source repository.  Therefore
\(L(3,5)\le26\) is established locally.

Research pass 2 independently replaces and extends the author-reported lower
search.  `evidence/search_exact_sat.py` splits lengths 10 through 18 into all
12 possible sorted positive-even generator-count patterns and encodes ordinary
free reduction by an exact interval grammar.  Complete generator/sign/rotation
symmetries retain a representative of every shortest admissible word; no
heuristic pruning is used.  Each case is UNSAT with a stored DRUP certificate,
and `evidence/check_drup.py` checked every clause using MiniSat 2.2.  Corrected
provenance identifies PySAT's `glucose3` backend as the producer of the stored
traces; a fresh `glucose3` run reproduced every CNF and proof byte for byte.
Independently, `drat-trim` accepted all 12 archived pairs with exit code zero
and the exact marker `s VERIFIED`.  The machine-readable audits are
`evidence/glucose_reproduction_audit.json` and
`evidence/drat_trim_audit.json`.  The full reduction and encoding proof are in
`evidence/exact_lower_bound_certificate.md`.  Consequently the current
independently certified window is

\[
20\le L(3,5)\le26.
\]

## Literature/status screen

On 2026-09-10, the live arXiv record for 2605.27617 showed only v1 (submitted
2026-05-26), and its Section 8 still called 3-out-of-5 the next open case.
Exact-phrase and equivalent-language searches in triage and research pass 2
returned that paper (and a mirror/copy) plus the foundational primary papers
Demaine et al., arXiv:1203.3602v2, and Wastlund, arXiv:2102.00984v1, but no
later exact value or lower bound for 3-out-of-5.  The decisive source PDF is
copied at `evidence/external/2605.27617.pdf` with its source-recorded SHA-256.
This bounded screen supports comparison with the cited source; it is not a
claim of exhaustive worldwide priority.

## Certificate requirements

An upper-bound certificate must supply a freely reduced signed word and show
the twenty essential deletion outcomes.  An optimality certificate must cover
every smaller length (odd lengths may be removed by the exponent-sum parity
lemma) and must justify every pruning and symmetry quotient.  A timeout,
heuristic failure, or unaudited run log is not an exclusion proof.

The current certificate meets these requirements only through length 18, so it
proves the subsidiary lower bound \(L(3,5)\ge20\) but does not resolve the
frozen exact-minimum question.
