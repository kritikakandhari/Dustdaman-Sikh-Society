import re

with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

# Change 'about' wrapper to white
html = html.replace('<div class="section-yellow" style="padding: 60px 0;">\n  <section id="about"', '<div class="section-white" style="padding: 60px 0;">\n  <section id="about"')
html = html.replace('<div class="section-yellow" style="padding: 60px 0;">\n<section id="about"', '<div class="section-white" style="padding: 60px 0;">\n<section id="about"')

# Change 'videos' wrapper to white
html = html.replace('<div class="section-yellow" style="padding: 60px 0;">\n  <section id="videos"', '<div class="section-white" style="padding: 60px 0;">\n  <section id="videos"')
html = html.replace('<div class="section-yellow" style="padding: 60px 0;">\n<section id="videos"', '<div class="section-white" style="padding: 60px 0;">\n<section id="videos"')

# Change 'location' wrapper to white
html = html.replace('<div class="section-yellow" style="padding: 60px 0;">\n  <section id="location"', '<div class="section-white" style="padding: 60px 0;">\n  <section id="location"')
html = html.replace('<div class="section-yellow" style="padding: 60px 0;">\n<section id="location"', '<div class="section-white" style="padding: 60px 0;">\n<section id="location"')

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html)
