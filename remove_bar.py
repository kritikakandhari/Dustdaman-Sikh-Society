import glob, re
for f in glob.glob('*.html'):
    with open(f, 'r', encoding='utf-8') as file:
        content = file.read()
    if '<div class="bar">' in content:
        print('Removing bar from ' + f)
        # only match the bar div and its immediate closing div
        content = re.sub(r'<div class="bar">.*?</div>\n?', '', content, flags=re.DOTALL)
        with open(f, 'w', encoding='utf-8') as file:
            file.write(content)
