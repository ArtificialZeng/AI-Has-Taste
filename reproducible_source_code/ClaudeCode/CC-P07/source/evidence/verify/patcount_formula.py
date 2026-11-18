# Independent count of prefix patterns (orbits of k-sequences of distinct cards
# under S4 (suits) x S13 (ranks)) by a closed formula:
# sequences that use exactly a given set of a suits and b ranks are acted on
# freely by S_a x S_b, so #orbits = sum_{a,b} Surj(a,b,k) / (a! b!), where
# Surj(a,b,k) = # injective k-sequences in an a x b grid using every row and
# column, by inclusion-exclusion.
from math import comb, factorial
def falling(n, k):
    r = 1
    for i in range(k): r *= (n - i)
    return r
def surj(a, b, k):
    return sum((-1)**(i+j) * comb(a,i) * comb(b,j) * falling((a-i)*(b-j), k)
               for i in range(a+1) for j in range(b+1))
for k in range(1, 10):
    tot = 0
    for a in range(1, 5):
        for b in range(1, 14):
            s = surj(a, b, k)
            assert s % (factorial(a)*factorial(b)) == 0
            tot += s // (factorial(a)*factorial(b))
    print(k, tot)
