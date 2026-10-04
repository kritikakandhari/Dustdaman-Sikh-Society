import re

with open('contact.html', 'r', encoding='utf-8') as f:
    html = f.read()

maps_iframe = """
<div style="margin-top: 40px;">
  <h3 style="color: var(--ac); margin-bottom: 20px;"><i class="fa-solid fa-map-location-dot"></i> Our Location</h3>
  <iframe src="https://www.google.com/maps?q=Dustdaman+Sikh+Society,+12899+76+Ave,+Surrey,+BC+V3W+1E6&output=embed" width="100%" height="400" style="border:0; border-radius: 16px; box-shadow: 0 4px 15px rgba(0,0,0,0.05);" allowfullscreen="" loading="lazy" referrerpolicy="no-referrer-when-downgrade"></iframe>
</div>
"""

html = html.replace('</div></div></section>', '</div></div>' + maps_iframe + '</section>')

with open('contact.html', 'w', encoding='utf-8') as f:
    f.write(html)
