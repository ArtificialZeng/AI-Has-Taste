# Fresh mathematical referee report

## Scope and integrity

I reviewed the frozen `resolution-paper` claim at snapshot digest
`e9e0944aa0761b1462cfeaa42dc7f70dae85a561120181fd741194eda84b424a`
for referee job `win-00078-p02-referee-e76c10f4546a`. I compared every file
listed in `audit/snapshot.json` with its recorded SHA-256 digest; all ten
bindings matched. In particular, `source.md` retained digest
`f9adb36e67090507335a9f6da0565b5ccaab0a8243cf217146d1f5c14097e858`
and the complete manifest retained digest
`108e3463bd6ab92b8e07f2c3160118b302d44b25eaf8098761a056b6de29c62a`.

The exact frozen scope is an existential census over all three- and
four-reaction subsets of the 30 loop-free directed reactions on
`(0,X,Y,2X,X+Y,2Y)`, subject to the three stated retention filters, followed
by the requested lexicographic minimum modulo only the swap of `X` and `Y`.
The claim answers that full question, rather than a restricted substitute.

## Reconstruction of the witness

For

\[
E_*=(0\to X,\ 0\to2X,\ X\to Y,\ X+Y\to0)
\]

in the displayed reaction order, direct reconstruction gives

\[
S=\begin{pmatrix}1&2&-1&-1\\0&0&1&-1\end{pmatrix},\qquad
S^-=\begin{pmatrix}0&0&1&1\\0&0&0&1\end{pmatrix},\qquad
G=\begin{pmatrix}2&2\\-1&0\\0&1\\0&1\end{pmatrix}.
\]

The minor of stoichiometric columns 0 and 2 is 1, hence `rank(S)=2`.
Multiplication gives `SG=0`, and the columns of `G` are independent. At
`z=(-1,2)` they give the strictly positive steady flux
`v=Gz=(2,1,2,2)`.

Writing the independent nonzero reactivities as
`a=r_(X->Y),X`, `b=r_(X+Y->0),X`, and
`c=r_(X+Y->0),Y`, I independently expanded the matrices and obtained

\[
\det(SR_{\rm gen})=\det[\,R_{\rm gen}\mid G\,]=2ac.
\]

Thus the third retention filter and generic invertibility both hold. For
inverse row `Y` and reaction column `0->X`, deletion of reaction row 0 and
species column `Y`, with the adjugate sign, gives

\[
C_{0,Y}=-a+b.
\]

This is a nonzero polynomial in the independent symbols, so the generic
inverse entry is nonzero. Under mass action at `x=(1,1)`, one has
`a=v_2`, `b=v_3`, `c=v_3`, and hence

\[
C_{0,Y}^{\rm MA}=-v_2+v_3=-(Sv)_Y.
\]

This is an exact ideal identity, not a sampled cancellation. On `Sv=0`, the
recorded basis gives `det A_MA=2z_1^2`; at the positive flux above it is 8.
Indeed positivity forces `v_2=v_3>0`, so the denominator is nonzero on the
entire positive steady-flux locus for this witness. There is therefore no
division-by-zero gap. Finally,
`A_MA(v,x)=A_MA(v,(1,1)) diag(x_X^-1,x_Y^-1,I)` shows that changing to any
positive concentration merely rescales the two species rows of the inverse
and preserves their zero status. Positive rate constants realizing the
displayed `(v,x)` exist by `k_rho=v_rho/x^(source(rho))`.

## Exhaustiveness and lexicographic minimum

I inspected both supplied implementations and then wrote and ran a fresh
exact verifier which imported neither of them. It used `Fraction` arithmetic,
a pivot-pair construction of a rational null basis, direct Gaussian
determinants of `[R_MA|G]`, and direct adjugate minors. It regenerated all
31,465 labelled edge sets, obtained 133 swap-fixed sets and 15,799 canonical
orbits, and classified every orbit and every reaction/species pair. As a
separate check of the strict-positivity filter, I used nonnegative circuit
coverage (circuits of size at most three for a rank-two matrix), rather than
the slice/interval test in the supplied programs. That check agreed on all
15,799 manifest records.

The fresh full census reproduced the following exact counts:

| check | count |
|---|---:|
| rank-two canonical orbits | 15,607 |
| rank-two orbits with a strictly positive kernel vector | 5,176 |
| retained orbits | 5,168 |
| retained orbits with identically zero mass-action determinant | 463 |
| generic-nonzero inverse cofactors checked | 35,968 |
| additional mass-action-zero pairs with nonzero determinant | 1,432 |

I also parsed and cross-checked the core classification and every recorded
generic/witness flag in all 15,799 lines of `census-manifest.jsonl`. The first
witness in the frozen ordering was again orbit 303, network `E_*`, reaction
row 0, species `Y`. There was no witness in orbits 0 through 302. Within
orbit 303 the only earlier pair is reaction row 0, species `X`; its generic
cofactor is nonzero but its mass-action cofactor is a nonzero multiple of the
positive coordinate `v_3`, so it is not a witness. The species-swapped image
of `E_*` begins with `0->Y`, whereas `E_*` begins with `0->X`, confirming that
the displayed orientation is its canonical representative. Equivariance
under the species swap makes orbit enumeration cover every labelled network.

## Source comparison and limitations

I checked the actual supplied primary-source PDF. Equations (22)--(25) define
the independent-symbol reactivity matrix, `SR`, its nondegeneracy condition,
and `A=[R|C]`; equation (45) gives the inverse-sensitivity convention used in
the claim. Remark 3.6 explicitly distinguishes classical mass action from
parameter-rich kinetics and notes its extra algebraic constraints. Theorem
3.23 characterizes the independent-symbol influence pattern. None of those
passages states the finite six-complex census or its first witness. The
candidate appropriately makes no priority claim and no assertion for larger
complex sets, other reaction counts, or kinetics outside the frozen scope.

No mathematical or scope gap remains in the submitted claim. The direct
witness proves the existential answer, and the independently replayed exact
enumeration proves the requested lexicographic minimum.

## Verdict

**Accept.** The frozen resolution claim is correct at its exact stated scope,
the inverse and positivity hypotheses are satisfied without a degenerate
locus issue, and the exhaustive minimum is supported by reproducible exact
certificates plus a fresh full recomputation.
