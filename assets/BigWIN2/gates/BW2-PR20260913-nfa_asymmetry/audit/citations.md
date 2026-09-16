# Verification Report

**Mode:** Two-pass, non-interactive primary-source verification, with accepted frozen proof and fresh exact diagnostics for internal mathematical claims.
**Document:** manuscript/main.tex and every source listed in publication.json.
**Generated (UTC):** 2026-09-12T19:47:19.837716+00:00
**Job:** primary-20260913-nfa-asymmetry-release-a0b9dbc9657e
**Overall status:** PASS for this exact final snapshot.

| Metric | Count |
| --- | ---: |
| Frozen claims | 36 |
| Verified claims | 36 |
| Verified cited publications | 7 |
| Selected active-library papers | 1 |
| Natural non-library publications | 6 |
| Numerical errors / unsupported claims / misquotations | 0 |
| Missing or undefined citations | 0 |

The first pass read the entire article and froze the 36 claims in
`audit/citation-claim-ledger.json` before source-support verification.
The second pass assessed those identifiers in order, using exact primary
passages and the unchanged accepted proof. The complete findings, source
locations, scope checks and confidence classifications are in
`audit/citation-verification.json`. Statements inside a proof are grouped
under the proposition or construction they establish; definitions alone
are not treated as external factual claims. No interactive confirmation,
agent delegation, other Codex process or background worker was used,
as expressly required by this job.

The citation-key union exactly matches all seven ordinary body-flow keys.
There are no hidden, commented, nocite-only, inert-macro or unused citations.
The active hook-compatible selection parser was actually run. It accepts
the literal smallest citation-bearing sentence at main.tex:342–346,
including its direct cite command with a source locator. The selected row,
DOI identity, canonical references.bib, registry/workbook checksums and
runner-issued attempt/launch bindings match. verified_at uses the actual
UTC date 2026-09-12, not the local date 2026-09-13.

## Publication-by-publication audit and coverage

Seven references are retained because each has a specific nearby use. Six
are non-library primary or method sources; the sole library selection is
a relevant verification-method comparison. The bibliography therefore
covers origin, closest results, imported theorem and nontrivial methods,
and is neither library-only nor padded to a fixed count.

| Key | Primary title / publication | Exact support and reason for retention |
| --- | --- | --- |
| goralcik1986 | [On discerning words by automata](https://link.springer.com/chapter/10.1007/3-540-16761-7_61); 1986; ICALP, LNCS 226, 116–122 | Printed p.116, opening definitions; author upload identified at lines 43–47. Historical deterministic formulation. |
| demaine2011 | [Remarks on Separating Words](https://erikdemaine.org/papers/WordSep_DFCS2011/); 2011; DCFS, LNCS 6808, 147–157 | Section 6, physical pp.8–10: opening definition, Open Problem 2, Theorems 3–5. Directional origin, closest earlier unary constructions and reversal principle. |
| nicol2026 | [Further Remarks on Separating Words](https://arxiv.org/abs/2608.30928); 2026; arXiv:2608.30928v1, submitted 31 August | Section 4 opening; Section 4.1; Theorem 6 and Figure 1; physical pp.3–4. Frozen original A(q), closest quadratic construction, model and prior bounds. |
| rabin1959 | [Finite Automata and Their Decision Problems](https://cris.huji.ac.il/en/publications/finite-automata-and-their-decision-problems/); 1959; IBM Journal of Research and Development 3(2), 114–125 | Section 5, Definition 11 and Theorem 11, printed p.121 / physical p.8. Primary subset-construction method underlying the 2^q bound. |
| schwarz1974 | [Sums of Powers of Binary Relations](https://www.dml.cz/handle/10338.dmlcz/126603?show=full); 1974; Matematický časopis 24(2), 161–171 | Printed pp.161 and 167; proof of Theorem 3, Case 1. Sole imported non-elementary all-relations index theorem. |
| zajac2012 | [Computing Indexes and Periods of All Boolean Matrices Up to Dimension n=8](https://www.cai.sk/ojs/index.php/cai/article/view/1310); 2012; Computing and Informatics 31(6), 1329–1344 | Abstract and Section 1; Theorem 1, printed p.1331. Corroborating index theorem and closest Boolean-matrix enumeration method. |
| zeng2026finite | [Exact Finite Certificates for the Four-Dimensional Ternary Borsuk Problem and Five-Dimensional Ternary Kissing Codes](https://www.preprints.org/manuscript/202608.1658/v1); 2026; Preprints.org v1, posted 24 August; preprint | Section 3 before Theorem 1 proof; Section 4 Lemma 3 and Proposition 1; Section 6. Concrete exact verification architecture: local integer predicates, rebuilt coverage and separate implementations. |

All seven BibTeX identities, authors, titles, years, venues and version/DOI/URL fields were verified. `manuscript/references.bib` is byte-identical to the writer snapshot. No citation key changed, no bibliography entry was removed, and no replacement metadata was fabricated.

- **goralcik1986:** Springer 2005 online date is distinguished from the 1986 proceedings year.
- **demaine2011:** Author BibTeX and DOI agree with the retained bibliographic identity; the author PDF is a 12-page version of the proceedings paper.
- **nicol2026:** The abstract record says John Nicol; the PDF author line spells John W. Nicol. Version and submission date are retained explicitly; PDF footer date is not used as the submission date.
- **rabin1959:** The author institutional record confirms DOI 10.1147/rd.32.0114. Chalmers scan and direct local download failed, but the Miami-hosted original scan was accessible and read through the web tool.
- **schwarz1974:** English title is the DML translation; original Russian text and images were checked. The 1970 proof is not claimed as inspected.
- **zajac2012:** The primary PDF and issue say 2012; OJS displays a 24 January 2013 posting. Retain the issue year. The malformed period definition is not used.
- **zeng2026finite:** The publisher full text confirms all authors, version and preprint status; its subject listing explicitly associates the work with DOI 10.20944/preprints202608.1658.v1. Only methodology is cited.

The official/author records and original text captures are retained in
`audit/source-open-0.json`, `audit/source-open-1.json`,
`audit/source-locators.json`, `audit/primary-zeng-nicol-records.json`,
`audit/zeng-doi-primary.json` and `audit/source-searches.json`.
The four frozen source PDFs were freshly converted to text under
`audit/primary-text/`. The original Schwarz pages 161 and 167 and Nicol's
Figure 1 page were also visually inspected. The original 1970 Schwarz
proof is not claimed as read, and no theorem depending on its unseen
proof details was added. The required all-relations statement is explicit
in the cited 1974 account.

Every applicable academic-search template was run. Supplemental full-title
and arXiv queries and a bounded exact-target search are saved in
`audit/source-searches-supplemental.json`. Discovery snippets and third-party
bibliographies were not used as mathematical support. The retained comparison
with Demaine and Nicol is limited to the inspected sources; no exhaustive
priority guarantee is made. No bibliography-revision files or fast-completion
handoffs were present. The sole intake handoff and its subsequent source
update were read, and their applicable local hash predicates matched.
No literature/crossref-*.json or crossref-*.md captures existed when enumerated.
Live DOI/API or WSL transport failures are recorded only as access limits;
alternative authoritative text and records support all retained citations.

## Claim-by-claim second pass

| ID | Source / precise locator | Outcome and support |
| --- | --- | --- |
| C01 | evidence/one-marker-proof.md: statement, upper bound and attainment; claim.json; manuscript Sections 2-4 | Verified (exact). The abstract exactly matches the accepted all-length one-marker theorem, its classical dependency and the spanning-prefix addition; it leaves unrestricted growth unresolved. |
| C02 | Goralcik-Koubek, printed p.116 opening definitions; audit/source-locators.json origins-3, author-uploaded text lines 43-72; Springer primary record in audit/source-open-0.json | Verified (paraphrase). The authors define discernibility by different terminal states of a deterministic action. Choosing one of those states accepting gives the manuscript separation formulation. Springer identifies ICALP 1986, LNCS 226, pp.116-122. |
| C03 | Demaine et al., Section 6, physical pp.8-9, opening paragraph, example and Open Problem 2; audit/primary-text/demaine2011.txt:356-377; Nicol Section 4.1 | Verified (paraphrase). The source explicitly defines nsep, gives the 000100/010000 asymmetric example, and asks whether the difference is unbounded. Nicol identifies the same antecedent. The shared line 52 also contains the next citation, verified separately as C04. |
| C04 | Nicol v1, Theorem 6, physical p.3; audit/primary-text/nicol2026.txt; evidence/source-views/nicol-p3.png | Verified (exact). The exact inequalities are >s^2 and <=s+1 for every integer s>=2, with equal-length binary words. They are not claimed as a new result. |
| C05 | Nicol v1, Section 4 opening, physical p.3; evidence/source-views/nicol-p3.png | Verified (exact). The primary paragraph explicitly specifies one initial state, arbitrary accepting set, partial relation and no epsilon transitions, and ordered acceptance/rejection. |
| C06 | Nicol v1, Section 4.1, bottom of physical p.3 and top of p.4; audit/primary-text/nicol2026.txt | Verified (exact). The definition and bounds match, including q>=3 and direction of nsep. The frozen original source and its PDF/HTML hashes match. |
| C07 | Rabin-Scott 1959, Section 5, Definition 11 and Theorem 11, printed p.121/physical p.8; University of Miami original scan, lines 654-692 in audit/source-locators.json; institutional metadata in audit/source-searches.json | Verified (paraphrase). Definition 11 uses all subsets, transitions formed by union, and accepting subsets intersecting F. Theorem 11 proves equality of recognized languages. The manuscript cardinality and complementation consequence are explicit elementary deductions from this construction. |
| C08 | claim.json; evidence/one-marker-proof.md: opening scope; manuscript theorem and limitations | Verified (exact). The paper does not settle the unrestricted growth question. This is a statement about this note, not a claimed exhaustive proof that nobody has solved it. |
| C09 | claim.json statement; evidence/one-marker-proof.md: all-size theorem; manuscript Sections 2-4 | Verified (exact). Every quantified hypothesis, direction and state convention matches the accepted theorem, including q>=3, empty blocks, all lengths and attainment. |
| C10 | Demaine et al., Section 6 Theorems 3-4, physical pp.9-10; audit/primary-text/demaine2011.txt:385-433; Nicol Theorem 6; accepted proof | Verified (paraphrase). Theorems 3-4 concern DFA/NFA comparison and length-based lower bounds with unary blocks. The new note instead proves a bound in terms of the opposite NFA cost. The identified antecedents and one-state strengthening are accurately delimited. |
| C11 | Demaine et al., inspected Section 6 and theorem list; Nicol v1 Sections 4.1-4.2, Theorem 6; audit/math.md source comparison | Verified (paraphrase). Neither inspected treatment states the one-marker maximum. The manuscript explicitly limits the comparison to these sources and makes no global priority assertion. |
| C12 | claim.json statement; evidence/one-marker-proof.md: upper bound and attainment; manuscript Theorem 1 | Verified (exact). The corollary follows by inclusion of the one-marker domain into the unrestricted domain and the proved uniform upper bound. No unrestricted upper bound is strengthened. |
| C13 | Schwarz 1974, printed pp.161 and 167, proof of Theorem 3 Case 1; evidence/source-views/schwarz-1974-p161.png and schwarz-1974-p167.png; audit/primary-text/schwarz1974.txt | Verified (paraphrase). Both original Russian pages were visually inspected. The sentence states that the indicated power belongs to the periodic group for every binary relation, independently of the surrounding case assumption. The account refers to the earlier 1970 result; that earlier proof is not represented as read. |
| C14 | Zajac-Jokay, Theorem 1, printed p.1331/physical p.3; audit/primary-text/zajac2012.txt:110-122 | Verified (exact). The universal index is exactly (n-1)^2+1. The manuscript uses this as corroboration, not the source of a new theorem or an assumed period formula. |
| C15 | evidence/one-marker-proof.md: classical dependency and elementary period argument; manuscript Lemma 4 proof | Verified (exact). Cycle insertion gives R^t subseteq R^(t+L_n) for t>=n. Since H_n>=n, iteration through a multiple of an eventual period closes the chain and gives equality. n>1 is maintained. |
| C16 | evidence/one-marker-proof.md: consequence of identity (1); manuscript lines 165-167 | Verified (exact). Repeated applications of the period identity handle positive and negative exponent differences; unreachable isolated padding leaves the recognized language unchanged. |
| C17 | evidence/one-marker-proof.md: upper bound Case 1; manuscript lines 179-189 | Verified (exact). A modulus not dividing the nonzero displacement exists; the sole marker edge selects its residue and the separate final zero-loop state accepts the suffix. r+1<=q+1<=H+1 holds for q>=3. |
| C18 | evidence/one-marker-proof.md: upper bound Case 2; manuscript lines 191-204 | Verified (exact). The chain constructions kill the rejected word at the first differing symbol and use k+2 states. This also holds at k=0. |
| C19 | Demaine et al., Theorem 5 and proof, physical p.10; audit/primary-text/demaine2011.txt:435-444; manuscript explicit machines | Verified (paraphrase). The primary proof reverses edges and chooses one accepting state of the desired path as initial. Here the constructed machines already have one final state, so the path-reversal use satisfies the single-initial convention directly. |
| C20 | evidence/one-marker-proof.md: upper bound Case 3; manuscript lines 215-231 | Verified (exact). The zero relations agree on each block, so both whole words induce identical binary relations. A reverse separator is therefore impossible in the remaining case. The cases exhaust the admitted pairs. |
| C21 | Nicol v1 Theorem 6 proof, physical p.3; accepted proof formula (2); manuscript lines 235-247 | Verified (exact). The primary source uses T=2^M. The note explicitly changes T to 2^(M+1) while retaining the word template and adjusts the prefix argument accordingly. The common length is M+T+P+1. |
| C22 | evidence/one-marker-proof.md: lower bound and attainment, accepting-path argument; manuscript Lemma 5 | Verified (exact). If the M-edge prefix is simple, it visits all states of an at-most-(M+1)-state machine; the suffix cycle can therefore be inserted at a prefix vertex. Otherwise a prefix cycle works. Its length divides P. The typography changes preserve every path endpoint and label. |
| C23 | evidence/one-marker-proof.md: subset orbit and equation (3); manuscript Lemma 5 | Verified (exact). At most 2^m<=T reachable subsets force a cycle by T; its period divides P, giving S_T=S_(T+P). The M+2-state chain supplies the converse. |
| C24 | Nicol v1 Figure 1, physical p.3, visually inspected in evidence/source-views/nicol-p3.png; manuscript Lemma 6 | Verified (exact). The zero edges go along 0,...,s with returns from s to 0 and 1; the sole marker loop is at the initial/final state 0. The direction of each arc matches the displayed manuscript list. |
| C25 | Nicol v1 Theorem 6 proof after Figure 1; accepted proof equation (4); manuscript lines 301-318 | Verified (exact). The return semigroup has beta>=1 and alpha>=0. Residue representatives 1,...,s yield maximal missing positive length s^2, while the empty return is explicitly separated. |
| C26 | evidence/one-marker-proof.md: final attainment paragraphs; manuscript lines 319-330 | Verified (exact). The easy graph rejects the prefix M and accepts both blocks M+P and T, all strictly larger than M. Combined with the hard direction this proves attainment without the Schwarz theorem. |
| C27 | Zajac-Jokay 2012, abstract and Section 1, printed pp.1329-1330; audit/primary-text/zajac2012.txt; supplementary verification.json | Verified (paraphrase). The prior paper computes Boolean-matrix index and period statistics through n=8; this note enumerates unary relations through n=4, and adds the stated mixed-symbol inclusion diagnostics. It does not claim to exceed that enumeration. |
| C28 | Zeng et al. v1, Section 3 final paragraph before Theorem 1 proof; Section 4 Lemma 3 and Proposition 1 certificate proof; Section 6; audit/primary-zeng-nicol-records.json and audit/source-locators.json | Verified (paraphrase). The original text explicitly reconstructs orbit coverage, uses integer adjacency predicates, and describes primary bitsets and a separate list implementation. The manuscript comparison is methodological and imports no geometric theorem. |
| C29 | evidence/research-checks.py: matrix_mul/matrix_power; manuscript/supplement/verify.py: relation/product/orbit_table/lookup | Verified (exact). The development relation implementation uses bit masks and binary powering; the separate supplement uses frozen destination sets and orbit indexing. These representations were directly inspected. |
| C30 | audit/supplement-replay/verification.json; audit/release-supplement-check.json; manuscript/supplement/verify.py: finite_relations | Verified (exact). Fresh byte-identical verifier replay has zero failed assertions and reproduces all semantic result fields. All B are enumerated for n=1..4, every C only for n=1..3. Inclusion covers all initial/final choices entrywise. |
| C31 | audit/supplement-replay/verification.json: relation_checks; rendered manuscript page 5 Table 1 | Verified (exact). Every table cell matches: unary 2,16,512,65536; binary pairs 4,256,262144; n=4 not enumerated. These are respectively 2^(n*n) and its square. |
| C32 | audit/supplement-replay/verification.json: construction_checks; supplementary README test families | Verified (exact). The fresh run reproduces q=3..12 and counts 16480,16480,8000. Loops iterate all indicated thresholds, both orientations and declared tail sets; no broader exhaustive word search is asserted. |
| C33 | audit/supplement-replay/verification.json: serialized_witness_checks; witnesses.json; accepted hard-direction proof | Verified (exact). The exact q=3 values M=4,T=32,P=144403552893600 match the fresh lcm computation. q=4 is also checked. Minimality remains a consequence of the symbolic proof, not the diagnostic census. |
| C34 | audit/supplement-replay/verification.json: negative_controls; verifier negative_controls function | Verified (exact). All eleven cases n=2..12 deliberately fail the stronger insertion assertion at n-2; their entry (0,n-2) witnesses the failure. |
| C35 | claim.json; evidence/one-marker-proof.md; manuscript upper bound and explicit limitations | Verified (exact). The subclass upper bound forces a superquadratic unrestricted witness outside the one-marker class. The note makes no additional minimal-length, reverse-minimum or equality-classification claim. |
| C36 | frozen research and referee artifacts; manuscript/supplement/verify.py and README; audit/release-supplement-check.json | Verified (exact). The packaged code runs under the installed Python 3.10.12 with standard-library imports only and exact operations. The records describe separate model review, not external peer review. No formal proof-assistant certificate is asserted. |

## Internal mathematics, computation and release scope

The manuscript theorem and corollary preserve claim.json verbatim in meaning:
A_one(q)=(q-1)^2+2 for every integer q>=3, with all word lengths, empty blocks,
attainment and the declared partial single-initial NFA convention. The original
unrestricted A(q) growth problem remains unresolved. The text does not turn
finite checks, a model review, or this release audit into a mathematical proof.

A byte-identical copy of the supplementary verifier and inputs was run in
`audit/supplement-replay/`, so neither the accepted evidence nor the published
supplement output was overwritten. It reproduced all semantic result fields
with zero failures under Python 3.10.12. Table 1 was checked cell by cell;
construction counts, compressed witnesses and all negative controls match.
The development bitset code and the supplementary set/orbit code were inspected.

The typography parser initially rejected the standard dotless-i and labeled
arrow macros. Only their source spellings were changed: a literal UTF-8
Goralčík at line 48 and equivalent overset/longrightarrow expressions at
lines 256–257 and 267. All claim texts, identifiers, line intervals, citation
keys, hypotheses and proof steps are unchanged. The affected claims were
rechecked, the article was cleanly rebuilt and refrozen, and the stored
excerpt/digest bindings were refreshed. No frozen mathematical file changed.

The final build and BibTeX logs have no unresolved references, citation warnings,
errors, overfull or underfull boxes. The mechanical bibliography checker finds
seven cited keys, seven entries and seven resolved aux entries, with no missing
or extra keys. All six final rendered pages were actually viewed; see
`audit/build.md` and `audit/visual.md`. This audit authorizes only a local
research artifact under the runner's subsequent gate, not journal acceptance,
external peer review, submission or public posting.
