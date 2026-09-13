# Gap ledger

| ID | Proposition/location | Missing step originally identified | Repair and evidence | Status |
|---|---|---|---|---|
| G01 | Baseline completeness through weight 19 | Reproduce the external computational artifact locally. | The exact R526 source was replayed; the seven representatives, rank 48, and matrix SHA-256 agree (`results/baseline_through_19.json`). | closed |
| G02 | Completeness through weight 20 | A solver's terminal UNSAT response is not an independent certificate. | Replaced it by the seven-fiber exhaustive manifest; the no-import verifier independently reconstructed all 1,209,813 normalized vanishing tuples and found zero unblocked tuples. | closed |
| G03 | Blocker sufficiency | All affine images of every lower minimal orbit must be present. | The verifier expands all 5,040 affine transformations of each serialized representative, checks orbit sizes and disjointness, and obtains exactly 1,331 distinct blockers. | closed |
| G04 | Exact vanishing model | Discovery and verifier could share a cyclotomic bug. | Discovery uses SymPy polynomial remainders; the verifier uses standard-library recursive monic division and recurrence. Both produce matrix SHA-256 `669ac026...2744`. The fiber calculation independently uses \(\Phi_{15}\). | closed |
| G05 | Candidate minimality | Every nonempty proper subset of each survivor must be excluded exactly. | Discovery used a Gray scan; the verifier separately uses meet-in-the-middle integer vector sums for all nine representatives. | closed |
| G06 | Affine orbit completeness | Translation normalization or orbit blocking might omit/duplicate a class. | Every nonempty set has a translate containing 0. The verifier checks canonicality, pairwise orbit disjointness, orbit sizes, and stabilizers under all 5,040 affine maps. | closed |
| G07 | Novelty at release | Gate 1 predates the newly known representatives. | Targeted second-pass searches for both exact representatives, conductor 105, weight 20, and later citations/code are recorded in `literature/search_log.md`. | closed |

No fatal or major gap remains.
