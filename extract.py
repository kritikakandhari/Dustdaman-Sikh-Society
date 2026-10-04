import re
with open('admin.html', 'r', encoding='utf-8') as f:
    html = f.read()

script = re.search(r'<script type="module">([\s\S]*?)<\/script>', html).group(1)
with open('temp.js', 'w', encoding='utf-8') as f:
    f.write(script)
