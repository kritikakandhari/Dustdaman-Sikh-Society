import glob

marquee_html = """
<div style="background: var(--pr); color: #451a03; padding: 6px 0; font-size: 1.2rem; font-weight: 700; border-bottom: 2px solid #ca8a04;">
  <marquee scrollamount="6">ਸਤਿਨਾਮ ਵਾਹਿਗੁਰੂ &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; ਸਤਿਨਾਮ ਵਾਹਿਗੁਰੂ &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; ਸਤਿਨਾਮ ਵਾਹਿਗੁਰੂ &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; ਸਤਿਨਾਮ ਵਾਹਿਗੁਰੂ &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; ਸਤਿਨਾਮ ਵਾਹਿਗੁਰੂ &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; ਸਤਿਨਾਮ ਵਾਹਿਗੁਰੂ &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; ਸਤਿਨਾਮ ਵਾਹਿਗੁਰੂ &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; ਸਤਿਨਾਮ ਵਾਹਿਗੁਰੂ</marquee>
</div>
"""

for f in glob.glob('*.html'):
    if f == 'admin.html': continue
    with open(f, 'r', encoding='utf-8') as file:
        html = file.read()
    
    # Don't add if already added
    if "ਸਤਿਨਾਮ ਵਾਹਿਗੁਰੂ" not in html:
        html = html.replace('<body>\n<header>', '<body>\n' + marquee_html.strip() + '\n<header>')
        # If the file doesn't have a newline
        html = html.replace('<body><header>', '<body>\n' + marquee_html.strip() + '\n<header>')
        
        with open(f, 'w', encoding='utf-8') as file:
            file.write(html)
