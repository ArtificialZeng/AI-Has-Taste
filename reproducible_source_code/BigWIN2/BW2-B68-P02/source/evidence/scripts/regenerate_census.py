#!/usr/bin/env python3
"""Regenerate every census using the pinned executable, compare exact bytes."""
import hashlib
import json
import subprocess
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2]
records=[]
for n in range(4,20,2):
    command=['tools/nauty-root/geng','-cld3D3',str(n),str(3*n//2)]
    result=subprocess.run(command,cwd=ROOT,capture_output=True,check=True)
    saved=(ROOT/f'census/n{n:02}.g6').read_bytes()
    assert result.stdout==saved
    log=ROOT/f'evidence/logs/regenerated_n{n:02}.stderr';log.write_bytes(result.stderr)
    records.append(dict(n=n,command=command,count=len(saved.splitlines()),
        sha256=hashlib.sha256(saved).hexdigest(),log=str(log.relative_to(ROOT)),byte_identical=True))
report=dict(status='pass',script='evidence/scripts/regenerate_census.py',orders=records,
    generator_sha256=hashlib.sha256((ROOT/'tools/nauty-root/geng').read_bytes()).hexdigest(),
    total=sum(r['count'] for r in records),random_seed=None,
    nondeterministic_options='none; no res/mod restriction')
(ROOT/'evidence/census_regeneration.json').write_text(json.dumps(report,indent=2)+'\n')
print(json.dumps(dict(status='pass',total=report['total'],orders=len(records))))
