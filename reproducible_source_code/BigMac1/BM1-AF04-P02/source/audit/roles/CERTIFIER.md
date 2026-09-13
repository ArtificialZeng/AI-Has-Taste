# Certifier record

Date: 2026-08-30.

Certificate type: exhaustive finite combinatorial enumeration.

The decisive verifier is `code/independent_verifier.py`.  It imports only
Python standard-library modules, does not import `discover_graph.py`, and
does not invoke nauty.  It:

1. parses JSON with duplicate-key rejection;
2. checks 80 exact STS(15) representatives;
3. reconstructs all Pasches using cycle graphs;
4. verifies every switch and explicit target isomorphism;
5. reconstructs and compares the complete simple edge set;
6. runs all-pairs BFS and checks components, eccentricities, diameter
   pairs, the distance row, layers, and geodesic.

Observed success record: 80 vertices, 1,390 replayed Pasches, 258 edges,
component sizes 79 and 1, diameter 11, radius 6.  A second standalone BFS
verifier, `code/verify_bfs.py`, reports the same endpoint.
