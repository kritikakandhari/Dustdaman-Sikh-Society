import re

with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

# Add the seamless marquee right before <section id="about">
seamless_marquee = """
<div class="marquee-wrapper">
  <div class="marquee-content">
    <span>ਸਤਿਨਾਮ ਵਾਹਿਗੁਰੂ</span><span>ਸਤਿਨਾਮ ਵਾਹਿਗੁਰੂ</span><span>ਸਤਿਨਾਮ ਵਾਹਿਗੁਰੂ</span><span>ਸਤਿਨਾਮ ਵਾਹਿਗੁਰੂ</span><span>ਸਤਿਨਾਮ ਵਾਹਿਗੁਰੂ</span>
    <span>ਸਤਿਨਾਮ ਵਾਹਿਗੁਰੂ</span><span>ਸਤਿਨਾਮ ਵਾਹਿਗੁਰੂ</span><span>ਸਤਿਨਾਮ ਵਾਹਿਗੁਰੂ</span><span>ਸਤਿਨਾਮ ਵਾਹਿਗੁਰੂ</span><span>ਸਤਿਨਾਮ ਵਾਹਿਗੁਰੂ</span>
    <!-- Duplicated for seamless loop -->
    <span>ਸਤਿਨਾਮ ਵਾਹਿਗੁਰੂ</span><span>ਸਤਿਨਾਮ ਵਾਹਿਗੁਰੂ</span><span>ਸਤਿਨਾਮ ਵਾਹਿਗੁਰੂ</span><span>ਸਤਿਨਾਮ ਵਾਹਿਗੁਰੂ</span><span>ਸਤਿਨਾਮ ਵਾਹਿਗੁਰੂ</span>
    <span>ਸਤਿਨਾਮ ਵਾਹਿਗੁਰੂ</span><span>ਸਤਿਨਾਮ ਵਾਹਿਗੁਰੂ</span><span>ਸਤਿਨਾਮ ਵਾਹਿਗੁਰੂ</span><span>ਸਤਿਨਾਮ ਵਾਹਿਗੁਰੂ</span><span>ਸਤਿਨਾਮ ਵਾਹਿਗੁਰੂ</span>
  </div>
</div>
"""
html = html.replace('<section id="about"', seamless_marquee + '\n<div class="section-yellow" style="padding: 60px 0;">\n<section id="about"')

# We must close the wrapper div after the about section ends.
# About section ends right before <section id="act-preview">
html = html.replace('<section id="act-preview"', '</div>\n\n<div class="section-white" style="padding: 60px 0;">\n<section id="act-preview"')

# act-preview has inline background #fffbeb which clashes with our pattern, let's remove it
html = html.replace('style="background: #fffbeb; padding-top:60px; padding-bottom:60px; margin-top:40px; border-radius: 20px;"', '')

# act-preview ends right before <section class="rv" style="text-align:center; padding: 60px 18px; background: #fff;"> (the videos section)
html = html.replace('<section class="rv" style="text-align:center; padding: 60px 18px; background: #fff;">', '</div>\n\n<div class="section-yellow" style="padding: 60px 0;">\n<section id="videos" class="rv" style="text-align:center;">')
# Remove old videos heading if we want, wait, it has <h2 data-i="s1"></h2> inside it. It doesn't have an ID in HTML? Ah, it didn't have ID. I added id="videos".

# The videos section ends right before <section id="reviews"
html = html.replace('<section id="reviews"', '</div>\n\n<div class="section-white" style="padding: 60px 0;">\n<section id="reviews"')

# Reviews section ends right before <section id="location"
html = html.replace('<section id="location"', '</div>\n\n<div class="section-yellow" style="padding: 60px 0;">\n<section id="location"')

# Location section ends right before <footer>
html = html.replace('<footer>', '</div>\n\n<footer>')

# Also remove inline margins from sections because padding on wrappers handles spacing now
html = re.sub(r'(<section[^>]*?)max-width:\s*\d+px;\s*margin:\s*[^;]+;?', r'\1', html)
html = re.sub(r'(<section[^>]*?)margin-bottom:\s*[^;]+;?', r'\1', html)
html = re.sub(r'(<section[^>]*?)margin-top:\s*[^;]+;?', r'\1', html)

# Some h2 inline styles override the new css, let's clean them up
html = re.sub(r'<h2 style="[^"]*?"', '<h2', html)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html)
