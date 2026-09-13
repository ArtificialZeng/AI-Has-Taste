# Final status

**Terminal state: `CERTIFIED_FINITE_RESULT`**

## Conclusion

The undirected simple Pasch-switch quotient graph on the 80 isomorphism
classes of STS(15) has 258 edges and two components of orders 79 and 1.
The 79-vertex component has

\[
\boxed{\operatorname{diam}=11}, \qquad \operatorname{rad}=6.
\]

The singleton is the unique anti-Pasch class (`V036`) and has diameter 0.
Exactly two unordered pairs attain distance 11 in the released canonical
numbering: `V000`--`V006` and `V000`--`V028`.

One certified geodesic is

`V000–V047–V002–V027–V054–V018–V035–V037–V066–V014–V023–V006`.

## Certificate and independent audit

The release contains all 80 representatives, all 1,390 Pasch occurrences,
the complete 258-edge list, all components and eccentricities, the diameter
pairs, a geodesic, a complete distance row, and BFS layers. The decisive
verifier uses a different Pasch enumerator from discovery, invokes no nauty,
constructs explicit Steiner-quasigroup isomorphisms for every target, and
rebuilds the full graph before BFS. A second standalone BFS verifier agrees.
Six mutated certificates are all rejected.

## Reproduction

```sh
python3 code/independent_verifier.py certificate
python3 code/verify_bfs.py
python3 tests/test_verifier_rejects.py --output certificate/negative_tests.json
python3 code/verify_published_baseline.py
cd paper
latexmk -C main.tex
latexmk -pdf -interaction=nonstopmode -halt-on-error main.tex
```

## Limitations and novelty wording

The computation does not reprove the classical theorem that there are
exactly 80 STS(15) isomorphism classes; it validates the released systems,
proves them pairwise nonisomorphic, and exactly binds their canonical set to
the official complete catalogue. The priority statement remains bounded:
the recorded two-pass search did not locate a publication stating diameter
11, although the complete 1999 switch table contains enough prior data to
derive it.

No proof assistant was used. No floating point, randomness, or optimizer
enters the decisive computation.

The manuscript, BibTeX, clean build, metadata, all five rendered PDF pages,
source package, and manifest have been audited. Author: Zijian Zeng; the
affiliation and both required emails agree in LaTeX, PDF body, and metadata.
