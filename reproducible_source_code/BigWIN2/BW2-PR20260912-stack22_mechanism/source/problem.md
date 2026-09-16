# Precise problem and proposed resolution scope

Source: immutable `source.md`, SHA256
`403df3b10d13461c45e5dfd74d1548350e575ce83ae62f17ab501428dc4855be`.
Research job: `primary-20260912-stack22-mechanism-research-897e72adb69b`.
The precise input model below is unchanged from triage.

For every integer n >= 0, let S_n be the permutations of [n], with S_0
containing the empty permutation. An input pi in S_n is consumed left to
right. A configuration is (i, s, k): i input entries have been consumed,
s is the stack word read top to bottom, and the output so far is
1,...,k-1. Initially (i,s,k)=(0,(),1).

If i<n, a push inserts pi(i+1) at one of positions
1,...,min(2,|s|+1), and increments i. A pop removes an entry from position
j <= min(2,|s|) and appends it to the output. For a successful sorting
trace this entry must equal k, after which k increases by one. No other
operations are available. A successful trace ends at (n,(),n+1), and
has exactly n pushes and n pops. Define C_n to consist of the inputs
admitting at least one such trace. Count inputs, not traces:
u_n=|C_n| and F(x)=sum_{n>=0} u_n x^n in Z[[x]], with u_0=1.

The requested contribution is a direct structural enumeration of C_n
valid for every n: an unambiguous mechanism language, bijective
decomposition, or comparably complete argument deriving F from these
operations. Any passage to generation from increasing input needs its
own object-preserving bijection. The frozen statement is not altered.

## Nearest prior result and source status

Live Vatter arXiv:2602.16355v2, Section 5, Theorem 5.9 and Problem 5.11,
was inspected on 2026-09-12. It attributes the basis
{23451,23541,32451,32541,245163,246153,425163,426153}
to Atkinson (1998), Theorem 4.1. The paragraph preceding Problem 5.11
reports Pantone's proof, via Combinatorial Exploration from that basis,
of the polynomial relation

2xF^3-(2x+3)F^2-(x-7)F-4=0.

At (x,F)=(0,1) the derivative with respect to F is 1, so this specifies
a unique formal power series with constant term 1. The displayed
coefficients begin 1,1,2,6,24,116,628,3636,21956, including the empty
input. These are calibration, not a proposed new theorem. Vatter's
Problem 5.11 explicitly asks for the mechanism derivation.

Source status: **open-supported** for this method request, on the
strength of that live primary problem list; the enumerative identity
itself is known. A bounded search is not a claim of global priority.
Atkinson's full proof and Pantone's actual exploration specification
have not been inspected. Details and URLs are in `literature/triage.md`.

## Proposed delta and evidence

Nearest prior result: the basis-derived algebraic generating function.
The proposed resolution is a complete mechanism derivation, supplied
for fresh review in `evidence/first_return_proof.md`. It proves the
following chain without using the forbidden basis or assuming the cubic:

1. Eager output and a smaller-top push choice give a deterministic
   complete sorter G; token reconstruction makes its rank words unique.
2. The push comparisons form an ordered forest whose preorder is the
   live stack. Respecting them requires only a leaf/nonleaf bit per token.
   The eager condition is the exclusion of the adjacent factor P2 Q1.
3. A complete first-return decomposition with boundary bits gives an
   unambiguous grammar. Its series reduce to
   F=1+xAF and A=1+xA(4A-2F-1), and these imply the known cubic.

The proposed theorem covers every n>=0 and exactly the original sortable
inputs. There is no switch to generation, no interpolation, and no
claim of a new polynomial. No mathematical gap is presently known to
the proposer; independent mathematical review is still pending.

`evidence/first_return_exact.py` compares all canonical input traces with
the bit language through n=8. `evidence/first_return_grammar.py` separately
expands the grammar and checks complete word sets, multiplicities, and
boundary states through n=8. A held-out n=9 comparison and an exhaustive
attack on all legal words through n=6 are in
`evidence/first_return_holdout.py`. `evidence/first_return_algebra.py`
checks a division-free polynomial identity and integer coefficients
through degree 40. All have completed JSON evidence, with zero reported
discrepancies. The finite checks support the all-size proof rather than
replace it.

`literature/outer-intake-handoff.md` was read. Its local primary capture
was inspected at the model definition and Section 5.11, then checked
against the live primary HTML. The complete capture is copied to
`evidence/external/vatter-2602.16355v2.html` for the candidate snapshot.
The bounded updated literature screen and source-access limits are in
`literature/research.md`. A newly located author-posted Atkinson PDF has
unreadable extracted text in the available tool; no full-text review is
claimed. Atkinson's and Pantone's proofs are not dependencies of the
self-contained proposed argument. Novelty is claimed only for the
direct forest/bit-language/first-return derivation, subject to review,
not for the elementary greedy normalization or the known enumeration.

No manuscript or audit acceptance is created in this research role.
