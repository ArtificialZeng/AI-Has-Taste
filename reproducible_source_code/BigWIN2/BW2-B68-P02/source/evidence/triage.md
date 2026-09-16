# Triage evidence (2026-09-07)

Job provenance: `win-00068-p02-triage-d1807b413b58`.

## Literature inspected

1. Matheus Adauto, Celina de Figueiredo, Diana Sasaki, and Rafael Schneider,
   *Order 14 is the largest order for which every 4-total coloring of every
   cubic graph is equitable*, arXiv:2609.05259v1,
   <https://arxiv.org/pdf/2609.05259>. Retrieved 2026-09-07. Inspected abstract;
   pp. 2--8 (definitions, count, Lemma 3.1, Corollary 3.2, Theorem 4.1); and
   pp. 13--17 (Question 7.1, proposed census, certificates, references).
   Question 7.1 is exactly the existential assertion in `source.md`. The paper
   reports 45,982 connected cubic graphs below order 20 and explicitly suggests
   systematic verification over the catalogue through ILP or SAT. It does not
   answer Question 7.1.
2. House of Graphs, “Connected cubic graphs,”
   <https://houseofgraphs.org/Cubic>. Retrieved 2026-09-07. The displayed
   counts at orders 4,6,...,18 are `1,2,5,19,85,509,4060,41301`, summing to
   `45,982`, consistent with the cited paper. This is an authoritative database
   check, not yet an independently regenerated census.

Exact-assertion and equivalent-language searches found the September 2026
preprint above but no inspected primary source claiming a resolution of its new
Question 7.1. This is only a bounded literature screen, not proof of open status
or priority.

## Feasibility and obstacles

Local deterministic inspection found Python 3 with NetworkX 3.4.2, PySAT
1.8.dev24, and OR-Tools 9.14.6206. No `geng`, `genreg`, canonical-label utility,
standalone proof-producing SAT solver, DRAT/LRAT checker, or independent
certificate checker was on `PATH`. Thus SAT prototyping is immediately
available, but a resolution cannot rely on current local solver status alone.
The next phase must install or build pinned generator/proof-checker sources in
the project (or otherwise record reproducible binaries and hashes) before any
full-census result can qualify.

