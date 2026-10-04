import re

with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

# Replace YouTube logic with Native Video
old_bg = """  <div id="hero-vid-bg" style="position:absolute; inset:0; z-index:0; overflow:hidden; background: #1a1a1a;">
    <div id="hero-thumb" style="position:absolute; inset:0; background: url('assets/img/kirtan.jpg') center/cover no-repeat; z-index: 1; transition: opacity 0.8s ease;"></div>
    <div class="video-cover">
      <div id="hero-player" style="width:100%; height:100%; transition: opacity 0.5s; opacity: 0;"></div>
    </div>
    <!-- Dark overlay for cinematic look -->
    <div style="position:absolute; inset:0; background:rgba(0,0,0,0.6); z-index: 2;"></div>
  </div>"""

new_bg = """  <!-- Native Video Background -->
  <video autoplay loop muted playsinline style="position:absolute; inset:0; width:100%; height:100%; object-fit:cover; z-index:0; pointer-events:none;">
    <source src="assets/img/KKDD.mp4" type="video/mp4">
  </video>
  <!-- Dark overlay for cinematic look -->
  <div style="position:absolute; inset:0; background:rgba(0,0,0,0.6); z-index: 1;"></div>"""

html = html.replace(old_bg, new_bg)

# Remove YouTube API Script
html = re.sub(r'<script src="https://www\.youtube\.com/iframe_api"></script>', '', html)
html = re.sub(r'var heroPlayer;\s*var HERO_VIDS = \[.*?\];.*?function onYouTubeIframeAPIReady\(\).*?\}\s*\}', '', html, flags=re.DOTALL)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html)


# Also clean up CSS
with open('assets/css/style.css', 'r', encoding='utf-8') as f:
    css = f.read()

css = re.sub(r'\.video-cover \{.*?\}', '', css, flags=re.DOTALL)
css = re.sub(r'#hero-thumb \{.*?\}', '', css, flags=re.DOTALL)

with open('assets/css/style.css', 'w', encoding='utf-8') as f:
    f.write(css)
