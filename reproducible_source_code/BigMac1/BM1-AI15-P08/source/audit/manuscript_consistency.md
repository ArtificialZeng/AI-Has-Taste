# Final manuscript consistency audit

Audit date: 2026-08-29 (Asia/Shanghai)  
Manuscript audited: `paper/main.tex` (492 lines, as inspected after the
targeted repairs described below)  
Comparison set: `problem/formal_statement.md`, `proof/builder_notes.md`,
`audit/referee_low_degree.md`, `proof/proof_dag.md`, and
`audit/PROOF_AUDIT.md`.

## Publication-gate verdict

**PASS on mathematical consistency of every frozen claim.**  No fatal or
major mathematical defect remains in the current manuscript.  The theorem in
`paper/main.tex:99--113` is exactly the audited frozen theorem: complete for
positive degrees \(1,2,3\), conditional in degrees \(4,5\), and complete on
the stated even sparse-support class.  The all-unimodular residual strata
\(2|a_n|<A\), \(n=4,5\), are explicitly excluded and are not silently used in
any corollary.

**HOLD on the release-artifact gate only.**  The current mathematics may be
published after the two local release items in Section 4 are closed: the
promised package manifest must exist, and the final source must receive a
fresh clean build and recorded page-by-page PDF audit.  Neither item changes
the theorem or proof.

## 1. Fatal findings

None.

No displayed identity has a wrong conjugation, phase, exponent, coefficient,
or inequality direction.  No proof invokes Q4-U or Q5-U, and no numerical
experiment is promoted to a theorem.

## 2. Major findings

None in the frozen manuscript.

Q4-U and Q5-U remain **major gaps relative to the user's larger request to
decide all of \(n=2,3,4,5\)**, but they are not defects in the theorem that the
manuscript actually states.  The residual description at
`paper/main.tex:115--125` is exact.  The condition \(|a_n|<A\) in
\eqref{eq:residual} is redundant because \(2|a_n|<A\) already implies it, but it correctly emphasizes
the non-endpoint branch and does not enlarge or shrink the residual set.

## 3. Claim-by-claim mathematical audit

### 3.1 Definitions, normalization, and basic lemmas — PASS

- `paper/main.tex:34--76` agrees with the formal statement: degree is exact,
  zeros are counted with multiplicity, conjugate inversion is used, and the
  coefficient relation is \(a_k=\omega\overline{a_{n-k}}\).  The source's
  literal unconjugated-\(1/\zeta\) caveat is disclosed rather than silently
  harmonized.
- `paper/main.tex:78--86` uses the same inradius and open-disk target as the
  formal statement.
- The Hermitian reduction at `paper/main.tex:129--133` is valid: an output
  phase can be chosen so that \(a_k=\overline{a_{n-k}}\), and input rotations
  and nonzero output scaling preserve the covering ratio.
- The endpoint disk at `paper/main.tex:136--143` is the exact Vieta
  root-product argument.  It handles the endpoint-maximal branch in every
  degree and is correctly labeled as known/background at
  `paper/main.tex:88--94`.
- The boundary-preimage lemma at `paper/main.tex:145--169` has both required
  directions for later use: a boundary value has no disk preimage and has a
  unit-circle preimage; for a self-inversive polynomial, zero is a boundary
  value exactly in the all-unimodular situation used in the puncture argument.
- The Schur transform at `paper/main.tex:171--199` has the correct reversal,
  constant cancellation, leading coefficient
  \(|h_m|^2-|h_0|^2\), strict branch, and equal-product branch.  Boundary zeros
  are legitimately handled by radial contraction and root continuity.

### 3.2 Degrees one and two — PASS

Degree one follows from the endpoint disk.  The quadratic normal form and
boundary identity at `paper/main.tex:209--223` are correct:

\[
z^{-1}(P(z)-2r)=b+r(z-z^{-1}),
\]

and \(rz^2+bz-r\) has exactly one disk root for \(b>0\).  The endpoint tie,
the \(b=0\) degeneration, repeated roots, and unit-circle roots are all
covered.

### 3.3 Degree three — PASS

- The non-endpoint normalization
  \(P=\overline d+z+z^2+dz^3\) and \(A=1\) at
  `paper/main.tex:231--235` is valid.  In fact the non-endpoint branch gives
  \(|d|<1\); the stated weaker \(|d|\le1\) is harmless.
- The reciprocal quotient and first Schur identity at
  `paper/main.tex:236--249` are exact.  The nominal leading coefficient cannot
  vanish, and the equal-product branch is correctly excluded because the
  displayed transform is nonzero.  Thus \(|1+z|\ge1\).
- The center \(C=1/2+2\overline d\), half-angle reduction, and separation at
  `paper/main.tex:251--263` are exact.  The \(d\)-dependent part is purely
  imaginary, while the relevant real part is
  \(\frac72x-2x^3\ge3/2\) on \(x\in[1/2,1]\).
- The derivative Schur inequalities at `paper/main.tex:265--283` have the
  correct conjugation and endpoints:
  
  \[
  |d|\ge\frac13,\qquad
  |6\overline d-2|\le 9|d|^2-1,
  \]
  
  and they imply \(|C|\ge7/6\) when zero is a boundary value.
- The repaired homotopy at `paper/main.tex:285--298` now tracks loss of the
  **last** interior root.  At such a first loss \(C_{s_*}\) is a boundary
  value, so the nonzero separation or the all-unimodular zero estimate gives
  the required contradiction.  This closes the center-membership step without
  assuming that an arbitrary unit-circle crossing is a boundary value.
- The segment argument at `paper/main.tex:300--309` proves the radius-one disk
  and the stated stronger radii.  The equality example
  \((1+z)^3/3\) is normalized correctly.

### 3.4 Degree four — PASS for the stated partial theorem

The Hermitian form and non-endpoint value of \(A\) at
`paper/main.tex:320--325` are correct.  The reciprocal quotient, first Schur
factor, and quadratic \(K_z\) at `paper/main.tex:326--337` agree term by term
with the independently reconstructed identity.  The first transform is
nonzero and has exact degree two, hence \(S\ne0\).  Both the strict and equal
second-Schur branches give

\[
|cS+u^2|\le S^2-|b|^2,
\]

so the reverse triangle inequality legitimately yields
\(|S|\ge\max(|b|,|c|)=A\).  The conjugations and signs in

\[
z^{-2}(P(z)-2\overline d)
=S+dz^2-\overline d z^{-2}
\]

at `paper/main.tex:347--353` are exact; the last two terms are purely
imaginary.

The repaired center homotopy at `paper/main.tex:355--360` now uses first loss
of membership/last loss of an interior preimage.  Because exact degree gives
\(d\ne0\), that boundary value is nonzero.  The off-circle-zero and
all-unimodular topology at `paper/main.tex:361--369` then gives respectively
the full disk and the punctured disk, with the puncture outside the open disk
when \(2|d|\ge A\).

### 3.5 Degree five — PASS for the stated partial theorem

The reciprocal quotient reduction and half-phase variables at
`paper/main.tex:378--398` are exact and independent of the choice of square
root.  The repaired sentence at `paper/main.tex:399` records exact degree
three and hence \(S\ne0\) before the division implicit in

\[
|SC+B^2|\le S^2-|B|^2\Longrightarrow |S|\ge|C|.
\]

In the equal-product Schur branch both endpoint coefficients vanish, so the
same inequality remains valid.  The signs and conjugations in

\[
z^{-5/2}(P(z)-2\overline d)
=S+dz^{5/2}-\overline d z^{-5/2}
\]

at `paper/main.tex:406--412` are correct.  The quartic homotopy and
punctured-disk proof carry over with the stated quintic \(P_s\); thus
`paper/main.tex:413--419` proves exactly the branches in the theorem and no
more.

### 3.6 Residual strata and sparse subclass — PASS

The warning at `paper/main.tex:422--428` correctly says that the proof does
not fill zero in Q4-U or Q5-U.  The example \((1+z)^4/6\) has \(A=1\),
\(d=1/6\), all roots on the unit circle, and zero strictly inside the candidate
disk, so deleting the puncture would indeed be invalid.

The sparse corollary at `paper/main.tex:431--442` is exact:
\(P(z)=Q(z^m)\), \(A(P)=A(Q)\), and
\(z^m(\mathbb D)=\mathbb D\).  The endpoint
binomial identity at `paper/main.tex:444--449` is elementary, valid in every
positive degree, and explicitly disclaimed as a novelty claim.

### 3.7 Novelty and computational scope — PASS

The abstract now says \(1\le n\le3\), so it does not accidentally include
constant polynomials.  It describes the residual strata as unresolved in the
present work.  The claim-specific negative literature statement at
`paper/main.tex:122--125` and the scope statement at
`paper/main.tex:468--471` are bounded by the search date and do not claim a
proof of literature absence.  This agrees with the second novelty lock.  The
endpoint branch is labeled known, and the endpoint-binomial observation is
labeled non-novel.

The exact-verification section at `paper/main.tex:451--466` correctly limits
the programs to algebraic identities and keeps numerical searches diagnostic.
The proof-assistant disclosure is accurate: no proof assistant was used.

## 4. Remaining local release findings

### L1. Promised manifest not yet present

- **Location:** `paper/main.tex:484--488`, especially line 488.
- **Finding:** the manuscript says SHA-256 bindings and reproduction commands
  are in a package manifest, but no manifest file is currently present in the
  workspace.
- **Minimal repair:** create the release manifest with the promised commands,
  hashes, and artifact inventory, or replace line 488 by an exact pointer to
  the existing audit files that contain those data.
- **Classification:** local, nonmathematical, publication-gating.

### L2. Final-build/PDF audit evidence is not synchronized to current source

- **Locations:** `audit/PDF_AUDIT.md:1--3`; compare the publication claim in
  `TASK_STATUS.json:9`.
- **Finding:** `audit/PDF_AUDIT.md` still says “not yet run,” while
  `TASK_STATUS.json` says the visual PDF audit passed.  The manuscript was also
  edited after the earlier LaTeX audit, so the release build must be regenerated
  from the final source before retention.
- **Minimal repair:** run a clean converged build from the final
  `paper/main.tex`, rerun log/citation checks, render every page, record the
  page-by-page inspection in `audit/PDF_AUDIT.md`, and synchronize the status
  record.  No mathematical source change is required.
- **Classification:** local, nonmathematical, publication-gating.

## 5. Repairs resolved during this audit

The following defects were present in an earlier draft and are fixed in the
current source:

1. The cubic and quartic homotopies formerly referred to an arbitrary “first
   unit-circle crossing.”  That was too strong because a unit-circle preimage
   need not be a boundary value while another disk preimage remains.  The
   current text at `paper/main.tex:293--298` and `355--360` uses first loss of
   membership/last interior root.
2. The quintic implication divided by \(|S|\) without stating \(S\ne0\).  The
   current `paper/main.tex:399--404` supplies exact degree three first.
3. The abstract formerly said “degrees at most three,” which could include the
   excluded constant case.  Current `paper/main.tex:37--38` says
   \(1\le n\le3\).
4. The final scope paragraph formerly made an unbounded categorical openness
   claim.  Current `paper/main.tex:468--471` states only the dated search result
   and what remains unresolved in this work.
5. The stale builder-notes digest in `audit/PROOF_AUDIT.md` was refreshed.  Its
   current SHA-256 line matches the present file.

Subject to L1--L2, the manuscript is internally consistent, accurately scoped,
and mathematically ready for the frozen partial-theorem publication.
