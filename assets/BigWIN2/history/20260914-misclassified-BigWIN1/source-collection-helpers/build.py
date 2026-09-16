#!/usr/bin/env python3
"""Clean LaTeX rebuild in a disposable copy, without modifying archived sources.

Requirements: Python 3.10+, latexmk, the required TeX packages. Run in Linux/WSL.
Usage: python3 build.py BW1-B06-P01
The regenerated PDF is a build check, not a replacement for the released PDF.
"""
from pathlib import Path
import argparse,gzip,json,shutil,subprocess,tempfile,hashlib
ROOT=Path(__file__).resolve().parent
def main():
    ap=argparse.ArgumentParser(description=__doc__);ap.add_argument('package');ap.add_argument('--timeout',type=int,default=120);ap.add_argument('--work-dir');args=ap.parse_args()
    package=(ROOT/args.package).resolve()
    if not package.is_relative_to(ROOT)or not(package/'package.json').is_file():raise SystemExit('Unknown package')
    meta=json.loads((package/'package.json').read_text(encoding='utf-8'))
    work=Path(args.work_dir).resolve()if args.work_dir else Path(tempfile.gettempdir())
    work.mkdir(parents=True,exist_ok=True)
    target=Path(tempfile.mkdtemp(prefix='bigwin-build-'+args.package+'-',dir=work))
    source=target/'source';shutil.copytree(package/'source',source)
    for item in meta['files']:
        if item['storage']!='gzip':continue
        restored=(target/item['path']).resolve()
        if not restored.is_relative_to(source):raise RuntimeError('Unsafe restoration path')
        restored.parent.mkdir(parents=True,exist_ok=True)
        h=hashlib.sha256()
        with gzip.open(package/item['stored_files'][0]['path'],'rb')as inp,restored.open('wb')as out:
            for b in iter(lambda:inp.read(1024*1024),b''):out.write(b);h.update(b)
        if h.hexdigest()!=item['original_sha256']:raise RuntimeError('Restored data checksum mismatch')
    main_tex=source/meta['main_tex']
    cwd=source if meta.get('build_cwd')=='source-root' else main_tex.parent
    command=['latexmk','-norc','-pdf','-g','-interaction=nonstopmode','-halt-on-error','-file-line-error','-no-shell-escape',str(main_tex.relative_to(cwd))]
    log=target/'build-output.txt'
    with log.open('w',encoding='utf-8')as out:
        try:result=subprocess.run(command,cwd=cwd,stdout=out,stderr=subprocess.STDOUT,timeout=args.timeout)
        except subprocess.TimeoutExpired:raise SystemExit('Build timed out; retained work at '+str(target))
    print(json.dumps(dict(package=args.package,exit_code=result.returncode,work=str(target),log=str(log),rebuilt_pdf=str(cwd/(main_tex.stem+'.pdf')))))
    raise SystemExit(result.returncode)
if __name__=='__main__':main()
