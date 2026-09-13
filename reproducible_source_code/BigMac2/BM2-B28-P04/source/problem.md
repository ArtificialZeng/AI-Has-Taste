# Precise problem: the label-realization radius at `(h,k)=(4,4)`

## Frozen source and mathematical objects

The immutable task is `source.md`. Its notation is read as follows. For a finite
set `A \subset \mathbb Z` and an integer `h\ge 1`, repetitions are allowed in

\[
hA=\{a_1+\cdots+a_h:a_1,\ldots,a_h\in A\}.
\]

For integers `h,k\ge 1`, define the set of attainable **labels**

\[
\mathcal R(h,k)=\{|hA|:A\subset\mathbb Z,\ |A|=k\}.
\]

For `D\in\mathbb Z_{\ge0}`, put

\[
\mathcal R_D(h,k)=
\{|hB|:B\subseteq\{0,1,\ldots,D\},\ |B|=k\}.
\]

Shin's diameter-compression parameter is

\[
\nu(h,4)=\min\{D\in\mathbb Z_{\ge0}:
\mathcal R_D(h,4)=\mathcal R(h,4)\}.
\]

Equivalently, `N(h,4)=nu(h,4)+1` when `N` denotes the number of integer
positions in the interval `[0,N-1]`. This is an off-by-one convention, not a
change of invariant.

## Exact quantified question

Determine the unique value `D\in\{15,16}` satisfying

\[
\forall A\subset\mathbb Z\ (|A|=4)\quad
\exists B\subseteq\{0,\ldots,D\}\ (|B|=4)\quad |4B|=|4A|,
\]

with `D` minimal. Thus:

- `nu(4,4)=15` means every attainable cardinality of a four-fold sumset of a
  four-element integer set has *some* four-element witness in `[0,15]`.
- `nu(4,4)=16` means there is an integer `n` and a four-element integer set
  `A` with `|4A|=n`, but no four-element `B\subseteq[0,15]` with `|4B|=n`;
  the cited upper bound then supplies representatives in `[0,16]` for all
  labels.

The representative `B` need not preserve the ordering, individual sum
equalities, or addition-table type of `A`; only the single integer label
`|4A|` must agree. In particular this is not the weak-type radius `H_4(4)`.
Translation, reflection, and multiplication by a nonzero integer preserve a
label, but the definition above quantifies over literal four-subsets of the
stated interval.

## Prior result and finite reduction

Henry Shin, *Iterated-sumset spectra: The complete exponent law and its rank
geometry*, arXiv:2609.01690v1, defines `nu(h,4)` immediately before Corollary
10.5. That corollary gives

\[
D_h^{\max}\le\nu(h,4)\le\max\{h^2,D_h^{\max}\},
\qquad
D_h^{\max}=\binom{h+2}{2}+\mathbf 1_{2\nmid h}.
\]

Consequently `D_4^{max}=15` and `15\le nu(4,4)\le16`. Shin explicitly leaves
open whether `nu(h,4)=D_h^{max}` for every `h\ge2`. Enkai Zhang,
arXiv:2609.08915v1, Remark 5.2 and Question 12.5, restates this distinction and
open question. Both primary texts were inspected on 2026-09-09; the exact
assertion search performed in this triage found no separate resolution, which
is not a claim of priority or exhaustive literature coverage.

Corollary 10.5 makes the present instance a finite exact test. It proves
`\mathcal R(4,4)=\mathcal R_{16}(4,4)`. Therefore

\[
\nu(4,4)=15\iff\mathcal R_{15}(4,4)=\mathcal R_{16}(4,4),
\]

whereas any element of
`\mathcal R_{16}(4,4)\setminus\mathcal R_{15}(4,4)`, together with its
four-set witness, proves `nu(4,4)=16`. Exhaustively forming four-fold sums for
all `\binom{16}{4}=1820` sets in `[0,15]` and all `\binom{17}{4}=2380` sets in
`[0,16]` is therefore a complete decision procedure, provided its exact data
and coverage are independently checked.

## Scope and proof standard

The requested resolution concerns only `(h,k)=(4,4)` and does not settle
Shin's all-`h` question. A computation must use exact integer arithmetic,
enumerate every four-subset in both finite intervals, record the resulting
label sets and witnesses, and be independently replayable or audited. A
floating-point experiment, solver status, or comparison of weak types is not a
proof.
