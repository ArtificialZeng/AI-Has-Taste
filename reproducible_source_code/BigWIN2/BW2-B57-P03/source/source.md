# Frozen source — win-00057-p03

## Problem

Audit and settle the complexity of the following first unsolved operation-count boundary from the cited model:

```text
J2 | res^t 111, p_ij=1, m_j<=3 | C_max.
```

There are two dedicated machines. Each job has at most three unit-time operations in a prescribed route (a machine may be revisited). There is one unit-capacity auxiliary resource; every operation of a given job has the same binary requirement `R(J_j) in {0,1}`. Operations of jobs with requirement one cannot overlap. The objective is minimum makespan.

Decide whether this problem is polynomial-time solvable or strongly NP-hard. First resolve a possible model-inclusion issue: the source explicitly permits jobs with resource requirement zero and cites strong NP-hardness of the unconstrained `J2|m_j<=3|C_max`. Determine rigorously whether setting every requirement to zero is a valid restriction. If a nondegeneracy convention requires at least one resource-using job, determine whether a bounded dummy-job transformation preserves the reduction.

## Primary source and contribution boundary

- Nour Elhouda Tellache and Abdenour Azerine, *Minimizing the makespan in job shop scheduling under conflict graph constraints*, arXiv:2609.04161v1, notation on PDF pp.1--2, Theorem 2/Corollary 1 and the following open-status sentence on p.6: https://arxiv.org/abs/2609.04161
- The paper proves the at-most-two-operation case polynomial and says the unrestricted unit-processing-time case remains open. Its literature section also cites NP-hardness of `J2|m_j<=3|C_max`.
- Proposed delta: a precise correction or first boundary theorem. If the reduction is immediate under the printed definitions, state that honestly and audit the cited NP-hardness source before treating it as publishable.

## Cheapest decisive test and certificate

Write the parameter inclusion as an explicit instance map and prove feasibility/makespan equivalence in both directions. Check whether the notation or cited source imposes a positive-use condition absent from the prose. A counterexample to the map is any legal base instance whose image violates a stated resource-model requirement.

## Provenance

Primary PDF: `batches/inbox/bigWin-57-materials/2609.04161.pdf`, SHA-256 `295cf1d99d1c439f3df33f36e236aea79d49e0ae2257c5bd30cf3fa5f4504ef3`.
