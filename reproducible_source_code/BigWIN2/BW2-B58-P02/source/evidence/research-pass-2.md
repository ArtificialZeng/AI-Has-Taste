# Research pass 2 evidence

Job: `win-00058-p02-research-7a3c7e99d2ae` (2026-09-07).

## Exact new-shell calculation

Lowering the denominator from 227 to 226 adds a deletion-total-`e`
contribution precisely when `s == e (mod 2)` and `226e < s <= 227e`.  The only
new separately excluded shells with `e <= 2` are therefore total 227 with one
deletion and total 454 with two deletions.  Higher new contributions remain in
the exact LLL sum and its recomputed rational tail.  The published empty shells
for D=227 remain valid statements about the fixed codebook, independently of
the denominator.

Python 3.10.12 reruns of `evidence/audit_one_deletion_shell.py` gave:

- total 227: all 132,240 normalized square-free-context cases locally killed,
  zero residuals, 9.98 s;
- published total-229 control: all 135,240 cases locally killed, with the exact
  published histogram `{0:100219, 1:27077, 2:7944}`, zero residuals, 9.72 s.

`evidence/audit_two_deletion_shell.py` is an exact Python translation of the
primary `verify_two_deletion_shell.mjs`, with diagonal runs replacing explicit
coordinate rebuilding and an exact CSP fallback for any local residual.  A
33,048-case test over all small half-lengths 2--9 and all 54 offsets proved that
the run representation expands to the naive primary pairing in every tested
mode and deletion pattern (`GROUPED_EDGE_EQUIVALENCE_PASS`).

The command

```text
python3 evidence/audit_two_deletion_shell.py evidence/external/ternary-synchronization-strings-artifact/inputs/codewords_54_952.txt 454 --progress
```

checked all three modes `(228,226)`, `(226,228)`, `(227,227)`, all 54 offsets,
and every deletion pattern.  The exact coverage formula is

`2*54*C(228,2) + 54*227^2 = 5,577,390`.

Every pattern has a local codebook relation incompatible for all three outer
alphabet differences, so all 5,577,390 are universal kills.  Consequently no
square-free outer context is required and there are zero context/CSP residuals.
Mode counts are 1,397,412, 1,397,412, and 2,782,566.  Wall time was 143.14 s.

The same program at published total 456 returned exactly the primary artifact's
independent expected record: 5,626,584 patterns and 5,626,584 universal kills,
with mode counts 1,409,724, 1,409,724, and 2,807,136 (136.97 s).  Exact result
records are `evidence/two-deletion-454-result.json` and
`evidence/two-deletion-456-control.json`.

## Final exact D=226 envelope

Both exact-rational implementations were rerun bilaterally with
`alpha=51/100000`, `beta=3/10`, denominator 226, and precisely the exclusions

`{227,229,231,...,463,454,456,462,464}`.

The primary verifier passed 34,946 retained finite event types.  It certified
`max x <= 0.000068906109636061649419 < 1/6000`,
`alpha-R0 >= 0.000000618068890291343247`, and
`beta-(109R0+R1) >= 0.003728877584891028227619` (3.10 s).  The independent
range-reduced exponential implementation also returned
`INDEPENDENT_D226_EXACT_REPLAY_PASS` with matching displayed margins (20.41 s).

## Integrity, sources, and scope

The copied artifact is clean at frozen commit
`5e9e0c05fca32a5d5735cab9914626ffe667c53c`.  The codebook SHA-256 is
`a1b4b912d956419ef59a15e5d0926ce337614a438da25923e19a65485da05e28`;
the new two-deletion verifier SHA-256 is
`1d85e49061694fcb584f6b7f2819289cfd12b79b4a216e298926b50bf8057c16`.
The copied primary PDF has the intake SHA-256
`930511506e2363891fd289c662273b496a5839286f01cf4f7eeb185a3b64668a`.

A bounded arXiv search on 2026-09-07 for the title and the exact 1/226 and
225/226 parameters found the cited arXiv:2609.04122v1 as the only directly
relevant primary record; it advertises only the D=227 refinement.  This is not
a priority proof.  The candidate is deliberately scoped as an improvement
inside that fixed v1 construction/framework.  It proves `C(226)` but does not
determine whether some `D < 226` works, so the original least-denominator
question remains unresolved.

## Next test

A fresh referee should independently audit the shell-difference argument, the
pairing equivalence and universal-kill logic in both new audit scripts, rerun the
227/454 enumerations and controls, and recompute both exact D=226 LLL passes.
