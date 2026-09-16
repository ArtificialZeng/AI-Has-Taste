# Exact resolution certificate

## Result

In the conventions and order frozen by `source.md` and `problem.md`, the
lexicographically first triple for which the independent-symbol inverse entry
is nonzero but its classical-mass-action specialization is identically zero is

\[
E_*=(0\to X,\;0\to2X,\;X\to Y,\;X+Y\to0),\qquad
\rho=0\to X,\qquad m=Y.
\]

Thus the existential alternative in the frozen question has a positive answer.
The minimality assertion is an exact finite-computation claim, certified below;
the existence assertion also has the following short symbolic proof.

## Direct exact witness

In reaction order as displayed,

\[
S=\begin{pmatrix}1&2&-1&-1\\0&0&1&-1\end{pmatrix},\qquad
S^-=\begin{pmatrix}0&0&1&1\\0&0&0&1\end{pmatrix},\qquad
G=\begin{pmatrix}2&2\\-1&0\\0&1\\0&1\end{pmatrix}.
\]

The minor of columns 0 and 2 of \(S\) is 1, so \(S\) has rank two.
Direct multiplication gives \(SG=0\), and \(G\) has two independent columns.
At \(z=(-1,2)^T\),

\[
v=Gz=(2,1,2,2)^T>0.
\]

Let \(a=r_{2X}, b=r_{3X}, c=r_{3Y}\) denote the three independent
nonzero derivative symbols. Then

\[
R_{\rm gen}=\begin{pmatrix}0&0\\0&0\\a&0\\b&c\end{pmatrix},
\quad
A_{\rm gen}=
\begin{pmatrix}
0&0&2&2\\0&0&-1&0\\a&0&0&1\\b&c&0&1
\end{pmatrix}.
\]

Exact expansion gives

\[
\det(SR_{\rm gen})=2ac,\qquad
\det A_{\rm gen}=2ac,
\]

so the third retention filter holds. The signed cofactor for inverse row \(Y\)
and reaction column 0 is

\[
C_{0,Y}=-a+b,
\qquad (A_{\rm gen}^{-1})_{Y,0}=\frac{-a+b}{2ac},
\]

which is not the zero rational function in the independent symbols.

At \(x=(1,1)\), mass action specializes
\(a=v_2,b=v_3,c=v_3\). Its cofactor obeys the exact ideal identity

\[
-v_2+v_3=-(Sv)_Y\in\langle(Sv)_X,(Sv)_Y\rangle.
\]

For the displayed Gale basis, \(v=(2z_0+2z_1,-z_0,z_1,z_1)\), and direct
expansion gives

\[
\det A_{\rm MA}=2z_1^2.
\]

It is 8 at \(z=(-1,2)\), while the cofactor is identically zero on
\(Sv=0\). Hence the mass-action inverse is generically defined on the positive
steady-state locus and the claimed entry vanishes there. The normalization
argument in `problem.md` carries the zero status from \(x=(1,1)\) to every
positive concentration.

## Exhaustive lexicographic-minimality certificate

`evidence/exact_census.py` performs the full exact census. It forms all edge
subsets of sizes 3 and 4 from the 30 loop-free directed edges, replaces each by
the smaller of itself and its species-swapped image, deduplicates, and sorts.
This gives 31,465 labelled networks, 133 swap-fixed networks, and 15,799 orbits.
The target \(E_*\) is at zero-based orbit index 303.

All filter and cofactor decisions use rational arithmetic. For transparency,
the decisive formulas are:

- rank is exact row reduction;
- for nullity one, strict positivity checks the two orientations of a Gale
  vector; for nullity two, the inequalities \(Gz>0\) are intersected exactly
  on the slices \(z_0=1\) and \(z_0=-1\). Every strict feasible cone meets one
  of these slices (a feasible point with \(z_0=0\) has a feasible nearby point
  with nonzero first coordinate);
- \(\det(SR_{\rm gen})\ne0\) exactly when some allowed pair \((j,k)\) has
  \(\det(S_{\bullet j},S_{\bullet k})\ne0\), because its monomial
  \(r_{jX}r_{kY}\) has precisely that coefficient;
- after deleting reaction row \(\rho\) and species column \(m\), the generic
  cofactor is linear in the remaining independent-symbol column. If its
  mass-action specialization is \(a^Tv\), its exact normal form on
  \(v=Gz\) is \(a^TGz\), so it vanishes identically exactly when every
  coefficient of that linear form is zero;
- `det([R_MA|G])` is nonzero exactly when `det(S R_MA)` is nonzero: the map
  induced by \(S\) from the quotient by \(\ker S\) is an isomorphism, so the
  two determinants differ by a fixed nonzero basis scalar. The census also
  expands `det([R_MA|G])` directly for every retained orbit.

The complete JSON-lines manifest has one record for every orbit and includes
the filter decisions, exact Gale data, positive flux witness when applicable,
mass-action determinant polynomial, and every generic-nonzero cofactor normal
form. Its SHA-256 is

`108e3463bd6ab92b8e07f2c3160118b302d44b25eaf8098761a056b6de29c62a`.

The full run found 15,607 rank-two orbits, 5,176 with a strict positive kernel,
and 5,168 retained orbits. It checked 35,968 generic-nonzero pairs. These global
counts are not needed for the positive answer, but document full coverage.

`evidence/independent_replay.py` is a separate implementation that imports
neither the census code nor SymPy. It uses `fractions.Fraction`, its own Gaussian
elimination, and direct determinant formulas. It reconstructed the 15,799
ordered representatives, replayed all 304 orbits through index 303, and found
no witness in an earlier orbit or earlier pair. It then checked the positive
flux and cofactor identity and obtained a nonzero direct determinant (-8; the
sign differs because its first Gale vector has the opposite orientation). Its
machine record is `evidence/independent-replay.json`.

## Reproduction

From the project root:

```text
python3 evidence/exact_census.py
python3 evidence/independent_replay.py
sha256sum source.md evidence/census-manifest.jsonl evidence/external/2609.05100.pdf
```

The expected hashes are, respectively,

```text
f9adb36e67090507335a9f6da0565b5ccaab0a8243cf217146d1f5c14097e858
108e3463bd6ab92b8e07f2c3160118b302d44b25eaf8098761a056b6de29c62a
948965eb5b52a0229289fb7ac885ad02fdd2860d07b55724ee717f7bb2585bdf
```

This certificate resolves only the finite frozen census. It makes no priority
claim and no assertion about larger complex sets or networks with other sizes.
