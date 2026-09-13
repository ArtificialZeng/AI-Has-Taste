# Certifier record

## Serialized input

`certificates/trees_n2_n9.json` contains exact integer edge lists, AHU
canonical codes, triangle-reconstruction codes, degree sequences, and full
per-element circuit-size incidence signatures for every order 2--9 tree.

## Discovery/certification separation

- Discovery generator: NetworkX `nonisomorphic_trees`.
- Independent verifier: Python standard library only; does not import the
  discovery module or NetworkX.
- Completeness mechanism: enumerate every Prüfer word at each order, decode it
  to a labelled tree, and compare the complete set of AHU free-tree codes with
  the serialized set.
- Decisive quantities are recomputed from edge lists, not trusted from the
  certificate.

## Successful verifier run

- Certificate SHA-256:
  `5be053e1f8e676769ad33237055bed21c76f9825fd373f7832fb2d21dc414fe6`
- Verifier SHA-256:
  `6a4b61fc2fe3bcbd0caec0e3cdb8049eecd36034349ffc798f223019cfb431b4`
- Counts: `1,1,2,3,6,11,23,47` for orders 2 through 9.
- Runtime observed: 48.35 seconds wall, deterministic and seed-free.

## Fail-closed tests

The verifier rejected six mutations: a missing order-nine tree, a duplicate
tree, a loop, a forged reconstruction code, a forged circuit-incidence
signature, and an unexpected schema field.
