import sys, itertools
from slither import Grid, parse, all_solutions
rows=[l.strip() for l in open(sys.argv[1]) if l.strip()]
g,clues=parse(rows); n=g.W
assert g.W==g.H
def diamond(i):
    S=set()
    for e,((x1,y1),(x2,y2)) in enumerate(g.edges):
        mx=(x1+x2)/2+1; my=(y1+y2)/2+1     # Beluhov coordinates (1-based)
        u=mx+my; v=mx-my
        if i+1<=u<=2*n-i+1 and -i<=v<=i: S.add(e)
    return frozenset(S)
D=[diamond(i) for i in range(1,n)]
masks=[sum(1<<e for e in d) for d in D]
def decompose(E):
    m=sum(1<<e for e in E)
    for bits in range(1<<len(D)) if len(D)<=16 else []:
        x=0
        for i in range(len(D)):
            if bits>>i&1: x^=masks[i]
        if x==m: return [i+1 for i in range(len(D)) if bits>>i&1]
    return None
sols=all_solutions(g,clues)
print(len(sols),"solutions")
base=sols[0]
for s in sols:
    print("diff from solution 1 =", decompose(base ^ s), " size", len(base^s))
