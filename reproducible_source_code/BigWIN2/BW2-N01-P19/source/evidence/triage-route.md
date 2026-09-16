# Triage audit of the proposed cutoff route

Job `newwin-00001-p19-triage-624bca8c0b20`; 2026-09-12.
Decision: admit to research. These are checked derivations and reproducible
finite tests, not a new resolution-paper candidate or independent referee report.

## Positive-remainder membership

For n>=1 and integer r>0, the handoff proposes the equivalence

    r in S_2(n)
    iff there exist q>=3 and a prime p<q such that
        (q+1)r <= n-q and pq divides (q-1)n+r.                 (1)

The forward argument checks as follows. Write n=qk+r with k in S_1(n)
and 0<r<k. If n=a*ell+k witnesses k in S_1(n), then ell>k, a>=2,
and n>=3k+2; hence q>=3. Choose a prime p dividing a. The integer
(n-k)/p >= ell > k, so p < n/k-1 = q-1+r/k < q. Moreover,
q(n-k)=(q-1)n+r, giving the divisibility in (1). The bound r+1<=k
is equivalent to (q+1)r<=n-q.

Conversely (1) implies q|(n-r). Set k=(n-r)/q, so k>=r+1.
The divisibility by pq implies p|(n-k), including when p divides q;
no cancellation modulo a nonunit is used. Set ell=(n-k)/p.
Since p<=q-1 and r>0, n-k=(q-1)k+r>pk, so ell>k.
Also ell<=n/2. Thus n mod ell=k, which puts k in S_1(n), and
n mod k=r. This handles integrality and both endpoint inequalities.
Zero is excluded from (1) and contributes at most one to s_2(n).

## Finite cutoff and counting

Let T_Q(n) be the number of positive r supplied by (1) with q<=Q,
for integer Q>=3, and set

    L_Q = lcm{pq : 3<=q<=Q, p prime, p<q}.

If an r in S_2(n) is missing from the truncated union, each available
witness has q>=Q+1, giving r<n/(Q+2). Consequently

    0 <= s_2(n)-T_Q(n) <= floor(n/(Q+2))+1.                 (2)

Fix n congruent to b modulo L_Q. For each residue a modulo L_Q let
w_b(a) be the least q in [3,Q] satisfying the congruence for some p<q,
or infinity if none. The endpoint

    H_q(n)=floor((n-q)/(q+1))=floor((n+1)/(q+1))-1

decreases as q increases. Thus a residue with first witness q contributes
exactly its positive representatives up to H_q(n). If A_q(b) is the number
of such residue classes, the coefficient is

    C_Q(b) = sum_(q=3)^Q A_q(b)/(L_Q*(q+1)).                (3)

The class-count error relative to H_q(n)/L_Q is at most 1 and
|H_q(n)-n/(q+1)|<2. Summing over at most L_Q classes gives the useful
explicit estimate, for n>=Q in the fixed progression,

    |T_Q(n)-n*C_Q(b)| <= L_Q+2.                            (4)

In particular the O(1) is uniform in n with Q fixed. Equations (2)–(4)
are the bridge from the finite arithmetic to subsequence bounds, and should
receive explicit attention in the subsequent complete proof/referee pass.

## Zero-class first witnesses and densities

When b=0, eligibility is simply pq|r. If a witnessing q is composite and
has a prime divisor ell different from p, the earlier witness
(q',p')=(max(p,ell),min(p,ell)) works. If q is a pure power of p,
the witness reduces to q'=p^2 because p^3|r. Thus the first eligible q is
either a prime or a prime square. More precisely, it is the minimum of
the second-smallest distinct prime factor of r (if present) and all p^2
for which p^3|r. Missing candidates are infinity.

For first witness a prime ell, exactly one prime p<ell divides r.
If p^2<ell, its exponent must be 1 or 2; otherwise any positive
exponent is allowed. The factor ell occurs with positive exponent, and
all other primes below ell are absent. With P_t=product_(a<t prime)(1-1/a),
CRT gives

    d_ell = (P_ell/ell) * sum_(p<ell prime) h(p,ell),
    h(p,ell) = 1/p+1/p^2 if p^2<ell, and 1/(p-1) otherwise.

For first witness p^2, one needs p^3|r and no other prime below p^2;
therefore d_(p^2)=P_(p^2)/(p^2*(p-1)). These factors agree with the handoff.
The independent verifier does not implement those displayed formulas.
It propagates exact CRT weights for prime valuations 0, {1,2}, and >=3,
tracking the smallest present prime and earliest witness. For p^2>Q the
last two valuation cases are merged. The required prime powers divide L_Q,
so the resulting probabilities are finite-period densities, not a heuristic
probabilistic model of n.

## New reproducible evidence and target bounds

Run `python3 evidence/triage_verify.py > evidence/triage-verification.json`.
The separate implementation uses only exact integers and Fraction arithmetic:

- Literal-set equality with (1) for every n=1,...,2048 (523,776 tested positive
  candidate pairs, plus comparison with the whole literal positive set).
- First-witness classification against direct pq-divisibility for every
  r=1,...,100000 at Q=50.
- Full residue scans at Q=10 for b=0,1; for b=0 every first-q density also
  matches the valuation-state computation.
- Exact zero-class valuation-state calculation at Q=50, agreeing with the
  handoff's constants. This does not enumerate all residues modulo L_50.

The recomputed values are

    L_10 = 75600,
    beta = C_10(1) = 1182869/9979200,
    L_50 = 691374732709966591241323368000,
    C_50(0) = 6191714756605250456368/69244275641746488908625,
    alpha = C_50(0)+1/52
          = 30093341768093808664597/276977102566985955634500,
    beta-alpha
          = 131410063319607383019139/13294900923215325870456000 > 0.

The proposed progressions are n_t=L_50*t and m_t=75600*t+1, t>=1.
The checked route (1)–(4), with the zero-class densities, supplies the desired
limsup upper bound alpha and liminf lower bound beta. No broken step was
found at triage, and this is a nontrivial route to the original j=2 problem.
Full proof assembly, artifact freezing, and fresh mathematical review remain
research/referee work; these finite tests alone do not prove nonconvergence.

One next test: turn (4) into an explicit finite-n separation certificate for
the two progressions, with a common integer t_0 and all floor/zero errors
included; verify the rational inequality controlling t_0, then freeze the
smallest complete j=2 claim for a fresh referee. Do not restart with scatterplots.
