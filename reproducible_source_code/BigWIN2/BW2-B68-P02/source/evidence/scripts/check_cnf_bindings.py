#!/usr/bin/env python3
"""Reconstruct every retained formula and bind it to its exact census row."""
import hashlib
import json
from pathlib import Path
import networkx as nx
from pysat.formula import CNF
from sweep_colorings import build_cnf

ROOT=Path(__file__).resolve().parents[2]
records=json.loads((ROOT/'evidence/unsat_certification.json').read_text())['records']
rows={(r['n'],r['index']):r for r in map(json.loads,(ROOT/'evidence/coloring_witnesses.jsonl').read_text().splitlines())}
for record in records:
    key=record['n'],record['index'];row=rows[key]
    assert record['graph6']==row['graph6']
    assert (ROOT/f'census/n{key[0]:02}.g6').read_text().splitlines()[key[1]]==row['graph6']
    predicate='A' if row['classification']=='A_unsat_observed' else 'E'
    assert record['predicate']==predicate
    graph=nx.from_graph6_bytes(row['graph6'].encode())
    expected,_=build_cnf(graph,equitable=(predicate=='E'))
    saved=CNF(from_file=str(ROOT/record['cnf']))
    assert saved.nv==expected.nv==record['variables']
    assert saved.clauses==expected.clauses
    assert len(saved.clauses)==record['clauses']
report=dict(status='pass',checked_cnf_graph_bindings=len(records),
    script='evidence/scripts/check_cnf_bindings.py',
    note='Formula-by-formula regeneration supplements independent mathematical inspection of encoding semantics.',
    input_sha256=hashlib.sha256((ROOT/'evidence/unsat_certification.json').read_bytes()).hexdigest())
(ROOT/'evidence/cnf_binding_verification.json').write_text(json.dumps(report,indent=2)+'\n')
print(json.dumps(report))
