# Mathematical referee report

**Verdict: ACCEPT, at the exact frozen scope.** The argument in
`evidence/research-proof.md` proves the original Ehrhart–word identity for
every rooted tree on the nonempty blocks of every partition of `[n]`, for
every integer `n >= 1`. Its binomial-content identity holds for every integer
`m >= 0`. No restriction on labels, block sizes, depth, or branching is needed.
The accepted workflow fields are `kind = resolution-paper` and
`original_status = proved`, exactly as frozen in `claim.json`.

Date: 2026-09-14 (UTC). Referee job:
`primary-20260914-arbor-ehrhart-words-referee-674d0f83ca3b`.
Snapshot digest:
`5f194544844405ff5f34b30b67d46783a6681d5dcd9e613d9868ceca69c19d76`.

This review began in a fresh context. I read the immutable source, precise
problem, claim, snapshot, and the listed mathematical and literature evidence.
I used actual primary-source passages for the source comparisons below. I did
not read the project checkpoint, scheduling state, earlier job transcripts,
or owner verdicts, and did not use proposer confidence as evidence. No agents
or additional model processes were used. All 16 frozen files and the canonical
snapshot digest matched their SHA-256 records; see `audit/referee-integrity.json`.
The frozen files were not edited.

## Reconstruction of the proof

Write `b_v = |B_v|` and `N_v = |D_v|`. For each vertex, the child descendant
sets and its own block form a disjoint partition of its descendant set:
`D_v = B_v disjoint-union (disjoint-union_c D_c)`. Consequently
`sum_c N_c = N_v - b_v`. This is the precise structural property used by
the proof. It holds for all the arbors in the frozen source.

Fix an arbitrary integer `m >= 0`. Let `F_v(x)` count nonnegative integer
vectors on `D_v`, by coordinate sum, subject to every upper subtree bound
`sum_(i in D_u) z_i <= m N_u` for `u` below or equal to `v`. It is a finite
polynomial of degree at most `m N_v`. Direct decomposition by blocks gives
\[
 F_v(x)=T_{\le mN_v}\left((1-x)^{-b_v}\prod_c F_c(x)\right).
\]
Here `(1-x)^(-b_v)` is used only as a formal series before a finite
truncation. At the root, `F_r(1)` is the lattice-point count in `m Q_tau`.
For positive `m`, the scaled inequalities describe `m Q_tau` by division
by `m`; for `m=0`, the nonnegativity and root upper bound force the zero
vector, consistently with `0 Q_tau = {0}`.

Define `G_v(y)` independently by enumerating vectors
`a in {0,...,m+1}^{D_v}` with all lower subtree bounds
`sum_(i in D_u) a_i >= N_u`, and weight
`y^(sum a_i) product_i binom(m+1,a_i)`. Its recurrence is
\[
 G_v(y)=T_{\ge N_v}\left((1+y)^{(m+1)b_v}\prod_c G_c(y)\right).
\]
Both recurrence interpretations follow from the original coordinate
conditions. In particular, the lower recurrence does not assume the desired
duality or the word formula.

The local identity used to link these recurrences is valid for all
integers `b >= 1`, `K >= 0`:
\[
 y^b\sum_{q=0}^K\binom{q+b-1}{b-1}(1+y)^{K-q}
 =T_{\ge b}(1+y)^{K+b}.
\]
I checked every coefficient symbolically. At degree `b+j`, for
`0 <= j <= K`, the left coefficient is
\[
 \sum_{q=0}^{K-j}\binom{q+b-1}{b-1}\binom{K-q}{j}
 =[z^{K-j}](1-z)^{-b}(1-z)^{-j-1}
 =\binom{K+b}{b+j}.
\]
Both sides vanish outside degrees `b,...,b+K`. This also checks the
potential boundary `K=0` directly. These are formal coefficient identities;
there is no convergence or interchange-of-limits issue.

To check the operator step without rational-truncation ambiguity, expand
`R(x) = product_c F_c(x) = sum_s r_s x^s`. For a vertex with `N=N_v`
and `b=b_v`, the degree bound gives `s <= m(N-b)`, hence
`K=mN-s >= mb >= 0`. The contribution of this monomial after upper
truncation and transformation is
\[
 r_s y^N\sum_{q=0}^{mN-s}\binom{q+b-1}{b-1}(1+y)^{mN-s-q}
 =r_s y^{N-b}T_{\ge b}(1+y)^{mN+b-s}.
\]
Summing and using
`y^(N-b) T_(>=b) P = T_(>=N)(y^(N-b) P)` proves operator identity (O)
of the candidate. Every exponent inside the truncation is nonnegative.
The step is linear and does not assume positive coefficients of `R`.
No infinite untruncated series is evaluated at `(1+y)^(-1)`.

Assume the transformation holds at the proper child subtrees. Their product,
with the block factor, is
\[
 (1+y)^{(m+1)b}\prod_cG_c(y)
 =y^{N-b}(1+y)^{mN+b}R((1+y)^{-1}).
\]
Applying the verified operator identity to this expression gives
\[
 G_v(y)=y^{N_v}(1+y)^{mN_v}F_v((1+y)^{-1}).
\]
The empty child product is `R=1`, so this is also the leaf step for every
nonempty leaf block. Induction on the finite rooted tree is therefore
valid. Multiplication clears all denominators since `deg F_v <= mN_v`.

At the root, extract the coefficient of `y^n`. The transformed expression
has coefficient `F_r(1)`: after removing `y^n`, its value at `y=0` is
`F_r(1)`. The independent interpretation of `G_r` gives exactly
\[
 |mQ_\tau\cap\mathbb Z^n|
 =\sum_{\substack{a\in\mathbb Z_{\ge0}^n,\ |a|=n\\
                   \sum_{i\in D_v}a_i\ge N_v\ \text{for all }v}}
       \prod_{i=1}^n\binom{m+1}{a_i}.
\]
Extending from the box to this finite set of contents is legitimate because
contents with `a_i > m+1` receive weight zero.

For the final conversion, a product of binomial coefficients counts subsets
of the `m+1` ordered boxes, one subset of size `a_i` for each letter `i`.
Reading each box in strictly decreasing order gives a word with exactly
`m` separating bars. Conversely the bars index the boxes, including all
empty boxes, and strict decrease ensures each letter gives a subset of box
indices. These constructions are mutually inverse.

For a fixed word `w`, every weak rise `w_j <= w_(j+1)` requires at least
one bar. There are `d(w)=n-1-des(w)` such gaps. After reserving one bar
in each required gap, the remaining `m-d(w)` bars can occupy any of the
`n+1` gaps, including both ends. The count is zero for `m<d(w)` and is
`binom(m-d(w)+n,n)` otherwise. Its formal generating series is
`t^d(w)/(1-t)^(n+1)`. Summing over the finite admissible content set
proves precisely the source identity, with ordinary descents and the
usual order on `[n]`.

## Adversarial checks and computational evidence

The proof covers `n=1`, `m=0`, `K=0`, absent letters, repeated letters,
arbitrarily large nonempty blocks, empty child products, and unrestricted
branching. At `m=0`, every `F_v=1` and every `G_v=y^(N_v)`; the word
side has exactly the descending permutation contributing to the constant
term. Equal adjacent letters require a bar. Leading, trailing, and repeated
bars are included. Numerical labels enter only in the word conversion,
which works for arbitrary interleaved labels.

The polytope contains `[0,1]^n`, so its dimension is `n`. The proof
establishes the counting series directly and does not rely on a
triangulation or an unverified Ehrhart formula. I also checked the cited
lattice-polytope statement in Chapoton, Lemma 1.2: its projection to the
product of the child polytopes and the affine simplex fibers give integral
vertices inductively.

I inspected `evidence/research_checks.py` and its serialized output, but did
not run its output-writing entry point against frozen evidence. Instead,
`audit/referee_checks.py` is a new standard-library verifier, importing no
proposer code. It reconstructs descendant sets from the blocks and parent
lists. Upper counts assign original coordinates and enforce the explicit
inequalities; lower counts enumerate the coordinate box directly; words
are enumerated literally with numerical descents. The upper and lower
enumerations do not use the subtree recurrences.

The command `python3 audit/referee_checks.py` completed successfully and
saved `audit/referee-checks.json`. Its exact finite coverage was:

| Domain | Checks performed | Result |
| --- | --- | --- |
| All rooted partition trees for `n=1,2,3,4` (respectively `1,3,16,133` trees) | Every `m=0,...,n`; entire upper/lower transformed distributions, binomial coefficient at degree `n`, word count, and numerator coefficients from finite differences | All 153 trees and 740 tree/dilation pairs pass |
| Three serialized six-label examples | Reconstructed descendant sets and word polynomials; every `m=0,1,2,3`; direct counts and full transformed distributions | All 12 pairs reproduce the supplied counts |
| One new seven-label example | Branching inside both top-level child subtrees, interleaved labels, and a non-singleton internal block; `m=0,1,2,3` | All four pairs pass |

The seven-label example has blocks `[[4],[1,6],[3],[7],[2],[5]]` and
parent list `[-1,0,0,1,2,2]`. Its independently enumerated word polynomial
has coefficients `(1,752,13727,42448,30674,4784,84)`, and the three counting
definitions all give `(1,760,19779,179456)` for `m=0,1,2,3`.
All arithmetic was exact and deterministic. These checks corroborate the
general argument; they are not its proof. No formal proof-assistant
certification is claimed.

## Primary-source comparison and contribution

The following are comparisons of actual inspected statements, not reliance
on search snippets or on the proposer's assessment.

| Primary source and inspected passage | Relationship to the frozen contribution |
| --- | --- |
| [Athanasiadis–Xiao–Yan, 2603.11654v1](https://arxiv.org/html/2603.11654v1), introduction, Theorem 1.5, Section 4, Conjecture 5.2 on printed p.13 | The conjecture is exactly the source statement. The theorem covers the octopus special cases. The fixed-content word identity is already used in Section 4. I also extracted p.13 directly from the frozen PDF. |
| [Athanasiadis–Chapoton, 2605.26916v1](https://arxiv.org/html/2605.26916v1), introduction, Conjecture 4.4, Proposition 4.5, Remark 7.3 on printed p.19 | The all-preorder conjecture contains the original arbor question. Remark 7.3 already gives the binomial-content reformulation. Proposition 4.5 requires a minimum vertex and uses modified ascents. I checked p.19 directly from the frozen PDF as well as the text and HTML. |
| [Chapoton, 2503.04247v2](https://arxiv.org/html/2503.04247v2), Lemma 1.2 and Section 2.1, Proposition 2.1, equation (8) and proof | Lattice integrality and the height recurrence are prior results. On replacing his root size by `b`, equation (8) is the candidate's upper recurrence. That passage does not supply the weighted lower recurrence or their intertwining. |
| [Athanasiadis, 2510.23903v3](https://arxiv.org/html/2510.23903v3), Section 4, Proposition 4.2 and proof | A composition-polytope formula uses strict ascents with an initial sentinel. It is the prior restricted formula credited by the candidate. |
| [Liu–Tang, 2605.08968v1](https://arxiv.org/html/2605.08968v1), family definition and Theorem 3.1 with its proofs | The chosen family has a singleton root and singleton leaves. Its generating-series proof uses height counting in that family, and does not provide the all-arbor transformation. |
| [Dai et al., 2608.16037v2](https://arxiv.org/html/2608.16037v2), Theorems 1.2/1.3 and the following comparison paragraph | These identify a support enumerator with the numerator of a different root polytope and prove support duality. I checked the same statements in the frozen HTML. |
| [Yan, 2608.15682v2](https://arxiv.org/html/2608.15682v2), Corollaries 5.3/5.4 and Section 5.3 definitions | The general preorder word formula is for `R_tau = Q_tau + Delta_E - 1`, with an auxiliary letter and a different ascent convention. It does not state the frozen formula for `Q_tau`. |
| [Menon, 2608.13247v1](https://arxiv.org/html/2608.13247v1), definition of `h(tau,t)` and Proposition 3.4 | The polynomial counts support sizes in the undilated polytope. Its gamma-positivity result for lopsided octopuses concerns a different assertion. |

In the arbor preorder the root is maximum. Every ideal is a disjoint union
of descendant subtrees, so the ideal inequalities of the May paper reduce
to the frozen subtree inequalities on both the upper and lower sides.
This confirms the identification of the original question inside that
paper; it does not extend this proof to arbitrary preorders.

The precise contribution is the compatible transformation between the two
subtree recurrences, and hence the full all-arbor consequence. It is not
the height recurrence, the binomial-series convolution by itself, or the
multiset-word identity. Resolving the stated conjecture gives a substantive
contribution without imposing an arbitrary restricted family. The
transformation also retains the full weighted subtree polynomial, rather
than merely an isolated count.

Live primary-source inspection and searches were performed on 2026-09-14.
The [March version history](https://arxiv.org/abs/2603.11654) and
[May version history](https://arxiv.org/abs/2605.26916) displayed only v1.
Searches combined the identifiers, conjecture/proof terms, and arbor,
Ehrhart, word, subtree, and truncation terms, with and without an arXiv
domain filter. Broad searches produced mostly irrelevant results and the
domain-filtered batch returned no results; neither is evidence of absence.
No equivalent proof was found in the primary passages inspected here.
This is a bounded comparison, not a priority guarantee or a full-paper
audit of every comparator. The supplied duplicate-registry predicates
concern other support-polynomial assertions; I did not inspect the full
external registries.

## Decision and remaining scope

No mathematical gap requiring revision was found in the frozen argument.
Scope, correctness, and contribution pass. Acceptance applies to the exact
original all-arbor assertion and its stated binomial reformulation, without
changing `claim.json` or any decisive evidence. Arbitrary preorders and
separate real-rootedness or support-polynomial conjectures remain outside
this accepted claim.

No manuscript or release artifact was prepared in this referee job. The next
workflow step is the runner's mathematical integrity/provenance gate, followed
by manuscript preparation preserving the scope and prior-result attributions
above. This local mathematical review is not journal peer review or a formal
machine proof.
