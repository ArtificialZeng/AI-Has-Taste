"""Direct word checks, independent of suffix-state enumeration."""
from collections import Counter, defaultdict
from itertools import product, combinations
from fractions import Fraction
from pathlib import Path
import hashlib
import json
from schur_profiles import tensor

def events(word):
    return tuple(int(word[i-1:i+1] == (1,0) or
                     i>=2 and word[i-2:i+1] == (0,1,1))
                 for i in range(1,len(word)))

conditional=0; equality=0; positive=0; maximum=Fraction(0)
profile_checks=0; scalar_checks=0
sharp_words=defaultdict(list)
for n in range(1,12):
    counts=Counter()
    for prefix in product((0,1),repeat=n-1):
        w=prefix+(1,);e=events(w)
        mask=sum(a<<j for j,a in enumerate(e));counts[mask]+=1
        if n==4 and not (mask & 2):
            sharp_words[str((int(bool(mask&1)),int(bool(mask&4))))].append(''.join(map(str,w)))
    for i,j in combinations(range(n-1),2):
        other=[k for k in range(n-1) if k not in (i,j)]
        for code in range(1<<len(other)):
            S=sum(((code>>k)&1)<<site for k,site in enumerate(other))
            A,B,C,D=(counts[S],counts[S|(1<<i)],counts[S|(1<<j)],
                     counts[S|(1<<i)|(1<<j)])
            assert A*D <= 2*B*C,(n,i,j,S,A,B,C,D)
            conditional+=1
            if B*C:
                positive+=1;maximum=max(maximum,Fraction(A*D,B*C))
                equality+=A*D==2*B*C
    if n<=8:
        direct=defaultdict(Counter)
        for a,ca in counts.items():
            for b,cb in counts.items():
                e=tuple(((a>>j)&1)+((b>>j)&1) for j in range(n-1))
                direct[e][a.bit_count()]+=ca*cb
        for e in product((0,1,2),repeat=n-1):
            h=tensor(e);expected=direct[e]
            assert h==[expected[j] for j in range(sum(e)+1)]
            profile_checks+=1;scalar_checks+=len(h)
assert maximum==2
out={"job_id":"primary-20260914-bigdescent-logconcavity-research-6ff0786c2423",
    "arithmetic":"exact direct binary-word enumeration",
    "fresh_model_audit":False,"word_length_max":11,
    "conditional_configurations_checked":conditional,
    "configurations_with_BC_positive":positive,
    "sharp_positive_configurations":equality,
    "maximum_exact_ratio_AD_over_BC":str(maximum),
    "sharp_n4_words":dict(sharp_words),
    "direct_pair_comparison_n_max":8,"ternary_profiles_compared":profile_checks,
    "scalar_coefficients_compared":scalar_checks,
    "qualification":"Direct count checks support the interpretation. The uniform theorem uses the separately proved matrix-word reduction and coefficient certificate, not this finite cutoff.",
    "source_sha256":hashlib.sha256(Path('source.md').read_bytes()).hexdigest(),
    "script_sha256":hashlib.sha256(Path(__file__).read_bytes()).hexdigest()}
Path(__file__).with_suffix('.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps(out,indent=2))
