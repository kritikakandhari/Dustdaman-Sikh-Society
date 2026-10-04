import re

with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

# The welcome section currently looks like:
# <section class="rv" style="text-align:center;  padding: 0 18px;">
#     <h2 data-i="welcomeT"></h2>
#     <p style="font-size: 1.15rem; color: var(--mu); line-height: 1.8;" data-i="welcomeP"></p>
# </section>

# Let's wrap it in a .section-white with padding.
replacement = """
<div class="section-white" style="padding: 80px 0 60px;">
  <section class="rv" style="text-align:center; max-width: 900px; margin: 0 auto; padding: 0 18px;">
      <h2 data-i="welcomeT"></h2>
      <p style="font-size: 1.15rem; color: var(--mu); line-height: 1.8;" data-i="welcomeP"></p>
  </section>
</div>
"""

# Regex to match the welcome section safely
html = re.sub(r'<section class="rv" style="text-align:center;\s*padding: 0 18px;">\s*<h2 data-i="welcomeT"><\/h2>\s*<p style="[^"]*" data-i="welcomeP"><\/p>\s*<\/section>', replacement.strip(), html)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html)
