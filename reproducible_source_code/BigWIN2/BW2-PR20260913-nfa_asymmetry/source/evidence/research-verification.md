# Owner verification and adversarial diagnostics

Job: primary-20260913-nfa-asymmetry-research-71ec4a8ef3d7.
This is owner verification in the research pass, not an independent audit.

The exact proposed formula was saved in `one-marker-proof.md` before running
the fresh diagnostics. No statement was fitted or revised in response to the
results. The script does not import the triage implementation. Reproduction:

    python3 evidence/research-checks.py

## Quantified exact finite observations

The script completed in one process, with zero failed assertions. Its source
hash and all coverage counts are in `research-checks.json`.

1. For q=3,...,8, it enumerated every ordered distinct one-marker pair with
   between 1 and 40 zeros in total: 137,760 parameterized cases across q.
   Explicit constructed machines were simulated using sets of reachable states
   and literal symbol steps, with state counts checked against H_q+1.
   There were 1,360 expected long/congruent cases in which the dichotomy gives
   no constructor; these are NOT counted as accepted or failed separations.
   They belong to the mathematical impossibility case in the proof.
2. Additional tests forced both prefix constructions and their reversals for
   every k=0,...,H_q-1, displacements 1,q,L_q, and paddings 0,H_q-1,H_q,H_q+1.
   This includes empty blocks and the upper threshold k=H_q-1 even when a
   modulus would have provided an easier construction. Across ordinary and
   forced tests there were 143,360 verified constructor applications: 133,404
   modulus, 2,665 of each prefix orientation, and 2,313 of each suffix orientation.
3. For every Boolean zero relation B on n=1,2,3,4 labeled states (2,16,512,65,536
   relations, respectively), put T=2^n and P=lcm(1,...,T). The script checked
   B^T=B^(T+P), the universal index identity, and the binary transfer inequality

       B^(n-1) C B^(T+P) <= B^(n-1+P) C B^T.

   Here <= means entrywise inclusion, with no restriction on initial or final
   states. For each B, every single-edge C was tested at every matrix entry.
   There are 1,053,250 such (B,C) basis cases in total. Every C is a union of
   its single-edge relations, and Boolean multiplication distributes over
   union, so these basis tests imply the inequality for every C in the stated
   dimensions. This is an explicitly justified algebraic domain reduction,
   NOT a claim to have iterated over all 2^(2n^2) transition tables. It checks
   the boundary transfer lemma rather than computing A_one(q) in these ranges.
4. A negative control rejects the overstrong assertion that any cyclic
   n-vertex graph satisfies B^(n-2)<=B^(n-2+L_n). For n=2,...,12, take a chain
   on 0,...,n-2 and an isolated loop at n-1. The entry (0,n-2) disappears after
   the length increase. Each exact matrix and failed entry is serialized.
   This demonstrates that the test detects a real failure if the prefix
   threshold is shortened by one. It is not a disproof of our theorem.
5. For q=3,4 the full large attaining words were represented by exact integer
   exponents, without expanding their literal strings. Boolean exponentiation
   verified acceptance/rejection by the q-state graph and by the explicit
   M+2-state hard-direction chain. The q=3 witness has M=4, T=32,
   P=144403552893600 and common length 144403552893637. Its claimed lower
   cost of six is established by the all-size proof, not by a five-state census.

## Mathematical audit points resolved by the argument

- The imported index constant is for all relations, including nilpotent and
  reducible graphs. Actual source statements and rendered pages are supplied.
- The period identity follows from that bound and cycle insertion, so no
  malformed definition of matrix period is being used.
- All four zero exponents and both signs of displacement are covered by the
  upper bound. Reversal keeps one initial state because the constructed machine
  has a single final state.
- The lower-bound prefix with M edges in M+1 states need not itself repeat a
  state. In that case it visits all states, which is the reason a cycle from
  the suffix can be inserted. This is the decisive extra-state argument.
- The suffix subset sequence has at most T values, so a repetition among its
  first T+1 terms ensures periodicity by time T. Its period divides P by the
  definition of P, with no primality or size assumption omitted.
- The easy witness has exactly q states; the nonreturn length is M, and both
  zero exponents of its accepted word exceed M. The hard chain has M+2 states.
- The original unrestricted optimization is not identified with its subclass.

Known mathematical gaps in the submitted proof: none identified by the owner.
The old source-access obstacle is closed at the level of an authoritative
primary statement, not by pretending to have read the unavailable 1970 proof.
Novelty and significance are screened, not certified. Fresh referee scrutiny
of the exact claim and decisive primary-source account is the next gate.
