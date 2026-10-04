import re

with open('contact.html', 'r', encoding='utf-8') as f:
    html = f.read()

html = html.replace(
    '<p><i class="fa-solid fa-phone"></i> <a href="tel:+16049024769">+1 (604) 902-4769</a></p>',
    '<p><i class="fa-solid fa-phone"></i> <a href="tel:+16049024769">+1 (604) 902-4769</a></p>\n<p><i class="fa-regular fa-clock" style="color:var(--pr);"></i> 7:00 AM - 7:00 PM (Monday Closed)</p>'
)

with open('contact.html', 'w', encoding='utf-8') as f:
    f.write(html)
