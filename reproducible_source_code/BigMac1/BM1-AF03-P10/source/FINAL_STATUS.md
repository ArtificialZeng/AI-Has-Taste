# Final status: Lotka–Volterra tree-systems：首个未验证阶 \(n=9\)

## PROVED

The original problem is complete.  In fact, the generic conjecture is proved
for every order, not only for (n=9): if two finite simple trees of the same
order (n\ge2) have linearly LV-equivalent generic homogeneous tree classes
over a characteristic-zero field, allowing a birational parameter remapping,
then the trees are isomorphic.

## Proof endpoint

At the generic point, the complete projective set of linear Darboux
polynomials consists of the (n) coordinates and the (n-1) edge forms.
Supports of size at least three are excluded exactly by C2--C3 and algebraic
independence.  Recursive diagonal scaling identifies their coefficient
configuration with the reduced incidence configuration of the cone over the
tree.  Its three-element circuits are precisely

\[
\{[x_u],[P_{uv}],[x_v]\},\qquad uv\in E(T),
\]

and the resulting 3-uniform hypergraph reconstructs the unlabeled tree.
Linear conjugacy bijects the full projective Darboux set and preserves these
circuits, so nonisomorphic trees cannot be equivalent.

The endpoint is generic/general.  It does not classify special parameter
subvarieties, nonlinear or time-dependent changes, or arbitrary birational
state transformations.  The exact codimension-one boundary
(2a_q-d_{p,q}-d_{r,q}=0), where an extra higher-support Darboux polynomial
may appear, is explicitly recorded rather than hidden.

## Exact finite certificate

The finite certificate independently reproduces the published (n<9)
baseline and exhausts (n=9).  The standard-library verifier enumerates all
Prüfer words, canonically reconstructs every unlabeled tree, and recomputes
both the triangle-reconstruction code and a full circuit-incidence signature.

- Counts for (n=2,\ldots,9): `1,1,2,3,6,11,23,47`.
- Certificate SHA-256:
  `5be053e1f8e676769ad33237055bed21c76f9825fd373f7832fb2d21dc414fe6`.
- Verifier SHA-256:
  `6a4b61fc2fe3bcbd0caec0e3cdb8049eecd36034349ffc798f223019cfb431b4`.
- Six corrupted certificates are rejected fail closed.
- No floating-point computation is used in the decisive verification.

## Independent audits and novelty

The proof passed serial builder, breaker, certifier, and definition-first
referee audits.  The verifier imports neither the discovery generator nor
NetworkX and reconstructs the finite universe from serialized edge lists and
all Prüfer words.  Gate 1 checked the version of record, DOI, latest arXiv
revision, subsequent citations, and public-code availability.  A second
theorem-specific search found no public antecedent for the general theorem or
the cone-incidence/three-circuit proof; this is a bounded novelty finding, not
an absolute priority claim.

All twelve frozen citation claims passed.  The three official DOI-exported
BibTeX records have no missing or unused keys.  A clean LaTeX build produced a
six-page PDF with no warnings, and every page passed visual inspection.

## Reproduction

```bash
python3 code/verifier/verify_tree_certificate.py certificates/trees_n2_n9.json
python3 tests/test_verifier_rejects.py
/opt/anaconda3/bin/python3.13 code/audit/check_three_vertex_boundary.py
cd paper && latexmk -C main.tex && latexmk -pdf -interaction=nonstopmode -halt-on-error main.tex && cd ..
python3 /Users/mac/.codex/skills/prove-or-disprove-math/scripts/verify_manifest.py release/frozen release/manifest.json
```

The paper, exact certificate, independent verifier, corruption tests, source
ZIP, citation audit, novelty ledgers, and release manifest accompany this
status.  The paper is authored only by Zijian Zeng with the required UCSI
University affiliation and both required email addresses.

No Lean, Coq, Isabelle, or other proof assistant was used.  Consequently no
machine-formalized theorem endpoint is claimed.
