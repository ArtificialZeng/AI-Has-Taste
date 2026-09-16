# Precise reading: minimal job count for an unsafe PI-B&B-H fathoming event

## Frozen question and status

The immutable statement is `source.md` (SHA-256
`1484e4a27d89eec927211cd209f805448a778efe887644e8e61611af2cf4b2ad`).
This document formalizes it; it does not replace or strengthen it.

The source status is **new-question / status-uncertain**. The nearest primary
result inspected is Alberto Locatelli, Jean-François Côté, and Leandro C.
Coelho, *An Exact Combinatorial Branch-and-Bound Algorithm for the Job
Sequencing and Tool Switching Problem*, arXiv:2609.03219v1 (2 September
2026), <https://arxiv.org/abs/2609.03219>. Sections 3, 4.2, and 6.3 were
inspected in the arXiv HTML on 7 September 2026. Section 6.3 gives an unsafe
event with five jobs but states no minimality theorem. Targeted searches for
the exact rule and a four-job/minimal-job result found no equivalent result;
this limited search is not a priority or open-status proof.

## Admissible normalized instances

An instance is a tuple

\[
 I=(n,m,c;(T_j)_{j\in J}),\qquad J=\{1,\ldots,n\},\quad
 T=\{1,\ldots,m\},
\]

with

\[
 1\le n\le4,\qquad 1\le m\le4,\qquad 1\le c<m,
 \qquad \varnothing\ne T_j\subseteq T,\quad |T_j|\le c,
 \qquad \bigcup_{j\in J}T_j=T.
\]

The last equality is the normalized reading of the primary SSP model: `T` is
the set of tools required by the instance. It also makes the paper's standing
condition that the required tools exceed capacity equivalent to `c<m`.
Unused all-zero tool columns are therefore not part of the frozen claim; if a
program generates them, their results must be reported separately as a
different literal reading rather than silently mixed into the certificate.
Repeated job toolsets are allowed. The constraints imply `m>=2`. Cases with
too few jobs to have a proper internal PI node are vacuous, but remain in the
quantified family.

Jobs and tools are labeled. Tool relabeling preserves all predicates. The
numeric job order matters in the fathoming test, so quotienting job relabelings
is valid only if every induced label order (and its orbit multiplicity) is
recovered.

## Exact tool-switch objective

A magazine configuration is a set `M subseteq T` with `|M|=c`. For a sequence
of distinct jobs `sigma=(sigma_1,...,sigma_l)`, a configuration sequence
`mathcal M=(M_1,...,M_l)` covers `sigma` when
`T_{sigma_i} subseteq M_i` for every `i`. Its transition cost is

\[
 z(\mathcal M)=\sum_{i=2}^{l}|M_i\setminus M_{i-1}|.
\]

Initial loading is not charged. Define

\[
 z_I(\sigma)=\min\{z(\mathcal M):\mathcal M\text{ covers }\sigma\},
 \qquad
 \operatorname{OPT}(I)=\min_{\pi\in S_J}z_I(\pi).
\]

KTNS is used to attain `z_I(sigma)` and to produce the configurations examined
by the rule. All costs and optima in the proposed certificate are exact
integers, not floating-point evaluations.

## PI insertion nodes and completions

The relevant tree is the paper's PI-B&B-H tree, not the prefix-extension tree.
Its root is an ordered pair chosen from a pair maximizing

\[
 |T_a\setminus T_b|+|T_b\setminus T_a|.
\]

At a node `sigma`, the next unsequenced job `j` maximizes

\[
 \min_{i=1,\ldots,|\sigma|}|T_{\sigma_i}\cup T_j|,
\]

and every insertion of `j` into one of the `|sigma|+1` positions is a child.
Reversal symmetry suppresses one of a sequence and its reverse. The paper
does not specify all root-orientation and maximizer tie breaks in the displayed
description. Accordingly, **reachable** means reachable under at least one
choice consistent with those rules and the reversal reduction. The
certificate must retain all such tie outcomes (or prove that a smaller
canonical representation recovers them). Depth-first child order does not
change reachability and is irrelevant here.

Only proper internal nodes are tested: `2 <= |sigma| < n`. The completions of
such a node are precisely

\[
 C_I(\sigma)=\{\pi\in S_J:\text{deleting }J\setminus J_\sigma
 \text{ from }\pi\text{ leaves }\sigma\}.
\]

This formulation records the insertion-tree meaning of completion and is not
the prefix meaning used by PE-B&B.

## Almost-exact fathoming and KTNS ties

For a KTNS-produced optimal configuration sequence
`mathcal M=(M_1,...,M_l)` covering `sigma`, define

\[
 F_I(\sigma,\mathcal M)\iff
 \exists i\in\{1,\ldots,l-1\}:\quad
 T_{\sigma_i}\subseteq M_{i+1}\ \text{ and }\ \sigma_i>\sigma_{i+1}.
\]

Section 6.3 fathoms `sigma` when this predicate holds. Let
`K_I(sigma)` be the set of configuration sequences obtainable by KTNS when all
unspecified equal-priority/filler choices are allowed. The paper passage
inspected does not give a deterministic KTNS tie convention, and the predicate
can in principle depend on the chosen optimal configurations. Therefore no
tie choice may be silently selected. Two exact variants must be reported:

- **possible-tie fathoming:** `exists mathcal M in K_I(sigma)` with `F_I`;
- **forced-tie fathoming:** `for all mathcal M in K_I(sigma)`, `F_I` holds.

If the implementation's actual global tie policy is recovered, its result is
the primary one; the two variants bound the ambiguity. Enumerating all optimal
configuration sequences is not automatically a substitute for enumerating
KTNS-reachable outputs unless their equality is proved.

A fathomed node is unsafe (for the chosen tie reading) exactly when

\[
 \exists\pi\in C_I(\sigma)\quad z_I(\pi)=\operatorname{OPT}(I).
\]

Thus unsafety concerns existence of one globally optimal completion in that
branch. It neither says that every completion is optimal nor that every
globally optimal branch is lost.

## Claim to resolve

For every admissible normalized instance `I` and every reachable proper
PI-B&B-H node `sigma`, the Section 6.3 rule does not fathom `sigma` unsafely.
Equivalently, whenever the applicable fathoming predicate holds, every
`pi in C_I(sigma)` has `z_I(pi)>OPT(I)`. The exhaustive result must be stated
separately for the possible-tie and forced-tie readings unless a unique actual
KTNS convention is established.

The cited paper supplies the nearest boundary point: for `n=5, m=4, c=3` and
`T_1={2,3}`, `T_2={1,3}`, `T_3={1,2}`, `T_4={3,4}`,
`T_5={1,4}`, it fathoms `(4,1,2,3)` although the completion
`(4,5,1,2,3)` is globally optimal with cost one. The proposed delta is a proof
that no such event occurs for `n<=4`, or one exact smaller counterexample.

## Bounded verification route

Enumerate the labeled instances directly (the largest raw row family has only
`(2^4-2)^4=38,416` four-job matrices before enforcing tool coverage), all full
orders, all reachable PI nodes including selection ties, and all KTNS tie
outcomes. Record exact optima, triggering indices, optimal completions, counts,
and a digest. A second independent implementation should replay the aggregate
negative certificate or any positive witness.
