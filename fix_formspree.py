import re

with open('contact.html', 'r', encoding='utf-8') as f:
    html = f.read()

old_form_match = re.search(r'<form id="cf".*?<\/form>', html, re.DOTALL)
if old_form_match:
    old_form = old_form_match.group(0)
    new_form = """<form id="cf" action="https://formspree.io/f/YOUR_FORMSPREE_ID" method="POST">
  <input type="text" id="cn" name="name" required data-ph="fN" placeholder="Your name">
  <input type="email" id="ce" name="email" required placeholder="Your email">
  <textarea id="cm" name="message" rows="4" required data-ph="fM" placeholder="Your message"></textarea>
  <button type="submit" id="cs" data-i="fS">Send by email</button>
</form>"""
    html = html.replace(old_form, new_form)
    
    with open('contact.html', 'w', encoding='utf-8') as f:
        f.write(html)
