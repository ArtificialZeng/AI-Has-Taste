# Fresh mathematical referee report

- Referee job: `win-00047-p02-referee-cb19b9efef84`
- Frozen snapshot: `bd5dbd5a44433d0e256a98c44f8a0078a26488047e4a7af8e835631852b7e126`
- Candidate kind and status: `resolution-paper`, `proved`

## Scope reviewed

I reviewed the exact frozen claim: for the six graphs obtained by deleting one
nonzero slope from the canonical order-seven Desarguesian MALS family, all six
graphs are isomorphic, with the stated coordinate map providing an explicit
isomorphism for every ordered pair.  The claim is restricted to the fixed
order-eight Paley matrix and the precise construction in `problem.md`.

The snapshot contains `claim.json`, `source.md`, `problem.md`, the proposed
proof, the verifier and its summary, the explicit certificate collection, and
all six adjacency lists.  I recomputed the canonical SHA-256 digest of the
13-file hash mapping and obtained the declared snapshot digest.  Each listed
file's current SHA-256 digest also agrees with `audit/snapshot.json`.

## Reconstruction of the decisive argument

For a deleted slope \(a\), write
\(S_a=\mathbb F_7^*\setminus\{a\}\).  Given nonzero \(a,b\), set
\(u=ba^{-1}\).  Then multiplication by \(u\) is a bijection
\(S_a\to S_b\), because it maps the unique omitted slope \(a\) to \(b\).
Multiplication by \(u^{-1}\) is a bijection on the row coordinate, and the
Hadamard coordinate is unchanged.  Thus

\[
 \phi_{a,b}(\alpha,r,x)=(u\alpha,u^{-1}r,x)
\]

is a bijection \(\Omega_a\to\Omega_b\).

For equal slopes, both slope equality and row inequality are preserved, so
the full \(A_4\) adjacency relation is preserved.  For distinct slopes, all
denominators below are nonzero in \(\mathbb F_7\), and direct substitution
gives

\[
\begin{aligned}
K_{u\alpha,u\beta}(u^{-1}r,u^{-1}s)
 &=\frac{(u\alpha)(u\beta)u^{-1}(r-s)}{u(\beta-\alpha)}\\
 &=\frac{\alpha\beta(r-s)}{\beta-\alpha}
 =K_{\alpha,\beta}(r,s).
\end{aligned}
\]

Consequently the same outer-product matrix \(B_K\) is consulted before and
after applying \(\phi_{a,b}\).  Since \(x,y\) are fixed, the condition
\((B_K)_{xy}=+1\) is unchanged.  This preserves the \(A_2\) relation as well.
The bijection therefore preserves adjacency in both directions and is a graph
isomorphism.  This works for every one of the 36 ordered pairs \((a,b)\), so
all six nonempty graphs form exactly one isomorphism class.  The ordered
adjacency file `evidence/adjacency/G_1.adj` is therefore a reproducible
representative of that class.

The argument covers the potentially problematic cases: \(a,b,u\) are
nonzero; the common-symbol denominator is used only when
\(\alpha\ne\beta\); scaling preserves both equality and inequality of row
labels; and the two adjacency relations exhaust the graph definition.  No
property of the Paley matrix beyond using the same fixed matrices \(B_t\) on
both sides is smuggled into the isomorphism argument.

## Exact artifact checks

I ran the supplied verifier in read-only verification mode:

```text
python3 evidence/verify_slope_scaling.py --verify-existing
```

It reconstructed six graphs with 280 vertices, constant degree 160, and
22,400 edges, reproduced the saved files byte for byte, and accepted all 36
ordered certificates.

I also performed a separate in-memory reconstruction without importing the
supplied verifier.  It parsed every saved adjacency list, rebuilt every edge
from the Latin-square/common-symbol and Paley-row definitions, and obtained
exact equality for all six graphs.  It independently checked simplicity,
symmetry, degree 160, and 22,400 edges.  It exhaustively checked all 1,470
choices of distinct slopes and two row labels against the scan definition of
the common symbol, all 8,820 corresponding nonzero scalings for invariance of
that symbol, and all 36 serialized 280-entry permutations for exact coordinate
mapping, bijectivity, and equality of image-neighbor sets.

These computations are corroborative rather than substitutes for the symbolic
proof.  They do additionally meet the frozen question's demand for
independently checkable adjacency lists and explicit vertex permutations.

## Source comparison and contribution

The frozen source asks for the number of isomorphism classes, a representative,
and complete certificates, and specifically asks whether the six graphs are
pairwise isomorphic.  The candidate answers each item at the exact frozen
scope.  The nearest result recorded in the frozen problem supplies the graph
construction and common invariants but not this deletion classification.  The
candidate makes no broader assertion for other Hadamard matrices or MALS
families and no priority claim.  Therefore the contribution is correctly
described as a complete resolution of this scoped finite classification, not
as a resolution of the broader dependence-on-inputs question.

## Gaps and verdict

I found no mathematical or certificate gap in the frozen claim.  The scope,
correctness, exact evidence, and stated contribution pass review.

**Verdict: accept.**
