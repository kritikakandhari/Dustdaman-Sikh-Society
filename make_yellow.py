import re

with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

# Replace the white wrapper for act-preview
html = html.replace('<div class="section-white" style="padding: 60px 0;">\n<section id="act-preview"', '<div class="section-yellow" style="padding: 60px 0;">\n<section id="act-preview"')

# Replace the white wrapper for reviews
html = html.replace('<div class="section-white" style="padding: 60px 0;">\n<section id="reviews"', '<div class="section-yellow" style="padding: 60px 0;">\n<section id="reviews"')

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html)
