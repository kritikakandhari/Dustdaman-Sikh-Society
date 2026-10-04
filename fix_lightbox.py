import re

with open('gallery.html', 'r', encoding='utf-8') as f:
    html = f.read()

# Fix close button HTML
html = re.sub(
    r'<span id="lightbox-close".*?</span>', 
    '<span id="lightbox-close" onclick="closeLightbox()"><i class="fa-solid fa-xmark"></i></span>', 
    html
)

# Add closeLightbox function and background click listener
new_func = """
window.openLightbox = (url) => {
  document.getElementById('lightbox-img').src = url;
  document.getElementById('lightbox').classList.add('on');
};
window.closeLightbox = () => {
  document.getElementById('lightbox').classList.remove('on');
};
document.getElementById('lightbox').addEventListener('click', function(e) {
  if (e.target === this) closeLightbox();
});
"""

html = re.sub(r'window\.openLightbox =[\s\S]*?classList\.add\(\'on\'\);\s*};', new_func, html)

# Fix CSS for close button
css_close = """
#lightbox-close { position: absolute; top: 20px; right: 30px; color: #fff; font-size: 2.5rem; cursor: pointer; text-shadow: 0 2px 10px rgba(0,0,0,0.8); z-index: 1001; transition: 0.2s; }
#lightbox-close:hover { color: #facc15; transform: scale(1.1); }
"""
html = re.sub(r'#lightbox-close\s*\{.*?\}', css_close.strip(), html)

# Ensure img object-fit is set
html = html.replace('#lightbox img { max-width: 92vw; max-height: 88vh; border-radius: 10px; }', '#lightbox img { max-width: 92vw; max-height: 88vh; border-radius: 10px; object-fit: contain; }')

# If they meant the gallery grid images are cropping: 
# Currently it's `object-fit: cover`. Let's keep it cover because contain creates ugly black bars.
# The user's screenshot was IN the lightbox, and they said "esko back krne ki option nhi hai".

with open('gallery.html', 'w', encoding='utf-8') as f:
    f.write(html)
