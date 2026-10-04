with open('script.js', 'r', encoding='utf-8') as f:
    js = f.read()

js = js.replace('"Gurbani Kirtan in a welcoming environment."', '"Gurbani Kirtan in a welcoming environment.<br><br><span style=\'color:var(--pr); font-weight:600;\'><i class=\'fa-solid fa-phone\'></i> For kirtan classes contact +1 778-712-0977</span>"')

with open('script.js', 'w', encoding='utf-8') as f:
    f.write(js)
