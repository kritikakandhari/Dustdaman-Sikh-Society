import glob

for f in glob.glob('*.html'):
    with open(f, 'r', encoding='utf-8') as file:
        html = file.read()
    
    # Replace in Directions link
    html = html.replace('12899+79+Ave+Surrey+BC+V3W+1E6', '12899+79+Ave,+Unit+267,+Surrey,+BC+V3W+1E6')
    
    # Replace in iframe query
    html = html.replace('Dustdaman+Sikh+Society,+12899+79+Ave,+Surrey,+BC+V3W+1E6', 'Dustdaman+Sikh+Society,+12899+79+Ave,+Unit+267,+Surrey,+BC+V3W+1E6')
    
    with open(f, 'w', encoding='utf-8') as file:
        file.write(html)
