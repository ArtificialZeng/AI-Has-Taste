# Fresh mathematical referee report

## Verdict and frozen scope

**Verdict: accept.** I audited the exact `result-note` statement in
`claim.json`, not the unresolved request to determine the least working
denominator. The evidence proves `C(226)` within the fixed Xu--Fu--Qiao--Tao
v1 construction and charge framework. It does not establish minimality of
226, global optimality, or a literature priority claim.

All files named by the frozen snapshot have the recorded SHA-256 digests. I
also recomputed the canonical digest of the snapshot file map and obtained
`497d503a6e24a847e2bb78948ee109c16990493dcb2abb9841a1f6b46e2a35aa`.
In particular, the codebook hash is
`a1b4b912d956419ef59a15e5d0926ce337614a438da25923e19a65485da05e28`
and the frozen source retains its recorded hash.

## Reconstruction of the decisive argument

Write `s=a+b` and `e=u+v=ED(X,Y)` for a deletion-volume term. Relative to
denominator 227, a term is newly present at denominator 226 exactly when

`226e < s <= 227e` and `s` has the same parity as `e`.

For `e=1` this adds only `s=227`; for `e=2` it adds only `s=454`. Every new
term with `e>=3` is retained in the recomputed exact LLL sum (or its
recomputed analytic tail), rather than being silently covered by the old
exclusion list. The exclusions used for 226 are precisely all odd totals
from 227 through 463, together with 454, 456, 462, and 464. The old odd
totals 229 through 463 and the even totals 456, 462, and 464 are unconditional
codebook shell statements proved in the primary source, so they remain valid
when the denominator changes.

At total 227, a violation has adjacent lengths 114 and 113 and edit distance
one. I reran `audit_one_deletion_shell.py` on the frozen codebook. It checked
both orientations, all 54 offsets, every deleted position, and every
normalized square-free outer context: all 132,240 cases were local
incompatibility kills, with no CSP residual. The edge histogram
`(99804,32022,414)` matches the frozen result. The same fresh run at the
published control total 229 reproduced all 135,240 kills and the published
histogram `(100219,27077,7944)`.

At total 454, the only relevant modes are `(228,226)`, `(226,228)`, and
`(227,227)`. The exact number of offset/deletion patterns is

`2*54*C(228,2) + 54*227^2 = 5,577,390`.

I inspected the equality-relation construction and independently compared
its diagonal-run representation with direct survivor-coordinate pairing for
614,088 patterns covering every mode, every offset, every deletion pattern,
and half-lengths 2 through 25. There was no mismatch. I then reran the full
total-454 audit. It returned 1,397,412, 1,397,412, and 2,782,566 universal
kills in the three modes, respectively: all 5,577,390 patterns contain a
macroblock relation empty for each of the three alphabet differences. Thus
there are no outer-context or CSP residuals. As a control, a fresh total-456
run exactly reproduced the primary-source counts: 5,626,584 universal kills,
split as 1,409,724, 1,409,724, and 2,807,136.

For every nonexcluded type, the paper's direct conditional-mass proof extends
without a hidden small-length failure. If `s>=227` and
`226|a-b|<s`, each interval length exceeds
`225s/(2*226)>54`, so the fragment-aware point-mass lemma applies in both
orientations. The two integer deletion volumes in the verifier are exactly
the sums obtained from `v-u=b-a`, `226(u+v)<s`, and the left/right fill
counts `3^u` and `3^v`. Reversal closure justifies taking the smaller of the
two conditional bounds.

I reran both frozen exact-rational LLL implementations with bilateral
conditioning and the exact exclusion set above. The primary calculation
retained 34,946 finite event types and certified

- maximum charge upper bound `0.000068906109636061649419 < 1/6000`;
- `alpha-R0 >= 0.000000618068890291343247 > 0`;
- `beta-(109R0+R1) >= 0.003728877584891028227619 > 0`.

The range-reduced implementation independently returned
`INDEPENDENT_D226_EXACT_REPLAY_PASS` with the same displayed margins. I also
checked the changed tail derivation. For `D=226`, the rational decay exponent
used by the verifier is

`c = 100417/4237500 > 1/43`,

so `exp(-c)<43/44`. The resulting first possible tail charge is bounded by
`2*952^2*(43/44)^4001 < 1/6000`; the first- and second-moment geometric sums
therefore validly bound the tail contributions to `R0` and `R1`. The neighbor
constant 109 and charges `alpha=51/100000`, `beta=3/10` are unchanged, so the
strict envelope inequalities give the asymmetric LLL condition.

Finally, the excluded and retained cases cover every adjacent nonempty pair.
For `s<=226`, length imbalance gives the bound unless the lengths are equal,
and square-freeness then gives edit distance at least two. At an excluded odd
total at most 463, parity reduces every possible violation to edit distance
one. At an excluded even total at most 464, it reduces every possible
violation to edit distance zero or two; square-freeness and the corresponding
two-deletion shell exclude these. All other imbalanced cases are automatic,
and all remaining direct bad events are empty or avoided by the LLL. Taking a
length-`n` prefix preserves the adjacent-pair inequality, proving the stated
quantifier for every `n>=1`.

## Source comparison and contribution

The listed primary PDF proves denominator 227 in Theorem 1.5 and Proposition
D.7. The candidate supplies the two newly required exact shell eliminations
and a denominator-dependent LLL recomputation, yielding the sharper weak gap
`1/226` (and hence every strict synchronization parameter greater than
`225/226`) in the same framework. This is a precise, nontrivial explicit
parameter improvement with direct use in the quantitative construction; it
is not merely the old 227 certificate with its exclusions reused. The least
working denominator remains unresolved. The recorded literature search is
bounded and is appropriately not presented as proof of priority; that
limitation should remain explicit in any manuscript.

