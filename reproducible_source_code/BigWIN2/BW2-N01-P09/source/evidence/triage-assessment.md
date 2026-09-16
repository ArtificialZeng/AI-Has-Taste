# SC229 triage assessment

Job: newwin-00001-p09-triage-d9fd6bb8283b. Date: 2026-09-12.
Decision: advance; candidate_kind=none; original_status=unresolved.

## New exact evidence

Run `python3 evidence/triage-check.py` from the project directory. The script
uses the literal multiplication table, retaining every ordered binary term;
it does not prune using the proposed tree equivalence. It records the tree
code separately by grafting the right child's tree onto the leftmost root,
retaining the first child and sorting the remaining children.

Every full term on each of the 63 nonempty subsets of six labels was evaluated
on all 729 ambient assignments. The full six-label support contains 30,240
syntactic terms and 21,150 distinct functions. On every support, a tree code has
exactly one truth table and a truth table has exactly one tree code. Counts for
sizes 1–6 are 1,2,12,108,1340,21150. All six truth-set digests match the supplied
mask enumeration. This newly supplies the previously missing literal n=6
comparison. There were 30,902,310 literal product-assignment cells evaluated.

The four-variable interchange identity passes all 81 assignments. The stronger
three-variable identity fails at (x,y,z)=(2,0,1): (x*y)*z=0 and (x*z)*y=1.
Thus the first left-spine child cannot be treated as interchangeable with all
later children under the 2023 theorem.

The Cartesian-product common-refinement property was tested on all 4,095
nonempty relations on {0,1}×{0,1}×{0,1,2}, across all five coordinate partitions.
All 6,489 ordered pairs of factorizing partitions have a factorizing common
refinement. These are exact finite observations, not an all-n proof.

## Local mathematical check of the generic refinement lemma

Let I be finite, let each A_i be a nonempty set, and let R be a nonempty subset
of the product over I. A partition P factorizes R when R is the product of its
coordinate projections pi_B(R), B∈P. If P and Q both factorize R, then for
B∈P, projecting the Q-product onto B gives

    pi_B(R) = product_{C∈Q, B∩C nonempty} pi_{B∩C}(R).

This follows because the C-coordinate blocks are disjoint, so their projected
coordinates can be chosen independently; nonempty omitted factors can be
filled. Substitution into the P-product proves that the partition of nonempty
intersections B∩C factorizes R. There are finitely many partitions of I, so
successive common refinement yields a unique finest factorizing partition.
Its factors are uniquely the projections of R. This argument is elementary
and no novelty is claimed for it. The empty relation is excluded to avoid
nonunique zero factors.

This resolves the generic product-refinement subtest at the level of a local
written argument. Its application to SC229 must still establish all essential
supports and identify the factors; numerical agreement cannot supply that step.

## One next test: the all-arity decoder lemma

For every nonleaf full linear term, write its known leftmost decomposition as
T=(((x_i*R_1)*R_2)...*R_m). Set q_R=1[R=1]; for a singleton x_j this is
1[x_j=1], whereas for nonleaf R it is the actual Boolean term function. Direct
use of the table gives

    F_T = G_i(q_R1) AND product_{j=2..m} (NOT q_Rj),
    G_i(q) = 1[x_i=2] OR (1[x_i=1] AND NOT q).

Prove or refute, simultaneously for all support sizes, that these displayed
factors are exactly the finest nonconstant AND factors on disjoint essential
supports, and that G_i is the unique such factor with an identically zero
coordinate slice at value 0, with i the unique coordinate of that slice.
The intended proof must justify nonconstancy, every variable's essentiality,
OR-primality of q_R from its leftmost-zero slice, AND-primality of G_i from
its root-2 slice, and the singleton/nonleaf distinction. Then restricting the
identified factor at x_i=1 should recover NOT q_R1 and permit recursive decoding.

A counterexample to this lemma changes the proposed normal form, not the
original counting problem. A complete proof would establish injectivity;
together with the evident term encoding and reconstruction, it would justify
the proposed EGF and coefficient formula in problem.md. No full all-n
classification, mathematical acceptance, or manuscript is asserted here.

## Limits

The code/function bijection is established computationally only through six
variables. The supplied formal-series counts above six are conditional model
counts, not function censuses. Novelty and historical deduplication remain
bounded as documented in `literature/triage-screen.md`. A fresh mathematical
referee is required after any complete proof is frozen.
