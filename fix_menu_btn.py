import glob
import re

for html_file in glob.glob('*.html'):
    with open(html_file, 'r', encoding='utf-8') as f:
        html = f.read()
    
    if 'class="menu-btn"' not in html:
        html = re.sub(
            r'(<b data-i="name"><\/b>)', 
            r'\1\n  <button class="menu-btn" onclick="document.querySelector(\'nav\').classList.toggle(\'active\')"><i class="fa-solid fa-bars"></i></button>', 
            html
        )
    
    with open(html_file, 'w', encoding='utf-8') as f:
        f.write(html)
