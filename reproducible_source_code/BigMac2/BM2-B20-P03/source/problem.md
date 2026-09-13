# Precise problem reading

## Frozen source and provenance

The original lead is preserved verbatim in `source.md` (SHA-256
`a5f6ee89bf21df93a868c15c50725b26f03e8d259a210c27788063657b7da7a5`).
This interpretation was revalidated for job
`bigMac-00020-p03-triage-2a15198d4f4b`; it does not alter or correct the
original statement.

## Graph and legal responses

Let
\[
V(Q_3)=\{0,1\}^3,
\qquad
xy\in E(Q_3)\iff d_H(x,y)=1,
\]
where `d_H` is Hamming distance. Thus graph distance in `Q_3` is Hamming
distance. For a vertex set `S`, write
\(N[S]=\{x:\operatorname{dist}(x,S)\leq 1\}\); staying put is included.

For a probe at `p` and robber position `r`, the legal partial-feedback answers
are
\[
D(p,r)=
\begin{cases}
\{p\},&p=r,\\
\{p\oplus e_j:p_j\ne r_j\},&p\ne r.
\end{cases}
\]
Equivalently, if the probe hits the robber, the answer is the probed vertex;
otherwise the answer is one neighbor of the probe lying on a shortest
`p`--`r` path. When several such neighbors exist, the robber chooses any one.

## Timing, information, and quantifiers

Fix a number `c` of cops. The robber chooses an unknown initial vertex before
round 1. In round `t`:

1. Based only on the public history, the cops simultaneously choose a probe
   tuple \(P_t=(p_{t,1},\ldots,p_{t,c})\in V(Q_3)^c\).
2. From the robber's current vertex `r_t`, the robber simultaneously chooses
   an answer tuple \(A_t=(a_{t,1},\ldots,a_{t,c})\), with
   \(a_{t,i}\in D(p_{t,i},r_t)\) for every `i`.
3. If the public history now determines `r_t` uniquely, the cops win
   immediately. Otherwise the robber may stay or traverse one edge, producing
   `r_{t+1}`.

Probe repetitions are allowed in this tuple formulation. They confer no extra
guaranteed information: the robber may return the same legal answer to every
copy, and unused cops' answers may be ignored. An exhaustive certificate may
therefore enumerate all ordered tuples (including repetitions), avoiding any
dependence on a distinct-probe convention.

Precisely, let `B_t` be the set of positions compatible with the public history
at the start of round `t`, with \(B_1=V(Q_3)\). For probes `P` and observed
answers `A`, define
\[
B'(B,P,A)=\{r\in B:a_i\in D(p_i,r)\text{ for every }i\}.
\]
A possible answer has \(B'\ne\varnothing\). The cops win on that answer exactly
when \(|B'|=1\); otherwise the next public belief is
\[
B^+=N[B'].
\]
This belief update includes every robber move compatible with the same public
history.

A `c`-cop winning strategy means: there exist a deterministic history-dependent
strategy and a finite uniform bound `T` such that, for every initial robber
vertex, every sequence of legal answers, and every sequence of legal robber
moves, a singleton `B'` is reached by round `T`. Random success or eventual
success without a uniform bound does not count. The partial-feedback
directional localization number \(\zeta_d(Q_3)\) is the least such `c`.

## Exact claim to resolve

Determine which one of the following mutually exclusive statements is true:
\[
\boxed{\zeta_d(Q_3)=3}\qquad\text{or}\qquad
\boxed{\zeta_d(Q_3)=4}.
\]

The known bracket makes this exhaustive. Jones--Kinnersley, Corollary 3.9,
proves \(\zeta_d(Q_n)\in\{n,n+1\}\) for every positive integer `n`; at `n=3`
this gives \(3\leq\zeta_d(Q_3)\leq4\). Their Question 6.1 asks for the exact
value for hypercubes and records the conjectural value `n`, without strong
evidence.

Either resolution must supply a checkable finite certificate:

- To prove value `3`, give a complete three-cop winning strategy. A sufficient
  positional certificate is an action and a nonnegative rank for every
  reachable winning belief, starting at `V(Q_3)`, such that every legal answer
  either gives a singleton or leads to a strictly smaller-ranked belief.
- To prove value `4`, give a three-cop robber safety certificate/trap containing
  the initial belief `V(Q_3)`: for every belief in the trap and every ordered three-probe
  tuple, exhibit a legal answer with at least two compatible positions whose
  recontaminated belief remains in the trap. Corollary 3.9 supplies the
  four-cop upper bound.

In either branch, a standalone replay must reconstruct `Q_3`, enumerate every
quantified action and answer, and validate the certificate. A solver's verdict
without such replay is not a proof.

## Source status, proposed delta, and scope

Nearest prior result: Jones and Kinnersley, *The Directional Localization Game
on Graphs*, arXiv:2609.01745v1 (submitted 2026-09-01), Corollary 3.9 on printed
page 14 and Question 6.1 on printed page 29. The local PDF inspected on
2026-09-09 has SHA-256
`1f1ac4c3c0a1313003b326c5c98cad06253482beaecfdbd14f7f0fd6c2a67d58`.
The arXiv record showed only v1 on that date. Exact-assertion and equivalent-term
searches located this primary paper but no separate `Q_3` resolution; this is a
limited literature screen, not a priority claim. Source status is therefore
`open-supported` relative to the cited v1, with present-day novelty still to be
rechecked before any release.

Proposed delta: close the first undecided hypercube slice by deciding the
three-cop belief game exactly. Verification route: exhaustive finite-state
retrograde analysis followed by an independently implemented exhaustive replay.

Scope is only the partial-feedback game on `Q_3`, with simultaneous probes,
adversarial legal directional answers, and stay-or-one-edge robber motion. It
does not address the full-feedback parameter \(\zeta_d^*\), all `Q_n`, noisy or
randomized play, physical cop movement, or capture instead of localization.
