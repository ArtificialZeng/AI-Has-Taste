# Finite result dossier: first residue-choice incompatibility

## Candidate theorem and scope

With the definitions frozen in `source.md` and made precise in `problem.md`,

\[
 n_*=24,
 \qquad
 \mathcal G_{24}
   =\bigl\{\{2\}\cup T:T\subseteq\{8,14,20\}\bigr\}.
\]

Thus the full literal classification consists of the eight sets

\[
\begin{gathered}
\{2\},\ \{2,8\},\ \{2,14\},\ \{2,20\},\\
\{2,8,14\},\ \{2,8,20\},\ \{2,14,20\},\
\{2,8,14,20\}.
\end{gathered}
\]

This is only a finite, source-derived result.  It does not settle the motivating
asymptotic question \(E(n)/N(n)\to0\), whose status remains unresolved here.
Publication novelty is also status-uncertain: the comparison made in this pass
is with Raso--Venturi, arXiv:2609.08528v1, especially Definitions 26 and 28--29,
Theorem 30, Corollaries 31 and 33, Remark 34, and Proposition 36.  Those passages
give the criterion and recurrence and note the possibility of incompatible
choices, but do not state a first layer or its classification.

## Exact exhaustive certificate

The search used no floating-point arithmetic.  A subset of
\(X_n=\{2,\ldots,n+1\}\) is an integer bit mask.  For every fixed \(n\),
`prop36_generator.py` begins with \(U_{1,n}=\{0\}\) and, for each
\(j=2,\ldots,n\), replaces the current set by

\[
 \{u\mathbin{\mathrm{OR}}e_{j,a}:u\in U_{j-1,n},\ 0\leq a<j\},
\]

where bit \(m-2\) of \(e_{j,a}\) is one exactly when
\(j<m\leq n+1\) and \(m\equiv a\pmod j\).  Deduplication is exact integer-set
deduplication.  Induction on \(j\) shows that the masks after stage \(j\) are
exactly all unions \(E^{(n)}_{2,r_2}\cup\cdots\cup E^{(n)}_{j,r_j}\).
Taking complements after stage \(n\) therefore gives exactly \(\mathcal F_n\).

For each survivor, `theorem30_csp.py` independently constructs every
\(\Omega_k^+(A)\) and every omitted-point clause from the definitions.  Its
backtracking is exhaustive: at an uncovered clause \(m\), any completing model
must set one still-unassigned witness variable \(a_k\) to \(m\bmod k\), and the
solver branches over every such witness.  An assigned matching variable would
already cover \(m\), while an assigned nonmatching variable cannot later do so.
Induction on the search tree proves that `sat` is returned exactly for the
Theorem 30 models.

The resulting complete layer totals are:

| \(n\) | \(N(n)=|\mathcal F_n|\) | CSP-extendible | satisfies \(L_n\) | \(|\mathcal G_n|\) |
|---:|---:|---:|---:|---:|
| 1 | 1 | 1 | 1 | 0 |
| 2 | 2 | 1 | 1 | 0 |
| 3 | 3 | 1 | 1 | 0 |
| 4 | 4 | 2 | 2 | 0 |
| 5 | 6 | 2 | 2 | 0 |
| 6 | 8 | 3 | 3 | 0 |
| 7 | 11 | 3 | 3 | 0 |
| 8 | 14 | 3 | 3 | 0 |
| 9 | 17 | 5 | 5 | 0 |
| 10 | 22 | 8 | 8 | 0 |
| 11 | 30 | 8 | 8 | 0 |
| 12 | 38 | 12 | 12 | 0 |
| 13 | 50 | 13 | 13 | 0 |
| 14 | 63 | 13 | 13 | 0 |
| 15 | 76 | 13 | 13 | 0 |
| 16 | 89 | 28 | 28 | 0 |
| 17 | 117 | 30 | 30 | 0 |
| 18 | 147 | 45 | 45 | 0 |
| 19 | 192 | 45 | 45 | 0 |
| 20 | 237 | 51 | 51 | 0 |
| 21 | 288 | 61 | 61 | 0 |
| 22 | 349 | 102 | 102 | 0 |
| 23 | 451 | 102 | 102 | 0 |
| 24 | 553 | 113 | 121 | 8 |

`first_incompatibility.json` serializes, for every row, all final survivor,
extendible, and locally feasible masks.  It also gives every Proposition 36
stage count, local mask, canonical stage hash, all eight full domain/clauses
records, deletion-minimal unsatisfiable cores, and replayable branch trees.  At
\(n=24\), the partial-union counts for \(j=1,\ldots,24\) are

\[
1,2,6,18,82,167,331,501,551,553,
\underbrace{553,\ldots,553}_{j=11,\ldots,24}.
\]

The published initial values \(N(1),\ldots,N(12)\) and
\(E(1),\ldots,E(10)\) are reproduced.  As a further independent check,
the generated family at \(n=25\) has size 666, and all 553 tests satisfy

\[
 A\text{ is CSP-extendible at }n=24
 \quad\Longleftrightarrow\quad A\cup\{26\}\in\mathcal F_{25}.
\]

There are 113 sets on both sides, also giving \(666-553=113\).

## Independent replay

`independent_audit.py` imports none of the search implementations.  It uses
`frozenset` unions rather than bit masks to regenerate every \(\mathcal F_n\),
and decides Theorem 30 by a different dynamic program: after modulus \(k\), its
states are exactly all unions of coverage blocks attainable by one domain value
for each modulus through \(k\).  It compares the complete survivor,
extendible, and local families—not only their cardinalities—with the serialized
certificate.  It independently obtains the same 24 rows, the same eight sets,
and the same Definition 26 cross-check against \(\mathcal F_{25}\).

The exact replay commands are

```text
/Users/mac/4prove-or-disprove-math/.research-venv/bin/python \
  evidence/find_first_incompatibility.py --max-n 80 \
  --output evidence/first_incompatibility.json
/Users/mac/4prove-or-disprove-math/.research-venv/bin/python \
  evidence/independent_audit.py
```

The first command deliberately stops upon finding the first nonempty layer, so
the recorded search coverage is exactly \(1\leq n\leq24\), not through 80.

## Membership and local feasibility of all eight sets

For completeness, here are explicit profiles realizing the eight survivors.
For every row set

\[
r_2=r_3=r_5=1,\quad
r_6=r_8=r_9=r_{11}=r_{12}=0,\quad
r_{14}=\cdots=r_{24}=0,
\]

and use the four displayed values below.  Direct substitution in the definition
of \(S_{24}(r)\) gives \(S_{24}(r)=\{2\}\cup T\); this replay is also asserted
and checked in `independent_audit.json`.

| \(T\) | \(r_4\) | \(r_7\) | \(r_{10}\) | \(r_{13}\) |
|---|---:|---:|---:|---:|
| \(\varnothing\) | 0 | 0 | 0 | 0 |
| \(\{8\}\) | 1 | 0 | 0 | 0 |
| \(\{14\}\) | 0 | 1 | 0 | 0 |
| \(\{20\}\) | 1 | 1 | 1 | 1 |
| \(\{8,14\}\) | 1 | 2 | 0 | 0 |
| \(\{8,20\}\) | 1 | 0 | 1 | 0 |
| \(\{14,20\}\) | 1 | 1 | 1 | 0 |
| \(\{8,14,20\}\) | 1 | 2 | 1 | 0 |

The following single list exhibits nonempty residue domains simultaneously for
all eight sets: choose the listed \(d_k\in\Omega_k^+(A)\).

| \(k\) | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 | 11 | 12 | 13 | 14 | 15 | 16 | 17 | 18 | 19 | 20 | 21 | 22 | 23 | 24 |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| \(d_k\) | 1 | 0 | 1 | 2 | 0 | 2 | 0 | 0 | 1 | 0 | 0 | 2 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |

Every omitted point has a witness as follows.

- If \(m\) is odd, use \((k,m\bmod k)=(2,1)\).
- If \(m\) is even and \(m\equiv0\pmod3\), use \((3,0)\).
- If \(m\) is even and \(m\equiv1\pmod3\), use \((3,1)\).
- The remaining possible omitted points are 8, 14, and 20.  Use respectively
  \((5,3),(5,4),(5,0)\).  These residues are distinct modulo 5; when the
  corresponding point is omitted, its residue is not forbidden by another
  member of \(T\), and none equals \(26\bmod5=1\).

This proves \(L_{24}(A)\) for every listed \(A\), independently of global CSP
satisfiability.

## Human-readable unsatisfiable conflict core

The same two-point core works for every one of the eight sets.  Since the new
point is 26 and every optional survivor 8, 14, or 20 is congruent to 2 modulo
3,

\[
 \Omega_2^+(A)=\{1\},\qquad \Omega_3^+(A)=\{0,1\}.
\]

For omitted point 4, modulus 2 offers residue 0, which is not admissible, while
modulus 3 offers residue 1.  Therefore

\[
 W_A(4)=\{3\},\qquad 4\text{'s clause forces }a_3=1.
\]

For omitted point 6, modulus 2 again offers inadmissible residue 0; modulus 3
offers residue 0; modulus 4 offers \(2=26\bmod4\); and modulus 5 offers
\(1=26\bmod5\).  Hence

\[
 W_A(6)=\{3\},\qquad 6\text{'s clause forces }a_3=0.
\]

The two clauses are incompatible.  They are deletion-minimal as a pair, so
each listed set is not extendible by Theorem 30 despite satisfying every local
nonemptiness condition.

## Integrity and remaining limits

- Frozen `source.md` SHA-256:
  `a4e8a9bb1fdaa7a9e9b0266a518a1ee0d134f343adf5c7f056e20034d68aa67e`.
- Search certificate SHA-256:
  `9aa3f366471bd31815492eebfdfc85f2fbaa975e4394ee1cf96bff283062857e`.
- Independent audit output SHA-256:
  `2c6f9a49fb3f236fca4f57c1c5bb7f6c67c6717ff7ac6342380c101a4bcf1035`.

No mathematical gap is presently known in the stated finite theorem.  It is a
research candidate, not a certified result: a fresh referee audit and any
broader novelty screen remain pending.  No claim is made outside the exact
finite scope above.
