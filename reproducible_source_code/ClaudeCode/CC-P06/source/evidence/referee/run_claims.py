#!/usr/bin/env python3
"""Count and list all solutions of the diagrams claimed in the note, with rdp.py."""
import time
import json
from rdp import Counter, check_solution, draw

DIAGRAMS = {
    'a_13x13_claim5': '3222222122223 2222222221122 2222122223232 2222221222112 2212222222222 2222222222221 '
                      '2221122211222 1222222222222 2222222222122 2112221222222 2323222212222 2211222222222 3222212222223',
    'b_12x12_claim6': '322222100123 222111211222 122231122221 222221122210 213222222210 211122221121 121122221112 '
                      '012222222312 012221122212 122221132222 222112112222 321001222123',
    'c_13x13_claim6': '3222221132222 2221112122312 1222311221112 2222211221121 2132222112210 2111222112210 '
                      '1211222221121 0122112221112 0122112222312 1211221122222 2101221132221 2012112111222 2221001222223',
    'd_knuth6x6_claim4': '322222 222232 222222 222222 232222 222223',
    'd_2x2_claim2': '32 23',
}

if __name__ == '__main__':
    allsol = {}
    for name, s in DIAGRAMS.items():
        rows = s.split()
        t = time.time()
        C = Counter(rows)
        cnt = C.count()
        sols = C.solutions()
        dt = time.time() - t
        checks = [check_solution(rows, E) for E in sols]
        distinct = len(set(sols)) == len(sols)
        print(f'== {name}: {len(rows)}x{len(rows[0])}  count={cnt}  listed={len(sols)}  distinct={distinct}  '
              f'all_valid={all(c[0] for c in checks)}  lengths={[c[1] for c in checks]}  '
              f'memo_states={len(C.memo)}  time={dt:.1f}s', flush=True)
        for i, E in enumerate(sols):
            print(f'-- solution {i + 1}')
            print(draw(rows, E))
        allsol[name] = {'rows': rows, 'count': cnt,
                        'solutions': [sorted(list(e) for e in E) for E in sols]}
    with open('solutions.json', 'w') as f:
        json.dump(allsol, f)
