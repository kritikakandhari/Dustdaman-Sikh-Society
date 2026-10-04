import re

with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

# I will find the reviews section I just added and replace its content with an Elfsight placeholder.
# The section started with <section id="reviews"
elfsight_section = """<section id="reviews" class="rv" style="max-width: 1040px; margin: 60px auto 20px; padding: 0 18px;">
    <div style="text-align:center; margin-bottom: 20px;">
        <h2 style="color: var(--ac); font-size:2.2rem; margin-bottom: 10px;"><i class="fa-brands fa-google" style="color:#4285F4;"></i> Google Reviews</h2>
    </div>
    
    <!-- ELFSIGHT WIDGET CODE YAHAN AAYEGA -->
    <script src="https://static.elfsight.com/platform/platform.js" data-use-service-core defer></script>
    <div class="elfsight-app-REPLACE_ME"></div>
    
</section>"""

html = re.sub(r'<section id="reviews".*?<\/section>', elfsight_section, html, flags=re.DOTALL)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html)
