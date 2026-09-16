# Triage evidence

Retrieval/inspection date: 2026-09-07 (Asia/Shanghai).

## Primary literature inspected

1. Lei Zhang and Jianhua Tu, *Stability of independence polynomials of
   spiders*, arXiv:2609.04694v1 (submitted 2026-09-04), official abstract
   <https://arxiv.org/abs/2609.04694> and attached official PDF
   `external/2609.04694.pdf`. PDF SHA-256:
   `fb1940a98c1cc1ec1e5ba479871431244090771b2b6ce3fa7c72dc888c6c4d82`.
   Inspected: abstract; pp. 1--2, especially Theorem 2, the paragraph immediately
   before Definition 3, Definition 3, and Theorem 4. The paper defines closed
   left-half-plane stability, reports the prior computation through 20
   vertices, and proves that all spider roots have strictly negative real part.
2. Jason I. Brown and Ben Cameron, *On the Stability of Independence
   Polynomials*, Electronic Journal of Combinatorics 25(1) (2018), #P1.46,
   publisher PDF
   <https://www.combinatorics.org/ojs/index.php/eljc/article/download/v25i1p46/pdf/>.
   Inspected: pp. 1--3 (definitions and Hermite--Biehler criterion), p. 7
   (reported computations for trees through 20), and p. 17 (Problem 4,
   characterization of stable trees). This is a nearest prior result, not a
   resolution of the order-21 question.

Exact-assertion and equivalent-language web searches on the inspection date did
not locate a primary source giving a complete stability census for 21-vertex
trees. Because the search was bounded and the source problem was formulated
only days after arXiv v1 appeared, this supports only the label
`new-question/status not independently settled`, not a novelty or priority
claim.

## Enumeration cross-check

OEIS A000055, <https://oeis.org/A000055> (inspected 2026-09-07), defines the
sequence as the number of trees with `n` unlabeled nodes and lists
`a(21)=2144505`. A research sweep must reproduce this total and demonstrate
one representative per isomorphism class; citing the sequence alone is not a
completeness certificate.

## Local feasibility check

NetworkX 3.4.2, SymPy 1.14.0, NumPy 2.2.6, and SciPy 1.15.3 are available.
No executable `geng`, `nauty-geng`, `dreadnaut`, Sage, or WolframScript and no
Python igraph or pynauty module was found. A transient Python benchmark used
`networkx.generators.nonisomorphic_trees`, integer polynomial convolution for
the standard include/exclude tree recurrence, and rational Routh tables. It
gave:

| order | generated | strictly Hurwitz | elapsed seconds |
|---:|---:|---:|---:|
| 10 | 106 | 106 | 0.011146 |
| 12 | 551 | 551 | 0.075607 |
| 14 | 3159 | 3159 | 0.567039 |
| 15 | 7741 | 7741 | 1.530947 |
| 16 | 19320 | 19320 | 4.423325 |

The generated counts agree with A000055 in these tested orders. This benchmark
was a tractability check only. It did not cover order 21, prove generator
completeness, independently recompute certificates, or address singular Routh
tables under closed-half-plane stability.
