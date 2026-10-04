import glob
import re

for f in glob.glob('*.html'):
    with open(f, 'r', encoding='utf-8') as file:
        html = file.read()
    
    # 1. Remove the custom Google Reviews heading
    html = re.sub(r'<div style="text-align:center; margin-bottom: 20px;">\s*<h2 style="color: var\(--ac\); font-size:2\.2rem; margin-bottom: 10px;"><i class="fa-brands fa-google" style="color:#4285F4;"><\/i> Google Reviews<\/h2>\s*<\/div>', '', html)
    
    # 2. Update Google Fonts link from Poppins to Lora
    html = html.replace('family=Poppins:wght@400;600;700', 'family=Lora:ital,wght@0,400;0,500;0,600;0,700;1,400')
    
    with open(f, 'w', encoding='utf-8') as file:
        file.write(html)

# 3. Update style.css to use Lora instead of Poppins
with open('style.css', 'r', encoding='utf-8') as f:
    css = f.read()

css = css.replace("font-family:'Poppins'", "font-family:'Lora', serif")
# Also just in case there's a fallback without Poppins
css = re.sub(r"font-family:\s*'Poppins'[^;]*;", "font-family: 'Lora', serif;", css)

with open('style.css', 'w', encoding='utf-8') as f:
    f.write(css)
