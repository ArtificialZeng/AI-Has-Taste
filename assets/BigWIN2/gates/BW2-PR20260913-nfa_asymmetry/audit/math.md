# Independent mathematical referee report

Verdict: **accept** the exact frozen `result-note` scope. The original problem
has status **unresolved**. No substantive claim or proof revision was made in
this review.

Job: `primary-20260913-nfa-asymmetry-referee-b2eca8229032`.
Review date: 2026-09-13, Asia/Shanghai.
Snapshot: `53dbff552fb4849eeba8f68fd2927ad5858490588792e71c8b44f2c188b7bd7b`.

The accepted assertion is precisely that, for every integer q >= 3, the maximum
directional NFA separation cost over distinct equal-length words
`0^a 1 0^b` and `0^c 1 0^d`, with all four exponents nonnegative and reverse
cost at most q, is `(q-1)^2+2`, and this maximum is attained. The model has one
initial state, an arbitrary accepting subset, partial transitions, and no
epsilon transitions. The lower bound for unrestricted A(q) is a corollary;
the asymptotic growth of unrestricted A(q) is not determined.

## Evidence and independence

I read the frozen original, precise interpretation, claim, snapshot, and the
listed proof, diagnostic artifacts, and relevant primary-source passages.
I did not read checkpoint.md, state.json, earlier job transcripts, unlisted
project research files, or prior referee decisions. Statements of the
proposer's confidence or absence of gaps were not used as evidence. No agent,
other Codex process, or background worker was spawned.

All 18 frozen file hashes and the canonical digest of their mapping were
recomputed and matched; see `audit/referee-integrity.json`. In particular,
source.md has SHA-256
`943c1349d18c0b8a8565a1a2143f82a664d2922c2cdf0acebf78e95bf66fb34d`.
No frozen file was edited. The research script was inspected but not rerun,
since it writes a frozen output file. The independent implementation is
`audit/referee-checks.py`; its results are `audit/referee-checks.json`.

## Reconstruction of the upper bound

Let `H=(q-1)^2+1` and `L=lcm(1,...,q)`. The sole imported theorem is that
every binary relation R on q > 1 points has entered its eventual periodic
part by exponent H. I checked the Russian printed statement in Schwarz,
*Sums of Powers of Binary Relations* (1974), p.167, against the definition of
the group of powers on p.161. It says the H-th power belongs to that group
for every binary relation. The quantifier is not restricted to irreducible
or primitive relations. Both PDF text and the listed images were inspected.
The [primary bibliographic record](https://www.dml.cz/handle/10338.dmlcz/126603?show=full)
confirms the paper and its reference to Schwarz's 1970 work. The original
1970 proof was not reviewed; using the author's explicit published account
as a classical dependency is adequate here.

For any walk of length t >= q, a repeated vertex supplies a simple directed
cycle of length h <= q. Inserting L/h extra traversals gives
`R^t subseteq R^(t+L)`. For t >= H >= q, let d be an eventual period. The
successive inclusions with step L end, after d steps, at
`R^(t+dL)=R^t`. Thus each inclusion is equality. Consequently two exponents
at least H that are congruent modulo L give identical powers. This derivation
does not assume the desired period as an additional theorem. Padding a smaller
NFA with isolated unreachable states is legitimate.

Now put Delta=a-c; equal length gives b-d=-Delta. If L does not divide Delta,
some r in {2,...,q} does not divide it. An r-state zero-cycle, a one-edge
only at residue a mod r, and a new accepting zero-loop state separate the
requested orientation with r+1 <= H+1 states. The distinct final state keeps
the marker test separate from later zeros.

If one of the four blocks is shorter than H, let k be the smaller of the
two corresponding prefix lengths, reversing both words first if necessary.
An early-marker separator has a k-edge zero-chain, then a one-edge to a final
zero-loop state. A late-marker separator has a (k+1)-edge zero-chain to an
accepting state with both loops. The wrong symbol kills the rejected word
at position k+1 in either case. Each construction uses k+2 <= H+1 states
and has exactly one final state. Reversing its edges and exchanging its
initial and final states therefore preserves the single-initial convention.

In the only remaining case all four exponents are at least H and L divides
Delta. For the zero and one relations B,C of any at-most-q-state machine,
`B^a=B^c` and `B^b=B^d`, so the two words induce the identical relation
`B^a C B^b = B^c C B^d`. No initial state or accepting subset can separate
them. In particular the hypothesized reverse separator cannot exist.
These cases exhaust the domain and prove the required uniform upper bound.

## Reconstruction of sharpness

Set s=q-1 >= 2, M=s^2, T=2^(M+1), and P=lcm(1,...,T). Consider

    u = 0^M 1 0^(T+P),       v = 0^(M+P) 1 0^T.

Suppose an m-state NFA with m <= M+1 accepts u. Fix an accepting path and
its state p immediately before the marker and state z immediately after it.
If the M-edge prefix repeats a vertex, it contains a simple zero-cycle. If
it does not repeat a vertex, it visits M+1 distinct states, forcing m=M+1
and visiting every state of the machine. The long all-zero suffix contains
a simple zero-cycle, and a vertex on this cycle must then also occur in the
prefix. In both cases some prefix vertex supports a zero-cycle of length
h <= m <= T. Since h divides P, extra cycle traversals extend the prefix
by exactly P while leaving p unchanged. A cycle need not have been traversed
in the original prefix to be available for insertion. This resolves the
boundary case m=M+1 without assuming an invalid prefix repetition.

Let S_j be the subset reachable from z after exactly j zeros. There are at
most 2^m <= T subsets. A repetition S_i=S_j among S_0,...,S_T, with i<j,
makes the sequence periodic from i with period c=j-i <= T. Since c divides
P and T >= i, `S_T=S_(T+P)`. The original final state is consequently
reachable after only T zeros. Join this suffix to the extended prefix and
the same one-edge: v is accepted. Hence no at-most-(M+1)-state separator
accepts u and rejects v. The explicit early-marker chain has M+2 states
and does so, proving `nsep(u,v)=M+2` without circularity.

For the reverse direction, the graph on 0,...,s has zero-edges j to j+1
for j<s and s to 0 and 1; its only one-edge is a loop at 0, which is both
initial and sole final state. I checked the edge orientation against
Nicol's Figure 1. The positive zero-return lengths are exactly
`as+b(s+1)`, a>=0, b>=1. In residue r in {1,...,s} modulo s, the least
positive return is r(s+1), and every subsequent length in that residue is
obtained by adding s. The largest excluded positive length is therefore
`max_r(r(s+1)-s)=s^2=M`. The empty return is also available and causes no
exception to this largest-exclusion calculation. The prefix M makes u
fail its unique possible marker transition, while both M+P and T exceed
M, so v is accepted. This is a q-state reverse separator, giving attainment.

The proof covers empty blocks in the upper bound, both signs of Delta,
all accepting subsets, disconnected graphs, and arbitrarily long words.
The witness is finite for each q. No limiting interchange, effective word
length ceiling, minimality of the reverse witness, or computational census
at the witness's hard state count is required.

## Independent exact diagnostics

The fresh verifier uses sets of destinations and exact orbit indexing,
without importing the research implementation or using its Boolean-power
routine. Running `python3 audit/referee-checks.py` completed with zero failed
assertions in about 5.1 seconds.

- It enumerated all 66,066 zero relations on one through four labeled states.
  The universal index/period identity and the suffix periodicity identity
  held. Directly measured maximum transient indices were 1,2,5,10;
  representative attaining relations are serialized.
- For every cyclic zero graph in those dimensions it checked the insertion
  inclusion at prefix length n-1. This also follows independently from the
  fact that a simple path of n-1 edges visits all n vertices.
- For n=1,2,3 it explicitly enumerated all 262,404 pairs (B,C), not only
  singleton C, and verified
  `B^(n-1) C B^(T+P) subseteq B^(n-1+P) C B^T`, with T=2^n and
  P=lcm(1,...,T). Entrywise inclusion covers every initial and final choice.
  No complete binary-relation census at n=4 or n=5 is claimed.
- It checked 16,480 prefix constructions, 16,480 reversed constructions,
  and 8,000 modular constructions for q=3,...,12. Tests include every
  k=0,...,H-1, both orientations, shifts 1,q,L,2L, and empty or threshold
  tails, as well as every proposed modulus r=2,...,q.
- It recomputed the serialized q=3,4 witness exponents using exact integer
  least common multiples, checked the graph data, and verified both explicit
  separators by subset orbits. For q=3 the recomputed shift is
  P=144403552893600. This checks acceptance, not the six-state minimum;
  minimality is supplied by the all-size argument above.
- Negative controls on n=2,...,12 recover the failure of the insertion
  inclusion at n-2 for a chain disjoint from a loop. Thus the extra-state
  step is not supported by a falsely stronger lemma.

The owner's reported finite checks have clearly delimited coverage and do
not substitute for an infinite proof. The independent diagnostics likewise
provide error checks rather than a formal proof assistant certificate.

## Source comparison, contribution, and limits

The nearest word-separation result is Nicol's Theorem 6 and Section 4.1 of
[the frozen v1 paper](https://arxiv.org/html/2608.30928v1). Its convention,
construction, and bound match the supplied source. The
[live version record](https://arxiv.org/abs/2608.30928) displayed only v1,
submitted 31 August 2026. Nicol gives hard cost greater than s^2 and reverse
cost at most s+1; he does not state the universal one-marker upper bound or
the sharp restricted maximum. The present lower argument adds the
spanning-prefix case and enlarges T. Its main delta is the matching
upper bound over the entire one-marker class.

I also read Sections 5-6, including Theorems 3-5, of the listed
[Demaine--Eisenstat--Shallit--Wilson author paper](https://erikdemaine.org/papers/WordSep_DFCS2011/paper.pdf).
Its unary-block indistinguishability and consecutive-cycle arguments are
antecedents, as is its reversal invariance. They do not determine the
directional maximum as a function of the opposite directional cost.
Schwarz's matrix theorem is explicitly classical. The listed Zajac--Jokay
paper, p.1331, reports the same universal index; its malformed printed
Definition 1 is real, but neither that definition nor an inferred repair is
needed for this proof. Its reference [6] points to Schwarz's 1974 account.

During this review I made bounded live searches including
`"one-marker" "nsep"`, `"separating words" "asymmetry" Nicol`,
`"one-marker" "separation" automata`,
`"nondeterministic" "separating words" "quadratic"`,
`"nsep" "A(q)" -pulse -electric -electroporation`,
`"separating words" "0*10*"`,
`"nondeterministic separation" words marker -pulse -electroporation -nanosecond`,
`"separating words" "unary" "index"`,
`"one-marker" automata "quadratic"`, and
`"separating words" "single 1"`.
No equivalent exact formula was found in the inspected primary sources or
these searches. Mirrors and unrelated hits were not treated as independent
sources. This is a bounded novelty screen, not a proof of priority or a
global guarantee of openness.

The contribution passes as a modest, coherent result note. The restriction
contains the complete known quadratic witness family and ranges over all
marker positions and all lengths, so it is mathematically motivated. The
uniform converse and the sharp extra-state argument are not supplied by
the previous directional bound alone. Their useful consequence is a precise
limit on this entire construction class: a search for superquadratic growth
of A(q) must leave the one-marker setting. The additive improvement to the
general lower bound by itself would be a much weaker contribution.

No unresolved mathematical gap was found in the frozen assertion. Acceptance
does not certify global priority, journal suitability, the unrestricted
asymptotic question, or a manuscript that has not yet been reviewed. Future
writing should preserve the exact scope, attribution to the 1974 account,
and the stated limits of computational and literature evidence. The runner
may next check the unchanged snapshot and review provenance before dispatching
the writing phase.
