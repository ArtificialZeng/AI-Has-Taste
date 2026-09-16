# SC229 full associative-commutative spectrum

## Frozen interpretation

The original statement is `source.md`, preserved byte for byte. Its SHA256 is
`519346c2f2624980063eb32e4a79d4df5ed7583e05944a6f25eb984e0590f6de`.
No correction or restriction of the source is proposed.

Let A={0,1,2}. The operation *:A×A→A is defined with its first argument
indexing the row and its second argument indexing the column:

| * | 0 | 1 | 2 |
|---|---|---|---|
| 0 | 0 | 0 | 0 |
| 1 | 1 | 0 | 1 |
| 2 | 1 | 1 | 1 |

For each finite nonempty label set I, define the full linear terms L(I)
recursively. If I={i}, then L(I)={x_i}. Otherwise L(I) contains all (u*v)
with u∈L(J), v∈L(K), where J and K are nonempty disjoint sets with J∪K=I.
Every variable occurs exactly once; constants and repeated variables are excluded.
This is equivalent to all permutations followed by all full binary bracketings.

For every integer n≥1, let [n]={1,...,n} and let t^*:A^n→A denote the
pointwise evaluation of t∈L([n]) using this table. Define

    s ~ t  iff  for every a∈A^n, s^*(a)=t^*(a),
    c_n = |L([n])/~|.

Variable labels are fixed coordinates: there is no further quotient by variable
permutations or by relabellings of A. The target is to determine c_n for every
n≥1 by an explicit formula, a proved effective counting recurrence, or a
combinatorial model with a proved bijection to the functions. The source's
acceptance requirement asks for an exhaustive normal form without duplicates;
a longer finite list or a generic generate-and-deduplicate algorithm alone does
not meet that requirement. The case n=1 is the ternary projection and gives
c_1=1. Every term with n≥2 is {0,1}-valued. The n=0 case is outside the problem.

## Nearest prior work and current status

The source question is explicitly open in the inspected 2024 primary paper.
A bounded literature screen on 2026-09-12 found no equivalent all-n answer;
this does not certify present-day priority. Research pass 1 now proposes a
complete proof, recorded in `evidence/decoder-proof.md`, with workflow outcome
candidate, kind=resolution-paper, original_status=proved. These are proposer
claims submitted for a fresh referee, not independent mathematical acceptance.

Huang–Lehtonen, [Associative-commutative Spectra for Some Varieties of
Groupoids](https://ecajournal.haifa.ac.il/Volume2024/ECA2024_S2A29.pdf),
ECA 4(4) (2024), S2R29: Definition 1.1 matches these quantifiers. Section 7,
p.17 gives this table, the five ac-spectrum values 1,2,12,108,1340, and the
suffix interchange identity ((w*x)*y)*z=((w*x)*z)*y, while asking for the
general spectrum. SC1553 is an anti-isomorphic partner, not an additional new
target. The printed PDF DOI and arXiv metadata disagree; see
`literature/triage-screen.md` before creating bibliography entries.

Huang–Lehtonen, [The associative-commutative spectrum of a binary
operation](https://arxiv.org/abs/2202.11826v2), Discrete Math. 346(10) (2023),
113535: Definitions 6.1.2–6.1.3, pp.14–15, already supply leftmost decomposition
and its rooted-tree encoding. Proposition 6.1.4 assumes (x*y)*z=(x*z)*y,
which fails here at (x,y,z)=(2,0,1), with outputs 0 and 1. Its unordered-tree
bound therefore does not settle SC229.

The fixed-variable-order SC258 question is distinct: its table in the same
2024 paper has rows 000/110/101. The historical registry itself was not supplied
inside this project; the inherited registry screen is not a newly verified
complete deduplication result.

## Proposed full-scope resolution and verification

Nearest prior result: five SC229 counts, a four-variable interchange identity,
and existing leftmost-tree tools. Proposed delta: a complete all-n classification
by rooted trees on [n] having one distinguished child at every nonleaf and an
unordered set of other children. The proposed contribution is the SC229
classification, not the tree construction or Lagrange inversion in isolation.
The original statement and its frozen interpretation above are unchanged.

The proposed proof establishes the bijection, including both realization and
injectivity by a function-only recursive decoder. With
T(x)=sum_{n≥1} c_n x^n/n!, it gives

    T(x)=x(1+T(x)exp(T(x))),
    c_n=(n-1)! [u^(n-1)](1+u exp(u))^n
       =(n-1)! sum_{k=0}^{n-1} binom(n,k) k^(n-1-k)/(n-1-k)!,

where 0^0=1. This is the exact proposed answer awaiting fresh mathematical
review. A direct integer recurrence, independent of Lagrange inversion, is
also proved: B_0=1, c_1=1, and

    B_r=sum_{j=1}^r binom(r-1,j-1)c_j B_(r-j)                  (r≥1),
    c_n=n sum_{k=1}^{n-1} binom(n-1,k)c_k B_(n-1-k)            (n≥2).

Here B_r counts sets of decorated trees on a fixed r-element label set.

Triage's literal evaluation of every full binary term on all 63 nonempty
subsets of six labels confirms code/function equivalence in that finite
range and c_1,...,c_6=1,2,12,108,1340,21150. Research pass 1 adds the universal
argument and a truth-table-only decoder test on all 1,463 distinct functions
through five variables, plus 16 structured cases on six and seven variables.
The recurrence and explicit sum agree through n=12; these higher values are
formula values, not new censuses. See `evidence/research-assessment.md`,
`evidence/decoder-check.py`, and `evidence/decoder-check.json`.

The decisive primary PDFs and freshly extracted texts are copied into
`evidence/external/huang-lehtonen-2024.pdf` and
`evidence/external/huang-lehtonen-2023.pdf` (with matching .txt files).
The current source comparison is `literature/research-screen.md`.
No known proof gap has been identified by the proposer, but there has been
no fresh referee or acceptance. One next test: audit the all-arity prime
factorization and recursive decoder in Sections 2--4 of the proof, including
singleton indicators, then verify the full-scope labelled count. No manuscript.
