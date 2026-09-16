# Primary-source verification and bounded novelty comparison

Job: primary-20260913-nfa-asymmetry-research-71ec4a8ef3d7.
Inspected 2026-09-13 Asia/Shanghai, during the first bounded research pass.

## Decisive classical dependency: the source gap is resolved precisely

The only matching handoff file was `literature/outer-intake-handoff.md`. It and
its referenced `source-update-schwarz.md` were read as leads. The supplied
1974 PDF was then independently text-read; printed pp.161 and 167 were rendered
and viewed. Its SHA256 matches the handoff, and its complete bytes, including
the cover/terms, have been copied to `evidence/external/schwarz-1974-sums.pdf`.

Schwarz, *Sums of Powers of Binary Relations*, Matematicky casopis 24(2)
(1974), 161-171, Russian:
[primary bibliographic record](https://www.dml.cz/handle/10338.dmlcz/126603?show=full).
Printed p.161 defines the index k, period d, and periodic group
G(rho)={rho^k,...,rho^(k+d-1)}. Printed p.167, proof of Theorem 3, Case 1,
explicitly states that rho^(n^2-2n+2) belongs to G(rho) for every binary
relation on n points. It cites his 1970 paper, printed p.653, for this fact.
Printed p.163 emphasizes applicability to reducible relations. Thus the
required all-relations upper index bound, with its precise constant, is
verified in an authoritative account by the theorem's author. It is not
merely the primitive-matrix exponent bound.

The 1974 paper is NOT the original proof of this index bound. The correct
earlier locator is Schwarz, *On the semigroup of binary relations on a finite
set*, Czechoslovak Mathematical Journal 20(4) (1970), 632-679,
[primary record and DOI](https://dml.cz/handle/10338.dmlcz/100989).
The live record and PDF cover were read. Attempts to render printed pp.653-654
through the web tool failed with cache misses; a local Python HTTPS download
was denied by the network sandbox. No full 1970 PDF was saved or original proof
read. This operational limit is disclosed; the candidate instead relies on
the exact authoritative 1974 statement, as allowed by the assigned test.

Zajac and Jokay, *Computing Indexes and Periods of All Boolean Matrices up to
Dimension n=8*, Computing and Informatics 31 (2012), 1329-1344:
[publisher PDF](https://www.cai.sk/ojs/index.php/cai/article/download/1310/485/3294).
The supplied full paper was read at its preliminaries and reference list;
printed p.1331 was rendered and viewed. Theorems 1-2 report the universal
index (n-1)^2+1 and the partition-lcm formula for the universal period. The
printed Definition 1 actually contains an error; this is not just an OCR
problem. We use neither that literal definition nor a repaired formula
inferred from it. The saved full PDF is
`evidence/external/boolean-matrix-index-cai.pdf`.

The proof dossier removes the need to import the period theorem: insertion
of cycles gives R^t<=R^(t+L_n) for t>=n; on the eventual periodic part a finite
chain of these inclusions returns to its start, forcing equality. Thus the
only non-elementary dependency is the verified index bound. No novelty is
claimed for the index bound or for the universal Boolean-power identity.

## Closest word-separation sources

Nicol, *Further Remarks on Separating Words*, arXiv:2608.30928v1:
[live primary text](https://arxiv.org/html/2608.30928v1) and
[version record](https://arxiv.org/abs/2608.30928).
Section 4.1 and the full proof of Theorem 6 were reread live, along with the
NFA convention, definition of A(q), bounds, and open-growth sentence. The
local PDF was text-read and printed p.3, including Figure 1, was rendered and
viewed. Its zero graph and sole one-loop agree with the proof dossier.
The live record displays v1, submitted 31 August 2026. Original PDF and HTML
copies with matching intake hashes are in `evidence/external/`.

**Exact comparison.** Nicol constructs one-marker words with
nsep(u,v)>s^2 and nsep(v,u)<=s+1 and obtains A(q)>=(q-1)^2+1.
Our lower argument adapts this construction, with T=2^(s^2+1), to show
nsep(u,v)=s^2+2. The extra step uses a simple initial path that visits every
state; it can insert a zero-cycle from the long suffix. The main proposed
contribution is the converse upper bound for EVERY ordered equal-length
one-marker pair having reverse cost at most q, giving the exact restricted
extremal formula. Nicol neither states that restricted upper bound nor the
resulting exact formula in the inspected source. We do not claim to resolve
the unrestricted growth question or rediscover the unbounded ratio theorem.

Demaine, Eisenstat, Shallit and Wilson, *Remarks on Separating Words*:
[author publication page](https://erikdemaine.org/papers/WordSep_DFCS2011/).
The supplied author PDF, copied to
`evidence/external/demaine-etal-wordsep-author.pdf`, was read at Sections 5-6,
including the asymmetry example, unary-normal-form argument, consecutive-cycle
construction, and reversal invariance. The old unbounded asymmetry question
has been addressed by Nicol. Their Theorem 4 supplies pairs indistinguishable
by small NFAs using long unary blocks; it does not optimize one directional
cost in terms of the opposite cost and supplies no equivalent exact one-marker
extremal formula. Their Theorem 5 permits reversal without a state increase.
Our explicit short-block machines have a sole final state, so our use of
reversal is additionally verified directly.

## Current search and its limits

Queries in this pass included:

- `"Sums of Powers of Binary Relations" Schwarz index`
- `"Boolean matrices" "index" "(n-1)" Schwarz`
- `"one-marker" "separating" words automata`
- `"nsep" "asymmetry" Nicol`
- `"nondeterministic" "separating words" "single"`
- `"separating words" "quadratic" "order"`
- `"separating words" "marker"`
- `"nsep" "A(q)" -pulse -electric -electroporation`
- `"nondeterministic separation" "asymmetry" -pulse`
- `"separating words" "one 1"`
- `"separating words" "0^a"`
- `"Nicol" "separation" automata one-marker`
- `"separating words" "one occurrence"`
- `"nondeterministic" "0*10*" separation`
- `"nsep" "quadratic" -pulse -electroporation -electric`
- `"directional" "word separation"`

Most extraneous hits concerned electric pulses, linguistics, or unrelated
automata models and were discarded. Mirrors and snippets served only as leads.
A current primary abstract for Chen Xu,
[arXiv:2609.08191](https://arxiv.org/abs/2609.08191), concerns deterministic
separation as a function of word length, a different parameter and model.
Kjos-Hanssen and Petit,
[arXiv:2608.22271v1](https://arxiv.org/html/2608.22271v1), concerns exact versus
unique automatic complexity, requiring rejection of all other equal-length
words; that differs from pairwise directional separation. No use is made of
their census or their theorem as evidence for the present candidate.

No equivalent exact one-marker formula was found in these inspected primary
sources and bounded searches on this date. This is a limited novelty screen,
not a proof of priority or an exhaustive search of all papers and theses.
An independent referee should judge whether the sharp subclass result is
sufficiently substantive; the additive one-state corollary alone is not the
proposed contribution. Original A(q) open status is supported only within
this checked source coverage.

The historical registry/Excel comparison was not repeated in this research
pass, and no fresh conversation-side comparison is claimed. Its earlier
documented scope remains in the triage evidence. No acceptance, external
submission, new manuscript, or research PDF has been created.
