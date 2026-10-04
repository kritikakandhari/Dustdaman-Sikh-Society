import re

with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

html = re.sub(r'<div style="text-align:center; margin-bottom: 20px;">\s*<h2><i class="fa-brands fa-google"[^>]*><\/i> Google Reviews<\/h2>\s*<\/div>', '', html)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html)
