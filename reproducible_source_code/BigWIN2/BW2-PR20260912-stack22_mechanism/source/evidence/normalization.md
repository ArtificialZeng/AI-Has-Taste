# Mechanism normalization: triage evidence

Job: `primary-20260912-stack22-mechanism-triage-654532f4a556`.
These elementary arguments are supplied for further checking; no novelty
or independent-referee acceptance is claimed. In particular, they may
overlap Atkinson's uninspected full paper. They do not derive F.

## Exact computational observation

`triage_exact.py` visits every input permutation for 0<=n<=8. A memoized
recursion explores every allowed push, and every pop consistent with sorted
output, including pushes that postpone an available pop. Its measure
2n-i-(k-1) decreases at each step. Therefore the recursion is finite and
counts all successful operation words exactly. The second version forces
an available pop, without changing push options. A third implementation
is the deterministic rule G below.

The 46,234 inputs in this range yield counts
1,1,2,6,24,116,628,3636,21956 for all three recognizers. All arithmetic is
integer arithmetic; the full sorter uses no pattern-basis oracle. A
successful deterministic trace is also a legal unrestricted trace, so
equal counts imply equality of accepted sets in each tested size.
The data are in `triage_exact.json` and can be reproduced by
`python3 evidence/triage_exact.py` from the project directory.

Eager output does not make traces unique. Input 21 has the two eager words
P1 P1 Q1 Q1 and P1 P2 Q2 Q1, where Pj inserts at j and Qj removes at j.
At n=8 there are 756,939 successful eager words for 21,956 sortable inputs.
This refutes uniqueness of the unrestricted eager language only.

## Elementary normalization arguments

**Eager-pop observation.** If the next required output k is among the top
two entries, popping it now preserves the existence of a successful
continuation. Take a successful continuation. Before its pop of k it
can only perform pushes. Pop k now and simulate those pushes with k
deleted from their stack configurations. If the deleted entry previously
lay before an insertion slot j, use j-1; otherwise use j. Slots remain
legal and at most 2. Omit the old pop of k. At that point the stacks,
unread inputs and outputs coincide, so the rest of the continuation works.
Repeated application gives eager output without claiming uniqueness.

**Top-pair dominance observation.** Let a<b. For a fixed unread input,
stack tail T and required sorted output, if stack (b,a,T) has a successful
continuation, then (a,b,T) does too. Until a is popped in the first
continuation, neither a nor b is popped. Simulate the same pushes and
pops of other labels from (a,b,T). The stacks have exactly the same
positions, with a and b interchanged. Just before the first continuation
pops a, b still precedes a; as a is within the top two positions, the top
pair must be (b,a). The simulated top pair is (a,b). Pop a from position
1 instead of 2. The remaining stacks now coincide, and all later
operations can be copied. Output order is unchanged.

**Deterministic sorter G.** Repeatedly pop the next required value when
it is in the top two positions. Otherwise, if input remains, push its
next value a at position 1 when the stack is empty or a is less than
the current top; push at position 2 otherwise. If neither action is
possible, accept exactly when all input and output are complete.

The two observations imply completeness of G. At a successful state,
an eager pop preserves success. When no pop is possible, a successful
continuation must begin with a push. The two possible resulting stacks
differ only by their top pair; the choice made by G puts that pair in
increasing order. Top-pair dominance preserves success. Induction on the
remaining number of operations proves that G sorts every sortable input.
Soundness is immediate from legality. Thus each sortable input has one
deterministically selected trace. This is an elementary recognition
normalization, not a proved finite counting grammar.

A rank-operation word also determines at most one input permutation
that produces increasing output: attach a distinct token to each push,
execute the rank operations, and label the token removed at the j-th pop
by j. Reading those labels in push order reconstructs the input.
Consequently the traces selected by G form an unambiguous set. Giving
this set a noncircular structural specification and deriving its series
remain the original task.

## First-return interface and remaining test

For h>=1, an excursion from height h which stays strictly above h until
its last step preserves the original stack tail below its top entry.
Indeed, let T be that tail of length h-1. Immediately after the opening
push it is a suffix. While the height exceeds h there are at least two
entries before T, so neither a pop nor a push in positions 1 or 2 touches
T. The final pop also starts above h. Hence T is unchanged on return.
The original top either survives or has been replaced by an entry pushed
within the excursion. The replacement need not be the opening push's
entry. The case h=0 is a separate empty-stack return.

Next test: construct a first-return recursive specification for the
G-selected operation words using this invariant, distinguishing survival
versus replacement of the original top and retaining the boundary value
comparisons required by G. Test that the proposed specification generates
each G trace exactly once and no extra word through n=8, using token
reconstruction rather than counts alone. A missing or multiply generated
word rejects the proposed specification. A successful finite comparison
still requires a complete recursive bijection before deriving F.
