# Order-31 tree independence-sequence certificate

This archive accompanies *Tree independence sequences are unimodal through
order 31*.  It certifies the finite statement that every tree on exactly 31
vertices has a weakly unimodal independent-set sequence.  It does not prove
the unrestricted Erdős #993 conjecture.

## Exact result

- residue classes completed: `120/120` (fixed modulus 120)
- unlabelled trees generated and checked: `40,330,829,030`
- non-unimodal sequences: `0`
- non-log-concave sequences: `159` (all independently rebuilt and unimodal)
- coefficient fingerprint modulo `2^64`: `92f46f1b00c219ad`
- parent-array fingerprint modulo `2^64`: `d53b120ed8c90b52`

All decisive counts and coefficient comparisons use exact integer arithmetic.
For order 31, every coefficient and intermediate counting accumulator is at
most `binom(31,15) = 300,540,195`, and its square is
`90,324,408,810,638,025 < 2^64 - 1`.

## Frozen inputs

- checker source SHA-256:
  `38fad81aaae42ab4fe4d764abd03482535b54483aa308b9b6ce924d8edd4db36`
- production checker SHA-256:
  `93a463c656872a4e977390fcae8110cbcd558570bf06a8b78e628dad7752c00e`
- nauty 2.9.3 archive SHA-256:
  `9fc4edae04f88a0f5883985be3b39cf7f898fd6cc96e96b9ee25452743cc1b5b`

The release-level `MANIFEST.sha256.json` binds every file in this archive
except the manifest itself.

## Verification

Run from the extracted archive root:

```sh
python3 audit/order31_independent_aggregate.py
python3 audit/fail_closed_rejection_tests.py
sh audit/rebuild_order31_checker.sh
```

The first command is a no-project-import verifier.  It requires all 240
completed chunk files, rejects unexpected completed-file names, aggregates all
120 residue classes, and reconstructs the 159 serialized exceptions with
Python integers.  The second command materializes four independent corruptions
and requires a nonzero rejection for each.  The third command extracts the
frozen nauty archive in a fresh temporary directory, rebuilds release and
debug checkers, reproduces an order-23 residue count and both fingerprints,
and directly enumerates all vertex subsets for all 436 unlabelled trees
through order 11.

The production aggregate can also be reproduced with:

```sh
python3 experiments/aggregate_tree_sweep.py \
  --order 31 --modulus 120 --expected 40330829030 \
  --results-dir results/order31_sweep --project-dir .
```

To rebuild the manuscript in a clean directory:

```sh
cd paper
pdflatex -interaction=nonstopmode -halt-on-error main.tex
bibtex main
pdflatex -interaction=nonstopmode -halt-on-error main.tex
pdflatex -interaction=nonstopmode -halt-on-error main.tex
```

The checked PDF has five pages and no LaTeX/BibTeX warnings.  No theorem
prover or proof assistant was used.
