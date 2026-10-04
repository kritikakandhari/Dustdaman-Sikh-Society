import glob
import re

for f in glob.glob('*.html'):
    with open(f, 'r', encoding='utf-8') as file:
        html = file.read()
    
    # Remove old marquee
    html = re.sub(r'<div style="background: var\(--pr\); color: #451a03; padding: 6px 0; font-size: 1\.2rem; font-weight: 700; border-bottom: 2px solid #ca8a04;">\s*<marquee[^>]*>.*?<\/marquee>\s*<\/div>', '', html, flags=re.DOTALL)
    
    # Fix empty newlines created by removal
    html = html.replace('<body>\n\n<header>', '<body>\n<header>')
    
    with open(f, 'w', encoding='utf-8') as file:
        file.write(html)

with open('style.css', 'r', encoding='utf-8') as f:
    css = f.read()

# Remove h2 line
css = re.sub(r'h2:after\{.*?\}', '', css)

# Update h2 styles to be centered and clean
css = re.sub(r'h2\{.*?\}', 'h2{color:var(--ac);font-size:2.2rem;margin:0 0 30px;text-align:center;font-weight:700;}', css)

# Update body background to white
css = re.sub(r'body\{([^}]+)background:var\(--bg\)', r'body{\1background:#ffffff', css)

# Add seamless marquee CSS
marquee_css = """
.marquee-wrapper {
  overflow: hidden;
  white-space: nowrap;
  background: var(--pr);
  color: #451a03;
  padding: 12px 0;
  font-size: 1.3rem;
  font-weight: 700;
  border-bottom: 3px solid #ca8a04;
  border-top: 3px solid #ca8a04;
  position: relative;
  display: flex;
}
.marquee-content {
  display: flex;
  animation: marquee-scroll 30s linear infinite;
}
.marquee-content span {
  padding: 0 40px;
}
@keyframes marquee-scroll {
  0% { transform: translateX(0); }
  100% { transform: translateX(-50%); }
}
.section-yellow {
  background-color: var(--bg); /* #fffbeb */
  border-top: 1px solid #fef08a;
  border-bottom: 1px solid #fef08a;
}
.section-white {
  background-color: #ffffff;
}
"""
css += marquee_css

with open('style.css', 'w', encoding='utf-8') as f:
    f.write(css)
