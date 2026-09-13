# Breaker and certifier notes: exact zero set

## Scope and trust boundary

These notes independently use the graph definition currently recorded in
`problem/formal_statement.md`: offsets 1 and 3 on `Z/nZ`, plus the diameter
offset `n/2` for even `n`.  If Gate 1 changes that definition, every result
below must be rechecked.  All arithmetic here is in `Z/3Z` unless explicitly
called an integer sum.

The executable certificate is `verifier/certificate.json`; its independent
checker is `verifier/verify_zero_set.py`.  The checker has no dependency on
discovery code or third-party packages.

## 1. Exact structural reduction

Given a colouring `c_i`, put

\[
 d_i=c_{i+1}-c_i\in\{+1,-1\}.
\]

Conversely, a sign word `d_0,...,d_{n-1}` with
`sum_i d_i = 0 (mod 3)` reconstructs a unique colouring after choosing
`c_0`; hence it reconstructs exactly three labelled colourings.

The chord of offset 3 is proper precisely when

\[
 d_i+d_{i+1}+d_{i+2}\ne0.
\]

For three signs this fails exactly when the three signs are all equal.
Therefore the offset-1 and offset-3 conditions are equivalent to:

1. the cyclic sign word has no run of three equal signs; and
2. its total sum is 0 modulo 3.

For even `n=2m`, define the half-window state

\[
 S_i=\sum_{j=0}^{m-1}d_{i+j}.
\]

The diameter condition is exactly `S_i != 0 (mod 3)` for every `i`, and

\[
 S_{i+1}=S_i-d_i+d_{i+m},\qquad S_{i+m}=-S_i,
\]

where the second identity uses the closing condition that the total sign sum
is zero modulo 3.  Consequently it is enough to check the first `m`
half-window states.

On a valid word each `S_i` is one of `+1,-1`.  The recurrence is therefore a
two-state exact automaton: a paired sign `d_i=d_{i+m}` leaves the state fixed;
if the paired signs differ, the only nonzero transition is

\[
 (S_i,d_i,d_{i+m})=(s,s,-s)\longmapsto S_{i+1}=-s.
\]

The other unequal pair lands at zero and is forbidden.  This two-state
description replaces the much larger transfer matrix for the existence
question and is the invariant used in the pump below.

This proves the equivalence used by the difference-word verifier; it is not a
numerical inference.

## 2. Infinite constructive theorem

### 2.1 Odd orders

Let odd `n>=9` and put `q=(n-3)/2`, so `q>=3`.  Around the cycle place `q`
isolated minus signs.  Immediately after three of them put a run `++`, and
after each of the remaining `q-3` put a single `+`.  There are `q+3` plus
signs, so the length is `2q+3=n` and the integer sign sum is exactly 3.
Every minus run has length 1 and every plus run has length at most 2.  Thus the
word is admissible and gives a proper colouring.

For `n=7`, any closing sign word would have odd integer sum divisible by 3.
The no-three rule excludes sums `+/-7`, so the only possibilities are `+/-3`.
For sum `+3` there would be five plus signs and two minus signs.  Those two
minus signs divide the plus signs into at most two cyclic runs, each of length
at most 2, which can contain at most four plus signs: contradiction.  Negating
all signs handles sum `-3`.  Hence `n=7` is impossible by a non-computational
argument.

### 2.2 Orders congruent to 2 modulo 4

Let `n=4k+2` (`k>=1`) and take the alternating word `+-+-...+-`.  Its total
sum is zero and it has no equal adjacent pair, much less a triple.  Its
half-length is `m=2k+1`; every length-`m` alternating window has integer sum
`+1` or `-1`, so every diameter is proper.  This covers `n=6,10,14,...`.

### 2.3 Orders divisible by 4 from 20 onward

For `t>=0` define halves of length `10+2t` by

\[
\begin{aligned}
 u_t&=\texttt{++-}(\texttt{+-})^t\texttt{++-++-+},\\
 v_t&=\texttt{+-+}(\texttt{+-})^t\texttt{+-++-+-},
\end{aligned}
\]

and let `d(t)=u_t v_t`.  Its order is `20+4t`, exactly every multiple of four
at least 20.

At `t=0`, direct integer checking gives total sum 6, no cyclic equal-sign
triple, and half-window residues (including the initial state and the state
after each of the ten paired transitions)

\[
 1,1,-1,1,1,-1,1,1,-1,1,-1
\]

(the last entry is the state after all ten paired transitions).  In
particular all are nonzero.

Passing from `t` to `t+1` synchronously inserts the block `+-` at paired index
3 in both halves.  This block has integer sum zero, so it changes neither the
total closing residue nor the initial half-window state.  At each of the two
new paired indices one has `d_i=d_{i+m}`, so the transition
`S -> S-d_i+d_{i+m}` fixes `S`.  All old nonzero states are therefore
preserved; the states in the other half are their negatives.  The inserted
material is alternating; at each of its four fixed
boundaries the local contexts (two symbols on either side suffice) have no
triple.  Thus no cyclic triple is created.  Induction proves admissibility for
every `t>=0`.

Together 2.1--2.3 prove existence for every `n>=6` outside
`{7,8,12,16}`.

## 3. Exact finite nonexistence certificate

The three remaining even exceptions are certified by complete enumeration,
twice and from different representations:

* all `2^n` sign words are tested against the exact characterization above;
* graph edges are reconstructed from offsets `1,3,n/2`, vertex 0 is fixed to
  colour 0 by colour-permutation symmetry, and every remaining three-colour
  assignment is exhausted by deterministic backtracking.

The difference-word enumeration gives the following exact counts (a labelled
colouring count is three times the displayed number):

| n | 6 | 7 | 8 | 9 | 10 | 11 | 12 | 13 | 14 | 15 | 16 | 17 | 18 | 19 | 20 |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| admissible sign words | 14 | 0 | 0 | 6 | 62 | 22 | 0 | 78 | 310 | 250 | 0 | 748 | 1526 | 2166 | 40 |

The independent graph backtracker reproduces every displayed count after
fixing `c_0=0`, and in particular returns zero completions for each of
`n=7,8,12,16`.  These are finite exhaustive theorems conditional only on the
short verifier's correct execution; the infinite positive families are
proved by the symbolic arguments in Section 2, not by sampled computation.

## 4. Breaker results and limitations

* Exhaustive counterexample search through `n=20` recovers exactly the four
  proposed zeros.  The constructive families then cover every larger order,
  so no order remains merely numerically searched.
* The fragile point was the even diameter condition.  It is explicitly
  represented by every half-window state rather than inferred from one
  window.
* The pump is synchronous in the two halves.  An insertion in only one half,
  or blocks with nonzero sign sum, would invalidate the state invariant.
* The result is conditional on the formal graph definition surviving the
  source audit.  No claim about novelty is made here.

## 5. Reproduction and formal-method disclosure

Run:

```bash
python3 verifier/verify_zero_set.py verifier/certificate.json
```

No proof assistant, SAT solver, CAS, floating-point computation, or external
library was used.  The certificate and all checks are integers, finite words,
and exhaustive finite enumeration.

## 6. Claim classification

* **Human theorem:** the difference-word equivalence; the odd construction;
  the direct contradiction for `n=7`; the alternating construction for
  `n=2 (mod 4)`; and the synchronous pump construction for every
  `n=0 (mod 4), n>=20`.
* **Certified finite theorem:** nonexistence at `n=8,12,16` and the exact
  counts for `6<=n<=20`, established by exhaustive integer enumeration in two
  independent representations.
* **Diagnostic computation only:** the extra concrete family samples checked
  by the verifier (and the separate stress run through order 2002) are
  regression tests.  They are not used to justify the infinite quantifiers.
