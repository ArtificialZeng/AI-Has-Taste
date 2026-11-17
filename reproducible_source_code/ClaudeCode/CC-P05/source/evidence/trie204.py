"""Literal transcription of the trie-building loop in answer 7.2.2.4-204(b) (Pre-Fascicle 8a), with the field count
d = TMS + (l + TMS = q-1 ? 3 : 2) as printed, versus the swapped version (l + TMS = q-1 ? 2 : 3).
Each new node occupies MEM[p .. p+d-1]; we record every field index used and check that it lies inside its node."""
import random, sys
def random_marked_involution(q, rng):
    """Uniform random marked involution of order q via T_n = 2 T_{n-1} + (n-1) T_{n-2}; encoded as a_1..a_q:
    -1 / 0 for the two kinds of fixed points, positive codes 1, 2, ... for pairs in order of first appearance."""
    T = [1, 2]
    for n in range(2, q + 1): T.append(2 * T[n - 1] + (n - 1) * T[n - 2])
    elems = list(range(1, q + 1)); mate = {}
    while elems:
        n = len(elems); x = elems.pop()           # decide the last element
        r = rng.randrange(T[n])
        if r < 2 * T[n - 1]: mate[x] = -1 if r < T[n - 1] else 0
        else:
            y = elems.pop(rng.randrange(len(elems))); mate[x] = y; mate[y] = x
    a, t = [0] * (q + 1), 0
    for k in range(1, q + 1):
        j = mate[k]
        if j <= 0: a[k] = j
        elif j > k: t += 1; a[k] = a[j] = t
    return a[1:]
def build(keys, q, printed):
    MEM = {}; nodes = []                          # nodes: (start, d)
    p = 0
    def owner(idx): return any(s <= idx < s + d for s, d in nodes)
    bad = 0
    for key in keys:
        a = [None] + key
        if p == 0:
            MEM[0] = MEM[1] = MEM[2] = 0; nodes.append((0, 3)); p = 3
            # root: t points so that t+a_1 hits MEM[0..2] for a_1 in {-1,0,1}
        TMS, TMX = 0, 1; TMAP, ITMAP = {}, {}
        t = l = 1
        while True:
            al = a[l]
            if al <= 0: t = t + al
            elif al == TMX:
                TMAP[TMS] = TMX; ITMAP[TMX] = TMS; TMS += 1; TMX += 1; t = t + TMS
            else:
                TMS -= 1; k = TMAP[TMS]; k2 = ITMAP[al]; TMAP[k2] = k; ITMAP[k] = k2; t = t + 1 + k2
            if not owner(t): bad += 1
            t2 = MEM.get(t, 0)
            if l == q: break
            if t2 == 0:
                if l + TMS == q: d = TMS; t2 = p - 1
                else:
                    t2 = p + 1
                    if printed: d = TMS + (3 if l + TMS == q - 1 else 2)
                    else: d = TMS + (2 if l + TMS == q - 1 else 3)
                MEM[t] = t2
                for k in range(d): MEM[p + k] = 0
                nodes.append((p, d)); p += d
            t = t2; l += 1
    return bad, p
rng = random.Random(1)
for q in (6, 8, 10, 14):
    keys = [random_marked_involution(q, rng) for _ in range(300)]
    for printed in (True, False):
        bad, p = build(keys, q, printed)
        print(f"q={q}: {'printed rule' if printed else 'swapped rule'}: accesses outside the node {bad}, pointers allocated {p}")
