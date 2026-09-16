# Fresh mathematical referee report

## Verdict

**Accept** the exact frozen `resolution-paper` claim.  Within the game and the
operational CircularShift interpretation stated in `claim.json`, the exhaustive
certificate proves the six optimal success counts, and the separately replayed
strategy transcripts prove simultaneous attainment.  This verdict does not
extend to the inconsistent displayed color-update cases in Definition 4.3, to
larger instances, or to a claim of priority over unavailable work.

## Frozen scope and integrity

I reviewed `source.md`, `problem.md`, `claim.json`, `audit/snapshot.json`, and
every file enumerated by that snapshot, without using an earlier review or an
owner verdict.  The SHA-256 digest of every frozen file agrees with the snapshot;
the snapshot digest is
`aaa8e989a58a45c6ac2db36bfb7537d8ef466a65f1547557a17f20db1118fa01`.

The scope is the 48-secret, 48-guess game
\(S_3\times\{0,1\}^{[3]}\), with colors indexed by values and feedback equal to
the positions where both value and its color agree.  The candidate asserts the
full original finite conclusion, not a subsidiary result: it determines every
\(N_r\) through saturation and proves attainment by one explicitly defined
CircularShift strategy.  The claim expressly restricts “CircularShift” to the
circuit-completion interpretation supported by the source's operational prose,
Figure 6, and the proof of Lemma 4.4; it expressly excludes equivalence with the
conflicting displayed cases of Definition 4.3.

## Reconstruction of the Bellman proof

For a viable set \(A\), guess \(g\), and response \(u\), let
\(A_{g,u}=\{x\in A:F(g,x)=u\}\).  If \(u=[3]\), the response cell is either
empty or the singleton \(\{g\}\), because a legal guess has full feedback
exactly against itself.  Therefore the exact finite-horizon value satisfies
\[
 V_0(A)=0,\qquad
 V_r(A)=\max_{g\in\Omega}\left(1_{g\in A}+
       \sum_{u\subsetneq[3]}V_{r-1}(A_{g,u})\right).
\]
The lower bound follows by choosing an optimal continuation independently in
each observed nonterminal cell.  For the upper bound, the first guess of any
deterministic strategy is one of the 48 legal guesses, and restricting that
strategy to each response cell yields at most the corresponding child value.
Induction on \(r\) proves equality.  Dependence on the viable set is sufficient:
two histories with the same set have the same remaining secrets, legal actions,
feedback partitions, and success objective.

The discovery program represents sets by exact 48-bit masks and evaluates all
48 actions at every memoized nonempty state.  It uses no floating point,
symmetry quotient, dominance rule, or pruning cutoff.  More importantly, I ran
the separate replay checker afresh.  That checker does not import the solver: it
reconstructs the canonical universe, recomputes all 2,304 guess-secret responses,
checks the serialized response table, and validates every dependency bottom-up.
At each of the 98,898 certificate states it recomputes all 48 action scores, so
the check establishes the maximum rather than merely replaying a selected
action.  The run checked 4,747,104 state-action scores, found no missing
dependency, and returned
\[
 (V_1(\Omega),\ldots,V_6(\Omega))=(1,8,24,40,47,48).
\]
The state counts by horizon were
\((48645,37125,10743,2143,241,1)\).  The root decompositions are consistent
with these values; for example, for the normalized first guess `123-000`, the
eight response-cell contributions at horizon 4 are
\(21,5,5,1,5,1,1,1\), totaling 40.  Since \(V_6(\Omega)=48\), monotonicity and
the 48-secret upper bound give \(N_r=48\) for all \(r\ge 6\).

## Reconstruction of CircularShift attainment

The operational rule keeps feedback positions fixed, cyclically shifts the
other ranks to the next active position, and increments a moved rank's color
exactly when its clockwise arc crosses that rank's identity position.  Equality
of old and new active position (the singleton-active case) represents a full
circuit.  This is a deterministic rule based only on the current guess and
feedback.

I ran the transcript checker afresh on a temporary copy of the frozen transcript
files, so the snapshot evidence was not rewritten.  The checker independently
parses the guesses, recomputes all 168 feedback sets and all 120 nonsolving
successor transitions, and verifies all 48 canonical secrets.  Every submitted
guess is a permutation with colors in \(\{0,1\}\), including singleton-active
transitions, so the strategy never leaves the legal alphabet in this instance.
The completion times agree secret by secret with
\[
 1+\operatorname{exc}(\sigma)+\sum_i\kappa(i),
\]
and give exact-round counts
\((1,7,16,16,7,1)\), hence cumulative counts
\((1,8,24,40,47,48)\).  The longest transcript, for `231-111`, consists of the
six legal guesses `123-000`, `312-000`, `231-000`, `123-111`, `312-111`, and
`231-111`; it also checks the saturation endpoint directly.

Combining this attainment with the Bellman upper bounds proves strong
distributional optimality simultaneously for every horizon.  Randomized
strategies do not enlarge the uniform success count, because fixing their
random bits gives deterministic strategies and averaging cannot exceed the
deterministic maximum.

## Primary-source comparison and discrepancy check

The frozen arXiv:2408.00903v3 PDF defines the same value-colored feedback in
Definition 4.1 and the paragraph following it, states the completion-time
formula in Lemma 4.4, and states horizon-by-horizon multicolor optimality as
Conjecture 4.5.  Its Section 7 continues to list the optimality question as
open.  The frozen arXiv:2609.01874v1 PDF proves strong optimality only for the
monochrome game (Theorem 10); its Section 7 calls the multicolor analogue a
conjecture and cites a work “in preparation.”

The candidate's warning about Definition 4.3 is correct and material.  For the
secret `213-000`, first feedback to `123-000` is \(\{3\}\).  The displayed
cyclic color condition increments rank 2 and produces `213-010`, whereas the
circuit-completion rule produces `213-000` and solves in round 2, as both the
Lemma 4.4 formula and the frozen transcript record.  Conversely, the proof of
Lemma 4.4 gives the crossing conditions \(a_j<i\le a_{j+1}\) for a noncyclic
move and \(i>a_\ell\) or \(i\le a_1\) for the wrap move, exactly the operational
rule checked here.  The six Figure 6 guesses are also independently replayed by
the transcript verifier.  Thus the accepted statement is the exact disclosed
operational interpretation in the frozen claim; publication must retain that
disclosure and must not state that the displayed cases are equivalent.

## Contribution and remaining limitations

The nearest frozen primary sources supply the CircularShift distribution and a
general conjecture, but not this exhaustive \((n,s)=(3,2)\) optimality result.
The older paper mentions Hiveley's proof of its monochrome Conjecture 2.2 for
horizons at most three; it does not provide the present two-color finite proof.
The certificate here supplies both attainment and upper bounds through all
decisive horizons, including four, five, and six.  The complete finite
resolution is therefore a nontrivial delta at the precise requested scope.

No mathematical gap remains in the frozen theorem.  Two limitations remain and
must be stated as limitations rather than conclusions: the formal display in
Definition 4.3 is inconsistent with the accepted operational strategy, and the
unavailable multicolor work in preparation prevents an unqualified priority
claim.  Neither limitation affects the correctness of the exact frozen finite
claim or its exhaustive certificates.
