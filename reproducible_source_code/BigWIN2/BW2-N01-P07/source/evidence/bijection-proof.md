# Restricted cyclic-block bijection: complete argument for review

Proposer: `newwin-00001-p07-research-4c610e4f54cc`, 2026-09-12.
Status: full-scope proof candidate, awaiting a fresh mathematical referee.
This is a research evidence document, not a publication manuscript.

## Exact statement and dependencies

Use classical subsequence patterns and compositional permutation powers.
For every integer n >= 0, let B_n consist of permutations pi of [n]
avoiding 312 and 321 such that pi^3 avoids 2143. Let C_n consist of
ordered compositions of n with at most one part outside {1,3}.
There is one empty permutation and one empty composition when n=0.
There is no hypothesis on pi^2.

For d >= 1 define epsilon_d=(2,3,...,d,1), with epsilon_1=(1).
The map

\[
F(d_1,\ldots,d_m)=\epsilon_{d_1}\oplus\cdots\oplus\epsilon_{d_m}
\]

restricts to a size-preserving bijection C_n -> B_n. In particular,

\[
\sum_{n\geq0}|B_n|z^n
=\frac1{1-z-z^3}
+\frac{z^2+z^4/(1-z)}{(1-z-z^3)^2}.
\]

The unrestricted composition encoding is the known Lemma 3.1 of
Archer--Bourne, *Pattern avoidance in compositions and powers of
permutations*, arXiv:2505.05218v3. It is proved again below, including
both inverse identities, so the mathematical argument has no unproved
external lemma. The source's Section 5, second paragraph, is the exact
cube conjecture to which this result applies. Source verification and
the limits of the novelty search are in `literature/research-screen.md`.

## 1. The unrestricted bijection and its inverse

For alpha in S_a and beta in S_b, alpha direct-sum beta concatenates
alpha with the entries of beta increased by a. Thus each summand occupies
a consecutive interval of positions and the identical interval of values.
F of the empty composition is the empty permutation.

Every F(d) avoids 312 and 321. In an epsilon block, an entry other than
the final 1 has precisely one smaller entry to its right, namely that 1.
The final 1 has none. All entries in later direct-sum blocks are larger.
Consequently an entry of F(d) has at most one smaller entry to its right,
whereas the first entry of either a 312 or a 321 occurrence must have two.

Conversely, let pi be a nonempty permutation avoiding 312 and 321, and
let d be the position of its minimum 1. For i<d<j, pi_i>pi_j would make
(pi_i,1,pi_j) an occurrence of 312. Therefore all entries before position
d are smaller than all entries after it. Together with the minimum 1,
the prefix of length d must have value set [d]. For i<j<d, pi_i>pi_j
would make (pi_i,pi_j,1) a 321. The prefix is therefore exactly
(2,3,...,d,1). These conclusions also hold when d=1 or d=n: the relevant
empty comparisons are vacuous, and the asserted prefix value set follows
in the same way (or is all of [n] when d=n).

Subtract d from every entry of the suffix. This gives a permutation rho
of [n-d] still avoiding 312 and 321, since relative orders in the suffix
are unchanged. Define recursively

\[
G(\varnothing)=(),\qquad G(\pi)=(d)\mathbin{\Vert}G(\rho),
\]

where the symbol denotes concatenation of lists. Each recursion removes
d>=1 entries, so G is defined and terminates on the entire avoidance class.

Both inverse identities hold for arbitrary sizes. If d is nonempty as a
composition, the minimum 1 of F(d) occurs exactly at the last position of
its first epsilon block, namely position d_1. Removing that block and
subtracting d_1 gives F(d_2,...,d_m). Induction on the number of parts,
starting with the empty composition, gives G(F(d))=d. For an arbitrary
312/321-avoider pi, the forced-prefix argument gives
pi=epsilon_d direct-sum rho. Induction on n, starting with n=0, gives
F(G(pi))=epsilon_d direct-sum F(G(rho))=pi. This also proves uniqueness
of the decomposition. G is applied to pi, not to its cube: different
compositions can have equal cubes, as (3) and (1,1,1) demonstrate.

## 2. The cube of one block

On [d], epsilon_d is addition of 1 modulo d, with residues represented
by 1,...,d. Hence

\[
q_d(i):=\epsilon_d^3(i)=1+((i-1+3)\bmod d).
\]

In particular,

\[
q_1=(1),\qquad q_2=(2,1),\qquad q_3=(1,2,3),\qquad
q_d=(4,5,\ldots,d,1,2,3)\quad(d\geq4).
\]

The block q_d is increasing if and only if d is 1 or 3. For d=2 there
is the inversion (2,1). For d>=4 the entries d and 1 at consecutive
positions d-3 and d-2 give an inversion. Sizes 1 and 3 give identities.

Every q_d avoids 2143. The identity cases are immediate. In the other
cases q_d is a concatenation of two increasing runs. Any subsequence
consists of entries from the first run followed by entries from the
second run, and thus has at most one adjacent descent. An occurrence of
2143 would have two adjacent descents, at its first and third positions.

Each direct-sum interval of F(d) is invariant under the permutation.
For its offset s and local coordinate i, F(d)(s+i)=s+epsilon_d(i).
Applying this formula three times proves

\[
F(d)^3=q_{d_1}\oplus\cdots\oplus q_{d_m}.
\]

## 3. Exact criterion for a direct sum

Lemma. If sigma_1,...,sigma_m are nonempty permutations that each avoid
2143, their direct sum avoids 2143 if and only if at most one sigma_i
contains an inversion. The empty direct sum satisfies the same assertion.

Proof. Every inversion in a direct sum lies in a single summand, because
an earlier summand has both smaller positions and smaller values than
a later summand. If sigma_r and sigma_s, with r<s, each contain an
inversion, choose endpoints a<b in the former and c<e in the latter.
Then a<b<c<e and their values satisfy

\[
q(b)<q(a)<q(e)<q(c),
\]

which is exactly an occurrence of 2143.

Conversely, any occurrence at a<b<c<e has the two inversions (a,b)
and (c,e). Each inversion lies in a summand. If their summands were the
same, all four entries would belong to it, contradicting its avoidance
of 2143. Thus the occurrence supplies two distinct summands containing
inversions. This proves both directions. For m=0 there is no inversion
or length-four subsequence, so both sides hold. QED.

By Section 2 every q_d satisfies the lemma's avoidance hypothesis, and
q_d has an inversion exactly when d is outside {1,3}. Consequently, for
every finite list of positive integers, including the empty list,

\[
F(d_1,\ldots,d_m)^3\text{ avoids }2143
\quad\Longleftrightarrow\quad
\#\{i:d_i\notin\{1,3\}\}\leq1.
\]

This equivalence and Section 1 show that F takes C_n into B_n and G takes
B_n into C_n. The already-proved inverse identities restrict to those
sets. Thus the claimed bijection holds for every n>=0, including the
empty and singleton cases. This is the full frozen claim, not a statement
only about an enumerated prefix or a condition on the square.

## 4. Formal enumeration

Work in the ring of formal power series with integer coefficients. Let

\[
A(z)=\sum_{r\geq0}(z+z^3)^r=\frac1{1-z-z^3},\qquad
E(z)=\sum_{d\notin\{1,3\},\ d\geq1}z^d
=z^2+\frac{z^4}{1-z}.
\]

The first series counts arbitrary sequences of ordinary parts 1 and 3;
the second counts a single exceptional part. A member of C_n either has
no exceptional part, counted by A, or has exactly one, with a unique
decomposition into an ordinary prefix, that exceptional part, and an
ordinary suffix. This case contributes AEA. Their disjoint union gives
A+AEA=A+EA^2, the stated generating series. Its constant term is 1,
accounting for the empty object. All coefficient sums are finite, and
each denominator has constant term 1, so no analytic convergence
assumption enters. QED.

## Gap list, scope, and assistance

Known mathematical gaps: none identified by the proposer. Fresh review
has not yet occurred. Every mathematical dependency needed for the
all-n result is proved above. The novelty claim is limited to resolving
the specific conjecture in the inspected Archer--Bourne source; absence
of a later equivalent resolution has only bounded search support.

The proof was developed with model assistance from the preserved triage
route and audited in this research job. Exact code provides separate
finite checks; it is not a proof of the all-n assertion, a formal proof
checker, or an independent referee. No additional agent was used.
