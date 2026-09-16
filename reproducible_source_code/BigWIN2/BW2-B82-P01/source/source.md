# Source statement: decide \(\mathsf E(8,4)\)

Source id: ARXIV-2609.06724-B82

Primary source: Junyu Zhou, *Cyclic Incidence Orderings of Complete Graphs
and 3-Uniform Hypergraphs*, arXiv:2609.06724v1, Definition 1.1,
Lemma 2.2, Theorems 1.3--1.4, and Conjecture 7.1.

Local source PDF:
\`batches/inbox/bigWin-82-materials/2609.06724.pdf\`, SHA-256
\`38a3b52321916d3a7902dffd3e9c4872b2d013c871a8dda9217635f01153dc63\`.

## Frozen question

Let \(N=\binom84=70\). Determine whether there exist

1. a bijection \(e:\mathbb Z_{70}\to\binom{[8]}4\);
2. a template \(D\subseteq\mathbb Z_{70}\) of size \(35\); and
3. shifts \(s_v\in\mathbb Z_{70}\) for every \(v\in[8]\),

such that
\[
   \{t\in\mathbb Z_{70}:v\in e(t)\}=D+s_v
   \quad\text{for every }v\in[8].
\]
This existence statement is denoted \(\mathsf E(8,4)\).

Conjecture 7.1 predicts that it is false because \(\gcd(8,4)>1\), but the
conjecture is not an answer. Either a proof of nonexistence or a
definition-level valid ordering resolves the frozen question.

## Verified source boundary

The source proves that \(\gcd(n,k)=1\) is sufficient for
\(\mathsf E(n,k)\), proves necessity for \(k=2,3\), and gives complement
symmetry. These statements determine every case with \(n\le7\);
\((8,4)\) is the first parameter not covered by them. A proposed proof
must check whether it is more than an unpublished direct specialization
of Lemma 2.2 and must screen the cited single-track/cyclic-factorization
literature before making any novelty claim.

## Required verification route

Use the source's shift congruence to derive, rather than assume, the
reduction to a ten-element quotient. Exhaust the reduced slice templates
and independently reconstruct all seventy candidate columns. A negative
computational branch needs a complete orbit table or a frozen CNF with a
checked LRAT/DRAT proof; a bare UNSAT return is insufficient.
