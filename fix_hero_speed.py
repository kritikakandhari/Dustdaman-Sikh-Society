import re

with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

# 1. Add background image to hero-vid-bg and an overlay thumbnail that we can fade out
new_hero_bg = """
  <!-- Video Carousel Background -->
  <div id="hero-vid-bg" style="position:absolute; inset:0; z-index:0; overflow:hidden; background: #1a1a1a;">
    <div id="hero-thumb" style="position:absolute; inset:0; background: url('https://img.youtube.com/vi/xDVx1Yb7sCQ/maxresdefault.jpg') center/cover no-repeat; z-index: 1; transition: opacity 0.8s ease;"></div>
    <div style="position:absolute; top:50%; left:50%; width:150%; height:150%; transform:translate(-50%,-50%); pointer-events:none; z-index: 0;">
      <div id="hero-player" style="width:100%; height:100%; transition: opacity 0.5s; opacity: 0;"></div>
    </div>
    <!-- Dark overlay for cinematic look -->
    <div style="position:absolute; inset:0; background:rgba(0,0,0,0.6); z-index: 2;"></div>
  </div>
"""

# Replace the existing hero-vid-bg
html = re.sub(r'<!-- Video Carousel Background -->[\s\S]*?<!-- Dark overlay for cinematic look -->\s*<div style="position:absolute; inset:0; background:rgba\(0,0,0,0\.6\);"><\/div>\s*<\/div>', new_hero_bg.strip(), html)

# 2. Update the JS to handle fading out the thumbnail and fading in the player
# Also update switchHeroVid to change the thumbnail
# I need to find switchHeroVid function
js_to_replace = r"""window\.switchHeroVid = function\(index\) \{
      if \(index === currentHeroVidIndex\) return;
      currentHeroVidIndex = index;
      if \(heroPlayer && heroPlayer\.loadVideoById\) \{
          heroPlayer\.loadVideoById\(HERO_VIDS\[index\]\);
          heroPlayer\.seekTo\(10, true\);
      \}
      var dots = document\.querySelectorAll\('\.vid-dot'\);
      dots\.forEach\(\(d, i\) => \{
          d\.style\.background = i === index \? '#ca8a04' : 'rgba\(202,138,4,0\.35\)';
          if \(i === index\) d\.classList\.add\('active'\);
          else d\.classList\.remove\('active'\);
      \}\);
  \};"""

new_switch_js = """window.switchHeroVid = function(index) {
      if (index === currentHeroVidIndex) return;
      currentHeroVidIndex = index;
      
      // Reset thumbnail to hide buffering
      var thumb = document.getElementById('hero-thumb');
      var playerDiv = document.getElementById('hero-player');
      thumb.style.backgroundImage = "url('https://img.youtube.com/vi/" + HERO_VIDS[index] + "/maxresdefault.jpg')";
      thumb.style.opacity = '1';
      playerDiv.style.opacity = '0';

      if (heroPlayer && heroPlayer.loadVideoById) {
          heroPlayer.loadVideoById(HERO_VIDS[index]);
          heroPlayer.seekTo(10, true);
      }
      var dots = document.querySelectorAll('.vid-dot');
      dots.forEach((d, i) => {
          d.style.background = i === index ? '#ca8a04' : 'rgba(202,138,4,0.35)';
          if (i === index) d.classList.add('active');
          else d.classList.remove('active');
      });
  };"""

html = re.sub(js_to_replace, new_switch_js, html)

# 3. Update onStateChange to fade out thumbnail when PLAYING
# Find the events block
onready_block = r"""'onReady': function\(e\)\{ 
                    e\.target\.seekTo\(10, true\); 
                    e\.target\.playVideo\(\); 
                    setInterval\(function\(\) \{
                        if \(e\.target\.getCurrentTime && e\.target\.getCurrentTime\(\) >= 30\) \{
                            e\.target\.seekTo\(10, true\);
                        \}
                    \}, 500\);
                \},
                'onStateChange': function\(e\)\{ \}"""

new_onready_block = """'onReady': function(e){ 
                    e.target.seekTo(10, true); 
                    e.target.playVideo(); 
                    setInterval(function() {
                        if (e.target.getCurrentTime && e.target.getCurrentTime() >= 30) {
                            e.target.seekTo(10, true);
                        }
                    }, 500);
                },
                'onStateChange': function(e){
                    if (e.data === YT.PlayerState.PLAYING) {
                        document.getElementById('hero-thumb').style.opacity = '0';
                        document.getElementById('hero-player').style.opacity = '1';
                    }
                }"""

html = re.sub(onready_block, new_onready_block, html)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html)
