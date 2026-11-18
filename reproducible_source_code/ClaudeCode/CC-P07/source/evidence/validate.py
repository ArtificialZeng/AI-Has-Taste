import random, time
from lb import *
deal="JH 5H TC 8D JC AC KS AH 4C 8S 5S 5D 2D TS AS 6H 3H TD".split()
c=[13*SUITS.index(x[1])+RANKS.index(x[0]) for x in deal]
after_AJ=tuple(c[:4]+[c[5]]+c[6:])            # A♣ (pos 6) captures J♣ (pos 5)
after_A10=tuple(c[:2]+[c[5]]+c[3:5]+c[6:])     # A♣ (pos 6) captures 10♣ (pos 3)
print("after AC x JC:", quench(after_AJ), " after AC xx TC:", quench(after_A10))
rng=random.Random(2026); wins=0; N=3000; t0=time.time(); agree=0
for d in range(N):
    deck=list(range(52)); rng.shuffle(deck); seq=tuple(deck[:18])
    w=quench(seq); wins+=w
    quench.cache_clear()
    if d<60:
        p,_=poison_test(list(seq)); agree+= (p==(not w))
print(f"random deals: {wins}/{N} = {wins/N:.4f} winnable ({time.time()-t0:.0f}s); SAT agrees with DFS on {agree}/60")
