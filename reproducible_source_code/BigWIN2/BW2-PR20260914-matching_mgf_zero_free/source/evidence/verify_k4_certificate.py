"""Standard-library-only checker for the complete k=4 certificate.

Rebuilds a cleared-denominator triangular recurrence in Z[m,n,t], performs
exact linear-factor divisions, reconstructs the transform by binomial sums,
and computes determinants by recursive Laplace expansion. No SymPy, numerical
root solver, or import from the certificate generator is used.
"""
import ast
from functools import lru_cache
from itertools import product
import json
from math import comb
from pathlib import Path
import signal
import time

signal.alarm(180)
started = time.monotonic()
ROOT = Path(__file__).resolve().parents[1]
ONE = {(0,0,0):1}
ZERO = {}


def const(c):
    return {(0,0,0):c} if c else {}


def add(a,b):
    c = a.copy()
    for e,v in b.items():
        c[e] = c.get(e,0)+v
        if c[e] == 0:
            del c[e]
    return c


def scale(a,c):
    return {e:v*c for e,v in a.items() if v*c}


def mul(a,b):
    out = {}
    for ea,va in a.items():
        for eb,vb in b.items():
            e = tuple(i+j for i,j in zip(ea,eb))
            out[e] = out.get(e,0)+va*vb
    return {e:v for e,v in out.items() if v}


def power(a,n):
    out = ONE
    for _ in range(n):
        out = mul(out,a)
    return out


def divide_linear(a,axis,root):
    """Exact division by variable[axis]-root, with zero remainder required."""
    remaining = a.copy()
    answer = {}
    while remaining and max(e[axis] for e in remaining)>0:
        degree = max(e[axis] for e in remaining)
        leading = [(e,v) for e,v in remaining.items() if e[axis]==degree]
        for e,v in leading:
            del remaining[e]
            lower = tuple(d-(i==axis) for i,d in enumerate(e))
            answer[lower] = answer.get(lower,0)+v
            remaining = add(remaining,{lower:v*root})
    assert not remaining, ('nonzero remainder',axis,root,remaining)
    return {e:v for e,v in answer.items() if v}


M={(1,0,0):1}; N={(0,1,0):1}; T={(0,0,1):1}


def parse(text):
    """Interpret only polynomial syntax; never eval a serialized expression."""
    def walk(node):
        if isinstance(node,ast.Constant) and type(node.value) is int:
            return const(node.value)
        if isinstance(node,ast.Name):
            return {'m':M,'n':N,'t':T}[node.id]
        if isinstance(node,ast.UnaryOp) and isinstance(node.op,ast.USub):
            return scale(walk(node.operand),-1)
        if isinstance(node,ast.BinOp):
            if isinstance(node.op,ast.Add): return add(walk(node.left),walk(node.right))
            if isinstance(node.op,ast.Sub): return add(walk(node.left),scale(walk(node.right),-1))
            if isinstance(node.op,ast.Mult): return mul(walk(node.left),walk(node.right))
            if isinstance(node.op,ast.Pow):
                assert isinstance(node.right,ast.Constant) and type(node.right.value) is int and node.right.value>=0
                return power(walk(node.left),node.right.value)
        raise ValueError(ast.dump(node))
    return walk(ast.parse(text,mode='eval').body)


def cells(i,j):
    return {(a,b) for a in range(1,i+1) for b in range(min(j,a-1)+1)}


factors = {(i,j):add(mul(add(M,const(-j)),add(N,const(i-4))),scale(T,j-i))
           for i in range(1,5) for j in range(i)}


def factor_product(indices):
    out = ONE
    for index in sorted(indices):
        out = mul(out,factors[index])
    return out


nums={(0,0):ONE}
for i in range(1,5):
    nn=add(N,const(i-4))
    for j in range(i):
        a=add(M,const(-j))
        current=cells(i,j)-{(i,j)}
        terms=[((i-1,j),nn)]
        if j>0:
            terms += [((i,j-1),scale(mul(a,T),i-j+1)),((i-1,j-1),mul(a,nn))]
        out=ZERO
        for index,weight in terms:
            prior=cells(*index)
            assert prior<=current
            out=add(out,mul(mul(weight,nums[index]),factor_product(current-prior)))
        nums[i,j]=out
    nums[i,i]=add(mul(T,divide_linear(nums[i,i-1],1,4-i)),
                  mul(nums[i-1,i-1],factor_product(cells(i,i)-cells(i-1,i-1))))

P=nums[4,4]
for axis in (0,1):
    for root in range(4):
        P=divide_linear(P,axis,root)
Q=factor_product(cells(4,4))
certificate=json.loads((ROOT/'evidence/research-k4-certificate.json').read_text())
stored_P=ZERO
for i,s in enumerate(certificate['P_ascending_t']):
    stored_P=add(stored_P,mul(parse(s),power(T,i)))
assert P==stored_P
assert Q==parse(certificate['Q'])
assert nums[4,4]==mul(parse(certificate['A']),P)

# Independent transform: direct binomial coefficient arithmetic, descending z.
h=[ZERO for _ in range(7)]
for (a,b,i),c in P.items():
    assert a+i>=3 and b+i>=3
    monomial={(a+i-3,b+i-3,0):c*4**(6-i)}
    for left in range(i+1):
        for right in range(7-i):
            exponent=left+right
            h[6-exponent]=add(h[6-exponent],scale(monomial,(-1)**left*comb(i,left)*comb(6-i,right)))


def shift(poly):
    out=ZERO
    for (a,b,c),v in poly.items():
        assert c==0
        for i,j in product(range(a+1),range(b+1)):
            out=add(out,{(i,j,0):v*comb(a,i)*comb(b,j)*4**(a+b-i-j)})
    return out


hs=[shift(a) for a in h]
def decode(terms):
    result={(i,j,0):int(c) for i,j,c in terms}
    assert len(result)==len(terms)
    return result
assert h==[parse(s) for s in certificate['h_descending_z']]
assert hs==[decode(a) for a in certificate['shifted_h']]
h0,h1,h2,h3,h4,h5,h6=hs
B=[[h1,h3,h5,ZERO,ZERO,ZERO],
   [h0,h2,h4,h6,ZERO,ZERO],
   [ZERO,h1,h3,h5,ZERO,ZERO],
   [ZERO,h0,h2,h4,h6,ZERO],
   [ZERO,ZERO,h1,h3,h5,ZERO],
   [ZERO,ZERO,h0,h2,h4,h6]]


def determinant(size):
    @lru_cache(None)
    def expand(row,columns):
        if not columns: return ONE
        out=ZERO
        for index,col in enumerate(columns):
            if B[row][col]:
                term=mul(B[row][col],expand(row+1,columns[:index]+columns[index+1:]))
                out=add(out,scale(term,(-1)**index))
        return out
    return expand(0,tuple(range(size)))


deltas=[determinant(size) for size in range(1,7)]
assert deltas==[decode(a) for a in certificate['hurwitz_minors']]
assert deltas[5]==mul(h6,deltas[4])
coverage=[]
for label,polys in [('h',hs),('delta',deltas)]:
    for index,poly in enumerate(polys):
        bound=3 if label=='h' else 3*(index+1)
        assert set(poly)=={(i,j,0) for i,j in product(range(bound+1),repeat=2)}
        assert min(poly.values())>0
        coverage.append({'name':f'{label}_{index if label=="h" else index+1}',
                         'full_support_rectangle':[bound,bound],
                         'coefficient_count':len(poly),'minimum':str(min(poly.values())),
                         'constant':str(poly[(0,0,0)])})

result={'scope':'Independent standard-library exact arithmetic check in the same research context; not a fresh referee audit.',
        'recurrence_method':'Cleared denominators in Z[m,n,t] using factor-set differences and exact linear division',
        'determinant_method':'Memoized recursive Laplace expansion of an explicitly written Hurwitz matrix',
        'checks':{'P_reconstructed':True,'Q_reconstructed':True,'A_normalization':True,
                  'transform_reconstructed':True,'all_seven_h_compared':True,'all_six_determinants_compared':True,
                  'delta6_identity':True,'full_support_and_strictly_positive_coefficients':True},
        'coverage':coverage,'seconds':time.monotonic()-started}
out=ROOT/'evidence/research-k4-verification.json'
tmp=out.with_suffix('.json.tmp')
tmp.write_text(json.dumps(result,indent=2)+'\n')
tmp.replace(out)
print(json.dumps(result,indent=2))
