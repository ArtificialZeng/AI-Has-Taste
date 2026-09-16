# Five jobs are minimal for an unsafe almost-exact fathoming event

## Immutable source statement

Use exactly the job--tool incidence model, KTNS magazine policy, permutation-insertion search tree, and the Section 6.3 almost-exact fathoming rule of the primary source. Call a partial sequence `sigma` unsafe if the rule fathoms `sigma` although `sigma` has at least one completion whose tool-switch cost equals the global optimum of the full instance.

Prove or disprove:

> For every 0--1 job--tool incidence instance with at most four jobs, at most four tools, and a magazine capacity `c` satisfying `max_j |T_j| <= c < m`, no partial sequence is unsafe.

Together with the five-job instance displayed in Section 6.3 of the source, this would make five the least number of jobs for which the rule can fathom a branch containing a globally optimal completion. The claim is about existence of an unsafe fathomed node, not about whether every globally optimal branch is lost.

## Quantifiers and scope

- Jobs and tools are labeled, but the exhaustive certificate may quotient simultaneous job and tool relabeling when canonical representatives and orbit recovery are recorded.
- All nonempty tool sets `T_j` with `|T_j| <= c` are included. Repeated job types are allowed.
- Every partial sequence that can occur in the underlying permutation-insertion tree is tested, independently of heuristic traversal order.
- KTNS tie cases must be handled under the source's actual convention. If the rule depends on an unspecified tie choice, the result must split the relevant universal or existential tie quantifier instead of choosing one silently.
- Exact switch counts and globally optimal full-sequence costs are required.

## Primary source and nearest result

- Alberto Locatelli, Jean-François Côté, and Leandro C. Coelho, *An Exact Combinatorial Branch-and-Bound Algorithm for the Job Sequencing and Tool Switching Problem*, arXiv:2609.03219v1 (2026), https://arxiv.org/abs/2609.03219.
- Local primary PDF: `batches/inbox/bigWin-55-materials/2609.03219.pdf`.
- Locators: KTNS and exact search definitions in Sections 3--5; the almost-exact rule in Section 6.3, PDF pp.12--13; Figure 3 and the five-job instance immediately following the rule.
- The source gives `n=5, m=4, c=3`, with `T_1={2,3}`, `T_2={1,3}`, `T_3={1,2}`, `T_4={3,4}`, and `T_5={1,4}`, and shows that the rule prunes the partial sequence `(4,1,2,3)` although it has the globally optimal completion `(4,5,1,2,3)` of cost one. It does not prove minimality in the number of jobs.

## Proposed contribution boundary

Establish the sharp lower boundary `n >= 5` for an unsafe event. This does not claim that the heuristic fails to return an optimum on the displayed instance, nor does it modify any performance theorem in the source.

## Cheapest decisive test and certificates

Enumerate all canonical incidence matrices for `n <= 4`, `m <= 4`, and admissible `c`; enumerate full orders to determine the exact optimum; replay KTNS and every applicable fathoming event on every partial order. Store canonical representatives, orbit multiplicities, tie-policy outcomes, witness optimal completions, aggregate counts, and a digest. Independently replay positive and negative cases with a second implementation. A single admissible instance with at most four jobs and an unsafe node refutes the claim.

## Provenance

Prepared on 2026-09-07 from the primary arXiv PDF during the authorized primary-literature fallback because the confirmed Chrome target tab could not be attached. This file freezes the minimal-job question and must not be strengthened to loss of every optimal branch without separate evidence.
