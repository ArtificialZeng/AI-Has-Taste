# Fresh mathematical referee report

Job: `win-00086-p05-referee-5dc71284a72c`  
Snapshot: `8f1b363bbd8b237d7500a1ba0c2d0a8bb86ea36dcef9c3ff602c3032595c87db`

## Scope and integrity

I reviewed the exact `resolution-paper` claim frozen in `claim.json`: there is
no signed coefficient function on \(G=\mathbb F_3^2\) with support size eight
and

\[
DD^{(-1)}=7[0]+\sum_{x\in G}[x].
\]

The SHA-256 digests of `claim.json`, `source.md`, `problem.md`, and all six
other files enumerated by `audit/snapshot.json` agree with the snapshot. The
claim is equivalent to, and covers the full quantifier scope of, the frozen
source problem; it is not a subsidiary or symmetry-restricted statement.

## Independent reconstruction of the proof

Suppose such a \(D=\sum_x a_x[x]\) exists. Applying the principal character
to the asserted group-ring identity gives

\[
\left(\sum_x a_x\right)^2=7+9=16.
\]

If \(p\) and \(n\) are the numbers of coefficients equal to \(+1\) and
\(-1\), then \(p+n=8\) and \(p-n=\pm4\). Thus the sign counts are \((6,2)\)
or \((2,6)\). Global negation preserves \(DD^{(-1)}\), so every candidate may
be put in the first case.

There is exactly one zero coefficient. Translating its position to \(0\)
preserves the product: if the old zero is \(z\), multiplication of \(D\) by
\([-z]\) is cancelled by multiplication of \(D^{(-1)}\) by \([z]\). Hence,
for distinct \(a,b\in G\setminus\{0\}\), every normalized candidate is

\[
D=\sum_{x\ne0}[x]-2([a]+[b]). \tag{1}
\]

Let \(\omega^2+\omega+1=0\), and for \(u\in\mathbb F_3^2\) put
\(\chi_u(x)=\omega^{u\cdot x}\). For nonzero \(u\), this is a nonprincipal
character. Applying it to the defining identity is legitimate and yields

\[
|\chi_u(D)|^2=7,
\]

because \(\chi_u(D^{(-1)})=\overline{\chi_u(D)}\) and
\(\sum_x\chi_u(x)=0\). Consequently \(\sum_{x\ne0}\chi_u(x)=-1\), so (1)
gives

\[
\chi_u(D)=-1-2\bigl(\chi_u(a)+\chi_u(b)\bigr). \tag{2}
\]

The pair \(\{a,b\}\) has two exhaustive types.

* If it is dependent, then distinctness and nonzeroness over \(\mathbb F_3\)
  force \(b=-a\). The kernel of \(u\mapsto u\cdot a\) is one-dimensional, so
  it contains a nonzero \(u\). For this \(u\), equation (2) gives
  \(\chi_u(D)=-5\), of exact squared modulus \(25\), contradicting \(7\).

* If it is independent, the map
  \(u\mapsto(u\cdot a,u\cdot b)\) is invertible. There is therefore a unique
  \(u\) with both coordinates equal to \(1\); it is nonzero. Equation (2)
  gives \(\chi_u(D)=-1-4\omega\), whose exact norm is
  \[
  (-1-4\omega)(-1-4\omega^2)
  =1+4(\omega+\omega^2)+16=13,
  \]
  again contradicting \(7\).

Thus every possible pair is obstructed, and the assumed signed difference
set does not exist.

## Quantifier, symmetry, and computation checks

No pair is lost through an unproved representative choice: distinct nonzero
vectors are either opposites or a basis. These classes contain respectively
four and twenty-four of the \(\binom82=28\) unordered pairs. They are also
the two `GL(2,3)` orbits, but transitivity is not needed for the proof because
the character is constructed for each pair type. Translation accounts for
all nine zero locations, and global sign accounts for both allowed sign-count
orientations.

I replayed all three exact supplied checkers with Python 3; each exited zero.
`research_independent_audit.py` reported 2,304 raw assignments, 504
principal-character-eligible assignments, all 28 normalized pairs with
multiplicity 18, orbit sizes 4 and 24, norms 25 and 13 for the selected
characters, and zero solutions. `full_assignment_check.py` independently
enumerated all 2,304 raw autocorrelations and found zero solutions.
`exact_character_check.py` checked all eight nonprincipal Eisenstein norms
and all eight nonzero autocorrelations for every normalized pair, again with
zero passing pairs. The finite checks corroborate rather than replace the
argument above.

I specifically checked the potential failure points: the unique-zero claim
uses support size eight in a group of order nine; the two negative positions
are distinct and nonzero after normalization; both selected character vectors
are nonzero; complex conjugation matches group inversion; the Eisenstein norm
calculations are exact; and no limiting, compactness, division, or empty-domain
issue occurs.

## Source comparison and contribution

The current official arXiv record for He--Wu, *Nonexistence Results and
Constructions for Signed Difference Sets* (arXiv:2608.22936), was checked on
2026-09-10. It still lists only v1 (2026-08-24). Its equations (2.3) and (2.4)
give the same principal and nonprincipal character conditions, while its
listed general results do not state this group-specific resolution. The
authors' official reproducibility repository currently shows the fixed
`sds.json` database snapshot, four commits, and the documented meaning of
`Open`; the 4.95 MB row itself was not renderable through the available web
interface. Exact-title, parameter, and equivalent-notation searches found no
later primary-source resolution. This is a bounded literature comparison,
not an unrestricted priority claim, and the access limitation does not affect
the self-contained nonexistence proof.

The proposed delta is therefore credible and mathematically substantive in
the frozen workflow sense: it completely resolves the identified open
group-specific case. A short proof is sufficient, and no claim weakening or
repair is needed.

## Verdict

**Accept.** The frozen full-scope nonexistence claim is correct, its
normalizations and character choices exhaust every case, the exact
computations reproduce successfully, and the contribution is honestly
scoped. No unresolved mathematical gap was found.
