# Mathematical referee report

Verdict: **accept** the exact frozen candidate.

Referee job: `primary-20260912-stack22-mechanism-referee-32c0ca02578d`.
Snapshot: `e88196a982b3f9753e89f4a49e8403bae251c1bcd5b1e6c02ea924fa5cd490bd`.
Review date: 2026-09-12 UTC.
Frozen kind: `resolution-paper`. Frozen original status: `proved`.

The proof in `evidence/first_return_proof.md` supplies a complete direct
mechanism derivation for the original input-sorting problem, for every
integer n >= 0. The accepted contribution is its canonical operation
language, comparison forest, exact bit encoding, and unambiguous
first-return enumeration. The polynomial itself was already known.
This acceptance neither changes the claim nor substitutes a partial result
for its stated resolution scope.

## Inputs and review method

I read `source.md`, `problem.md`, `claim.json`, `audit/snapshot.json`, and
all 13 files listed as evidence in the claim/snapshot, including the four
programs and their recorded outputs. I inspected the relevant section of
the frozen Vatter HTML and checked the actual live source. I did not read
the checkpoint, scheduling state, earlier reports or transcripts, or any
unlisted local research evidence. No agents or other model processes were
used. Statements of proposer confidence played no evidentiary role.

All 14 snapshot file hashes, including `claim.json`, match. Independently
serializing the mapping as compact sorted-key JSON reproduces the snapshot
digest. The original source retains SHA256
`403df3b10d13461c45e5dfd74d1548350e575ce83ae62f17ab501428dc4855be`.
No frozen input was edited. The release contract was read in full before
creating `audit/math.json`.

The decisive assessment is the all-size argument reconstructed below.
Fresh exact programs provide finite checks of vulnerable steps; they are
not the basis for extending a finite observation to all sizes. This is a
fresh model review pass, not external peer review or statistically
independent evidence.

## Reconstruction of the proof

### Canonical sorting and counting objects once

Fix a state with next required output k and a successful continuation.
Before that continuation pops k, it can only push: any earlier pop would
already violate increasing output. If k is currently accessible, delete
it now and replay that initial push segment with k absent. For an old
insertion slot j, lower j by one exactly when k lies before the slot.
The resulting slot is still legal, including the singleton and empty
cases. At the original pop of k the two states coincide. Thus eager
output preserves success.

For a < b, consider a successful continuation from stack (b,a,T).
Until a is removed, neither a nor b can have been popped. Interchanging
their positions while applying all other rank operations preserves the
rest of the state. Immediately before a's removal in the original run,
b still precedes a. Since a is accessible, they must be exactly the
first two tokens. Removing a at rank 1 in the exchanged state, instead
of rank 2 in the original state, leaves identical stacks and outputs.
Consequently (a,b,T) is sortable whenever (b,a,T) is.

If no eager pop is possible, any successful continuation must push.
The two push choices create the two orderings of the same new top pair;
the smaller-top ordering preserves success by the preceding argument.
Induction on the remaining operations proves completeness of G. Its
soundness follows from its permitted operations and increasing output.
There are no equal-label cases because the inputs are permutations.

For any complete legal rank word, assign distinct tokens in push order
and label each token by its pop number. Reading these labels in push
order gives the unique input sorted by this word. On the G-selected
language this map is injective: the reconstructed input has only one
deterministic G trace. Completeness makes it surjective onto the sortable
inputs. Each push contributes exactly one input entry. This proves the
claimed object-preserving bijection without switching to generation.

### Comparisons, peaks, and the bit invariant

At each nonempty push, the greedy comparison demands that the upper
token of the new top pair precede the lower token in output order.
Direct that edge from the upper token to the lower token. A word uses
the correct push choices exactly when it respects all these comparisons.

In a G trace, a push immediately followed by a pop must push the next
required token. A push cannot bring an old inaccessible token closer to
the top. The new token is smaller than every remaining token, so the
peak is P1 Q1. Conversely, if every peak is P1 Q1, then at any moment
before a push, the next pop removes the last token of the ensuing push
run. That token has not yet arrived at the moment considered. Thus G
cannot pop at that moment. With the comparison condition, all the
word's operations are exactly G's operations.

The live edge graph is an ordered forest whose preorder is the stack.
P1 installs a root above the former first root; P2 adds a first child
to the first root. Q1 deletes that root and promotes its children.
For Q2, the second token is an independent root exactly when the first
root is a leaf; otherwise it is the first child of that root and has
an unmet incoming comparison. These observations prove necessity and
sufficiency of the allowed pops by induction on the prefix.

A surviving vertex cannot lose a child, because that child cannot be
removed first. Its leaf/nonleaf bit therefore needs no child count.
The four transitions in the claim follow exactly. The first bit after
a nonempty push is 1, so neither P1 Q2 nor P2 Q2 is possible. From an
empty stack, Q2 is unavailable by height. Excluding P2 Q1 therefore
leaves precisely the required peaks. This verifies the entire claimed
bit language at arbitrary depth, not just at a tested depth.

### First-return interface and unambiguity

Let the positive floor be h, with one top token followed by a protected
suffix. A first-return excursion stays at height at least h+1 until
closure. The suffix below that initial top is untouched. More precisely,
after the opening push the stored second token and the suffix are below
the interior's floor: a pop that could reach that stored token would
already close the excursion. Pushes only modify the active top bit or
insert above that stored part. This proves the claimed context
independence. Token identity at the endpoint is unnecessary; the top
bit is sufficient.

An opening P1 stores the old top bit a; an opening P2 stores 0.
Both leave active top bit 1. A closing Q1 restores the stored bit.
A closing Q2 requires the interior endpoint to be 0, and retains that
0 while deleting the stored token. If the interior is empty, P2 Q1
is excluded. Induction on length proves that a path from bit 0 cannot
return as bit 1; it would require a shorter such interior path.

The opening/interior/closing possibilities are therefore exactly:

| First return | Interior | Endpoint behavior |
| --- | --- | --- |
| P1 ... Q1 | B or C | preserves initial bit |
| P1 ... Q2 | B | returns 0 |
| P2 ... Q1 | B or nonempty C | returns 0 |
| P2 ... Q2 | B | returns 0 |

This is precisely E and D in the frozen proof. First returns give
A = epsilon + (E + D)A, C = epsilon + EC, and B = EB + DA.
For an empty-stack path, the first push is P1 and the final pop of
its first component is Q1; its interior is A. Hence
L = epsilon + P1 A Q1 L.

The height profile fixes the first-return position, interior, and
remaining suffix. The first and last ranks distinguish the alternatives
except P2 ... Q1, where the deterministic interior endpoint distinguishes
B from C. Induction gives unique parses. Conversely each production
respects its bits, floor, and peak restriction. New concatenation
boundaries are pop-push boundaries; an empty interior creates only the
explicitly handled peaks. Thus both completeness and absence of extra
or duplicated words are proved. A formal initial bit 1 in an auxiliary
language causes no physical-state assumption: the languages are defined
in the abstract bit machine, and L starts in the actual empty state.

### Formal power series

Weight pushes by x. The grammar gives e=x(B+C), d=x(3B+C-1),
A=1+(e+d)A, C=1+eC, B=eB+dA, and F=1+xAF.
The subtraction removes only the forbidden empty C interior. Every
nonempty excursion has a push, so these are productive recursive
equations with finite coefficients and the stated constant terms.

All inverses used in the proof are units of Z[[x]]. Specifically,
A=(1-e-d)^(-1), C=(1-e)^(-1), and B=dAC=A-C.
Thus B+C=A, and both C and F equal (1-xA)^(-1). This yields exactly

    F = 1 + xAF,
    A = 1 + xA(4A-2F-1).

The displayed residual identity eliminates A without dividing by x.
I checked it independently as an exact polynomial identity. It gives

    2xF^3-(2x+3)F^2-(x-7)F-4 = 0.

Writing F=1+H turns the left side into
H-3H^2+x(-1+H+4H^2+2H^3). Since H has constant term zero,
its coefficient at each new positive degree has multiplier 1, with
all other terms determined by earlier degrees. This proves uniqueness
of the formal branch with F(0)=1 over the integers. The empty word
contributes exactly u_0=1. No analytic convergence, limit exchange,
positivity assumption for a formal inverse, or excluded size is needed.

## Independent finite checks actually performed

The new programs import no candidate implementation and do not execute
any candidate program's output-writing main function.

`python3 audit/referee_verify.py` completed and saved
`audit/referee_verify.json`. It checks:

* All 46,234 permutations across 0 <= n <= 8. A memoized search explores
  the original legal push/pop choices as needed to decide sortability,
  permitting both pushes even when a pop is available. It uses neither
  normalization lemma. Across all inputs it visits 11,774,156 states.
  Exact sortability and a separately implemented G agree everywhere.
* Complete bit words through n=8, generated with an integer bit stack,
  agree objectwise with the G traces, with unique reconstruction and
  exactly one complete grammar parse. Their serialized trace hashes
  match the frozen observations. Counts are
  1,1,2,6,24,116,628,3636,21956.
* Every positive-floor bit word through n=7 has the predicted endpoint
  and unique A/B/C parse. The languages from initial 0 and initial 1
  have the same word sets, split by the latter endpoint as claimed.
* Through n=5, all auxiliary words are replayed with every protected
  suffix of length 0 through 3, for 13,860 cases. Both the suffix bits
  and its token identities survive unchanged; endpoint bits agree.
* An independent coefficient recursion from the expanded cubic agrees
  with every frozen F coefficient through degree 40.

`python3 -B audit/referee_grammar_attack.py` completed and saved
`audit/referee_grammar_attack.json`. Unlike a test of only accepted
machine words, it enumerates all legal rank words at floor 0 through
n=6 and floor 1 through n=5, including words rejected by the bit rules.
Across 107,848 words, grammar parse multiplicities equal the appropriate
0/1 bit-language membership indicators. Thus it finds no missing,
spurious, or ambiguous parses in those ranges.

The same program verifies the residual polynomial identity on a
3 by 3 by 4 integer grid. Its separate degree bounds in (x,A,F)
are at most (2,2,3), as checked directly from the displayed factors.
Repeated univariate interpolation therefore makes this an exact
identity certificate, not an empirical numerical spot check.

The proposer's held-out n=9 artifact was inspected but not independently
recomputed in this pass. No independent n=9 coverage is claimed. The
fresh checks above and the all-size proof are kept distinct.

## Source comparison, contribution, and limits

The frozen HTML and the live [Vatter problem list, Section 5](https://arxiv.org/html/2602.16355v2#S5)
agree on the model. Theorem 5.9 attributes the basis to Atkinson;
the text before Problem 5.11 reports Pantone's basis-derived cubic
through Combinatorial Exploration. Problem 5.11 asks for a derivation
from the stack mechanism. The candidate proves precisely that additional
method statement, rather than inferring the equation from coefficients.
Its forest compression and finite first-return interface supply a
substantive explanation absent from the stated basis-derived result.

The live [source-author OEIS entry A393395](https://oeis.org/A393395/internal)
confirms the known model, coefficients, and equation including the
constant term. Neither the equation nor its coefficient sequence is
accepted as a new discovery.

I searched the exact phrases `(2,2)-stack` with `first-return`,
`generating function direct`, and `Problem 5.11`, as well as
`2,2-stack permutations enumeration` and `stack comparison forest
permutations`. The relevant retrieved primary records were the Vatter
problem list and its source-author OEIS record; no equivalent direct
derivation was identified. This is a bounded current comparison, not a
proof of global priority or an exhaustive literature review.

The [author-posted Atkinson PDF](https://www.researchgate.net/profile/M-Atkinson/publication/220357801_Generalized_Stack_Permutations/links/00b49514bc2c99ffbf000000/Generalized-Stack-Permutations.pdf)
was recognized as a nine-page PDF. The extracted text inspected was
garbled, and screenshot requests for pages 7--9 each returned a cache
miss. I do not claim to have read its full proof. Pantone's actual
exploration specification was also not inspected. Their proofs are
not mathematical dependencies here: all normalizations, comparisons,
language correspondences, and enumerative steps used by the candidate
are proved in the frozen argument. Historical statements should remain
attributed to Vatter, and stronger claims about the contents of those
prior works require readable primary checking in the citation phase.

These source-access limits do not supply mathematical evidence and
do not establish novelty by absence. The contribution passes at its
stated, limited historical scope: a self-contained direct solution of
the explicitly documented mechanism request, with the enumerative
identity acknowledged as known.

## Decision and next action

No unresolved mathematical gap was found in the frozen all-size
mechanism derivation, bijection, grammar, or formal-series elimination.
Correctness, full original scope, and a substantive method contribution
pass. **Accept**, with `candidate_kind=resolution-paper` and
`original_status=proved` unchanged from `claim.json`.

No substantive revision is requested. The runner should check the
snapshot/provenance binding with `check-math` before dispatching writing.
The later manuscript and citation reviews should preserve the known-result
attribution and bounded literature language stated above. Any substantive
change to the claim or decisive proof requires a new snapshot and fresh
mathematical review. No manuscript, PDF, or release was created here.
