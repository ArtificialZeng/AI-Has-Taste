#!/usr/bin/env python3
"""Run from PROJECT_DIR: python3 evidence/pruned_forms_pilot.py

Enumerates all raw trees to n=8, retaining original zero-based leaf labels.
The import shares the raw scalar evaluator, so this is not an independent audit.
"""
import json
from itertools import product
from pathlib import Path
from exact_spectrum import trees, evaluate


def prune(t):
    if isinstance(t, int):
        return t
    left, right = t
    if not isinstance(left, int) and not isinstance(right, int):
        return prune(left)
    return (prune(left), prune(right))


def main():
    rows = []
    for n in range(2, 9):
        inputs = tuple(product(range(3), repeat=n))
        forms = {prune(t) for t in trees(n)}
        functions = {}
        collisions = []
        for t in forms:
            key = bytes(evaluate(t, x) for x in inputs)
            if key in functions:
                collisions.append([functions[key], t])
            functions[key] = t
        row = {'n': n, 'raw_trees': len(trees(n)),
               'pruned_forms': len(forms), 'functions': len(functions),
               'collisions': collisions[:3]}
        rows.append(row)
        print(json.dumps(row))
    Path('evidence/pruned-forms-pilot.json').write_text(json.dumps({
        'job_id': 'newwin-00001-p02-triage-ba81b5c3d443',
        'status': 'finite test only; no all-n injectivity proved',
        'leaf_labels': 'zero-based; never relabeled after pruning',
        'rows': rows}, indent=2)+'\n')


if __name__ == '__main__':
    main()
