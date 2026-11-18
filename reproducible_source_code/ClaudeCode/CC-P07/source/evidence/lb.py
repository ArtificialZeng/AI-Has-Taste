"""Late Binding solitaire (TAOCP 7.2.2.2-486): quenching solver and SAT poison test."""
import itertools, functools, random, sys
from pysat.solvers import Solver
SUITS='SHDC'; RANKS='A23456789TJQK'
def suit(c): return c//13
def rank(c): return c%13
def name(c): return RANKS[rank(c)]+SUITS[suit(c)]
def match(a,b): return suit(a)==suit(b) or rank(a)==rank(b)

@functools.lru_cache(maxsize=None)
def quench(seq):
    """True iff the sequence of top cards can be reduced to one pile"""
    n=len(seq)
    if n==1: return True
    for k in range(n-1):
        if match(seq[k],seq[k+1]):
            if quench(seq[:k]+seq[k+1:]): return True
    for l in range(n-3):
        if match(seq[l],seq[l+3]):
            if quench(seq[:l]+(seq[l+3],)+seq[l+1:l+3]+seq[l+4:]): return True
    return False

def poison_test(prefix, n=18, symbreak=True, solver='cadical195', budget=None):
    """SAT test: returns (False, completion) if some completion of `prefix` to n cards wins, (True, None) if none does."""
    k=len(prefix); top=[0]
    def nv(): top[0]+=1; return top[0]
    X={}
    for t in range(n-1):
        m=n-t
        for i in range(1,m+1):
            for j in range(i+1,m+1): X[(t,i,j)]=nv()
    Q={(t,kk):nv() for t in range(n-1) for kk in range(1,n-t)}
    S={(t,l):nv() for t in range(n-1) for l in range(1,n-t-2)}
    cl=[]
    for t in range(n-1):
        m=n-t
        cl.append([Q[(t,kk)] for kk in range(1,m)]+[S[(t,l)] for l in range(1,m-2)])
        for kk in range(1,m):
            cl.append([-Q[(t,kk)],X[(t,kk,kk+1)]])
            if t+1<n-1:
                for i in range(1,m):
                    for j in range(i+1,m):
                        i2=i+(i>=kk); j2=j+(j>=kk)
                        cl.append([-Q[(t,kk)],-X[(t+1,i,j)],X[(t,i2,j2)]])
        for l in range(1,m-2):
            cl.append([-S[(t,l)],X[(t,l,l+3)]])
            if t+1<n-1:
                for i in range(1,m):
                    for j in range(i+1,m):
                        a=i+(i>=l+3)+3*(i==l); b=j+(j>=l+3)+3*(j==l)
                        cl.append([-S[(t,l)],-X[(t+1,i,j)],X[(t,min(a,b),max(a,b))]])
    # suffix cards: suit and rank one-hot
    SV={(p,s):nv() for p in range(k+1,n+1) for s in range(4)}
    RV={(p,r):nv() for p in range(k+1,n+1) for r in range(13)}
    for p in range(k+1,n+1):
        cl.append([SV[(p,s)] for s in range(4)]); cl+= [[-SV[(p,a)],-SV[(p,b)]] for a,b in itertools.combinations(range(4),2)]
        cl.append([RV[(p,r)] for r in range(13)]); cl+= [[-RV[(p,a)],-RV[(p,b)]] for a,b in itertools.combinations(range(13),2)]
        for c in prefix: cl.append([-SV[(p,suit(c))],-RV[(p,rank(c))]])
    for p,q in itertools.combinations(range(k+1,n+1),2):
        for s in range(4):
            for r in range(13): cl.append([-SV[(p,s)],-RV[(p,r)],-SV[(q,s)],-RV[(q,r)]])
    # initial adjacency
    for i in range(1,n+1):
        for j in range(i+1,n+1):
            x=X[(0,i,j)]
            if j<=k:
                if not match(prefix[i-1],prefix[j-1]): cl.append([-x])
            elif i<=k:
                c=prefix[i-1]; cl.append([-x,SV[(j,suit(c))],RV[(j,rank(c))]])
            else:
                aux=[]
                for s in range(4):
                    a=nv(); aux.append(a); cl+=[[-a,SV[(i,s)]],[-a,SV[(j,s)]]]
                for r in range(13):
                    a=nv(); aux.append(a); cl+=[[-a,RV[(i,r)]],[-a,RV[(j,r)]]]
                cl.append([-x]+aux)
    if symbreak:   # commutativity breaking from answer 485 (adjacent time steps)
        for t in range(n-2):
            m=n-t; t2=t+1
            for kk in range(1,m):
                for k2 in range(kk,m-1):
                    if (t2,k2) in Q and (t,k2+1) in Q and kk<k2: cl.append([-Q[(t,k2+1)],-Q[(t2,kk)]])
    s=Solver(name=solver, bootstrap_with=cl)
    ok=s.solve() if budget is None else s.solve_limited()
    if not ok:
        s.delete(); return True,None
    m=set(l for l in s.get_model() if l>0); s.delete()
    comp=list(prefix)
    for p in range(k+1,n+1):
        su=next(x for x in range(4) if SV[(p,x)] in m); ra=next(x for x in range(13) if RV[(p,x)] in m)
        comp.append(13*su+ra)
    return False,comp

if __name__=="__main__":
    # Knuth's example deal from exercise 486: J♥ 5♥ 10♣ 8♦ J♣ A♣ K♠ A♥ 4♣ 8♠ 5♠ 5♦ 2♦ 10♠ A♠ 6♥ 3♥ 10♦  (suit letters S H D C)
    deal="JH 5H TC 8D JC AC KS AH 4C 8S 5S 5D 2D TS AS 6H 3H TD".split()
    cards=[13*SUITS.index(x[1])+RANKS.index(x[0]) for x in deal]
    print("Knuth's deal winnable:", quench(tuple(cards)))
    print("SAT with full deal as prefix -> poison?", poison_test(cards)[0])
    print("SAT with 17-card prefix -> poison?", poison_test(cards[:17])[0])
