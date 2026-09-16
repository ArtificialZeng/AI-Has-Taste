#!/usr/bin/env python3
import argparse,json
from pathlib import Path
import networkx as nx
from breaker_wlp_exact import edge_masks,alpha_exact
p=argparse.ArgumentParser();p.add_argument("--graphs",required=True);p.add_argument("--output",required=True);p.add_argument("shards",nargs="+");a=p.parse_args()
records=[]
for f in a.shards:
 with open(f) as h: records.extend(json.loads(x) for x in h if x.strip())
records.sort(key=lambda r:r["geng_index"])
assert len({r["geng_index"] for r in records})==len(records)
expected=[]
with open(a.graphs,"rb") as f:
 for i,raw in enumerate(f):
  if raw.startswith(b">") or not raw.strip(): continue
  g6=raw.strip().decode();g=nx.from_graph6_bytes(g6.encode())
  if alpha_exact(edge_masks(g))==3: expected.append((i,g6))
assert [(r["geng_index"],r["graph6"]) for r in records]==expected
with open(a.output,"w") as f:
 for r in records:f.write(json.dumps(r,separators=(",",":"),sort_keys=True)+"\n")
print(json.dumps({"merged":len(records),"expected_alpha3":len(expected),"first_index":records[0]["geng_index"],"last_index":records[-1]["geng_index"],"status":"OK"}))
