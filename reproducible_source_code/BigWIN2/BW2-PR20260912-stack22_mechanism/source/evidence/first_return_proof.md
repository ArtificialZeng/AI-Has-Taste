# Direct enumeration from comparison obligations

Research job: `primary-20260912-stack22-mechanism-research-897e72adb69b`.
This is the complete proposed argument for a fresh referee, not an audit
acceptance or a publication manuscript. No mathematical gap is presently
known to the proposer. Literature limits are recorded separately.

## Exact scope

Use precisely the input-sorting model in `source.md` and `problem.md`:
distinct labels 1,...,n, left-to-right input, insertion/removal at either
of the first two available stack positions, increasing output, empty
initial and final stack. Let u_n count inputs admitting a sorting trace,
once each, and let F(x)=sum u_n x^n, including u_0=1.

**Proposed theorem.** The operations admit the unambiguous canonical
language and first-return specification below. They imply, in Z[[x]],

    2xF^3-(2x+3)F^2-(x-7)F-4 = 0,    F(0)=1.

The polynomial is previously known. The proposed contribution is the
complete derivation directly from sorting operations, including the
comparison information and the bijection with inputs. Neither a pattern
basis nor the known polynomial is used to discover or justify the
specification. No passage to permutation generation is needed.

## 1. One canonical trace for each sortable input

Write P_j for insertion at position j and Q_j for removal at position j,
with stack positions read top to bottom. At a state whose required next
output is k, popping k when it is accessible preserves sortability.
Indeed, in any successful continuation, the steps before its pop of k
are pushes only. Pop k immediately, then simulate these pushes with k
deleted: if k lay strictly before the old insertion slot j, use slot j-1;
otherwise use slot j. All slots remain available and at most 2. Omit the
old pop of k; the configurations and outputs now agree.

For a<b and any fixed suffix T and unread input, sortability from stack
(b,a,T) implies sortability from (a,b,T). Simulate a successful
continuation until a is popped, interchanging a and b in the two stacks.
Neither is popped earlier, since the output is increasing. All operations
on other tokens have the same positions in the two configurations.
Survivors do not change relative stack order. Immediately before a is
popped, b precedes a and a is accessible, so the top pair must be (b,a).
In the second configuration pop a from position 1 instead of position 2.
The remaining stacks agree, and the rest of the continuation is identical.

Consequently the following deterministic sorter G is complete as well as
sound. Pop k whenever it is in the first two positions. Otherwise read
the next input a, placing it at position 1 if the stack is empty or a is
smaller than the old top b, and at position 2 if b<a. Reject if neither
operation is possible before completion. To prove completeness, induct
on the remaining number of operations of a successful continuation: an
eager pop preserves success; if none is available a push is forced, and
the top-pair observation says the choice made by G preserves success.
The two possible pushes give exactly the two top-pair orderings.

A complete legal rank word determines one input permutation. Give each
push a new token, execute the rank operations, and label the token at
the j-th pop by j. Read these labels in push order. This produces a
permutation and the word sorts it. It is the only labeling giving
increasing output. Therefore distinct G-selected rank words correspond
to distinct sortable inputs, and every sortable input has exactly one
such word.

## 2. Push comparisons and the eager condition

For a complete legal rank word, use the reconstructed labels just
described. A nonempty-stack P1 is the G choice precisely when its new
token precedes the old top in output order; P2 is the G choice precisely
when the old top precedes the new token. Record the required comparison
as an edge directed from the earlier-output token to the later-output
token. At each push that edge points from the upper token of the new
top pair to the lower token. Empty-stack P1 creates no comparison.

Call a word comparison-valid if every recorded edge has its source
popped before its target. This is exactly the requirement that all its
pushes use G's comparison choice; it says nothing yet about eager output.

**Peak criterion.** A comparison-valid complete word is G-selected if
and only if every adjacent push-pop pair is P1 Q1.

For necessity, consider a push immediately followed by a pop in a
G trace. The required token was not accessible before the push. A push
cannot move an old token closer to the top, so the popped token must be
the newly pushed token. It is smaller than all resident tokens, hence
was inserted at position 1 and is popped there.

For sufficiency, consider any moment immediately before a push. The next
pop follows a nonempty run of pushes, ending in P1 Q1 by the criterion.
That pop removes the token of the last push in this run. This token is
not yet present at the moment considered. Thus the required next output
is not accessible, and G must push. All push choices agree with G by
comparison-validity. At pop steps the required token, by reconstructed
labeling, is exactly the token removed and is accessible. Hence every
operation agrees with G. This proves both directions without an
assumption about the sizes of the stack or of push runs.

## 3. A single bit per token retains all live comparisons

Process a word while requiring each pop to respect the comparison edges.
Maintain the graph on unpopped tokens, deleting a token and all its
incident edges when it is popped. This graph is an ordered rooted forest
whose preorder is the current top-to-bottom stack word. Initially it is
empty. The invariant follows under each admissible operation:

* Empty-stack P1 creates a singleton tree.
* Nonempty P1 creates a new root with the previous first tree as its sole
  child; all later trees are unchanged.
* P2 attaches the new token as the first child of the first root.
* Q1 removes the first root and promotes its children to roots in order.
* Q2 is admissible exactly when the first root is a leaf. In that case
  the second token is another root: removing it promotes its children
  after the surviving first root. If the first root is not a leaf, the
  second token is its first child and its removal would violate the edge
  from the first root.

This also proves the test is necessary, not just sufficient: assuming
earlier pops respected all edges, the displayed forest invariant holds,
and the only possible incoming edge obstructing either top-two pop is
the one just specified. A comparison-valid word can never make the
forbidden Q2. Conversely, deleting only roots respects every edge ever
created, so the test guarantees comparison-validity after all tokens
are popped.

Store bit 0 for a leaf and bit 1 for a nonleaf, on each token. A surviving
vertex cannot lose a child: that child has an incoming edge until its
parent is removed. Therefore these bits need no child counts and never
change from 1 to 0 while their token survives. With bit strings read
top to bottom, the exact transition rules are

    P1: empty -> 0;       aT -> 1aT,
    P2: aT -> 10T,
    Q1: aT -> T,
    Q2: 0bT -> 0T,

where a,b are either bit and T is any suffix. P2 keeps and marks the old
top and inserts the new leaf second. Q2 requires at least two tokens.
All other tokens retain their bits.

Add the single forbidden adjacent factor P2 Q1. The bit transitions
already disallow P1 Q2 and P2 Q2: a push into a nonempty stack leaves
top bit 1, and a push into the empty stack leaves only one token.
Thus the allowed peaks are exactly P1 Q1. By the preceding two sections,
complete paths of this bit machine, with P2 Q1 forbidden, are in
bijection with sortable inputs, with one push per input entry.

In particular this is more than a finite-state approximation to the
boundary comparisons: the forest invariant proves the compression for
arbitrary depth, degree and word length.

## 4. An unambiguous first-return specification

All following languages consist of rank words, not labeled tokens. A
positive-floor path starts with top bit a and a protected suffix T,
ends at the same height, and never goes below its initial height. A
nonempty first-return excursion stays strictly above that height until
its last step. In such an excursion the initial suffix T is never
inspected or changed: above the initial height there are at least two
tokens before T. The initial top may survive or be replaced. Accordingly
the endpoint top bit, rather than token identity, is the interface.
Auxiliary paths are defined in the abstract bit machine, so a formal
initial bit 1 need not itself be a complete physical singleton forest.
The protected suffix can always be supplied; its contents do not affect
the path language.

Opening P1 from top a leaves top 1 and stores bit a in the second
position. Opening P2 leaves top 1 and stores bit 0 in the second
position. The interior is a positive-floor path beginning at bit 1.
At closure, Q1 restores the stored bit; Q2 is possible only if the
interior ends with bit 0, and then retains 0. If the interior is empty,
opening P2 and closing Q1 is forbidden. These cases exhaust every
first-return excursion.

It follows directly, or inductively on length using this decomposition,
that a positive-floor path starting with 0 can only return with 0.
A path starting with 1 can return with 1 or with 0. Let

    A = paths 0 -> 0,
    B = paths 1 -> 0,
    C = paths 1 -> 1.

A and C include the empty word epsilon; B does not. Define two
first-return word languages E and D by the following disjoint unions;
juxtaposition means concatenation:

    E = P1 (B union C) Q1,
    D = P1 B Q2
        union P2 B Q1
        union P2 (C minus {epsilon}) Q1
        union P2 B Q2.

From initial bit 1, E preserves bit 1 and D changes it to 0.
From initial bit 0, both E and D return to 0. This is exactly the
opening/interior/closure case split above. In particular the only
empty-interior exclusion is explicitly present in the third term of D.

Decomposing at the first return gives

    A = {epsilon} union E A union D A,
    C = {epsilon} union E C,
    B = E B union D A.

For a complete path starting at the empty stack, opening P1 creates
bit 0. Its interior is A and its final step is Q1. If L denotes the
complete language, then

    L = {epsilon} union P1 A Q1 L.

Every union and product is unambiguous. For a nonempty path, its first
return is fixed by the push/pop height profile, so its interior and
remaining suffix have unique lengths. Within a first return the first
and last ranks distinguish E and all terms of D except the two P2...Q1
terms. Those are distinguished by the uniquely determined endpoint bit
of the interior (0 for B and 1 for C); the empty word is excluded
where required. Repeating this argument gives a unique parse by
induction. Conversely each production satisfies the prescribed state
transitions, floor and forbidden-factor conditions. Concatenation adds
only a pop-push boundary, so introduces no new forbidden peak. Hence
the specification is both complete and unambiguous at every size.

## 5. Deriving the generating function

Use the same letters A,B,C for the ordinary generating functions of the
languages, with x counting pushes, and put S=B+C. The first-return
series are

    e=xS,             d=x(3B+C-1).

The subtraction of 1 removes precisely the excluded empty interior;
it is not an inclusion-exclusion guess. The specification gives

    A = 1+(e+d)A,
    C = 1+eC,
    B = eB+dA,
    F = 1+xAF.

These equations determine the coefficients recursively: every
first-return term has at least one push, so coefficient n depends only
on smaller-size interior and suffix coefficients. The constants are
A(0)=C(0)=F(0)=1 and B(0)=0.

Since e and d have zero constant term, their complements are units in
Z[[x]], and

    A=1/(1-e-d),    C=1/(1-e),    B=dAC=A-C.

Therefore S=A, and C=1/(1-xA)=F. Substituting B=A-F gives

    F=1+xAF,
    A=1+xA(4A-2F-1).

For a division-free elimination, set

    R1=F-1-xAF,
    R2=A-1-xA(4A-2F-1).

Direct expansion gives the polynomial identity

    2xF^3-(2x+3)F^2-(x-7)F-4
      = x F^2 R2 + (-4xAF+2xF^2+xF-3F+4) R1.

Both residuals vanish by the specification, giving the stated cubic.
At x=0 the cubic is -(F-1)(3F-4). Its derivative with respect to F
at (0,1) equals 1. More elementarily, after writing F=1+H with H(0)=0,
the coefficient of x^n in the cubic contains the new coefficient of H
with multiplier 1; all other contributions depend on smaller degrees.
Thus there is a unique formal power series with constant term 1
satisfying the cubic, and the operation language derives that series
for every n. This settles the requested mechanism derivation if the
argument is accepted on fresh mathematical review.

## 6. Verification and boundaries of the claim

`first_return_exact.py` independently traverses the bit machine and
compares with G on every permutation through n=8. It compares complete
word sets, multiplicities, and reconstructed inputs, not just counts.
`first_return_grammar.py` expands the recursive specification as Counters,
checks each auxiliary word's bit endpoint and its derivation count,
and compares the complete language against the separate bit traversal.
The corresponding JSON files show no missing, extra or duplicated
complete word. They also verify, in the tested range, the language
identities A=B disjoint-union C and F=C implied by the specification.
The finite checks support the implementation; Sections 1--5 carry the
all-size mathematical assertion.

The known coefficients and polynomial are calibration. The new proposed
scope is the canonical-language/forest/first-return derivation. This
does not assert novelty for the elementary greedy normalization alone,
does not address other (r,s)-stacks, and does not assert global priority.
All mathematical dependencies used in this argument are proved here.
The source author reports the earlier basis-derived enumeration; the
uninspected Atkinson and Pantone proofs are not mathematical dependencies
of this argument. A fresh referee has not yet assessed correctness or
the substantive distinction from prior work.
