"""Reproduce the auxiliary fixed-unit-factor and initial ratio probe."""
from fractions import Fraction
import json
from pathlib import Path
from triage_probe import factor, delta, shifts

P = [1]
rows = []
for n in range(1,129):
    P = factor(P,n)
    row = {'n':n}
    for k in [1,2,3,4]:
        a = P
        for _ in range(k):
            a = factor(a,1)
        j = next((j for j in range(1,len(a)-1) if delta(a,j)<0),None)
        if j is not None:
            row[str(k)] = {'j':j,'triple':a[j-1:j+2],'minor':delta(a,j)}
    rows.append(row)
a = [1]
least = None
for n in range(1,129):
    for s in shifts(n):
        old = a
        a = factor(a,s)
        if n >= 9:
            for j in range(1,len(a)-1):
                base = delta(old,j)+delta(old,j-s)
                if base > 0:
                    ratio = Fraction(delta(a,j),base)
                    if least is None or ratio < least[0]:
                        least = (ratio,n,s,j,delta(a,j),base)
out = {'range':[1,128],'extra_unit_factors':[1,2,3,4],'rows':rows,
       'minimum_stage_minor_ratio':{'fraction':str(least[0]),'n':least[1],
           'shift':least[2],'j':least[3],'new_minor':least[4],'sum_old_minors':least[5]}}
Path('evidence/smoothing_probe.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps(out['minimum_stage_minor_ratio']))
