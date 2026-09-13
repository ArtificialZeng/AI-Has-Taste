# Gate 4 round 3: post-fix diff audit for `t16_branch.md`

Date: 2026-08-29  
Role: independent referee; narrow post-fix review only  
Pre-fix SHA-256: `2cdf4ec6316db12036add92dfdc6c86b52f9a9d6d44837ccd1599f467fa9b022`  
Post-fix SHA-256: `114d861529243e3eb96415e10f14920370b91f5085d1538fc0bb0f564e26d889`

## Verdict

**PASS.**  The current target resolves all three local issues recorded in
`audit/referee_round3_t16.md`.  The repairs preserve the mathematical scope
and conclusion of Lemma 2.  No new fatal, major, or local issue is introduced
in the edited passages.

This was a deliberately narrow diff audit.  No proof, verifier, frame audit,
runner, or log was modified.

## Reviewed changes

### R3-TEX-QUAD: resolved

Equation (1) now reads

```tex
v_S=H\mathbf1_S,\quad g_a>0.
```

The missing control-sequence backslash is restored.  This is the intended
typesetting-only change and does not alter the formula.

### R3-KERNEL-V: resolved

Equation (12) now states

\[
\ker(C|_{\mathbf1^\perp})=K_Z
=\{u:\operatorname{supp}u\subseteq Z,\ \sum_{r\in Z}u_r=0\}.
\]

This is exactly the kernel identity proved by the preceding calculation.
It no longer makes the false ambient-space assertion
\(\ker C=K_Z\), which omitted the ever-present vector \(\mathbf1\).
The set delimiter was also made explicit with `\{`, improving the displayed
formula without changing its content.

The later use of the identity remains correct: positivity of the rank-one
sum only needs \(K_Z\subseteq\ker C\), which follows from the corrected
restriction statement.

### R3-Z-ALL: resolved

The proof now explicitly observes that \(W=[11]\setminus Z\) is nonempty.
If \(Z=[11]\), constancy of each remaining cut indicator on \(Z\) would make
the cut trivial, contrary to both the cut convention and \(R\ge1\).

Once \(Z\ne[11]\), the orientation paragraph is complete:

* if the indicator is zero on \(Z\), use its original nonempty side
  \(S_a\subseteq W\);
* if it is one on \(Z\), use the nonempty complementary side
  \(S_a^c\subseteq W\).

Properness of the original cut supplies nonemptiness in both cases.  The
subsequent independence of \((He_w)_{w\in W}\), existence of a left inverse,
and diagonal/off-diagonal argument therefore apply without an equality
assumption on \(|Z|\) and \(R\).

## Effect on the previous verdict

The round-3 result is strengthened from “PASS with three local presentation
issues” to **PASS with those issues resolved**.  Conditional on the earlier
audited endpoint \(t\ge16\), the proof still establishes \(t\ge17\).  It
still makes no claim about eliminating the \(t\ge17\) strata or proving the
full Kusner conjecture.

The previously created `audit/referee_t16_check.py` intentionally pins the
pre-fix proof hash.  It will now fail closed with a proof-hash mismatch; that
is expected snapshot-binding behavior, not a mathematical regression.  The
present task prohibited modifying that checker, and the reviewed edits touch
no finite arithmetic checked by it.

## Reproducible snapshot command

```bash
shasum -a 256 proof/t16_branch.md
```

Expected output:

```text
114d861529243e3eb96415e10f14920370b91f5085d1538fc0bb0f564e26d889  proof/t16_branch.md
```

## Proof-assistant disclosure

No proof assistant was used in this diff review.
