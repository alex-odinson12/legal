"""Build static legal pages from Markdown. Run with --effective-date YYYY-MM-DD."""
from pathlib import Path
import argparse, datetime, html, re
import markdown

parser = argparse.ArgumentParser()
parser.add_argument('--effective-date', required=True, type=datetime.date.fromisoformat)
args = parser.parse_args()
root = Path(__file__).resolve().parent
base = 'https://alex-odinson12.github.io/legal/heritageface/android/'
for lang in ('en', 'ru'):
    date = args.effective_date.isoformat()
    label = {'en': {'privacy':'Privacy Policy','terms':'Terms of Use'},
             'ru': {'privacy':'Политика конфиденциальности','terms':'Условия использования'}}[lang]
    for kind in ('privacy', 'terms'):
        source = (root/'source'/lang/f'{kind}.md').read_text(encoding='utf-8')
        assert source.startswith('# ') and source.count('{{EFFECTIVE_DATE}}') == 1
        lines = source.replace('{{EFFECTIVE_DATE}}', date).splitlines()
        title = lines[0][2:]
        body = markdown.markdown('\n'.join(lines[2:]), extensions=['sane_lists'])
        alternate = 'ru' if lang == 'en' else 'en'
        output = root/lang/kind/'index.html'
        output.parent.mkdir(parents=True, exist_ok=True)
        output.write_text(f'''<!DOCTYPE html>
<html lang="{lang}">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<meta http-equiv="Content-Security-Policy" content="default-src 'self'; script-src 'none'; object-src 'none'; base-uri 'self'">
<title>{html.escape(title)}</title>
<link rel="canonical" href="{base}{lang}/{kind}/">
<link rel="alternate" hreflang="{alternate}" href="{base}{alternate}/{kind}/">
<link rel="stylesheet" href="../../../../style.css">
<link rel="stylesheet" href="../../style.css">
</head>
<body>
<header><p class="brand">AI Ethnicity: Face Scanner · Android</p><h1>{html.escape(label[kind])}</h1>
<p class="meta">Fablewood Studio · <a href="../../{alternate}/{kind}/">{'Русский' if alternate=='ru' else 'English'}</a></p></header>
<main>{body}</main>
<footer><nav aria-label="{'Legal documents' if lang=='en' else 'Правовые документы'}"><a href="../privacy/">{label['privacy']}</a> · <a href="../terms/">{label['terms']}</a></nav>
<p>Fablewood Studio · <a href="mailto:quicklysearch.bot@gmail.com">quicklysearch.bot@gmail.com</a></p></footer>
</body>
</html>
''', encoding='utf-8')
print('Built four pages; no publication performed.')
