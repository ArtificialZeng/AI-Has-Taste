# Current primary-source comparison for the double-star candidate

Job: primary-20260913-subtree-annulus-research-bac30ce160a8.
Retrieval and inspection: 2026-09-13 +08, 2026-09-12 UTC.
No project-local `literature/*handoff*.md` existed when enumerated.

## Decisive original and nearest prior result

Brown and Mol, *On the roots of the subtree polynomial*,
[arXiv:1810.08655v1](https://arxiv.org/pdf/1810.08655v1): checked the primary
PDF text on physical pp.1-3 and 14, with targeted text screening elsewhere.
Their subtree convention is precisely connected induced vertex subsets.
The star and path formulas are already on p.1. Conjecture 4.2 on p.14 is the
full shifted annulus and the reported check is through order 18. The
unchanged primary PDF is `external/brown-mol-1810.08655v1.pdf`; its SHA256
matches the immutable intake. This is prior finite evidence, not this job's
contribution.

Jin, Ma and Wang, *Proof of a Brown-Mol conjecture on subtree roots*,
[arXiv:2608.07898v2](https://arxiv.org/html/2608.07898v2): the
[live version record](https://arxiv.org/abs/2608.07898) still identifies v2,
14 August 2026. Read Theorem 1.3, the relevant Section 3 equality argument,
and Section 5. The theorem gives the origin-centred upper bound and its
equality classification. Conjecture 5.1 still states the stronger shifted
annulus. Their inequalities use a fixed modulus |z|>=2, whereas the proposed
proof controls both |z| and |1+z| on a circle centred at -1/2. The radial
disk itself does not imply the shifted annulus. The proposed result neither
reproves their universal radial theorem nor claims their equality result as
new. Direct current primary-text renderings are saved in
`external/jmw-v2-front-research-live-web.txt` and
`external/jmw-v2-research-live-web.txt`. The latter contains the full displayed
Section 3-5 text, including the exact Conjecture 5.1. The intake's original
v1 HTML was also copied unchanged to
`external/subtree-roots-2608.07898v1.html`, rather than substituted by a
summary. These sources are not proof dependencies of the family theorem.

## Additional substantive leads checked

Stephan Wagner and Ruoyu Wang, *The distribution of subtrees in dense graphs
and the roots of the subtree polynomial*,
[arXiv:2605.03583v1](https://arxiv.org/html/2605.03583v1), May 2026.
Read definitions and Theorems 1-3, including the comparison to the tree
annulus. Their graph-subtree convention counts tree subgraphs, not necessarily
induced; on a tree this agrees with ours. The root theorem assumes a fixed
alpha>0 and minimum degree at least alpha*n, for sufficiently large n.
Double stars have minimum degree one, so no unbounded double-star family
satisfies that hypothesis. This theorem supplies no all-parameter result
for the proposed family. Their introduction also states the shifted annulus
as a conjecture. The displayed primary text including all main statements is
`external/wagner-wang-v1-research-live-web.txt`.

Brown and Mol, *On the roots of the node reliability polynomial*,
[arXiv:1607.08496v1](https://arxiv.org/pdf/1607.08496v1), Networks 68(3)
(2016), 238-246. Read definitions and the connected-set transformation on
physical pp.3-4, main root statements on pp.5-9, and pp.15-21 on complex
closure and concluding problems. The transformation is

    NRel(T;p)=(1-p)^n Phi_T(p/(1-p)).

For z!=-1 and p=z/(1+z), direct algebra gives
Re p=(|z|^2+Re z)/|1+z|^2. Thus the inner-disk problem can be screened in
the language of node-reliability roots in the right half-plane. This is an
equivalent-language observation, not a separate new contribution. No
double-star annulus or equivalent half-plane family theorem was found in the
inspected portions; the main complex-closure construction uses connected
graphs with cycles. Text finds for `star` and `half` returned no match.
Displayed primary text and the find results are preserved in
`external/node-reliability-v1-research-live-web.txt`. Intervening unrendered
pages are not claimed fully inspected.

An additional primary lead, Hanshu Yu, *Properties of node reliability
polynomials*, [TU Delft thesis](https://repository.tudelft.nl/file/File_35464569-654a-4b1a-be98-fe8dce043f11),
was checked at its abstract, contents, Section 2.6 star/path formulas and
root keyword results. Its announced contribution concerns polynomial
intersections and computation; the inspected formulas are elementary prior
formulas, and no matching complex-root family result appeared. This was a
bounded section/keyword screen, not a full thesis audit. The front matter
has inconsistent year labels (preface/project duration indicate February
2022); no novelty conclusion depends on choosing a year. Actual rendered
excerpts are in `external/yu-node-reliability-front-live-web.txt` and
`external/yu-node-reliability-research-live-web.txt`.

## Search scope, contribution and limits

Live query strings included: `"subtree roots" "double stars"`;
`"subtree polynomial" annulus diameter`; `"Brown" "Mol" "annulus" subtree`;
`"subtree polynomial" "double" roots`; `"node reliability" "double star"`;
`"node reliability" roots "trees" half-plane`;
`"subtree" "annulus" "double-star"`;
`"subtree polynomial" "diameter three"`; `"subtree polynomial" "bistar"`;
`"connected set polynomial" "double"`;
`"residual node connectedness" "roots" tree`.
Raw result leads are saved separately; irrelevant search hits and secondary
summaries are not used as mathematical sources.

No equivalent all-double-star result was found in the inspected primary
sources on this date. This limited negative search is not a proof of
priority. It does not exhaust unpublished work, theses, non-English sources,
or a full citation-network search. In particular, Mol's 2016 thesis was a
search lead but was not read in full during this job. The previous registry
screen was not repeated; this is the same admitted family, not a new target.

The proposed delta is a complete analytic verification of both shifted
boundaries for all two-parameter double stars, with strictness for every
nonzero root. Combined with the known star formula, it settles the entire
diameter-at-most-three class. The proof's substantive step is the convex
endpoint comparison on the translated circle, not another prefix of the
known tree census. This is a modest family theorem with a reusable scalar
estimate, submitted for a referee's judgment of correctness and value;
the original arbitrary-tree conjecture remains unresolved.

Shell downloads were denied by the sandbox. The web tool successfully
retrieved the named primary text; its outputs were saved programmatically,
without proposer transcription. Such files are expressly labelled rendered
primary excerpts, not original HTML/PDF bytes. The already local original
Brown-Mol PDF and JMW v1 HTML were copied byte-for-byte into `external/`.
No access failure has been turned into a novelty or mathematical claim.
