#!/usr/bin/env python3
"""Create exact sparse kernel certificates for every n=8 graph with alpha=3."""
import argparse, hashlib, json, time
from pathlib import Path
import networkx as nx
from breaker_wlp_exact import edge_masks, alpha_exact, whiskered_independent_layers, inclusion_matrix


def sparse_column(X, col, length):
    return [[i, int(X[i, col])] for i in range(length) if X[i, col] != 0]


def certify(g6):
    g=nx.from_graph6_bytes(g6.encode()); adj=edge_masks(g)
    assert len(adj)==8 and alpha_exact(adj)==3
    layers=whiskered_independent_layers(adj); h=list(map(len,layers))
    # Structural reduction says WLP would require injectivity at d=4 and
    # surjectivity at d=5.  Seek an exact witness in that order.
    M4=inclusion_matrix(layers[4],layers[5])
    X4,n4=M4.nullspace()
    if n4:
        return {"graph6":g6,"alpha":3,"hilbert":h,"degree":4,"side":"right",
                "matrix_shape":[h[5],h[4]],"vector_length":h[4],
                "vector_sparse":sparse_column(X4,0,h[4])}
    M5=inclusion_matrix(layers[5],layers[6])
    X5,n5=M5.transpose().nullspace()
    if n5:
        return {"graph6":g6,"alpha":3,"hilbert":h,"degree":5,"side":"left",
                "matrix_shape":[h[6],h[5]],"vector_length":h[6],
                "vector_sparse":sparse_column(X5,0,h[6])}
    return {"graph6":g6,"alpha":3,"hilbert":h,"degree":None,"side":None,
            "matrix_shape":None,"vector_length":0,"vector_sparse":[]}


def main():
    ap=argparse.ArgumentParser(); ap.add_argument("--input",required=True); ap.add_argument("--output",required=True)
    ap.add_argument("--residue",type=int,default=0); ap.add_argument("--modulus",type=int,default=1); a=ap.parse_args()
    assert a.modulus>0 and 0<=a.residue<a.modulus
    counts={"all":0,"alpha0":0,"alpha1":0,"alpha2":0,"alpha3":0,"alpha4":0,"alpha5":0,"alpha6":0,"alpha7":0,"alpha8":0,"uncertified":0,"right_d4":0,"left_d5":0}
    start=time.time(); out=Path(a.output)
    with open(a.input,"rb") as fi,out.open("w") as fo:
      for raw in fi:
        if raw.startswith(b">") or not raw.strip(): continue
        index=counts["all"]; counts["all"]+=1; g6=raw.strip().decode(); g=nx.from_graph6_bytes(g6.encode())
        al=alpha_exact(edge_masks(g)); counts["alpha"+str(al)]+=1
        if al!=3 or index%a.modulus!=a.residue: continue
        rec=certify(g6); rec["geng_index"]=index; counts["alpha3"] += 0  # already counted above
        if rec["side"] is None: counts["uncertified"]+=1
        elif rec["degree"]==4: counts["right_d4"]+=1
        else: counts["left_d5"]+=1
        fo.write(json.dumps(rec,separators=(",",":"),sort_keys=True)+"\n")
        if (counts["right_d4"]+counts["left_d5"]+counts["uncertified"])%100==0:
            print(json.dumps({**counts,"seconds":round(time.time()-start,3)}),flush=True)
    summary={**counts,"residue":a.residue,"modulus":a.modulus,"seconds":time.time()-start,"certificate_sha256":hashlib.sha256(out.read_bytes()).hexdigest()}
    Path(str(out)+".summary.json").write_text(json.dumps(summary,indent=2)+"\n")
    print(json.dumps(summary,sort_keys=True))
if __name__=="__main__": main()
