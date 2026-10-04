import re

with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

maps_section = """
<section id="location" class="rv" style="max-width: 1040px; margin: 40px auto 40px; padding: 0 18px;">
    <h2 style="text-align:center; color: var(--ac); font-size:2.2rem; margin-bottom: 30px;"><i class="fa-solid fa-map-location-dot"></i> Our Location</h2>
    <div style="width:100%; border-radius:16px; overflow:hidden; box-shadow:0 4px 15px rgba(0,0,0,0.05); border: 2px solid var(--bd);">
        <iframe src="https://www.google.com/maps?q=Dustdaman+Sikh+Society,+12899+76+Ave,+Surrey,+BC+V3W+1E6&output=embed" width="100%" height="400" style="border:0; display:block;" allowfullscreen="" loading="lazy" referrerpolicy="no-referrer-when-downgrade"></iframe>
    </div>
    <div style="text-align:center; margin-top:20px;">
        <p style="color:var(--mu); font-size:1.1rem;"><i class="fa-solid fa-location-dot" style="color:var(--pr);"></i> 267# 12899 76 Ave, Surrey, BC V3W 1E6</p>
    </div>
</section>
"""

html = html.replace('</section>\n<footer>', '</section>\n' + maps_section + '\n<footer>')

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html)
