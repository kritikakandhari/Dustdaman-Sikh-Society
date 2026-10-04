import glob

for f in glob.glob('*.html'):
    with open(f, 'r', encoding='utf-8') as file:
        html = file.read()
        
    # Replace in normal text
    html = html.replace('Unit 267, 12899 79 Ave', '12899 79 Ave, Unit 267')
    
    with open(f, 'w', encoding='utf-8') as file:
        file.write(html)
