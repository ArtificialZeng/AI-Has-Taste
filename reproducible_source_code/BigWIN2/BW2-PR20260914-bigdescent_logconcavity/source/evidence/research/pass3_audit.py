"""Recompute every parameter coefficient using 9-state tensor products.

This implementation reads the serialized certificate but imports none of its
code. NumPy object arrays store arbitrary-precision Python integers. A second
check computes conditional profiles by direct binary-word enumeration.
"""
from itertools import product, combinations, combinations_with_replacement as cwr
from collections import Counter
from pathlib import Path
import hashlib
import json
import time
import numpy as np

JOB = "primary-20260914-bigdescent-logconcavity-research-5c6b908e3ed6"
P=np.array([[1,0,0],[1,0,0],[0,0,1]],dtype=object)
Q=np.array([[0,1,1],[0,0,0],[0,1,0]],dtype=object)
I=np.eye(3,dtype=object)
O=np.array([[1,0,0],[0,1,0],[1,0,1],[0,1,1]],dtype=object)
J=np.array([[1,0,0],[1,1,0],[1,0,1],[1,1,1]],dtype=object)
F={"I":(I,),"P":(P,P@Q@P),"Q":(Q,Q@P@Q),
   "PQ":(P@Q,P@Q@P@Q),"QP":(Q@P,Q@P@Q@P)}


def pair(A,B,same):
    return np.kron(A,B) if same else np.kron(A,B)+np.kron(B,A)


def word_events(w):
    return sum((w[i-1:i+1]==(1,0) or
                i>=2 and w[i-2:i+1]==(0,1,1))<<(i-1)
               for i in range(1,len(w)))


def main():
    start=time.perf_counter()
    cert_path=Path(__file__).with_name('multi_singleton_certificate.json')
    cert=json.loads(cert_path.read_text())
    assert np.array_equal(P@P,P)
    assert np.array_equal(Q@Q@Q,np.zeros((3,3),dtype=object))
    assert np.array_equal(P@Q@P@Q@P,P@Q@P+P)
    assert np.array_equal(Q@P@Q@P@Q,Q@P@Q+Q)
    assert np.array_equal(P@Q@P@Q@P@Q,P@Q@P@Q+P@Q)
    assert np.array_equal(Q@P@Q@P@Q@P,Q@P@Q@P+Q@P)
    bout=np.array([pair(O[a],O[b],a==b) for a,b in cwr(range(4),2)],dtype=object)
    binp=np.array([pair(J[a],J[b],a==b) for a,b in cwr(range(4),2)],dtype=object).T
    S0,S1=np.kron(P,Q),np.kron(Q,P)
    checked=0
    by_m={}
    for sm,result in cert['results'].items():
        m=int(sm); count=0
        for key,fam in result['families'].items():
            names=key.split(',')
            choices=[list(cwr(range(len(F[name])),2)) for name in names]
            gap_terms=tuple(product(*choices))
            new=np.zeros((m//2+1,10,10,len(gap_terms)),dtype=object)
            for c,gs in enumerate(gap_terms):
                # Build R M1^(2) R ... M_(m-1)^(2) R as a t-polynomial.
                mat=[S0,S1]
                for name,(a,b) in zip(names,gs):
                    G=pair(F[name][a],F[name][b],a==b)
                    out=[np.zeros((9,9),dtype=object) for _ in range(len(mat)+1)]
                    for k,B in enumerate(mat):
                        BG=B@G
                        out[k]+=BG@S0
                        out[k+1]+=BG@S1
                    mat=out
                h=[bout@B@binp for B in mat]
                assert all(np.array_equal(h[j],h[m-j]) for j in range(m+1))
                for j in range(m//2+1):
                    new[j,:,:,c]=h[j]-(h[j-1] if j else 0)
            flat=new.reshape((m//2+1,-1)).tolist()
            assert flat==fam['coefficients'],(m,names)
            assert all(c>=0 for row in flat for c in row),(m,names)
            count+=new.size
        assert count==result['coefficient_positions']
        checked+=count
        by_m[sm]=count
        print(json.dumps({'tensor_m':m,'coefficients_matched':count,
                          'seconds':time.perf_counter()-start}),flush=True)

    # Rank-one reset vectors and cone preservation, checked independently.
    e0=np.array([1,0,0],dtype=object)
    e1=np.array([0,1,0],dtype=object)
    assert np.array_equal(Q@Q,np.outer(e0,e1))
    def in_cone(v):
        a,b,c=map(int,v)
        return min(a,b,c)>=0 and b<=a and c<=a
    def out_cone(v):
        a,b,c=map(int,v)
        return min(a,b,c)>=0 and c<=a+b
    assert all(in_cone(M@r) for M in (P,Q) for r in J)
    assert all(out_cone(l@M) for M in (P,Q) for l in O)

    # Every choice of 0..4 free sites and all other indicators fixed, n<=11.
    configurations=profiles=nonzero=0
    by_n={}
    for n in range(1,12):
        a=Counter(word_events(prefix+(1,))
                  for prefix in product((0,1),repeat=n-1))
        local=0
        for m in range(min(4,n-1)+1):
            for free in combinations(range(n-1),m):
                rest=[i for i in range(n-1) if i not in free]
                for code in range(1<<len(rest)):
                    fixed=sum(((code>>j)&1)<<i for j,i in enumerate(rest))
                    vals=[a[fixed|sum(((t>>j)&1)<<i for j,i in enumerate(free))]
                          for t in range(1<<m)]
                    h=[0]*(m+1)
                    for t,v in enumerate(vals):
                        h[t.bit_count()]+=v*vals[((1<<m)-1)^t]
                    assert h==h[::-1]
                    assert all(h[j]>=h[j-1] for j in range(1,m//2+1)),(n,free,fixed,h)
                    configurations+=1;local+=1
                    profiles+=m//2+1;nonzero+=any(h)
        by_n[str(n)]=local
    # A general Boolean weight satisfying every two-coordinate factor-two
    # bound need not satisfy the three-coordinate conclusion. This witness
    # is deliberately outside the binary-word model.
    generic=[2 if t in (0,7) else 1 for t in range(8)]
    face_bounds=[]
    for fixed_site in range(3):
        free=[i for i in range(3) if i!=fixed_site]
        for bit in (0,1):
            s=bit<<fixed_site
            a,b,c,d=[generic[s|((t&1)<<free[0])|(((t>>1)&1)<<free[1])]
                     for t in range(4)]
            assert a*d==2*b*c
            face_bounds.append([a,b,c,d])
    generic_h=[sum(generic[t]*generic[7^t] for t in range(8)
                   if t.bit_count()==j) for j in range(4)]
    assert generic_h==[4,3,3,4]
    out={"job_id":JOB,"arithmetic":"Python integers, including NumPy object-array operations",
         "fresh_model_audit":False,
         "tensor_coefficients_matched":checked,"tensor_by_m":by_m,
         "rank_one_Q_squared_factorization_verified":True,
         "alternating_word_identities_verified":True,
         "boundary_cones_preserved":True,
         "direct_word_n_max":11,"free_sites_max":4,
         "direct_conditional_configurations":configurations,
         "direct_nonzero_pair_profiles":nonzero,
         "direct_Schur_coefficients_checked":profiles,
         "configurations_by_n":by_n,
         "two_position_bound_does_not_imply_three_position_Schur":{
             "domain":"Generic weights on subsets of a three-element set, not actual words",
             "weights_in_bitmask_order":generic,"six_two_dimensional_faces":face_bounds,
             "pair_polynomial_coefficients":generic_h,"Schur_coefficients":[4,-1]},
         "qualification":"Separate deterministic implementations in the same worker. All polynomial coefficient positions are checked; direct words have only the stated finite range. No fresh referee or general all-profile result.",
         "seconds":time.perf_counter()-start,
         "certificate_sha256":hashlib.sha256(cert_path.read_bytes()).hexdigest(),
         "script_sha256":hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
         "source_sha256":hashlib.sha256(Path('source.md').read_bytes()).hexdigest()}
    Path(__file__).with_suffix('.json').write_text(json.dumps(out,indent=2)+'\n')
    print(json.dumps(out,indent=2))


if __name__=='__main__':
    main()
