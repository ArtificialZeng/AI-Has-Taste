#!/usr/bin/env python3
"""Verify archived bytes and optionally restore losslessly compressed data.

python3 prepare.py --verify
python3 prepare.py --restore BW1-B36-P02
Never replaces an existing file whose digest differs from the frozen source.
"""
from pathlib import Path
import argparse,gzip,hashlib,json,os
ROOT=Path(__file__).resolve().parent
def digest(p):
    h=hashlib.sha256()
    with p.open('rb')as f:
        for c in iter(lambda:f.read(1024*1024),b''):h.update(c)
    return h.hexdigest()
def checked_path(base,relative):
    p=(base/relative).resolve()
    if not p.is_relative_to(base.resolve()):raise ValueError('Path leaves package')
    return p
def main():
    ap=argparse.ArgumentParser(description=__doc__);ap.add_argument('--verify',action='store_true');ap.add_argument('--restore',metavar='PACKAGE_ID');args=ap.parse_args()
    ids=[args.restore]if args.restore else sorted(p.name for p in ROOT.iterdir()if p.is_dir()and(p/'package.json').exists())
    count=restored=0
    for ident in ids:
        base=checked_path(ROOT,ident);meta=json.loads((base/'package.json').read_text(encoding='utf-8'))
        for item in meta['files']:
            for stored in item['stored_files']:
                p=checked_path(base,stored['path'])
                if not p.is_file()or digest(p)!=stored['sha256']:raise RuntimeError('Stored input mismatch: '+str(p))
                count+=1
            if item['storage']=='gzip' and args.restore:
                target=checked_path(base,item['path']);target.parent.mkdir(parents=True,exist_ok=True)
                if target.exists():
                    if digest(target)!=item['original_sha256']:raise RuntimeError('Refusing to overwrite modified restored data: '+str(target))
                    continue
                compressed=checked_path(base,item['stored_files'][0]['path']);tmp=target.with_name(target.name+'.restoring')
                if tmp.exists():raise RuntimeError('Leftover restoration file: '+str(tmp))
                h=hashlib.sha256();size=0
                with gzip.open(compressed,'rb')as src,tmp.open('xb')as out:
                    for chunk in iter(lambda:src.read(1024*1024),b''):out.write(chunk);h.update(chunk);size+=len(chunk)
                if h.hexdigest()!=item['original_sha256']or size!=item['original_bytes']:raise RuntimeError('Uncompressed input mismatch')
                os.replace(tmp,target);restored+=1
    print(json.dumps(dict(packages=len(ids),stored_files_verified=count,restored=restored)))
if __name__=='__main__':main()
