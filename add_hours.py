import glob, re

for f in glob.glob('*.html'):
    if f == 'admin.html': continue
    with open(f, 'r', encoding='utf-8') as file:
        content = file.read()
    
    new_contact = '''<div class="f-contact">
    <h3>Contact Us</h3>
    <a href="tel:+16049024769"><i class="fa-solid fa-phone"></i> +1 (604) 902-4769</a>
    <span style="display:block; padding: 6px 0; font-size: 0.95rem; color: var(--tx);"><i class="fa-regular fa-clock" style="color:var(--pr); width:20px; text-align:center; margin-right:8px;"></i> 7:00 AM - 7:00 PM (Monday Closed)</span>
    <a href="mailto:dustdamansikhsociety@gmail.com"><i class="fa-solid fa-envelope"></i> dustdamansikhsociety@gmail.com</a>
    <a href="https://youtube.com/@dustdamansikhsociety2023?si=8NLfI50wWl8-PMSh" target="_blank" rel="noopener"><i class="fa-brands fa-youtube" style="color:#ef4444;"></i> YouTube Channel</a>
  </div>'''
    
    # We will just replace the inner part to be safe
    content = re.sub(r'<div class="f-contact">.*?</div>', new_contact, content, flags=re.DOTALL)
    
    with open(f, 'w', encoding='utf-8') as file:
        file.write(content)
