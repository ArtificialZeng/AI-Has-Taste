# Precise problem and triage scope

Provenance: `bigMac-00015-p01-triage-4574f58c90d8`, 2026-09-08.
The verbatim original is `source.md`, which is immutable. Its initial SHA-256
is recorded in `evidence/source.sha256`. No corrections to its claim are needed.

For every integer n >= 2 and every monic irreducible polynomial p in F_2[t]
of degree n, let F = F_2[t]/(p) and alpha = t mod p. Identify F_2^n with F
by the linear map phi(x) = sum_{i=0}^{n-1} x_i alpha^i. Define
J_{n,p}(0) = 0 and J_{n,p}(x) = phi^{-1}(phi(x)^{-1}) for x != 0.
Write e_i for the ith standard coordinate vector, indexed from zero.

The input consists of n^2+n independent Boolean variables
V = {p_{ij}: 0 <= i,j < n} union {u_j: 0 <= j < n}.
Here p_{ij} denotes a matrix entry and is distinct from the polynomial p.
For every P in Mat_n(F_2) and u in F_2^n, define
G_{n,p}(P,u) = adj(P) J_{n,p}(Pu), where
adj(P)_{ab} = det(P with row b and column a deleted).
All operations are over F_2. Singular P are included, using the adjugate,
not an inverse, and no alternative extension from GL_n is allowed.

In the Boolean ring F_2[V]/(v^2-v : v in V), write the unique vector ANF
G = XOR_{A subset V} c_A product_{v in A} v, with c_A in F_2^n.
Equivalently c_A = XOR_{C subset A} G(1_C). Define
S = {A subset V : c_A != 0} and s = |S|. The map is nonzero since
G(I,u)=J_{n,p}(u), and c_empty=0. A support is counted once even if it
appears in multiple output coordinates. Set

L(G) = min over all permutations (A_1,...,A_s) of S of
       max_{1 <= j <= s} |A_j minus union_{i<j} A_i|.

The target is the universal equality L(G_{n,p}) = n. The ordering can depend
on n and p. Neither a single modulus nor a restriction to nonsingular P
settles the claim. General ordered bases are outside the frozen target.

The nearest inspected result is Zhang and Zhang,
[arXiv:2609.04583v1](https://arxiv.org/html/2609.04583v1): Definition 11
and Proposition 12 (printed p.11), Definitions 13–14 (pp.11–12), and
Theorem 17 (pp.14–15). These give the same Boolean extension,
deg(G) <= 3(n-1), and |A| >= n for every supported A, hence L(G) >= n.
Table 1 is on printed p.18, following the experimental description on p.17;
Appendix A.3 and Tables 7–8 (pp.27–28) give explicit n=3,4 certificates.
These numerical examples do not quantify over every irreducible modulus.

Source status: new-question / status-uncertain for this exact universal
refinement. The inspected paper proposes general raw ANF values as future
work; the bounded literature search did not establish priority or certified
open status. See `evidence/triage-literature.md`.

Proposed delta: a uniform explicit support-ordering prefix establishing the
matching upper bound n. Verification route: exploit sparse rank-(n-1)
partial permutation matrices, use the exact coefficient formula to certify
the prefix, and show that only one matrix row remains unseen. A promising
general derivation is recorded separately in `evidence/cyclic-prefix.md`;
it is a research handoff, not a mathematical acceptance decision.
