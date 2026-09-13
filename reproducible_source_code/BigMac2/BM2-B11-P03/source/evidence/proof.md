# Exact resolution of the independent-row `(2,2)` product

All groups and species below use the convention frozen in `problem.md`.  Put

\[
G=S_4,\qquad H=\langle(12),(34)\rangle
 =\{e,(12),(34),(12)(34)\}.
\]

## Theorem

For the independent-row molecular species (K_{(2,2)}=X^4/H),

\[
K_{(2,2)}\times K_{(2,2)}
 \cong 2K_{(2,2)}\;\coprod\;K_{(1,1,1,1)}.
\]

Consequently, in the order

\[
(4),(3,1),(2,2),(2,1,1),(1,1,1,1),
\]

the requested coefficient vector is

\[
(0,0,2,0,1).
\]

This expansion is unique as a species decomposition and in the Grothendieck
group.  There are no nonzero integral linear relations among the five displayed
species, and there are no nonzero integral relations among their five cycle
indices.

## Complete double-coset proof

The diagonal (G)-set (G/H\times G/H) has the standard orbit decomposition

\[
G/H\times G/H\cong
\coprod_{HgH\in H\backslash G/H}G/(H\cap gHg^{-1}). \tag{1}
\]

We determine every term without relying on enumeration.  The only
transpositions in (H) are ((12)) and ((34)).  Conjugation preserves cycle
type, so every element of (N_G(H)) must preserve the unordered pair

\[
\big\{\{1,2\},\{3,4\}\big\}.
\]

Conversely, every permutation preserving that block system normalizes (H).
Thus

\[
N_G(H)=(S_{\{1,2\}}\times S_{\{3,4\}})\rtimes S_2,
\qquad |N_G(H)|=2^2\cdot2=8.
\]

Since (H\triangleleft N_G(H)) and ([N_G(H):H]=2), the normalizer is the
disjoint union of the two double cosets represented by (e) and
(q=(13)(24)).  Both have size four, and both have intersection subgroup (H).

Now take (r=(23)).  Direct conjugation gives

\[
rHr^{-1}=\{e,(13),(24),(13)(24)\},
\qquad H\cap rHr^{-1}=\{e\}.
\]

The double-coset cardinality formula therefore gives

\[
|HrH|=\frac{|H|^2}{|H\cap rHr^{-1}|}=16.
\]

Moreover (HrH\cap N_G(H)=\varnothing): otherwise (h_1rh_2\in N_G(H))
for some (h_1,h_2\in H\subset N_G(H)), which would imply (r\in N_G(H)),
contrary to (r\{1,2\}=\{1,3\}).  The complement of the order-eight
normalizer in (S_4) has exactly sixteen elements, so (HrH=G\setminus N_G(H)).
This proves that the three representatives

\[
e,\quad (23),\quad (13)(24)
\]

are complete, with double-coset sizes (4,16,4) and intersection orders
(4,1,4), respectively.  Substitution in (1) proves

\[
G/H\times G/H\cong G/H\;\coprod\;G/1\;\coprod\;G/H,
\]

which is the asserted species identity.

The machine-readable certificate `evidence/s4_certificate.json` independently
lists all 24 permutations (one-line and cycle notation), their double coset,
and each intersection.  Its generator, `evidence/s4_certificate.py`, asserts
pairwise disjointness, union equal to (S_4), the double-coset size formula,
the normalizer description, and every identity below using only exact integer
and rational arithmetic.

## Exact table-of-marks and uniqueness check

Let the row subgroups and column stabilizers, in both cases, be

\[
G_{(4)},G_{(3,1)},G_{(2,2)},G_{(2,1,1)},G_{(1,1,1,1)}.
\]

For (M_{K,L}=|(G/L)^K|), exhaustive coset containment gives

\[
M=\begin{pmatrix}
2&0&0&0&0\\
0&2&0&0&0\\
0&0&2&0&0\\
0&0&2&2&0\\
6&8&6&12&24
\end{pmatrix},
\qquad \det M=384.
\]

The (G/H) mark vector is (m=(0,0,2,2,6)^T).  Fixed points commute with
Cartesian products, so the product has mark vector

\[
m\odot m=(0,0,4,4,36)^T.
\]

Exact rational elimination gives the unique solution

\[
Mc=m\odot m,\qquad c=(0,0,2,0,1)^T.
\]

In particular the displayed five transitive species have no integral relation.
This also follows abstractly from uniqueness of orbit decomposition: their
stabilizers are pairwise nonconjugate (the only equal orders are the cyclic
(G_{(4)}\cong C_4) and noncyclic (G_{(2,2)}\cong C_2^2)).

For the separate cycle-index question, use power-sum rows

\[
p_4,p_3p_1,p_2^2,p_2p_1^2,p_1^4
\]

and the same five species columns.  Their exact coefficient matrix is

\[
\begin{pmatrix}
1/2&0&0&0&0\\
0&2/3&0&0&0\\
1/4&0&1/4&0&0\\
0&0&1/2&1/2&0\\
1/4&1/3&1/4&1/2&1
\end{pmatrix},
\qquad \det=\frac1{24}\ne0.
\]

Hence their cycle indices also have zero integral relation module.

## Exact power-sum identity

The two relevant cycle indices are

\[
Z_H=\frac14\left(p_1^4+2p_2p_1^2+p_2^2\right),
\qquad Z_1=p_1^4.
\]

Using
(p_\lambda\star p_\mu=\delta_{\lambda\mu}z_\lambda p_\lambda) and

\[
z_{(1^4)}=24,\qquad z_{(2,1,1)}=4,\qquad z_{(2,2)}=8,
\]

one obtains exactly

\[
Z_H\star Z_H
=\frac32p_1^4+p_2p_1^2+\frac12p_2^2
=2Z_H+Z_1.
\]

This is an arithmetic check of the species proof, not its replacement.

## Reproduction and gap list

Run

```sh
python3 evidence/s4_certificate.py --output evidence/s4_certificate.json
```

from the project root.  Repeated runs are byte-identical.  At the time of this
proof, the SHA-256 values are

- `395feb3435a195c79aff0f2c3dd3481831dbef46efcec1ca38c14e62d51bb3f7`
  for `evidence/s4_certificate.py`;
- `49c3629f84c0369b1ebdf469fca48d2277201f9f2aecd0a3c717fa5a57ec7f8b`
  for `evidence/s4_certificate.json`.

Known mathematical gaps in the stated finite result: none.  This has not yet
received the workflow's fresh-referee audit, and no novelty or priority claim is
made here.
