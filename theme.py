import re

with open('style.css', 'r', encoding='utf-8') as f:
    css = f.read()

# Remove dark mode completely
css = re.sub(r'@media\(prefers-color-scheme:dark\)\{.*?\}', '', css)
css = re.sub(r':root\[data-theme="dark"\]\{.*?\}', '', css)

# Update variables to white/yellow theme
css = css.replace(
    ':root{--bg:#f8fafc;--card:#ffffff;--tx:#0f172a;--mu:#475569;--pr:#1d4ed8;--pr2:#1e3a8a;--ac:#ea580c;--gd:#f59e0b;--bd:#e2e8f0;--sh:0 10px 15px -3px rgba(0,0,0,.1),0 4px 6px -4px rgba(0,0,0,.1);box-sizing:border-box;padding-top:env(safe-area-inset-top,0px);padding-bottom:env(safe-area-inset-bottom,0px)}',
    ':root{--bg:#ffffff;--card:#ffffff;--tx:#333333;--mu:#666666;--pr:#eab308;--pr2:#facc15;--ac:#ca8a04;--gd:#fef08a;--bd:#fde047;--sh:0 10px 15px -3px rgba(0,0,0,.1),0 4px 6px -4px rgba(0,0,0,.1);box-sizing:border-box;padding-top:env(safe-area-inset-top,0px);padding-bottom:env(safe-area-inset-bottom,0px)}'
)

# Fix hero
hero_old = r'.hero{position:relative;text-align:center;padding:80px 16px 120px;color:#fff;overflow:hidden;background:radial-gradient(circle at 20% 20%,rgba(245,158,11,.35),transparent 40%),radial-gradient(circle at 85% 70%,rgba(234,88,12,.3),transparent 40%),linear-gradient(160deg,#1e3a8a,#0f172a)}'
hero_new = r'.hero{position:relative;text-align:center;padding:80px 16px 120px;color:#5a3811;overflow:hidden;background:radial-gradient(circle at 20% 20%,rgba(250,204,21,.4),transparent 40%),radial-gradient(circle at 85% 70%,rgba(253,224,71,.5),transparent 40%),linear-gradient(160deg,#ffffff,#fef9c3)}'
css = css.replace(hero_old, hero_new)

# Fix hero dots pattern (was white dots, make them yellow)
css = css.replace('radial-gradient(rgba(255,255,255,.12) 2px,transparent 2px)', 'radial-gradient(rgba(202,138,4,.12) 2px,transparent 2px)')

# Fix header and top colors
css = css.replace('border-bottom:3px solid var(--ac)', 'border-bottom:3px solid var(--pr)')
css = css.replace('.top{background:var(--pr2);color:#fff', '.top{background:#fff;color:#5a3811;border-bottom:1px solid var(--bd)')
css = css.replace('.top a{color:#fff', '.top a{color:#5a3811')

# Fix footer and bar
css = css.replace('footer{text-align:center;padding:26px;color:#fff;background:var(--pr2);border-top:5px solid var(--ac)}', 'footer{text-align:center;padding:26px;color:#5a3811;background:#fef9c3;border-top:5px solid var(--pr)}')
css = css.replace('.bar{position:fixed;bottom:0;left:0;right:0;background:var(--pr2)', '.bar{position:fixed;bottom:0;left:0;right:0;background:#fff;border-top:2px solid var(--bd)')
css = css.replace('.bar a{display:block;flex:1;text-align:center;color:#fff', '.bar a{display:block;flex:1;text-align:center;color:#5a3811')

# Fix buttons
css = css.replace('button,.btn{background:linear-gradient(135deg,var(--ac),var(--gd));color:#fff;', 'button,.btn{background:linear-gradient(135deg,#ca8a04,#facc15);color:#fff;')
css = css.replace('button.alt{background:var(--pr2);color:#fff;', 'button.alt{background:#eab308;color:#fff;')

with open('style.css', 'w', encoding='utf-8') as f:
    f.write(css)
print("Done")
