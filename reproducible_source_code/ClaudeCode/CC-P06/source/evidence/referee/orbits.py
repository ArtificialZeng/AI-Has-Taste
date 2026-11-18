#!/usr/bin/env python3
"""Summarise 'SIG mult rows...' lines of msearch2: distinct signatures and
classes under the 8 symmetries of the square, by multiplicity.
usage: orbits.py logfile [show]"""
import sys
from collections import defaultdict


def syms(rows):
    def rot(r):
        return tuple(''.join(r[len(r) - 1 - j][i] for j in range(len(r))) for i in range(len(r[0])))

    def flip(r):
        return tuple(x[::-1] for x in r)
    out = []
    for f in (False, True):
        r = flip(rows) if f else rows
        for _ in range(4):
            out.append(r)
            r = rot(r)
    return out


if __name__ == '__main__':
    sigs = defaultdict(int)
    mult = {}
    for line in open(sys.argv[1]):
        if line.startswith('SIG '):
            parts = line.split()
            k = int(parts[1])
            rows = tuple(parts[2:])
            sigs[rows] += 1
            mult[rows] = k
    bad = [r for r in sigs if sigs[r] != mult[r]]
    print(f'{len(sigs)} distinct signatures; each reached exactly mult times: {not bad}')
    by = defaultdict(set)
    classes = defaultdict(set)
    for rows, k in mult.items():
        by[k].add(rows)
        classes[k].add(min(syms(rows)))
    for k in sorted(by):
        print(f'  multiplicity {k}: {len(by[k])} signatures, {len(classes[k])} classes under the dihedral group')
    if len(sys.argv) > 2:
        for k in sorted(classes):
            for c in sorted(classes[k]):
                print(k, ' '.join(c))
