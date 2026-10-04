import re

with open('admin.html', 'r', encoding='utf-8') as f:
    html = f.read()

# Remove the button
html = re.sub(r'<button class="adm-tab" onclick="showTab\(\'tab-text\', this\)".*?<\/button>', '', html, flags=re.DOTALL)

# Remove the whole tab-text div
# Since it's the last tab, it ends just before the closing </div> of adm-wrap.
start = html.find('<!-- TAB 2: TEXT -->')
end = html.find('<script type="module">')

if start != -1 and end != -1:
    # the </script> is right after the admin-panel div.
    # so we should keep the last `</div></div>` which close `adm-wrap` and `admin-panel`
    part1 = html[:start]
    part2 = html[end:]
    
    # Actually, part2 is `<script...` which means we cut out the closing `</div></div>`.
    # Let's put them back.
    html = part1 + "    </div>\n  </div>\n\n  " + part2

with open('admin.html', 'w', encoding='utf-8') as f:
    f.write(html)
