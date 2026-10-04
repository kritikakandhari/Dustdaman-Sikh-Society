import re

with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

# Replace switchHeroVid
js_to_replace = r"""function switchHeroVid\(idx\) \{
  clearTimeout\(heroTimer\);
  heroCurIdx = idx;
  if \(heroPlayer && heroPlayer\.loadVideoById\) \{
    heroPlayer\.loadVideoById\(\{videoId: HERO_VIDS\[idx\], startSeconds: 10\}\);
  \}
  document\.querySelectorAll\('\.vid-dot'\)\.forEach\(function\(d,i\)\{
    d\.style\.background = i === idx \? '#ca8a04' : 'rgba\(202,138,4,0\.35\)';
  \}\);
  startHeroTimer\(\);
\}"""

new_switch_js = """function switchHeroVid(idx) {
  clearTimeout(heroTimer);
  heroCurIdx = idx;
  
  // Update Thumbnail Image Instantly
  var thumb = document.getElementById('hero-thumb');
  var playerDiv = document.getElementById('hero-player');
  if(thumb && playerDiv) {
      thumb.style.backgroundImage = "url('https://img.youtube.com/vi/" + HERO_VIDS[idx] + "/maxresdefault.jpg')";
      thumb.style.opacity = '1';
      playerDiv.style.opacity = '0';
  }

  if (heroPlayer && heroPlayer.loadVideoById) {
    heroPlayer.loadVideoById({videoId: HERO_VIDS[idx], startSeconds: 10});
  }
  document.querySelectorAll('.vid-dot').forEach(function(d,i){
    d.style.background = i === idx ? '#ca8a04' : 'rgba(202,138,4,0.35)';
  });
  startHeroTimer();
}"""

html = re.sub(js_to_replace, new_switch_js, html, flags=re.MULTILINE)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html)
