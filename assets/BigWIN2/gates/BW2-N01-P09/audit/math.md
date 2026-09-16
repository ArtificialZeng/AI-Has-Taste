# Mathematical referee report

**Verdict: accept the exact frozen claim.** The submitted all-arity
classification and count resolve the original SC229 question, including its
requirement for exhaustive representatives without duplicate functions.
No restriction of the domain, arity range, variable permutations, or claimed
contribution is needed. The frozen fields remain `kind=resolution-paper` and
`original_status=proved`.

Referee job: `newwin-00001-p09-referee-0e4bde7f7f81`.
Review date: 2026-09-12.
Snapshot digest:
`18815edf6e7f240c1b5c28e90cced864fbed61ffa4fc3c27160e18c4b9bfea38`.

This is a fresh-context review with no delegated agents or other model
processes. I used the original statement, precise interpretation, frozen
claim, listed proof/code/certificates and primary-source evidence. I did not
use the owner's checkpoint, state, earlier audit, job transcripts, or
research-assessment summary. Proposer acceptance/confidence assertions
embedded in required inputs were not treated as evidence. This pass is a
separate mathematical check, not external peer review or a claim of
statistical independence.

## Scope and integrity

The given operation has rows `000/101/111`, with the first argument indexing
the row. Terms use each coordinate exactly once, with arbitrary permutation
and binary bracketing, without constants. Labels are fixed coordinates, not
an additional quotient. The assertion covers every finite nonempty label
set and every integer n >= 1.

All 17 file hashes in the snapshot matched. I independently recomputed the
snapshot digest from its sorted-key compact JSON file mapping. The original
`source.md` SHA256 is
`519346c2f2624980063eb32e4a79d4df5ed7583e05944a6f25eb984e0590f6de`.
The fresh verifier checked all frozen hashes again after its computations.
No frozen input was edited and no manuscript was created.

## Reconstruction of the decisive argument

**1. Indicators and evaluation.** Put q_R = 1[R*=1]. A leaf has
q_x(a)=1[a=1], although its actual term function is the ternary projection.
Every composite term is Boolean-valued because the table never outputs 2.
For a leftmost decomposition

    t = (((x_i * R_1) * R_2) ... * R_m),

the table gives

    q_t = H_i(q_R1) product_{j=2}^m (1-q_Rj),
    H_i(q) = 1[a_i=2] OR (1[a_i=1] AND (1-q)).

This follows by checking the first multiplication separately; each later
left operand is Boolean and b*a = b(1-1[a=1]). Child supports and the root
are disjoint. Thus the first child is distinguished while the other children
can be unordered. Recursive realization of any such decorated labelled
tree supplies surjectivity.

Every q_R vanishes at the all-zero tuple, attains both Boolean values, and
depends essentially on every coordinate. For composite terms, output 1 is
witnessed by root value 2 and all child coordinates zero. Essentiality in
the distinguished child is exposed by root value 1 with ordinary children
zero; essentiality in an ordinary child is exposed by root value 2 with
all other children zero. These assignments change only the coordinate
under test. The leaf base case is immediate. Every indicator also has an
identically zero slice at value 0 of its leftmost coordinate.

**2. Unique disjoint AND factors.** For a nonempty relation S and two
factorizing coordinate partitions P,Q, projecting the Q-product onto a
block B of P gives the product of the projections onto the nonempty sets
B intersect C, C in Q. Substitution into the P-product proves that the
common refinement factorizes S. There are finitely many coordinate
partitions, so their common refinement is the unique finest one. Its
blocks have prime projections, and any partition into prime projections
must equal this finest partition.

Applied to S = h^{-1}(1), this yields unique disjoint AND-prime factors of
a nonzero Boolean function essential in every coordinate. The factors are
the indicators of the corresponding projections of S. Nonemptiness excludes
zero factors, and essentiality excludes a constant-one factor on a nonempty
block. These hypotheses were established for q_t; neither empty truth sets
nor unused coordinates are being silently discarded.

**3. Primality and recognition.** Each q_R is OR-prime. In an OR
decomposition on two nonempty coordinate blocks, only one block contains
the leftmost coordinate. Setting that coordinate to 0 forces the other
factor identically zero, contradicting essentiality of its block. The
singleton case has no proper split. Consequently every 1-q_R is AND-prime.

H_i(q_R1) is essential on the root together with the distinguished child's
support. In a putative AND split, place i in the first block. Its root-2
slice is identically one, forcing the factor on the other block identically
one, again contradicting essentiality. Hence this root factor is AND-prime.
The displayed evaluation formula is therefore exactly the unique prime
factorization, not merely one possible product representation.

The root factor has an identically zero value-0 slice in coordinate i.
It has no such slice in any child coordinate, since setting the root to 2
makes the factor one. Every ordinary factor 1-q_R contains the all-zero
tuple in its truth set, so none has a zero value-0 slice. The function alone
therefore identifies exactly one root factor and exactly one root coordinate.
This argument concerns the root factor's root-2 slice, not a generally false
assertion that the entire term function is one on that slice.

**4. Decoding and injectivity.** Remove the root coordinate from its prime
factor's support and complement its root-1 slice to recover q_R1. Complement
each other factor to recover the ordinary child indicators. All recovered
supports are nonempty and strictly smaller than the original one. Their
existence as term indicators follows from the original factorization; the
decoder's choice of factors and root uses only the function. Induction
recovers every child tree, and the first recovered one is distinguished.
On a singleton support the indicator is decoded as a leaf, not identified
with a composite Boolean term. This proves injectivity for indicators, hence
for all composite term functions; n=1 has just its projection.

Ordering ordinary child representatives by their least label gives a genuine
normal form on [n]. On any other finite label set, fix a total order if a
syntactic representative is desired; the underlying bijection does not
depend on such an order. There are no implicit relabellings or function
deduplication steps in the resulting counting model.

**5. Enumeration.** A tree is a labelled root with either no children or one
distinguished decorated tree and an unordered set of other decorated trees.
Disjoint labelled supports remove any issue with isomorphic unlabelled
children. Therefore T=x(1+T exp(T)). Directly, for sets of trees counted by
B_r, isolating the block of a fixed label yields

    B_0=1,
    B_r=sum_{j=1}^r binom(r-1,j-1)c_j B_(r-j).

Choosing the root and distinguished-child label subset yields

    c_1=1,
    c_n=n sum_{k=1}^{n-1} binom(n-1,k)c_k B_(n-1-k).

These recurrences can be evaluated successively and already meet the
original counting requirement. Formal Lagrange inversion gives

    c_n=(n-1)! [u^(n-1)](1+u exp(u))^n
       =(n-1)! sum_{k=0}^{n-1} binom(n,k) k^(n-1-k)/(n-1-k)!.

Here phi(0)=1, and terms with k >= n contribute zero to the coefficient.
The convention 0^0=1 gives c_1=1. This is a formal-series argument, with no
analytic convergence assumption, limiting interchange, or zero denominator.

## Checks actually performed

I wrote and ran `audit/referee-checks.py`; it imports no proposer code and
does not rerun a proposer search. Its exact results are in
`audit/referee-checks.json`. Two independently organized generators were used:

- Catalan shapes followed by all coordinate permutations, evaluating each
  multiplication from all nine literal table entries with integer bitsets;
- all Prüfer words, each possible root, and all choices of a distinguished
  child at every nonleaf, followed by literal evaluation of representatives.

For each n from 1 through 6, these gave precisely the same function-to-tree
mapping. Raw term counts were 1, 2, 12, 120, 1680, 30240. Distinct decorated
tree/function counts were 1, 2, 12, 108, 1340, 21150, with no collisions and
all 3^n assignments represented. All six sorted truth-set digests matched
the frozen certificates.

A fresh truth-set decoder, which recursively searches binary coordinate
splits rather than enumerating all set partitions, recovered all 1,463
distinct functions for n <= 5. It performed 25,556 bipartition checks and
7,173 recursive indicator decodes. This does not claim exhaustive decoder
testing at n=6. The explicit finite sum and integer recurrence agreed for
n=1,...,12; values beyond six are formula checks, not function censuses.
The suffix interchange identity was checked on all 81 four-variable inputs.
The stronger three-variable identity fails at (2,0,1), giving 0 versus 1.

Finite checks corroborate the separately reconstructed universal proof;
they do not establish the universal quantifier by extrapolation. No proof
assistant was used. The verifier completed normally with all checks passed.

## Primary-source comparison and contribution

The frozen 2024 primary text was inspected at Definition 1.1 and Section 7,
p.17; the journal PDF was also opened live. It defines the same arbitrary-order
linear terms and gives exactly the SC229 table, five initial counts, and
suffix interchange identity, while asking for a general answer. Thus the
scope is the original question, not the distinct fixed-order SC258 problem.
[Huang--Lehtonen, 2024](https://ecajournal.haifa.ac.il/Volume2024/ECA2024_S2A29.pdf).

The frozen 2023 primary text was inspected at Definitions 6.1.2--6.1.3 and
Proposition 6.1.4, pp.14--15, and its primary metadata was checked live. The
leftmost decomposition and ordered rooted tree encoding are prior work.
The proposition forgets all child order under (xy)z=(xz)y, an assumption
that the exact witness above disproves for SC229. It therefore does not
supply the submitted classification.
[Huang--Lehtonen, 2023](https://arxiv.org/abs/2202.11826v2).

I also checked the cited adjacent preprint's Definition 2.1 and Proposition
3.2 live: its evaluation-word/context-map framework is consistent with the
limited comparison in the dossier, and a whole-page search found no SC229
mention. These inspected results do not supply the decorated-tree
classification. No conclusion about all consequences of that framework is
needed here.
[Yildiz, 2026](https://arxiv.org/html/2604.01486v1).

Fresh searches on 2026-09-12 included `"SC229" "spectrum"`,
`"SC229" groupoids associative commutative`, `"SC1553" groupoids`,
`"SC229" "groupoid" "classification"`,
`"1340" "21150" spectrum`, and 2025/2026 queries for
`"associative-commutative"` spectra. The author's current publication list
was also consulted. No competing exact SC229 result was identified in this
bounded screen; unrelated matches and index dates were not mathematical
evidence. This is not an exhaustive priority or unpublished-work search.
[Lehtonen's publication list](https://n-ary.fi/publications.html).

The substantive delta is the injective SC229-specific factorization decoder
and the resulting all-n function classification. It supplies both a concrete
term-equivalence test and the exact spectrum. It is not just the routine
enumeration of an unverified tree model. The attribution of earlier tree
tools and standard coefficient extraction is appropriate.

## Gaps and disposition

No unresolved mathematical gap was found in the frozen claim. No substantive
repair, auxiliary unproved assertion, or numerical extrapolation is required
for acceptance. The recorded journal/arXiv DOI discrepancy is bibliographic;
the primary paper is unambiguously identified and its needed statements were
checked. It should be resolved in the later citation audit without changing
the accepted mathematics.

The exact frozen `resolution-paper` scope passes correctness, full-scope
equivalence, and contribution review. The next workflow step is the runner's
provenance/integrity gate, followed by manuscript preparation and its separate
citation, build, and visual checks. Those later checks are not completed or
pre-approved by this mathematical verdict.
