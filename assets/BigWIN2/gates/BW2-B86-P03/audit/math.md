# Fresh mathematical referee report

**Verdict: accept.** The frozen `resolution-paper` claim is correct at its
exact stated scope. It proves both clauses of the immutable problem and does
not substitute EA inequivalence for CCZ inequivalence.

## Frozen scope and integrity

I reviewed the claim bound to snapshot
`a320fb6964e6a39e8b81a23f4dc99b39f13527219ea77c8601f179cd00288f1e`.
I recomputed the canonical snapshot digest and every listed file hash. They
match `audit/snapshot.json`. In particular, `source.md` still has SHA-256
`9b0a3b9fc1ae610c9ab9e3165640b060077794cfe36987fb04833f06c658b2dd`.

The claim to be judged is the full conjunction over the fixed field
\(\mathbb F_{11}\): the stated projective matrix maps all of \(S_{x^4}\)
onto \(S_{x^8}\), and no invertible affine map of \(\mathbb F_{11}^2\)
maps \(\Gamma_{x^4}\) onto \(\Gamma_{x^8}\). This is exactly the frozen
original problem, not a subsidiary or weakened statement.

## Reconstruction of the projective equivalence

Let
\[
M=\begin{pmatrix}1&0&0\\0&0&1\\0&1&0\end{pmatrix}.
\]
Its determinant is \(-1=10\pmod {11}\), so it induces a projectivity.
It interchanges the affine zero point \((0:0:1)\) and the added point
\((0:1:0)\). For \(x\ne0\),
\[
 M(x:x^4:1)=(x:1:x^4)=(x^{-3}:x^{-4}:1).
\]
Writing \(u=x^{-3}\), the map \(x\mapsto u\) permutes
\(\mathbb F_{11}^{*}\), because \(\gcd(3,10)=1\). Also
\(u^8=x^{-24}=x^{-4}\), since nonzero exponents may be reduced modulo
10. Hence the ten nonzero affine points map bijectively to
\((u:u^8:1)\), while the zero and infinite points map to one another.
This accounts for all 12 points. I independently applied the matrix to the
12 serialized source points and obtained exactly the serialized and directly
constructed target set.

## Reconstruction of the CCZ obstruction

For any affine permutation \(T(z)=Az+t\), subtraction cancels \(t\) and
gives
\[
 T(P)-T(Q)=A(P-Q).
\]
The induced map on ordered pairs is bijective. Thus, for every nonzero
\(w\),
\[
 \Delta_{T\Gamma}(Aw)=\Delta_\Gamma(w).
\]
Because invertible \(A\) permutes the 120 nonzero vectors, the complete
multiset of these counts is an affine-graph, hence CCZ, invariant. This
argument is self-contained and does not rely on a characteristic-two version
of a differential-spectrum theorem.

For \(d\in\{4,8\}\), a difference \((a,b)\) with \(a\ne0\) comes from
\((y+a,(y+a)^d)-(y,y^d)\). Substitution \(y=at\) gives
\[
 \Delta_d(a,b)=\#\{t\in\mathbb F_{11}:
       (t+1)^d-t^d=b/a^d\}.
\]
For \(a=0\) and \(b\ne0\), the count is zero; no division is made in this
case. Direct evaluation for \(t=0,\ldots,10\) gives the following counts,
indexed by the derivative value \(0,1,\ldots,10\):
\[
 d=4:\quad(1,3,0,0,1,1,1,1,0,0,3),
\]
\[
 d=8:\quad(1,1,2,0,1,1,1,1,0,2,1).
\]
For each of the ten choices \(a\ne0\), scaling by \(a^d\) only permutes
the eleven \(b\)-entries. Including the ten forced zero counts with
\(a=0,b\ne0\), the full 120-entry histograms are therefore
\[
 x^4:\quad\{0:50,\ 1:50,\ 3:20\},
 \qquad
 x^8:\quad\{0:30,\ 1:70,\ 2:20\}.
\]
They differ, already in their largest count, so no affine graph
equivalence exists.

I checked the edge cases relevant to this count: \((0,0)\) is excluded;
the other ten vertical vectors have count zero; each complete table has 120
entries; and its entries sum to 110, the number of ordered pairs of distinct
graph points. The tables decoded from
`evidence/research_exact_certificate.json` agree entry by entry with a fresh
direct enumeration of graph pairs.

As a separate falsification route, `audit/referee_exact_check.py` exhausts
all 13,200 matrices in \(\operatorname{GL}(2,11)\). Since the source graph
contains \((0,0)\), the translation in any possible equivalence must be one
of the 11 target graph points. Testing all 145,200 resulting affine maps
finds zero graph equivalences. This direct search does not use the histogram
obstruction. The supplied checker also ran successfully and reproduced its
frozen certificate byte for byte.

## Source comparison and contribution

I checked the current arXiv v2 primary text. Its Example 2.11 gives the
projective equivalence of \(x^4\) and \(x^8\) over \(\mathbb F_{11}\) but
records only their EA inequivalence. Its Definition 2.14 defines CCZ
equivalence by an invertible affine transformation between graphs, and its
Open Problem 4 asks whether projectively equivalent polynomials can fail to
be CCZ-equivalent. Thus the exact non-CCZ proof above supplies the missing
clause and makes this pair a witness for that stated open problem.

The difference table/differential spectrum is established prior machinery;
the candidate expressly makes no claim to have invented it. The invariant
needed here is also proved directly in the candidate's scope. A fresh bounded
search using the exact pair, the primary paper identifier, and the wording of
Open Problem 4 found no later primary resolution. This negative search is
appropriately treated only as a literature limit, not as proof of priority.
The manuscript/release phase should still verify final bibliographic metadata
and use bounded novelty language, but this leaves no gap in the mathematical
claim under review.

## Final assessment

All quantifiers in the frozen claim are discharged: the matrix is an explicit
valid witness for projective equivalence, and the unequal invariant rules out
every affine permutation allowed by CCZ equivalence. The exact certificate is
complete and independently reproducible. The new-to-the-primary-source
non-CCZ separation is a substantive full resolution of the frozen problem.
There is no unresolved mathematical gap requiring revision.
