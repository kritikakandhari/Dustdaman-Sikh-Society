import glob
import re

for f in glob.glob('*.html'):
    with open(f, 'r', encoding='utf-8') as file:
        html = file.read()
        
    # JSON-LD replacements
    html = html.replace('267-12899 76 Ave', 'Unit 267, 12899 79 Ave')
    
    # HTML text replacements
    html = html.replace('267# 12899 76 Ave, Surrey, BC V3W 1E6', 'Unit 267, 12899 79 Ave, Surrey, BC V3W 1E6')
    html = html.replace('267# 12899 76 Ave', 'Unit 267, 12899 79 Ave')
    
    # Google Maps iframe replacements
    html = html.replace('12899+76+Ave', '12899+79+Ave')
    
    # Contact page directions link
    html = html.replace('12899+76+Ave+Surrey+BC+V3W+1E6', '12899+79+Ave+Surrey+BC+V3W+1E6')
    
    with open(f, 'w', encoding='utf-8') as file:
        file.write(html)
