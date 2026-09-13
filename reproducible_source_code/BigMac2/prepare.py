#!/usr/bin/env python3
"""Materialize one BigMac2 source package into a NEW working directory."""
from pathlib import Path
import argparse,gzip,hashlib,json,shutil

def digest(data):
    return hashlib.sha256(data).hexdigest()

def main():
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('paper_id')
    parser.add_argument('--output',type=Path,required=True)
    args=parser.parse_args()
    collection=Path(__file__).resolve().parent
    package=collection/args.paper_id
    if package.parent!=collection or not (package/'package.json').is_file():
        parser.error('Unknown paper ID')
    dest=args.output.resolve()
    if dest.exists():parser.error('Output directory already exists; choose a new working directory')
    repo=collection.parents[1]
    data=json.loads((package/'package.json').read_text())
    verified=[]
    for item in data['source_files']:
        stored=repo/item['path']
        if not stored.resolve().is_relative_to(package.resolve()):raise ValueError('Invalid package storage path')
        content=stored.read_bytes()
        if digest(content)!=item['sha256']:raise ValueError('Changed stored file: '+item['path'])
        name=item.get('materialized_path') or str(stored.relative_to(package/'source'))
        target=dest/name
        if not target.resolve().is_relative_to(dest):raise ValueError('Invalid output path')
        if item.get('compression')=='gzip':content=gzip.decompress(content)
        if digest(content)!=item['original_sha256']:raise ValueError('Changed original content: '+name)
        verified.append((target,content,stored))
    dest.mkdir(parents=True)
    for target,content,stored in verified:
        target.parent.mkdir(parents=True,exist_ok=True)
        target.write_bytes(content)
        target.chmod(stored.stat().st_mode & 0o777)
    for name in ['README.md','requirements.txt']:
        if (package/name).is_file():shutil.copy2(package/name,dest/('PACKAGE_'+name))
    print(json.dumps({'paper_id':args.paper_id,'verified_source_files':len(verified),'working_directory':str(dest),'scope':'Materialization and byte verification only; no mathematical program was executed.'}))

if __name__=='__main__':main()
