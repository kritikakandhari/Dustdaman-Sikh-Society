import re

with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

elfsight_code = """
<!-- Elfsight Google Reviews -->
<script src="https://elfsightcdn.com/platform.js" async></script>
<div class="elfsight-app-ed19ba72-a9b2-4929-8f5c-10d361804603" data-elfsight-app-lazy></div>
"""

# The current placeholder is:
# <!-- ELFSIGHT WIDGET CODE YAHAN AAYEGA -->
# <script src="https://static.elfsight.com/platform/platform.js" data-use-service-core defer></script>
# <div class="elfsight-app-REPLACE_ME"></div>

html = re.sub(r'<!-- ELFSIGHT WIDGET CODE YAHAN AAYEGA -->[\s\S]*?<\/div>', elfsight_code.strip(), html)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html)
