# lit-260527617-p01 — exact minimum for the 3-out-of-5 picture-hanging word

## Immutable primary-source record

- Tom Verhoeff, *The k-out-of-n picture-hanging puzzle: shorter solutions for
  small k and n-k*, arXiv:2605.27617v1 (submitted 26 May 2026).
- Official abstract: <https://arxiv.org/abs/2605.27617v1>
- Official full text: <https://arxiv.org/html/2605.27617v1>
- Local PDF:
  `batches/inbox/primary-20260910-materials/2605.27617.pdf`, SHA-256
  `966846391fd29d0563aa095e0cadf675745b0025eebed249999d6c6e87b56527`.
- Author's official search-and-verification repository:
  <https://gitlab.tue.nl/t-verhoeff-software/picture-hanging-puzzles/>,
  screened at commit
  `c501b3d6df0fc4eaaf7932d440087d336cc863dd` (commit timestamp
  2026-05-26T20:47:58+02:00). A read-only snapshot is under
  `batches/inbox/primary-20260910-materials/picture-hanging-puzzles/`.
- Source locators: Definition and essential-removals criterion in Section 2;
  parity and symmetry quotienting in Section 6; the second question in
  Section 8.

This is a primary-literature fallback candidate admitted while the canonical
Chrome intake was unavailable. It is not a ChatGPT-generated batch and does
not consume or register batch 87.

## Frozen problem

Let `F_5=<x_1,...,x_5>` be the free group. For a subset
`S` of `{1,...,5}`, let `pi_S:F_5 -> F_5` be the endomorphism that sends
`x_i` to the identity for `i in S` and fixes the other generators. The length
`|w|` is the number of signed generators in the freely reduced word for `w`.

A word `w in F_5` solves the 3-out-of-5 picture-hanging problem (Demaine's
convention) when

1. `w` is not the identity;
2. `pi_S(w)` is the identity for every `S` with `|S|=3`; and
3. `pi_S(w)` is not the identity for every `S` with `|S|=2`.

The monotonicity argument in the source makes these size-three and size-two
tests equivalent to the full requirements: the picture falls after any three
or more nails are removed and remains hanging after fewer than three are
removed.

Determine the exact integer

`L(3,5) = min{|w| : w solves the 3-out-of-5 problem}`.

The main contribution must be the exact value, not merely another upper bound
or a nonexhaustive search. Classification of all minimizers modulo the source's
four symmetries is useful secondary output but is not required by the frozen
question.

## Nearest result and current certified window

Section 8 of arXiv:2605.27617v1 explicitly calls 3-out-of-5 the next smallest
open exact-minimum case and says it should be within reach with a more efficient
implementation. The paper proves that every nontrivial k<n solution has even
length and zero exponent sum in every generator. The official repository logs
a symmetry-quotiented exhaustive search finding no solution at lengths
2,4,...,16; the length-16 run took 16,455.54 seconds. Treat that log as prior
computational evidence, not as a new result and not as a certificate until its
code, completeness argument, and output are independently replayed or audited.

The one-step extension in Proposition 15, combined with the optimal
3-out-of-4 word of length 8 and a 2-out-of-4 word of length 16, gives a direct
finite upper bound of 34 before any junction cancellation. Thus the primary
source supports at least the provisional finite window `18 <= L(3,5) <= 34`.
The exact optimum within this window is not supplied.

As of the 2026-09-10 screen, the official arXiv record still showed only v1,
the official repository HEAD was the commit recorded above, and bounded
primary-source searches found no later exact resolution. This is an access and
coverage statement, not proof of worldwide priority or openness.

## Contribution boundary and certificates

An upper-bound certificate is an explicit freely reduced signed word. An
independent verifier must evaluate all ten size-three deletions to the identity,
all ten size-two deletions to nonidentity, and verify its reduced length.

An optimality certificate must exclude every shorter even length. Acceptable
routes include a proved-complete canonical augmentation, a SAT/SMT encoding
with independently checkable UNSAT certificates, or an analytic lower bound.
The four symmetries used in the source are generator relabeling, independent
generator sign flips, reversal/inversion, and cyclic rotation; any symmetry
reduction must prove that every equivalence class has a retained representative.

The cheapest decisive next test is an optimized, independently checkable
length-18 search. A found word immediately improves the upper bound and, when
combined with an audited no-solution-through-16 certificate, decides the exact
value. A complete length-18 exclusion raises the lower bound to 20 and gives a
precise next frontier, but alone does not resolve the frozen problem unless a
matching construction is also available. Fast falsification of any proposed
word is a single offending deletion: either a size-three deletion that remains
nontrivial or a size-two deletion that becomes trivial.

Finite logs, timeouts, floating-point hashes, or failure of a heuristic are not
proof of optimality. Record exact code version, domain, pruning lemmas, machine
and language versions, and replayable certificates separately from universal
claims.
