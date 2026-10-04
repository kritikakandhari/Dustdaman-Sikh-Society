import re

with open('style.css', 'r', encoding='utf-8') as f:
    css = f.read()

css = re.sub(r'font-family:[^;]+;', "font-family: 'Lora', 'Noto Sans Gurmukhi', serif;", css)

with open('style.css', 'w', encoding='utf-8') as f:
    f.write(css)
