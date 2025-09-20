import yaml, re, pathlib

P = pathlib.Path

# 자동 채움 값 불러오기
vals = yaml.safe_load(P('docs/_autofill.yml').read_text(encoding='utf-8'))

def patch(path):
    f = P(path)
    if not f.exists():
        return
    txt = f.read_text(encoding='utf-8')
    for k, v in vals.items():
        # {{ KEY }} 형태를 실제 값으로 치환
        txt = re.sub(r'{{\s*'+re.escape(k)+r'\s*}}', str(v), txt)
    f.write_text(txt, encoding='utf-8')

# 대상 파일: 원고/부록/방법
for target in [
    'docs/manuscript.md',
    'docs/Supplementary_Materials.md',
    'docs/Methods.md'
]:
    patch(target)

print("Tokens patched.")
