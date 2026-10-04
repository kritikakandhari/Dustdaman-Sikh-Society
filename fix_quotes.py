import glob

for html_file in glob.glob('*.html'):
    with open(html_file, 'r', encoding='utf-8') as f:
        html = f.read()
    
    html = html.replace(r"\'nav\'", "'nav'")
    html = html.replace(r"\'active\'", "'active'")
    
    with open(html_file, 'w', encoding='utf-8') as f:
        f.write(html)
