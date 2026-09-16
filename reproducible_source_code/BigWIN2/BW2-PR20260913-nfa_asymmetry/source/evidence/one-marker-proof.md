# Exact directional separation for words with one marker

Proposer: primary-20260913-nfa-asymmetry-research-71ec4a8ef3d7.
Date: 2026-09-13 Asia/Shanghai. Research proof submitted for fresh review;
this document is not an independent referee report.

## Statement and relation to the original question

Use precisely the partial, epsilon-free binary NFA convention of `problem.md`:
one initial state, any accepting subset, and a nonempty finite state set.
For distinct words w,x, let nsep(w,x) minimize the number of states of an NFA
accepting w and rejecting x, with arbitrary behavior on every other word.

For each integer q>=3, define

    A_one(q) = max { nsep(0^a 1 0^b, 0^c 1 0^d) :
        a,b,c,d are nonnegative integers, a+b=c+d, a!=c,
        nsep(0^c 1 0^d, 0^a 1 0^b)<=q }.

**Theorem.** For every integer q>=3,

    A_one(q) = (q-1)^2+2.

All word lengths are included. The proof below establishes a uniform upper
bound and constructs an attaining pair, so the displayed maximum exists.
As a corollary, the unrestricted quantity in `source.md` satisfies
A(q)>=(q-1)^2+2. Its asymptotic growth is not determined here. The substantive
scope is the exact optimum on the entire one-marker class, not the additive
one-state improvement alone.

## Classical dependency and elementary period argument

For n>1 write H_n=(n-1)^2+1 and L_n=lcm(1,...,n). Products and powers of
Boolean matrices use OR and AND; R^0 is the identity relation.

**Imported index bound (Schwarz).** For every binary relation R on n>1
points, its powers are periodic starting at some index at most H_n.
Equivalently, R^(H_n) belongs to the periodic group of the powers of R.

This precise all-relations statement is given by Schwarz himself in
*Sums of Powers of Binary Relations* (1974), printed p.167, proof of Theorem 3,
Case 1, with a pointer to his 1970 paper, p.653. The periodic-group definition
is on printed p.161. This account explicitly includes reducible relations.
The original 1970 proof has not been inspected in this pass; the 1974 account
and its rendered statement were inspected. Zajac-Jokay (2012), Theorem 1,
printed p.1331, independently reports the same universal index. Their printed
Definition 1 has a typographical error and is not used. These are classical
dependencies, not results claimed as new here.

Here is a direct argument for the precise period we need, avoiding reliance
on Zajac-Jokay's separate partition-period formula. A directed walk of length
t>=n has a repeated vertex and contains a simple directed cycle of length
h with 1<=h<=n. Insert L_n/h extra traversals of that cycle. Its endpoints
are unchanged and its length increases by L_n. Therefore

    R^t is contained in R^(t+L_n), for every t>=n.

Since H_n>=n for n>=2, fix any t>=H_n. By the imported theorem, there is a
positive period d with R^(t+jd)=R^t for every nonnegative integer j.
Consequently the inclusion chain

    R^t <= R^(t+L_n) <= ... <= R^(t+d L_n) = R^t

forces equality throughout. We have proved the identity used below:

    R^(t+L_n) = R^t, for every t>=H_n.                 (1)

In particular, exponents at least H_n that are congruent modulo L_n give
the same relation. Padding an NFA with unreachable isolated states allows
the identity for n=q to apply to any NFA with at most q states.

## Upper bound

Fix an admissible ordered pair w=0^a 1 0^b and x=0^c 1 0^d.
Let H=(q-1)^2+1, L=lcm(1,...,q), and Delta=a-c. Thus Delta!=0 and b-d=-Delta.
An NFA with at most q states accepts x and rejects w by admissibility.

**Case 1: L does not divide Delta.** Some r in {2,...,q} does not divide
Delta, since otherwise their least common multiple would divide it. Build
an r-state directed zero-cycle with initial residue 0. Add a new final state f
with a zero-loop. Only the cycle state of residue a modulo r has a one-edge,
which leads to f. All other edges are missing, and f is the sole final state.
This NFA accepts w and rejects x because a and c have different residues.
It has r+1<=q+1<=H+1 states. This also covers a=0 or b=0.

**Case 2: one of a,b,c,d is less than H.** First suppose k=min(a,c)<H.
The words first differ immediately after their common prefix 0^k.
If the word to be accepted has the earlier marker, use states 0,...,k and f,
zero-edges j->j+1 for j<k, a one-edge k->f, and a zero-loop at f.
Start at 0, accept only at f, and omit every other edge. The later-marker
word dies when it reads zero at state k. If the word to be accepted has the
later marker, use states 0,...,k+1, zero-edges j->j+1 for j<=k, and both loops
at state k+1. Start at 0 and accept only at k+1. The earlier-marker word dies
on its marker. In either orientation the state count is k+2<=H+1.

If instead k=min(b,d)<H, apply those prefix constructions to w reversed and
x reversed. Each constructed NFA has exactly one final state. Reverse every
edge, use that sole final state as the new initial state, and use the old
initial state as the sole final state. Reversing paths verifies both acceptance
and rejection, preserves the state count, and keeps one initial state. Thus
every short-block case is covered, including empty suffixes.

**Case 3: L divides Delta and all four exponents are at least H.** Let B,C
be the zero and one relations in the assumed at-most-q-state separator, padded
to q states. By (1), B^a=B^c and B^b=B^d. Hence

    B^a C B^b = B^c C B^d.

The two words induce identical relations and therefore cannot be separated
by any initial or accepting states on this graph, a contradiction.

The cases exhaust all possibilities, and in every feasible case the requested
orientation has a separator with at most H+1 states. This proves
A_one(q)<=(q-1)^2+2.

## Lower bound and attainment

This part is elementary and does not use the imported index bound. Set

    s=q-1 >=2, M=s^2, T=2^(M+1), P=lcm(1,...,T),
    u=0^M 1 0^(T+P), v=0^(M+P) 1 0^T.              (2)

Both words have length M+T+P+1, contain exactly one marker, and are distinct.
The following argument strengthens Nicol's Theorem 6, which excludes only
at-most-M-state separators and uses T=2^M. The larger T in (2) covers M+1
states as well.

Suppose an NFA with m<=M+1 states accepts u, and choose an accepting path

    i --0^M--> p --1--> z --0^(T+P)--> f.

If its first segment repeats a vertex, that segment contains a simple zero-cycle
of some length h<=m. If it has no repeated vertex, it visits M+1 distinct
vertices, so m=M+1 and it visits every state of the NFA. The final segment,
whose length exceeds m, contains a simple zero-cycle; a vertex on that cycle
then occurs on the first segment. In both cases, a vertex of the first segment
supports a directed zero-cycle of length h<=m. As h<=M+1<=T, h divides P.
Inserting P/h traversals at that vertex gives a path i --0^(M+P)--> p.
The cycle need not originally have been traversed in the first segment.

Let S_j be the subset reachable from z by exactly j zeros, starting at S_0={z}.
The update S_j -> S_(j+1) is a deterministic function on at most 2^m<=T subsets.
Among S_0,...,S_T some pair S_i=S_j has i<j<=T. Hence, from time i onwards,
the sequence has period c=j-i with 1<=c<=T. Since c divides P and T>=i,

    S_T = S_(T+P).

The old accepting state f belongs to S_(T+P), hence also S_T. Combining this
shortened suffix with the extended prefix and the same one-edge yields an
accepting path on v. Thus no NFA with at most M+1 states accepts u and rejects v.
Conversely, the early-marker chain in Case 2, with k=M, accepts u and rejects v
with M+2 states. Therefore

    nsep(u,v)=M+2.                                      (3)

For the opposite orientation, use Nicol's q=s+1-state graph. Its states are
0,1,...,s, the zero-edges are j->j+1 for j<s and s->0, s->1, and its only
one-edge is the loop at 0. State 0 is both initial and the sole final state.

A positive zero return to 0 has length exactly

    a s + b(s+1), with a>=0 and b>=1.                    (4)

Indeed, each return uses the (s+1)-cycle, and between departure and return one
may traverse the s-cycle through 1,...,s any number of times. Multiple returns
give precisely (4), and every choice of a,b can be realized. In the residue
represented by r in {1,...,s} modulo s, the least positive return length is
r(s+1); all subsequent lengths in that residue are obtained by adding s.
The largest excluded nonnegative length in that residue is r(s+1)-s.
For s>=2 these numbers are positive, and their maximum is s^2=M.
Thus M is not a return length and every length greater than M is a return length.

The graph rejects u because the only one-edge is at 0 and M is not a return
length. It accepts v because M+P>M and T>M. Hence nsep(v,u)<=q. Together
with (3), this provides an admissible pair attaining (q-1)^2+2 and proves
the theorem.

## Dependency and gap record

The only non-elementary dependency is the classical all-relations index bound,
used for the upper bound. It has been checked in an authoritative primary
account, including its exact scope and exponent. No new proof of that classical
theorem is claimed. The lower argument, its extra-state step, the separator
constructions, and the period consequence are proved above in full.

Known mathematical gaps in this submitted statement: none identified by the
proposer. Independent mathematical review and evaluation of novelty/value are
pending. Finite checks in `research-checks.json` are diagnostics, not an
infinite proof or independent referee certification. The original unrestricted
asymptotic question remains unresolved.
