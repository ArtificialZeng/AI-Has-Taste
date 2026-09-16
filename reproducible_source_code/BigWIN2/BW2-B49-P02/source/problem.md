# Precise problem reading

Provenance: triage job `win-00049-p02-triage-ac4f3c27efd5`, 2026-09-07.  The
immutable statement is `source.md`; this file fixes notation and the
interpretation used for subsequent computation.

## Finite game and quantifiers

Put \([3]=\{1,2,3\}\), \(C=\{0,1\}\), and
\[
\Omega=S_3\times C^{[3]}.
\]
Thus \(|\Omega|=6\cdot 2^3=48\).  Canonically encode
\((\sigma,\kappa)\) by the permutation word
\(\sigma(1)\sigma(2)\sigma(3)\), followed by the bit word
\(\kappa(1)\kappa(2)\kappa(3)\).  The color is attached to a *value* (rank),
not to a position.

A secret and every legal guess both lie in \(\Omega\).  For a guess
\(g=(\gamma,c)\) and secret \(x=(\sigma,\kappa)\), the complete feedback is
the subset
\[
F(g,x)=\{i\in[3]:\gamma(i)=\sigma(i)\text{ and }
c(\gamma(i))=\kappa(\sigma(i))\}\subseteq[3].
\]
In particular, \(F(g,x)=[3]\) if and only if \(g=x\).

A deterministic adaptive strategy \(\mathcal S\) chooses its round-\(t\)
guess in \(\Omega\) as a function of all feedback from rounds
\(1,\ldots,t-1\) (equivalently, of the full legal history; impossible
histories may be assigned arbitrarily).  Define
\[
T_{\mathcal S}(x)=\min\{t\geq1:g_t=x\},
\]
with value \(\infty\) if the secret is never guessed.  For every integer
\(r\geq1\),
\[
N_r=\max_{\mathcal S}\#\{x\in\Omega:T_{\mathcal S}(x)\leq r\}.
\]
This is the maximum uniform-distribution success count.  Randomization cannot
increase it: the success count of a randomized strategy is an average of the
counts of deterministic strategies after its internal randomness is fixed.

The frozen claim asks whether the Kutin--Smithline two-color
`CircularShift` strategy \(\mathcal C\) satisfies, simultaneously for every
\(r\geq1\),
\[
\#\{x:T_{\mathcal C}(x)\leq r\}=N_r.
\]
If it does, compute all \(N_r\) through saturation.  If it does not, find the
least failing horizon and give an explicit superior strategy tree.  No claim
for other \(n\), other numbers of colors, or repeated-rank guesses is included.

## CircularShift benchmark

For the interpretation matching Definition 4.3 and Lemma 4.4 of the current
arXiv version of Kutin--Smithline, start with \(\gamma_1=123\) and
\(c_1\equiv0\).  After feedback \(U_r\), retain the entries at positions in
\(U_r\) and cyclically move the remaining ranks one step to the right through
the increasing list of remaining positions.  A moved rank's color counter is
incremented when that rank completes a circuit past its starting position, as
specified in their Definition 4.3.  In the two-color instance the guesses used
before solution have colors in \(C\).

Their proved cost formula is
\[
T_{\mathcal C}(\sigma,\kappa)
=1+\operatorname{exc}(\sigma)+\kappa(1)+\kappa(2)+\kappa(3),
\qquad
\operatorname{exc}(\sigma)=\#\{i:\sigma(i)>i\}.
\]
Since the excedance enumerator of \(S_3\) is \(1+4z+z^2\) and the color-sum
enumerator is \((1+z)^3\), the established exact completion-count benchmark is
\[
(1+4z+z^2)(1+z)^3
=1+7z+16z^2+16z^3+7z^4+z^5.
\]
Consequently CircularShift solves exactly
\[
(1,7,16,16,7,1)
\]
secrets in rounds \(1,\ldots,6\), and its cumulative counts are
\[
(1,8,24,40,47,48).
\]
These are prior results about this named strategy, not evidence that the values
are globally optimal.  The original claim is therefore equivalent to proving
\(N_r=(1,8,24,40,47,48)_r\) for \(1\leq r\leq6\); after \(N_6=48\), all later
values are automatically 48.

## Exact Bellman target

For \(A\subseteq\Omega\), \(g\in\Omega\), and \(u\subseteq[3]\), put
\[
A_{g,u}=\{x\in A:F(g,x)=u\}.
\]
Let \(V_0(A)=0\).  The unpruned recurrence covering every legal adaptive
strategy is
\[
V_r(A)=\max_{g\in\Omega}\left(
 |A_{g,[3]}|+\sum_{u\subsetneq[3]}V_{r-1}(A_{g,u})
\right)\qquad(r\geq1).
\]
Here \(|A_{g,[3]}|\leq1\), and the nonterminal feedback cells are disjoint, so
their optimal continuation values add.  The desired values are
\(N_r=V_r(\Omega)\).  A certificate may quotient states by symmetries only if
it supplies the action on secrets and guesses, feedback preservation, and a
replayable mapping for every omitted state.

## Literature position and version note

Primary sources inspected on 2026-09-07:

- Kutin--Smithline--Vatter, arXiv:2609.01874v1, Theorem 10 and Section 7,
  <https://arxiv.org/html/2609.01874v1>.  The theorem proves strong optimality
  for the monochrome game; Section 7 separately states the multicolor
  extension as conjectural and cites a multicolor work “in preparation.”
- Kutin--Smithline, arXiv:2408.00903v1,
  <https://arxiv.org/html/2408.00903v1>.  Section 4 defines suited Permutation
  Wordle and Conjecture 4.2 asserts horizon-by-horizon optimality; Section 5
  lists it as open.
- Kutin--Smithline, arXiv:2408.00903v3,
  <https://arxiv.org/html/2408.00903>.  Definition 4.1 gives multicolor
  permutations, Definition 4.3 gives the updated strategy, Lemma 4.4 gives the
  displayed cost formula, Conjecture 4.5 states strong multicolor optimality,
  and Section 7 still lists the question as open.

The labels “Definitions 4.1 and 4.3, Lemma 4.4, Conjecture 2.2, and Section 7”
in `source.md` align with v3 rather than v1 of arXiv:2408.00903.  This is a
bibliographic/version mismatch, not an ambiguity in the finite game above.
The current-v3 algorithm and formula are used for the named benchmark; the
v1 two-color count recurrence gives the same six completion counts.  No
primary source located in the exact-assertion searches above proves or
disproves the \((n,s)=(3,2)\) finite optimality claim itself.

## Proposed contribution

Nearest prior result: the exact CircularShift distribution above and a general
conjecture of its optimality.  Proposed delta: a complete, independently
replayable determination of \(V_r(\Omega)\) for \(1\leq r\leq6\), with either
equality to the benchmark at every horizon or the least counterexample
horizon and a superior tree.  Verification route: exhaustive exact-mask
Bellman computation followed by a separately implemented certificate replay.
