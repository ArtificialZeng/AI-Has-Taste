# Proof dependency graph

The frozen claims have the following exact dependency structure.

```text
standard self-inversive coefficient normalization
                |
                +--> endpoint product disk (1.4) --> endpoint-max cases, all n
                |
                +--> boundary-preimage Lemma 1 --> Schur Lemma 2
                              |                         |
                              |                         +--> cubic boundary separation
                              |                         |        + derivative Schur bound
                              |                         |        + root-count homotopy
                              |                         |        --> complete n=3 theorem
                              |                         |
                              |                         +--> quartic/quintic nonzero-boundary separation
                              |                                  + zero off unit circle OR 2|a_n|>=A
                              |                                  --> partial n=4,5 theorems
                              |
quadratic normal form + product/boundary argument --> complete n=2 theorem

complete n=2 theorem + z -> z^m image identity --> even sparse support {0,m,2m}
endpoint product disk --> odd endpoint-binomial subclass
```

The open nodes Q4-U and Q5-U are not dependencies of any frozen claim.  The
CAS checker and the independently implemented sparse-Laurent checker verify
displayed algebraic identities only; the human proof supplies the analytic
boundary, Schur, and homotopy arguments.
