# lit-260318638-p01 — exact two-hole value in the `{4,5}` tessellation

## Immutable primary-source record

- Summer Eldridge, Adithya Prabha, Aiden Roger, Cooper Roger, Erika Roldan,
  and Rosemberg Toala-Enriquez, *Holey Hyperbolic Polyforms*,
  arXiv:2603.18638v1 (19 March 2026).
- Official abstract: <https://arxiv.org/abs/2603.18638>
- Official HTML: <https://arxiv.org/html/2603.18638>
- Local official PDF: `primary-20260910-materials/2603.18638.pdf`, SHA-256
  `a58c8695b3be38b3e4aa8cb492f509d3d6cb565170fa38dd3bf87721d7d910df`.
- Closest structural source: Gabriel Malen, Erika Roldan, and Rosemberg
  Toala-Enriquez, *Extremal {p,q}-Animals*, arXiv:2109.05331v1.
- Local official PDF: `primary-20260910-materials/2109.05331.pdf`, SHA-256
  `5db9c997ea993a03d535ce7e58548cf45992b2e179f8d1b72a05e5214911adfe`.
- Retrieved and searched on 10 September 2026.  The first paper still had
  only version 1.  Searches of arXiv, Crossref, OpenAlex citation records,
  the relevant author publication list, and the authors' official repository
  found no later primary source resolving this exact cell.  This bounded
  search is not a claim of priority or proof that no other resolution exists.

This item was ingested directly from primary literature while the authorized
Chrome intake surface was unavailable.  It is not a ChatGPT-generated batch
item and does not consume the reserved `# Win-第87批` number.

## Definitions

In the regular hyperbolic `{4,5}` tessellation, a polyform is a finite
collection of square tiles whose interior is connected; connectivity is by
shared tile edges, although nonconsecutive tiles may additionally meet only
at a vertex.  A hole is a bounded connected component of the complement.
For positive `h`, let

`g_{4,5}(h) = min{|A| : A is a {4,5}-polyform with exactly h holes}`.

These are the conventions of Definition 1.1 and the surrounding text of
arXiv:2603.18638v1.  Any computational certificate must use the actual
incidence structure of the infinite `{4,5}` tessellation rather than a
generic square grid or an arbitrary planar graph.

## Frozen assertion

Prove or disprove that there exists a `{4,5}`-polyform with exactly two holes
and exactly 16 tiles.  Equivalently, decide which of

`g_{4,5}(2)=16`  and  `g_{4,5}(2)=17`

holds.

An existence proof must give an exact finite tile/incidence certificate and
independently verify edge connectivity and exactly two bounded complementary
components.  A nonexistence proof must cover every 16-tile `{4,5}`-polyform,
with a proved-complete structural classification or exhaustive enumeration
and an independently replayable certificate; failure of a heuristic search
does not suffice.

## Nearest result and exact one-unit gap

In arXiv:2603.18638v1, Theorem 1.2 and Table 1 give an explicit 17-tile
two-hole `{4,5}` polyform, while the unshaded-table statement says unresolved
cells remain open.  Table 2 evaluates the paper's obstruction at that entry:

`M(15,2)=1.5`, `M(16,2)=2.0`, and `M(17,2)=2.0`.

Corollary 2.2 therefore excludes 15 tiles but not 16, proving the currently
documented window `16 <= g_{4,5}(2) <= 17`.  The proposed contribution is
exactly the missing endpoint decision, not a general formula for `g_{p,q}`.

The authors' official code is
<https://github.com/CRoger20/megl-polyforms/>.  At screening time its `main`
HEAD was `18f605873ff8963a541cf4ba18688295526926f3`, with no tag or release.
Its default recursion expands only from the most recently added tile, and a
source TODO explicitly warns that shapes requiring a turn-around can be
missed.  It may supply representations and tests, but it cannot certify the
16-tile nonexistence branch without a new completeness argument.

## Cheapest decisive attack

First derive, rather than assume, the equality consequences for a hypothetical
16-tile two-hole polyform.  The counting chain suggests that equality should
force its edge-dual graph to be a tree, both holes to be single tiles, and the
filled 18-tile animal to have minimum perimeter `P_min(18)=26`.  If all three
implications are valid, classify the 18-tile extremal `{4,5}` animals and test
whether deleting two appropriate interior tiles leaves an edge-connected
16-tile set with exactly two single-tile holes.

Theorem 6.4 of arXiv:2109.05331 is the first cheap structural test: verify its
definitions, indices, uniqueness scope, and whether its claimed extremal
family actually specializes to every 18-tile minimum-perimeter `{4,5}`
animal.  The fact that the 2026 authors cite this theory yet leave the cell
open is a warning that a definition, index, or local-geometry exception may
invalidate the apparent shortcut.  If uniqueness cannot be proved, use
canonical augmentation under the `{4,5}` tessellation symmetry group and
publish the complete representative list plus adjacency, perimeter, and hole
certificates.

