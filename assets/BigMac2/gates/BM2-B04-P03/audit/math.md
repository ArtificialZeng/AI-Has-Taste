# Fresh mathematical referee report

## Scope and verdict

I reviewed the exact `resolution-paper` claim frozen by snapshot digest
`d1cd38b08aad32076bab5102c4b96643aca988b3dda4cacf13323d7b7e6dff25`.
All seven frozen file hashes, including the immutable `source.md` hash
`fbffc6b3d9b3b2db7bac8945473758846ca4cf5d4db8d9fb17073f50d47cfe43`,
recomputed to the values in `audit/snapshot.json`; the canonical digest of the
file mapping also recomputed to the declared snapshot digest.

**Verdict: accept.** The proof resolves the original problem at its full
quantified scope: it covers every admissible positive integer (m), gives the
exact value (L(m)), gives the complete maximizer set modulo one, and derives
the strict near-tight set. I found no substantive scope, correctness, or
contribution defect.

## Reconstruction of the proof

Write

\[
g(t)=\min_{v\in\{1,4,5,6,7\}}\|vt\|.
\]

Symmetry reduces the base analysis to (0\leq t\leq 1/2). Intersecting, for
each of the five speeds, the exact intervals on which
(\|vt\|\geq 2/13) gives

\[
\{t:g(t)\geq2/13\}\cap[0,1/2]
=\{4/13\}\cup[14/39,24/65]\cup[41/91,6/13].
\]

On the two nondegenerate intervals the lower envelope is respectively

\[
\min(6t-2,2-5t),\qquad \min(7t-3,2-4t).
\]

Their unique peaks in the half-circle are (4/11) and (5/11), both of
height (2/11). Reflection therefore gives

\[
\max g=2/11,\qquad \operatorname{argmax}g
=\{4/11,5/11,6/11,7/11\}.
\]

If (11\nmid m), evaluation of the added runner at these four and only these
four possible equality times reduces to the two residues
(11\|4m/11\|) and (11\|5m/11\|). The ten nonzero residue classes give
exactly the three maximizer cases in `claim.json`; at least one pair survives
in every class. The base upper bound then proves (L(m)=2/11), while the base
argmax classification proves completeness of the displayed (A(m)).

Now put (m=11n). For (n\geq3), let

\[
Q=11n+4,\quad q=\frac{2n}{Q},\quad
\Delta=\frac2{11}-q=\frac8{11Q}.
\]

Here (2/13<q<2/11). The reconstructed base envelope shows that its
(q)-superlevel set in the half-circle is exactly

\[
J_4=\left[\frac4{11}-\frac\Delta6,
          \frac4{11}+\frac\Delta5\right],\qquad
J_5=\left[\frac5{11}-\frac\Delta7,
          \frac5{11}+\frac\Delta4\right].
\]

Writing (t=4/11+x) on (J_4), one has

\[
\|11nt\|=|11nx|\leq\frac{8n}{5Q}<q.
\]

Writing (t=5/11+x) on (J_5), the range of (11nx) is contained in
([-8n/(7Q),q]), with both endpoint magnitudes below (1/2); equality with
(q) occurs only at (x=\Delta/4). Outside these two intervals (g<q).
Thus the unique maximizing time in the half-circle is
((5n+2)/Q), and reflection gives the other time ((6n+2)/Q).
This proves the asserted all-(n\geq3) formula without a finite cutoff.

For (n=1,2), the same exact base decomposition is used at level (2/13).
On the interval about (4/11), the added coordinate is strictly below
(2/13). On the interval about (5/11), it is strictly below (2/13)
except at the right endpoint for (n=2), which is (6/13). The isolated
base point (4/13) remains feasible because the added norms are (5/13)
and (3/13), respectively. Reflection yields exactly
({4/13,9/13}) for (m=11) and
({4/13,6/13,7/13,9/13}) for (m=22).

Finally, (2/11>1/6), (1/7<2/13<1/6), and for (n\geq3)

\[
\frac{2n}{11n+4}<\frac16\quad\Longleftrightarrow\quad n<4.
\]

Since the same values are already (>2/13>1/7), the strict near-tight set
is exactly ({11,22,33}); (n=4) is correctly excluded as the equality
case (L=1/6).

## Adversarial checks performed

- Quantifiers and partition: the nonzero classes modulo 11 and the cases
  (m=11), (m=22), and (m=11n, n\geq3), are mutually exclusive and
  exhaust the stated domain. The five forbidden duplicate speeds remain
  excluded exactly as in the frozen problem.
- Equality cases: the argument works with complete superlevel sets, not just
  witnessing times. Reflection supplies every point on the other half-circle;
  no endpoint or isolated component is lost.
- Circle norms and wraparound: every replacement of a circle norm by an
  absolute value is accompanied by a strict or weak bound below (1/2).
  There is no division by a parameter that can vanish.
- Exact supplied computation: `evidence/verify_family_formula.py` passed using
  `Fraction` arithmetic for all admissible (m\leq180), all (n\leq100),
  and (n=127,251), and independently recovered the three base superlevel
  components.
- Structurally different recomputation: I formed every sawtooth cell of the
  six functions (\|vt\|), wrote each as an exact affine function on that
  cell, and evaluated all cell endpoints and pairwise affine intersections.
  This exact lower-envelope method matched both (L(m)) and the full (A(m))
  for every admissible (m\leq220), and additionally for
  (m=11n) with (n=23,47,101,257,509). This is a finite cross-check only;
  the universal conclusion rests on the preceding symbolic argument.

## Source comparison and limits

The supplied PDF is Francesco Cordella, *Odd denominators in the Lonely
Runner spectrum for six speeds*, matching the correction in `problem.md`.
Its Lemma 2.2 supports the exact collision/antipode candidate check. Its
Theorem 6.1 gives a finite-exception structural result for near-tight
sextuples, not this complete one-parameter classification. Table 2 records
((1,4,5,6,7,22)) with value (2/13) and
((1,4,5,6,7,33)) with value (6/37), consistent with the theorem under
review. The discussion identifies those two adjoined-runner examples but does
not state the all-(m) value and full argmax theorem.

The supplied literature scope is one primary source, so this audit does not
certify priority against all literature. That is not silently promoted into a
novelty claim: `claim.json` expressly limits its comparison to the inspected
source and disclaims broader priority. Within the frozen candidate scope, the
complete exact family theorem is a substantive resolution rather than a
finite pattern, toy restriction, or restatement of the cited examples.

## Remaining gaps

No mathematical or frozen-scope gap remains. Broader literature priority and
later manuscript/citation/presentation review are separate release-stage
questions and do not affect this mathematical verdict.
