import re

with open('admin.html', 'r', encoding='utf-8') as f:
    html = f.read()

# Remove loadTextFields call
html = html.replace('loadTextFields();', '')

# Remove loadTextFields definition
html = re.sub(r'async function loadTextFields\(\)[\s\S]*?\}\s*\}', '', html)

# Remove saveText definition
html = re.sub(r'window\.saveText = async[\s\S]*?\}\s*\};', '', html)

with open('admin.html', 'w', encoding='utf-8') as f:
    f.write(html)
