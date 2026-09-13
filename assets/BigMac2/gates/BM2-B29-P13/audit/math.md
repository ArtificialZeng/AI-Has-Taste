# Fresh mathematical referee report

Referee job: `bigMac-00029-p13-referee-4dd05edac1e1`  
Frozen evidence digest: `e72a058f7568b7218d0ac764304fe9fe521908ccb6e06489b6f4241cbc08f2f0`

## Scope reviewed

I reviewed the exact `result-note` claim frozen in `claim.json`: under the
definitions in `problem.md`,

\[
 n_*=24,\qquad
 \mathcal G_{24}=\{\{2\}\cup T:T\subseteq\{8,14,20\}\}.
\]

The verdict below is confined to that finite theorem and its complete literal
classification. It does not resolve, estimate, or otherwise change the status
of the motivating limit \(E(n)/N(n)\to0\).

The snapshot was intact before review. Every frozen file had its recorded
SHA-256 digest, including `source.md` with digest
`a4e8a9bb1fdaa7a9e9b0266a518a1ee0d134f343adf5c7f056e20034d68aa67e`.

## Reconstruction of the decisive argument

For fixed \(n\), choosing a residue \(r_k\) eliminates precisely

\[
 E_{k,r_k}^{(n)}=\{m:k<m\le n+1,\ m\equiv r_k\pmod k\}.
\]

Consequently every profile produces the complement in \(X_n\) of
\(\bigcup_{k=2}^nE_{k,r_k}^{(n)}\), and every such union comes from a profile.
Starting with the empty union and adjoining every possible
\(E_{k,a}^{(n)}\) at stage \(k\), with exact deduplication, therefore enumerates
all and only of \(\mathcal F_n\). This proves the completeness of the finite
generation procedure by induction on \(k\); it is not a sampling argument.

For a fixed survivor \(A\), a choice \(a_k\in\Omega_k^+(A)\) neither eliminates
an element of \(A\) nor eliminates the prospective new point \(n+2\). It
realizes exactly \(A\) precisely when every omitted \(m\) is eliminated by at
least one lower modulus, which is the clause

\[
 \bigvee_{k\in W_A(m)}(a_k=m\bmod k).
\]

Thus the displayed finite CSP is equivalent to extendibility. The candidate's
clause solver is exhaustive: at an uncovered clause, a completion must use one
of its still-unassigned witnesses, and the solver branches over all of them.
The separate coverage DP is also exhaustive because, after modulus \(k\), its
states are exactly the coverage unions attainable from one allowed value for
each modulus through \(k\).

Exact enumeration gives no locally feasible nonextendible survivor for
\(1\le n<24\). The survivor counts for \(n=1,\ldots,24\) are

\[
1,2,3,4,6,8,11,14,17,22,30,38,50,63,76,89,117,147,192,237,288,349,451,553.
\]

Through \(n=23\), the CSP-extendible and locally feasible families are equal.
At \(n=24\), there are 113 extendible sets and 121 locally feasible sets; their
difference is exactly

\[
\{2\},\ \{2,8\},\ \{2,14\},\ \{2,20\},\
\{2,8,14\},\ \{2,8,20\},\ \{2,14,20\},\ \{2,8,14,20\}.
\]

The realizing profiles in `evidence/finite_result.md` directly establish that
all eight belong to \(\mathcal F_{24}\). Their local feasibility also has a
uniform human-readable certificate. For every such set,
\(\Omega_2^+=\{1\}\) and \(\Omega_3^+=\{0,1\}\). Odd omitted points use
residue 1 modulo 2; even omitted points congruent to 0 or 1 modulo 3 use that
residue modulo 3; and a possibly omitted 8, 14, or 20 uses respectively
residue 3, 4, or 0 modulo 5. These three modulo-5 residues are distinct and
also differ from \(26\bmod5=1\). The dossier separately gives one admissible
representative for every residue domain.

The shared conflict core is decisive. Since 4 is omitted, its only allowed
witness is \((3,1)\), so its clause forces \(a_3=1\). Since 6 is omitted, the
moduli 2, 4, and 5 offer respectively residues forbidden by 26 (and by the
domain restrictions), leaving only \((3,0)\); its clause forces \(a_3=0\).
The two clauses are incompatible. Hence all eight locally feasible survivors
are nonextendible.

## Independent checks performed

I inspected the frozen generator, CSP solver, independent replay, serialized
layer data, profiles, local witnesses, and core records. I then performed these
exact checks with the mandated interpreter
`/Users/mac/4prove-or-disprove-math/.research-venv/bin/python`:

1. Re-ran `evidence/find_first_incompatibility.py`. It reproduced all 24 layer
   totals and rewrote `evidence/first_incompatibility.json` byte-for-byte, with
   SHA-256
   `9aa3f366471bd31815492eebfdfc85f2fbaa975e4394ee1cf96bff283062857e`.
2. Re-ran `evidence/independent_audit.py`. Its set-based generator and coverage
   DP reproduced the same full survivor, extendible, and local families and
   rewrote its output byte-for-byte, with SHA-256
   `2c6f9a49fb3f236fca4f57c1c5bb7f6c67c6717ff7ac6342380c101a4bcf1035`.
3. Wrote and ran `audit/referee_replay.py`, which imports none of the candidate
   implementations. It generates survivors directly by repeated profile
   elimination, tests extendibility independently by membership of
   \(A\cup\{n+2\}\) in \(\mathcal F_{n+1}\), and separately decides the CSP by
   exact integer coverage states. For every survivor at every
   \(1\le n\le24\), the CSP decision equaled next-layer membership and the
   complete computed subfamilies equaled the frozen serialized subfamilies.
   It also regenerated \(|\mathcal F_{25}|=666\), the eight literal exception
   sets, and each displayed \(\{4,6\}\) core. Its output is
   `audit/referee_replay.json`.

I specifically checked the empty-product case \(n=1\), the fact that every
survivor contains 2 (so the empty witness set for an omitted 2 cannot be
silently ignored), strict inequalities \(k<m\) in elimination and coverage,
the restriction \(x>k\) in the residue domains, and the use of \(n+2\) rather
than \(n+1\). All computation is finite and exact; no floating-point inference,
solver heuristic, limiting exchange, or probabilistic completeness claim is
used.

## Contribution and source limitation

The nearest result identified in the frozen materials is the Raso--Venturi
recurrence and exact CSP criterion, together with its observation that local
conditions can have incompatible residue choices. The precise delta here is a
natural one: the first such layer, its complete exception family, and explicit
cores. It is not an arbitrary restriction or a routine one-line corollary; the
minimality and completeness assertions require exhaustive generation and a
global compatibility decision. The result supplies a concrete benchmark for
the boundary between the local conditions and the exact CSP.

The cited source PDF was not part of the frozen evidence available to this
referee, so I did not independently certify its bibliography, its exact printed
wording, or any broad priority claim. This is not silently upgraded to novelty:
the candidate already labels publication novelty `status-uncertain`, and this
audit preserves that limitation. The explicit finite theorem itself is
self-contained under `problem.md` and does not depend on a novelty assertion.

## Verdict

**ACCEPT** the exact frozen `result-note` scope. The finite theorem, first-layer
minimality, literal classification, local certificates, and nonextendibility
cores are correct and reproducible. The original asymptotic problem remains
unresolved, and broad publication priority remains unverified.
