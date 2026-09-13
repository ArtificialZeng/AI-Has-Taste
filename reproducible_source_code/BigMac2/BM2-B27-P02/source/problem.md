# Precise problem reading

## Frozen input and notation

The immutable statement is `source.md` (SHA-256
`610cc9c263bff685d832a637955902eeac836f99bcce568b8fcc33ef3cf716e2`).
The word `square` there is read as the Cartesian-product symbol `\square`, as
in the cited paper.

Let

\[
V=\mathbb Z_8\times\mathbb Z_8
\]

and let `G=C_8 \square C_8` be the simple, undirected Cartesian product of two
8-cycles. Thus each `(i,j) in V` has exactly the four distinct neighbors

\[
(i+1,j),\ (i-1,j),\ (i,j+1),\ (i,j-1),
\]

with both coordinates reduced modulo 8. Coordinate representatives may be
chosen as either `0,...,7` or `1,...,8`, provided a certificate states its
choice.

For every initial set `S subseteq V`, define the synchronous 3-neighbor process
by

\[
I_0=S,\qquad
I_{r+1}=I_r\cup\{v\in V\setminus I_r:|N_G(v)\cap I_r|\ge 3\}.
\]

Its closure is `cl_3(S)=union_{r>=0} I_r`. The set `S` *percolates* exactly
when `cl_3(S)=V`. Define

\[
t_3(8,8)=\min\{|S|:S\subseteq V,\ \operatorname{cl}_3(S)=V\}.
\]

The requested determination quantifies over **all** subsets of the labelled
64-vertex torus; translations, reflections, rotations, or coordinate exchange
may reduce a search only when the reduction is proved exhaustive.

## Exact target and acceptable resolution

The cited bounds leave precisely the dichotomy

\[
t_3(8,8)\in\{22,23\}.
\]

To establish `t_3(8,8)=22`, it is enough to give a labelled 22-element set
`S` and its exact synchronous infection layers
`L_0=S`, `L_r=I_r setminus I_{r-1}` through the first `R` with `I_R=V`.
For an exact trace, each displayed layer must equal—not merely be contained
in—the set of all previously uninfected vertices having at least three
neighbors in the preceding infected set.

To establish `t_3(8,8)=23`, one must give a labelled percolating 23-element
set (with a directly checkable infection trace) and an independently
checkable exhaustive certificate that no 22-element set percolates. An
acceptable negative certificate must expose the exact finite encoding or
case tree and a proof artifact checked independently; if symmetry is used,
its orbit coverage and stabilizer cases must also be checkable. A solver's
`UNSAT` status, floating-point output, or an undocumented symmetry reduction
is not a proof.

The fixed-size exclusion is sufficient: bootstrap closure is monotone in the
initial set, so any percolating set of size below 22 could be enlarged to a
percolating 22-set. In any event, the cited perimeter bound already excludes
sizes at most 21.

## Nearest prior result and status

The local primary source
`/Users/mac/4prove-or-disprove-math/batches/literature/bigMac-27/2608.06133v1.pdf`
has SHA-256
`d5e8b1a28649cafea12d4b47fead8a692abb9ee1634a556cbd779d59276073e6`.
Its Theorem 3.1 (PDF p. 23) gives

\[
t_3(8,8)\ge \left\lceil\frac{8\cdot8+1}{3}\right\rceil=22.
\]

Because `8 congruent 2 (mod 6)`, Theorem 1.8 (PDF p. 3) supplies the matching
general upper bound plus one, namely `t_3(8,8)<=23`. Question 4.3 (PDF p. 38)
asks when the lower bound is strict and mentions the `8 x 10` torus, not the
`8 x 8` torus, as a strict example. Thus this source does not determine the
present value.

The official arXiv record inspected on 2026-09-09 was still v1:
<https://arxiv.org/abs/2608.06133>. Exact-assertion searches for `t_3(8,8)`
and equivalent `8 x 8` torus language found no separate primary resolution
in this bounded triage. That is only a limited negative search result, not a
novelty or open-status proof. The source status is therefore
**status-uncertain**, while the target remains suitable for exact finite
research.

## Bibliographic correction, without changing the source

`source.md` attributes arXiv:2608.06133v1 to Alexander Clifton and Noah
Kravitz Shaw under a different title. Both the hashed local PDF and the
official arXiv record instead identify **Neal Bushaw and Alexander Clifton**,
*3-Neighbor bootstrap percolation on two-dimensional grids*. The theorem
numbers and torus bounds cited in `source.md` do occur in that PDF, so this is
a bibliographic defect rather than an ambiguity in the mathematical target.

## Scope and proposed contribution

Only the fixed graph `C_8 \square C_8` and threshold 3 are in scope. The task
does not seek the full two-parameter classification in Question 4.3.

Nearest prior result X: the rigorous gap `22<=t_3(8,8)<=23`. Proposed delta Y:
close that one-unit gap exactly. Verification route Z: first search for a
22-set and independently recompute its synchronous closure; only if that
fails should a proof-producing exhaustive exclusion of all 22-sets be built.
