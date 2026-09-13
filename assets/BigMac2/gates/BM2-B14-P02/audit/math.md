# Fresh mathematical audit

## Frozen scope and integrity

I reviewed the exact `resolution-paper` claim frozen by snapshot
`77e5155bbd028adda1f6ea77987065be2ac927f99e1f34c12d0977b433293ea9`.
Fresh SHA-256 calculations for `claim.json`, `source.md`, `problem.md`, and
`evidence/skeleton_transfer.md` agree with every entry of the snapshot, and a
fresh canonical hash of the snapshot's file map agrees with its recorded
digest.  The claim addresses the full fixed-\(\rho<1\) source statement; it is
not a partial replacement or a simultaneous-\(k,n\) assertion.

## Reconstruction of the decisive argument

Put \(q=1-\rho>0\), let \(M_n=\sum_{t=1}^n B_t\), and set
\(X_t=Y_{M_t}\).  Conditional on the past, when \(B_t=0\) the next label is
the current label, while when \(B_t=1\), \(Y_{M_{t-1}+1}\) is a fresh
independent draw from \(\pi\).  Thus this construction has exactly the stated
sticky-refresh transition law and starts in stationarity.

The integer-valued path \((M_t)_{0\leq t\leq n}\) starts at zero and has
increments in \(\{0,1\}\), so its attained indices are exactly
\(0,1,\ldots,M_n\).  It follows pathwise that
\[
 V_n=\{Y_0,\ldots,Y_{M_n}\}.
\]
If \(B_t=0\), the clock transition is a self-loop and is deleted.  At the
time of the \(j\)-th success of \(B\), the transition is precisely
\((Y_{j-1},Y_j)\).  These success times run once through
\(j=1,\ldots,M_n\).  A successful refresh that redraws the current label is
a self-loop on both sides.  After deleting loops and suppressing duplicates,
the directed and undirected edge sets therefore equal, respectively, those
of the iid word \(Y_0,\ldots,Y_{M_n}\).  Hence all vertex degrees and the
observed-range denominator agree.

For the directed convention that omits a label appearing only as the final
iid observation, the omitted label is new and has out-degree zero.  An old
final label was already in the numerator's domain.  Thus for every \(k\geq1\)
both the degree-\(k\) and degree-at-least-\(k\) numerators agree as asserted.
There is no analogous discrepancy in the stated undirected convention.
Consequently, with \(N_n=M_n+1\), all four sticky statistics are exactly the
corresponding iid statistics at sample size \(N_n\).

By the strong law, \(M_n/n\to q>0\) almost surely, so \(N_n\to\infty\).
For each of the four statistic types and every positive integer \(k\), take
the probability-one event supplied by the iid theorem.  Their countable
intersection still has probability one.  On that event, ordinary convergence
of the full iid sequence implies convergence along the (pathwise diverging)
integer sequence \(N_n\).  Independence of the random index and the iid
limit event is not needed.  This proves the four inner clock-time limits
simultaneously for all fixed \(k\).

Only after those inner limits, the four deterministic iid asymptotics recorded
in the frozen source comparison give
\[
 r_{k+}^{\to}\sim\pi_k^\gamma,\qquad
 r_{k+}^{\mathrm u}\sim2^\gamma\pi_k^\gamma,
 \qquad
 r_k^{\to}\sim\pi_k^\gamma/k,\qquad
 r_k^{\mathrm u}\sim2^\gamma\pi_k^\gamma/k.
\]
Thus no \(q\)- or \(\rho\)-factor can enter under observed-range
normalization.  Division of the paired asymptotics gives the stated
undirected-to-directed amplitude ratio \(2^\gamma\), and
\(\pi_k^\gamma/k\in RV_{-2}\), which gives the local exponent two.

## Adversarial checks

- The proof uses \(q>0\) essentially.  It covers \(\rho=0\), while the
  excluded endpoint \(\rho=1\) would make the skeleton size constant.
- Non-refresh loops and same-label refresh loops are both deleted on the two
  sides of the identity; neither creates a hidden edge.
- The range denominator is never zero and is identical pathwise, so a
  deterministic-clock normalization and its possible \(q^\gamma\) factor do
  not enter the claim.
- No exchange of the \(n\)- and \(k\)-limits, uniformity as \(\rho\uparrow1\),
  or growing-degree regime is used.
- The probability-one statement is for each fixed \(\rho\), as claimed, and
  is simultaneous only over the countable set of fixed positive integers
  \(k\); no uncountable intersection over \(\rho\) is asserted.

## Source comparison and contribution

The only imported mathematical result is the loop-deleted iid theorem with
the four fixed-\(k\) limits and four outer asymptotics stated in `problem.md`
and quoted explicitly in the frozen proof.  Its hypotheses and normalization
match the frozen claim, and the transfer invokes it only along a diverging
subsequence.  The designated primary PDF was not among the snapshot-listed
evidence files and, under the bounded evidence restriction, was not separately
opened in this pass; this audit therefore assesses the new transfer relative
to the frozen statement of that established iid result.  No literature-priority
claim is being accepted.

The exact skeleton identity resolves the full dependent specialization asked
in `source.md`, including the normalization and all four ordered asymptotics.
It is a substantive complete reduction rather than a toy restriction or a
silent weakening.

## Verdict

**Accept.**  The frozen full-scope claim follows from the reconstructed
pathwise identity and the cited iid limit theorem.  I found no unresolved
mathematical gap in the submitted scope.
