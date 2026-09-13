# Exact experiments

## Order-31 exhaustive checker

`order31_checker.c` is an independent exact evaluator attached to nauty's
`gentreeg` generator.  It reconstructs the unordered child lists from each
parent array, evaluates the two rooted states in recursive postorder, tests
weak unimodality and log-concavity, and emits order-independent hashes.

Build:

```bash
sh experiments/build_order31_checker.sh
```

One small exact run:

```bash
experiments/gentreeg_order31_checker -q 20 >results/order20_exceptions.txt \
  2>results/order20_summary.txt
```

No order-31 conclusion is certified until all declared chunks have completed,
their counts equal OEIS A000055(31) = 40,330,829,030, every chunk reports zero
non-unimodal trees, and the aggregation plus independent small-order evaluator
tests pass.
