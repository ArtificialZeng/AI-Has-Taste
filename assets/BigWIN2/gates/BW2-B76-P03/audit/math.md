# Fresh mathematical audit

**Verdict: accept.** The frozen `resolution-paper` claim proves the full
existential assertion in `source.md` by an exact four-dimensional witness.
The proof covers every vector-space complement of the displayed polarization;
it is not a finite or numerical search.

## Scope and snapshot

I reviewed snapshot
`1046c72193e41c234f4822c2378f8d62da6342dd7751ae2db2137d4e1fce6aca`.
I recomputed the canonical digest of its file-hash map and the SHA-256 hash of
each frozen file; all values agree with `audit/snapshot.json`. The candidate is
a full resolution of the frozen bounded existential statement, not a partial
classification claim: one valid witness of dimension at most four is decisive.

## Reconstruction of the witness

Let the ordered real basis be \((e_1,e_2,r,z)\), with nonzero brackets, up to
skew-symmetry,
\[
 [e_1,e_2]=e_1+z,\qquad [e_1,r]=-r,\qquad [z,r]=r.
\]
The four Jacobi sums on distinct basis triples vanish. For
\((e_1,e_2,r)\), the only surviving contribution is
\([r,e_1+z]=r-r=0\). For \((e_1,e_2,z)\) it is
\([z,e_1+z]=0\). For \((e_1,r,z)\), the two nonzero terms are
\([e_1,-r]=r\) and \([z,-r]=-r\). The \((e_2,r,z)\) sum is zero termwise.
Alternation then covers all triples. As exact machine cross-checks, the supplied
verifier checked all 64 ordered basis triples, and a separate change-of-basis
calculation checked all 16 identities
\([\operatorname{ad}_{e_i},\operatorname{ad}_{e_j}]
=\operatorname{ad}_{[e_i,e_j]}\).

Set \(V=\operatorname{span}(e_1,e_2,r)\). Since
\(z=[e_1,e_2]-e_1\), this \(V\) Lie-generates the four-dimensional algebra.
Also \(\mathfrak h=V\oplus\mathbb Rz\). For each basis vector \(B\) of
\(V\), \([B,z]\in V\), so the one-dimensional complement component of
\(\operatorname{ad}_B(z)\) is zero. By linearity,
\(\kappa_{\mathbb Rz}|_V=0\).

## Universal complement calculation

Every complement of this fixed codimension-one \(V\) has a unique normalized
generator
\[
 w=z-p,\qquad p=xe_1+ye_2+tr,
\]
for arbitrary \(x,y,t\in\mathbb R\). This is exhaustive: a vector spanning a
complement has a nonzero \(z\)-coefficient and can be uniquely normalized to
one; the graph basis \((e_1,e_2,r,w)\) has determinant one.

Because the complement is one-dimensional, its projected trace is the
coefficient of \(w\), equivalently the \(z\)-coefficient in the original
splitting. Direct expansion gives
\[
 \bigl(\kappa_{\mathbb Rw}(e_1),
       \kappa_{\mathbb Rw}(e_2),
       \kappa_{\mathbb Rw}(r)\bigr)=(-y,x,0).
\]
Thus the vertical balance condition holds exactly when \(x=y=0\), with
\(t\) unrestricted.

For the other trace, project \(\operatorname{ad}_w|_V\) along
\(\mathbb Rw\). Its diagonal entries in the ordered basis
\((e_1,e_2,r)\) are
\[
 y(1+x),\qquad -xy,\qquad 1+x,
\]
and hence
\[
 \kappa_V^{\mathbb Rw}(w)=1+x+y.
\]
If vertical balance holds, \(x=y=0\), and this horizontal trace is \(1\),
independently of \(t\). Therefore the two balance systems have no common real
solution. Linearity shows that checking the displayed bases and the generator
\(w\) checks the full quantified trace conditions. This proves that no
complement of the same \(V\) is modularly balanced.

I reran `evidence/verify_witness.py` under exact SymPy arithmetic; it returned
the same traces and remainder \(1\) on reducing \(1+x+y\) modulo the vertical
ideal \(\langle x,y\rangle\). I also recomputed the traces independently by
forming the four adjoint matrices and conjugating them into the graph basis.
That calculation again gave \((-y,x,0)\) and \(1+x+y\).

## Quantifiers, edge cases, and source comparison

No division by a parameter, limiting argument, topology, or unproved
classification enters the proof. The normalization of a complement is valid
precisely because its spanning line is not contained in \(V\). The parameters
range over all of \(\mathbb R^3\), including the unrestricted \(t\)-direction.
The witness has dimension exactly four, its displayed complement satisfies the
necessary half-condition, and failure of full balance is proved for every
complement, so every quantifier in the frozen assertion is met.

The frozen primary-source comparison records that Definition 8.2 and equations
(57)--(60) use exactly these projected trace conditions, and that Question 1
asks whether the necessary half-condition can hold although no modularly
balanced complement exists. Consequently this witness also supplies a positive
example for that existence question. The recorded literature search was a
small, date-bounded exact-phrase screen, so it does not establish priority or
exhaust the literature. The candidate expressly makes no priority claim; that
limitation does not weaken the exact mathematical resolution reviewed here and
should remain explicit in any manuscript.

## Gaps and decision

I found no mathematical gap or scope mismatch in the frozen claim. Broader
classification, minimality of dimension, and priority are not asserted and are
not needed to prove the original existential statement. The exact witness,
Jacobi and generation checks, and exhaustive graph-complement obstruction pass
review. **Verdict: accept.**
