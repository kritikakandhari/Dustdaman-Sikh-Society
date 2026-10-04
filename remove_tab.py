import re

with open('admin.html', 'r', encoding='utf-8') as f:
    html = f.read()

# Remove the tab button
html = re.sub(r'<button class="adm-tab" onclick="showTab\(\'tab-text\', this\)".*?<\/button>', '', html, flags=re.DOTALL)

# Remove the tab panel
html = re.sub(r'<div id="tab-text" class="tab-panel".*?<!-- End of admin panels -->', '<!-- End of admin panels -->', html, flags=re.DOTALL)

with open('admin.html', 'w', encoding='utf-8') as f:
    f.write(html)
