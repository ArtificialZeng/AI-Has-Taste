# Fresh mathematical audit

- Referee job: `win-00077-p02-referee-c20489c93893`
- Frozen snapshot: `e8e48fe62a0cae459d86a046b490e06864e164163857f3b4712abeaa535cabc3`
- Candidate scope: `resolution-paper`, proving the full frozen assertion through weight eight
- Verdict: **accept**

## Frozen scope and source check

I reviewed the exact assertion in `source.md` and `problem.md`, the frozen
`claim.json`, every file named by `audit/snapshot.json`, and no owner verdict or
progress summary.  All eight frozen file hashes match the snapshot, and the
canonical digest recomputes to the value above.  The immutable source PDF has
the recorded SHA-256 digest.  Its Section 3.2 identifies the same admissible
quasi-shuffle algebra and weight, Theorem 3.5 proves
\(Z(\tau u)=Z(u)\), equation (42) defines the quotient by the full
quasi-shuffle ideal, and Conjecture 3.6 asserts the unrestricted isomorphism.
Thus the source supplies exactly the kernel inclusion used below, while the
claim remains restricted to the induced filtered piece \(W_8\).

## Reconstruction of the proof

Let \(V=W_8H^0\).  The generating series for nonempty admissible words is

\[
\frac{t}{1-3t+t^2},
\]

because the first positive index contributes \(t/(1-t)\), while a later
letter has series \(2t+t^2/(1-t)\).  Including the empty word gives exact
weight counts

\[
1,1,3,8,21,55,144,377,987,
\]

and hence \(\dim_{\mathbb Q}V=1597\).

For basis words \(u,v\) with
\(\operatorname{wt}(u)+\operatorname{wt}(v)\leq8\), set

\[
J=\operatorname{span}_{\mathbb Q}
\{v*(\tau(u)-u)\}\subseteq V.
\]

The binary-word implementation of \(\tau\) is correct: write
\(z_s=x^sz_0\), reverse the binary string, and interchange \(x\) and
\(z_0\).  It preserves admissibility and weight.  The three-term
quasi-shuffle recursion has integral coefficients, and merging indices does
not increase total weight because
\(\max(a+b,1)\leq\max(a,1)+\max(b,1)\).  Every displayed generator therefore
lies in \(V\) and in the full ideal \(I\), so \(J\subseteq I\cap V\).  The
certificate construction yields 4636 nonzero such rows in the fixed
1597-word basis; call their integer matrix \(R\).

Let \(C\) be the \(165\times1597\) integer matrix whose row of degree \(n\)
is \([q^n]Z(w)\), for \(0\leq n\leq164\).  The coefficient recurrence in the
evidence is exact.  For a positive index,

\[
[q^{m\ell}]\left(\frac{q^m}{1-q^m}\right)^s
=\binom{\ell-1}{s-1}\quad(\ell\geq s),
\]

whereas a zero index contributes the factor 1.  The update uses the strict
tail bound \(M-1\), including for zero-index suffixes.  Since every
admissible word starts with a positive index, an outer summation index above
164 cannot affect these retained coefficients.  Thus \(C\) is an exact
integer matrix, not a floating-point or asymptotic approximation.

The frozen certificates exhibit the following nonzero modular minors:

| prime | minor of \(R\) | determinant | minor of \(C\) | determinant |
|---:|---:|---:|---:|---:|
| 1000003 | \(1432\times1432\) | 795164 | \(165\times165\) | 372525 |
| 1000033 | \(1432\times1432\) | 221688 | \(165\times165\) | 994554 |

Both moduli are prime.  Nonvanishing of either pair of minors proves over
\(\mathbb Q\) that

\[
\dim J=\operatorname{rank}R\geq1432,
\qquad \operatorname{rank}C\geq165.
\]

Theorem 3.5 and multiplicativity of the quasi-shuffle evaluation give the
exact inclusion \(J\subseteq\ker C\).  Consequently

\[
1597=\dim V\geq\dim J+\operatorname{rank}C
\geq1432+165=1597.
\]

All inequalities are equalities, so \(\ker C=J\subseteq I\).  If
\(a\in W_8H^0\) satisfies \(Z(a)=0\) as a formal series, its first 165
coefficients vanish; hence \(Ca=0\), then \(a\in J\subseteq I\).  This is
precisely the quantified assertion frozen in the claim.  It is not an
inference from finite rank deficiency, and it does not assume the
conjectural dimension formula (44).

## Checks actually performed

I inspected the producer program line by line, including word enumeration,
the anti-involution, all three stuffle branches, strict-index updates, the
empty word, later zero indices, binomial coefficients, pivot extraction,
prime testing, and modular determinant selection.  The bounded modular
arithmetic stays within signed 64-bit range before each reduction.

I also wrote and ran `audit/independent_verify.py`, which does not import the
producer program.  It independently reconstructed all 1597 words and all
4636 nonzero ideal rows.  It rebuilt each selected relation minor, and it
recomputed the selected q-series columns using separate out-of-place suffix
tables rather than the producer's shared in-place update.  It reproduced all
four determinant residues in the table and checked the elementary anchors
\(Z(z_1)\) (divisor-count coefficients) and
\(Z(z_2)=Z(z_1z_0)\).  Finally, I reran the frozen producer for each prime;
the complete regenerated JSON streams had exactly the two snapshot hashes
`7bcfbd5901c787362d848f5bcf892dd6a6da69654afa4057f3c28aaa7ff876ed`
and
`704d36b2b12b8e91d7e721cd7227ce0a9b6075dc8dcf9c1a2809efaceeeaf235`.

## Scope, contribution, and limitations

The supplied Mozgovoy source leaves the all-weight isomorphism conjectural.
The scoped literature record in `problem.md` reports Takeyama's nearest
finite computation only through weight seven and reports no settlement of
this weight-eight assertion in the other inspected primary work.  Against
that frozen comparison, an exact independently reproducible weight-eight
certificate is a substantive full-scope resolution of the selected problem,
not a toy restriction or a routine corollary.  This audit does not assert an
exhaustive priority search beyond the bounded literature statement already
made in the claim.

No mathematical gap remains in the frozen assertion.  The proof neither
settles Conjecture 3.6 above weight eight nor proves that the displayed row
family equals all of \(I\cap V\); neither stronger statement is needed.
Possible cancellations from higher filtered degree are harmless because the
explicit subspace \(J\subseteq I\) already saturates the complementary
coefficient-rank bound.

**Verdict: accept.**
