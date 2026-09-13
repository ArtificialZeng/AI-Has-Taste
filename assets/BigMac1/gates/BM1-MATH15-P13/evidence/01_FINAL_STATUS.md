# Final scientific status

**Terminal status: partial theorem.**

## Exact result

Let $A$ be the ordered two-vertex edge.  In the class $\mathcal S_<$ of
finite linearly ordered split graphs under induced order-preserving embeddings,

\[
t_{\mathcal S_<}(A)=3.
\]

The upper bound encodes a chosen split partition by a unary $Q/I$ mark and a
directed cross-edge relation.  This finite ordered relational class has ordered
free amalgamation, so its three ordered edge types $QQ,QI,IQ$ can be
homogenized successively.  The proof then explicitly forgets the mark and
checks that the resulting copy is still induced and order preserving.  The
matching lower bound is forced by the ordered path
$i_1<q_1<q_2<i_2$, whose only split partition is
$Q=\{q_1,q_2\}$, $I=\{i_1,i_2\}$.

## Original chordal problem

The exact degree for all finite linearly ordered chordal graphs remains open in
the recorded literature search through 2026-08-28.  The certified full-class
result is only $t(A)\ge 2$.  Exact diagrams show both that ordinary free
amalgamation creates an induced four-cycle and that chordal graphs with a named
perfect elimination ordering fail amalgamation.  Therefore neither shortcut
supplies the missing upper bound.

## Submission gates and deliverables

The proof, forgetful expansion, quantifiers, external Ramsey theorem,
bibliography, bounded novelty claim, and exact witness were audited.  The PDF
was clean-built, checked for forbidden content and embedded fonts, and inspected
page by page.  The ZIP was extracted into an empty directory, where the source
build, citation audit, manifest, and exact verifier all passed.

- Batch-stable manuscript PDF:
  `output/pdf/ordered_split_edge_ramsey_degree.pdf`
- Batch-stable LaTeX and supplementary package:
  `output/source/ordered_split_edge_ramsey_degree_source.zip`
- Independent referee report: `proof/referee_notes.md`
- Submission audit: `audit/SUBMISSION_AUDIT.md`

Recommended continuation: construct an edge-specific partite argument that
preserves induced chordality without relying on amalgamation of named PEOs.
