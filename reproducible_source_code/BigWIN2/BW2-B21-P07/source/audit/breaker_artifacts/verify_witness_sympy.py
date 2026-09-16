#!/usr/bin/env python3
"""Independent verifier using SymPy's prime iterator, not discovery sieve code."""
import hashlib, json, platform, sys, time
from pathlib import Path
import sympy

def odd_part_via_valuation(x):
    # Deliberately differs from both discovery evaluators.
    v=(x & -x).bit_length()-1
    return x >> v

path=Path(sys.argv[1]); w=json.loads(path.read_text())
keys={"n","p_n","a_prev","sum","exponent"}
if set(w)!=keys or any(type(w[k]) is not int for k in keys): raise SystemExit("FAIL schema")
if w["n"]<=33900: raise SystemExit("FAIL index")
t=time.time(); a=0; prev=-1; count=0; lastp=0
for p in sympy.sieve.primerange(2,w["p_n"]+1):
    count+=1; prev=a; a=odd_part_via_valuation(a+int(p)); lastp=int(p)
if count!=w["n"] or lastp!=w["p_n"]: raise SystemExit("FAIL prime index")
if prev!=w["a_prev"] or a!=1: raise SystemExit("FAIL recurrence")
if prev+lastp!=w["sum"] or w["sum"]!=(1<<w["exponent"]): raise SystemExit("FAIL power identity")
print("VERIFIED",json.dumps({"n":count,"p_n":lastp,"a_prev":prev,"a_n":a,"sum":prev+lastp,
 "sympy":sympy.__version__,"python":sys.version,"platform":platform.platform(),"elapsed_seconds":time.time()-t,
 "witness_sha256":hashlib.sha256(path.read_bytes()).hexdigest()},sort_keys=True))
