# Frozen source — win-00074-p02

## Exact claim to prove or disprove

Let `K` be any field and, for every integer `c>=2`, set

`I_c=(x^2,y^2,z^c,xyz) subset K[x,y,z]`.

Let `overline(I_c)` denote the integral closure and let `v(J)` be the v-number used in Biswas–Mandal–Phukan: the least degree of a homogeneous `f` for which `(J:f)` is an associated prime of `J`.

Prove or disprove the simultaneous formulas

`v(I_c)=2` and `v(overline(I_c))=ceil(c/2)` for every `c>=2`.

If true, record the exact comparison: `v(overline(I_2))<v(I_2)`, equality for `c=3,4`, and `v(I_c)<v(overline(I_c))` exactly for `c>=5`. The original formula, including all endpoints, is frozen; a proof of only `c=5` is a rediscovery.

## Nearest theorem and contribution boundary

Prativa Biswas, Mousumi Mandal and Partha Phukan, *A comparison of the v-number of a monomial ideal and its integral closure*, arXiv:2609.05044v1, Theorem 3.2 proves the comparison in two variables. Example 3.3 gives only `I_5=(x^2,y^2,z^5,xyz)` with `v(I_5)=2<v(overline(I_5))=3`. The proposed delta is the exact infinite one-parameter classification and the sharp first reversal at `c=5`.

Primary PDF: `batches/inbox/bigWin-74-materials/2609.05044v1.pdf` (SHA-256 `e8ba90b5273578389918379df6e5b66fc899825ddb3b66dcb0f866f04e1561ab`).

## Required first test

Derive the Newton-polyhedron lattice criterion rather than infer it from finitely many cases. Then list the minimal-degree socle monomials of both ideals and independently enumerate `2<=c<=20`. Distinguish a universal proof from the finite check.
