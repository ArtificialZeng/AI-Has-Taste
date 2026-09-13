# Gate 5 counterexample-hunter report

## Scope and outcome

I independently attacked the stated real rank-`<=2` inequality for `n=3` and
`n=4`.  I found **no exact counterexample** in the searches below.  This is
negative computational evidence only; none of the finite or floating searches
covers the full real parameter space, so this report is not a proof.

No proof assistant was used.

## Parameterizations and exact objective

Two generic parameterizations were searched independently.

1. Bilinear factors: `T = u v^T + x y^T`, with independently sampled integer
   vectors.  This parameterization represents every real rank-at-most-two
   matrix (over the reals, with real factors).
2. The row/column-scale quotient chart `T_ij = 1 + a_i b_j`, sampled with
   integer `a,b`.  This is a generic chart, not a coverage claim for all
   boundary strata.

Two further boundary-oriented charts were used.

3. Forced `per(T)=0`: because `per(1+a_i b_j)` is affine in the final `a_i`,
   I solved that parameter exactly.  If `c0=per(T)|_{a_n=0}` and
   `c1=per(T)|_{a_n=1}-c0`, the final row was replaced by the integer row
   `(c1-c0*b_j)_j`.  Thus `per(T)=0` is an integer identity, not a floating
   tolerance.
4. Sparse gauge chart: the first two rows of the left factor are fixed to
   `(1,0),(0,1)`; the remaining left-factor rows and all right-factor rows are
   exhaustively enumerated over `{-1,0,1}`.

For the quotient chart there is also the exact binary-factor identity

```
per(1+a_i b_j) = sum_{k=0}^n k!(n-k)! e_k(a)e_k(b).
```

With each `a_i,b_j` repeated twice, the same expansion gives the permanent of
the duplicated block at order `2n`.  This identity is useful structurally, but
the adversarial floating search ultimately evaluated the small matrix entries
directly to avoid catastrophic cancellation in this expansion near
`1+a_i b_j=0`.

## Evaluators and certification discipline

The integer search score used exact Python integers with:

- Ryser inclusion-exclusion for `per(T)`;
- coefficient DP for the duplicated block, using
  `2^n [z_1^2...z_n^2] product_i(sum_j T_ij z_j)^2`.

Every retained exact best point was then recomputed by three mutually
different routes: definition/permutation enumeration, Ryser
inclusion-exclusion, and the repeated-row/column coefficient DP.  Exact rank
was computed over `Q`.

The standalone verifier `experiments/breaker_verify.py` imports no discovery
code.  From serialized matrices it reconstructs the literal `2n x 2n` block,
uses a row/mask permanent DP, independently performs rational Gaussian
elimination, and checks every recorded integer.  Its output is
`certificates/breaker_verification_results.json`; all eight retained exact
records verified.

## Searches

| `n` | route | seed | exact/float scale | result |
|---:|---|---:|---:|---|
| 3 | integer `uv` | 120034 | 200,000 trials, entries in `[-3,3]` | no positive `D` |
| 3 | integer canonical | 120035 | 200,000 trials, parameters in `[-5,5]` | no positive `D` |
| 4 | integer `uv` | 120036 | 100,000 trials, entries in `[-3,3]` | no positive `D` |
| 4 | integer canonical | 120037 | 100,000 trials, parameters in `[-5,5]` | no positive `D` |
| 3 | forced `per(T)=0` | 120038 | 200,000 durably logged exact trials; an earlier deterministic 1,000,000-trial run also had no positive `D` | no positive block permanent |
| 4 | forced `per(T)=0` | 120039 | 200,000 durably logged exact trials; an earlier deterministic 1,000,000-trial run also had no positive `D` | no positive block permanent |
| 3 | sparse gauge exhaustion | deterministic | `3^8 = 6,561` matrices | no positive `D` |
| 4 | sparse gauge exhaustion | deterministic | `3^12 = 531,441` matrices | no positive `D` |
| 3 | adversarial canonical | 120040 | 20,000 mixture-random points + DE 250 generations + Nelder-Mead | no exact positive |
| 4 | adversarial canonical | 120041 | 20,000 mixture-random points + DE 250 generations + Nelder-Mead | no exact positive |

Here `D = per([[T,T],[T,T]]) - binom(2n,n) per(T)^2`.

The floating optimizers converged to rank-one/equality-near regions and
reported tiny positive normalized values (`4.41e-15` for `n=3` and
`2.64e-26` for `n=4`).  These are roundoff diagnostics, not candidates.  The
logs serialize fixed-denominator-`10,000` integer reconstructions; exact
recomputation gives strict *negative* differences, respectively

```
-4403605354520845687173865989926720000000000000000
-107389953393578289082230689621312816109465600000000000000000.
```

Thus no floating value was promoted to a mathematical claim.

## Durable artifacts

- Search and exact-evaluator code: `experiments/breaker_search.py`
- Floating adversarial code: `experiments/breaker_optimize.py`
- Independent verifier: `experiments/breaker_verify.py`
- Integer logs: `experiments/breaker_random_*.json`,
  `experiments/breaker_zero_*.json`, `experiments/breaker_sparse_*.json`
- Adversarial logs: `experiments/breaker_optimize_*.json`
- Independent verification transcript:
  `certificates/breaker_verification_results.json`

No counterexample certificate file was produced because no strict exact
positive difference was found.

## Reproduction

```bash
python experiments/breaker_search.py --n 3 --mode uv --trials 200000 --bound 3 --seed 120034 --log experiments/breaker_random_n3_uv.json
python experiments/breaker_search.py --n 3 --mode canonical --trials 200000 --bound 5 --seed 120035 --log experiments/breaker_random_n3_canonical.json
python experiments/breaker_search.py --n 4 --mode uv --trials 100000 --bound 3 --seed 120036 --log experiments/breaker_random_n4_uv.json
python experiments/breaker_search.py --n 4 --mode canonical --trials 100000 --bound 5 --seed 120037 --log experiments/breaker_random_n4_canonical.json
python experiments/breaker_search.py --n 3 --mode zero --trials 200000 --bound 8 --seed 120038 --log experiments/breaker_zero_n3.json
python experiments/breaker_search.py --n 4 --mode zero --trials 200000 --bound 6 --seed 120039 --log experiments/breaker_zero_n4.json
python experiments/breaker_search.py --n 3 --mode sparse --bound 1 --log experiments/breaker_sparse_n3.json
python experiments/breaker_search.py --n 4 --mode sparse --bound 1 --log experiments/breaker_sparse_n4.json
python experiments/breaker_optimize.py --n 3 --seed 120040 --random-trials 20000 --de-maxiter 250 --bound 20 --log experiments/breaker_optimize_n3.json
python experiments/breaker_optimize.py --n 4 --seed 120041 --random-trials 20000 --de-maxiter 250 --bound 20 --log experiments/breaker_optimize_n4.json
python experiments/breaker_verify.py experiments/breaker_random_n3_uv.json experiments/breaker_random_n3_canonical.json experiments/breaker_random_n4_uv.json experiments/breaker_random_n4_canonical.json experiments/breaker_zero_n3.json experiments/breaker_zero_n4.json experiments/breaker_sparse_n3.json experiments/breaker_sparse_n4.json
```

## Referee caveats

- The canonical chart is noncompact and its finite boxes do not certify its
  complement.
- Random bilinear factors are not a finite cover of real factor space.
- Sparse exhaustion certifies only its explicitly enumerated gauge/alphabet
  class.
- The forced-zero search samples, but does not exhaust, the algebraic
  hypersurface `per(T)=0`.
- The best exact points in several searches lie on known rank-one/equality or
  zero-support strata; this makes maximization numerically deceptive.
- Therefore the only justified conclusion is “no counterexample found in the
  recorded scope.”
