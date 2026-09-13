"""Release consistency checks; no claim that these certify mathematics or vision."""
from pathlib import Path
import hashlib
import json
import re
import subprocess

ROOT = Path(__file__).resolve().parent.parent
def sha(path):
    return hashlib.sha256((ROOT / path).read_bytes()).hexdigest()
def readj(path):
    return json.loads((ROOT / path).read_text())
def capture(command):
    return subprocess.run(command, cwd=ROOT, check=True, capture_output=True, text=True).stdout

snapshot = readj('audit/snapshot.json')
ms = readj('audit/manuscript-snapshot.json')
pub = readj('publication.json')
for snap in (snapshot, ms):
    assert all(sha(p) == h for p, h in snap['files'].items())
    mapping = json.dumps(snap['files'], sort_keys=True, separators=(',', ':'), ensure_ascii=False)
    assert hashlib.sha256(mapping.encode()).hexdigest() == snap['digest']
assert ms['snapshot_digest'] == snapshot['digest']
assert sha(pub['pdf']) == ms['pdf_digest']

tex = (ROOT / 'manuscript/main.tex').read_text()
bib = (ROOT / 'manuscript/references.bib').read_text()
bbl = (ROOT / 'manuscript/main.bbl').read_text()
workbook_note = (ROOT / 'literature/user_bibliography_check.md').read_text()
authoritative = workbook_note.split('```bibtex\n', 1)[1].split('```', 1)[0].strip()
assert authoritative in bib
keys = sorted(set(re.findall(r'\\cite(?:\[[^\]]*\])*\{([^}]+)\}', tex)))
bibkeys = sorted(re.findall(r'@\w+\{([^,]+),', bib))
bblkeys = sorted(re.findall(r'\\entry\{([^}]+)\}', bbl))
assert keys == bibkeys == bblkeys
assert not re.search(r'\\(?:input|include|includegraphics|lstinputlisting)\b', tex)
assert re.findall(r'\\addbibresource\{([^}]+)\}', tex) == ['references.bib']
assert sorted(pub['source_files']) == ['manuscript/main.bbl', 'manuscript/main.tex', 'manuscript/references.bib']

log = (ROOT / 'manuscript/main.log').read_text()
blg = (ROOT / 'manuscript/main.blg').read_text()
diagnostic = r'(?im)^!|(?:LaTeX|Package [^\n]+) Warning:|Overfull \\[hv]box|Underfull \\[hv]box|Fatal error|Emergency stop|Undefined control sequence|Missing character:|\b(?:WARN|ERROR) -'
assert not re.search(diagnostic, log + '\n' + blg)
transcript = (ROOT / 'evidence/write-build-transcript.txt').read_text()
final_pass = transcript.rsplit('\n$ pdflatex ', 1)[1].split('\n', 1)[1]
assert not re.search(diagnostic, final_pass)
commands = readj('evidence/write-build-commands.json')
assert commands['clean'] and len(commands['commands']) == 4
assert all(c['returncode'] == 0 for c in commands['commands'])
assert 'Output written on main.pdf (3 pages, 345504 bytes).' in log
assert (ROOT / pub['pdf']).stat().st_size == 345504

info = capture(['pdfinfo', pub['pdf']])
fonts = capture(['pdffonts', pub['pdf']])
(ROOT / 'evidence/release-pdfinfo.txt').write_text(info)
(ROOT / 'evidence/release-fonts.txt').write_text(fonts)
assert re.search(r'^Pages:\s+3$', info, re.M)
assert re.search(r'^Encrypted:\s+no$', info, re.M)
font_lines = fonts.strip().splitlines()[2:]
assert len(font_lines) == 25 and all('yes yes yes' in line for line in font_lines)
text = (ROOT / 'evidence/release-pdf-text.txt').read_text()
assert len(text.strip()) > 500 and '??' not in text
assert '10.2139/ssrn.7380519' in text and '2609.03926v1' in text

outputs = {}
for program in ('evidence/research_b5_independent.py', 'evidence/triage_b5.py'):
    outputs[program] = capture(['python3', program])
(ROOT / 'evidence/release-coefficients.json').write_text(json.dumps(outputs, indent=2))
sigma = lambda n: sum(d for d in range(1, n + 1) if n % d == 0)
c = [0] + [16 * (sigma(j) - (sigma(j//2) if j % 2 == 0 else 0)) for j in range(1, 6)]
b = [1]
for n in range(1, 6):
    numerator = sum(c[j] * b[n-j] for j in range(1, n+1))
    assert numerator % n == 0
    b.append(numerator // n)
assert c[1:] == [16,32,64,64,96]
assert b == [1,16,144,960,5264,25056]
assert 16*5264+32*960+64*144+64*16+96 == 125280 == 5*b[5]

result = {
    'job_id': 'bigMac-00006-p03-release-45c673bd9503',
    'snapshot_digest': snapshot['digest'], 'manuscript_digest': ms['digest'],
    'pdf_digest': ms['pdf_digest'], 'source_sha256': sha('source.md'),
    'frozen_inputs_unchanged': True, 'authoritative_bibtex_verbatim': True,
    'source_files': sorted(pub['source_files']), 'citekeys': keys,
    'final_build_diagnostics': [], 'build_log_digest': sha('manuscript/main.log'),
    'build_audit_basis': 'existing clean four-command build, actual final compiler log, Biber log, transcript and command records',
    'pages': 3, 'embedded_subset_fonts_with_unicode': len(font_lines),
    'exact_recurrence_c': c[1:], 'exact_recurrence_b': b,
    'render_sha256': {f'evidence/release-render/page-{n}.png': sha(f'evidence/release-render/page-{n}.png') for n in (1,2,3)},
    'visual_note': 'Image hashes attest files only; direct page observations are in audit/visual.md.'
}
(ROOT / 'evidence/release-validation.json').write_text(json.dumps(result, indent=2) + '\n')
print(json.dumps(result, separators=(',', ':')))
