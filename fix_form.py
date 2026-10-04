import re

with open('contact.html', 'r', encoding='utf-8') as f:
    html = f.read()

old_form = '<div id="cf"><input id="cn" data-ph="fN"><textarea id="cm" rows="4" data-ph="fM"></textarea><button id="cs" data-i="fS"></button></div>'
new_form = """<form id="cf" action="https://formsubmit.co/dustdamansikhsociety@gmail.com" method="POST">
  <input type="hidden" name="_subject" value="New message from Website">
  <input type="hidden" name="_captcha" value="false">
  <input type="text" id="cn" name="Name" required data-ph="fN">
  <textarea id="cm" name="Message" rows="4" required data-ph="fM"></textarea>
  <button type="submit" id="cs" data-i="fS"></button>
</form>"""

html = html.replace(old_form, new_form)

with open('contact.html', 'w', encoding='utf-8') as f:
    f.write(html)
