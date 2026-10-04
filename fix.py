import re

with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

# Let's cleanly remove any script tag containing HERO_VIDS
html = re.sub(r'<script>\s*var HERO_VIDS.*?</script>', '', html, flags=re.DOTALL)
# Remove the broken remaining lines (like "      }\n    }\n  });\n}\n") that I left by mistake
html = re.sub(r'\s*\}\s*\}\s*\}\);\s*\}\s*function startHeroTimer\(\) \{.*?switchHeroVid\(heroCurIdx\);\s*\}', '', html, flags=re.DOTALL)
# Remove the old youtube API init
html = re.sub(r'<script>\s*var tag = document\.createElement.*?clickTimers.*?</script>', '', html, flags=re.DOTALL)


unified_script = """
<script>
// --- HERO VIDEO CAROUSEL ---
var HERO_VIDS = ['xDVx1Yb7sCQ', 'GYaoqV-mCA4'];
var heroPlayer, heroCurIdx = 0, heroTimer;

function startHeroTimer() {
  heroTimer = setTimeout(nextHeroVid, 60000); 
}

function nextHeroVid() {
  clearTimeout(heroTimer);
  heroCurIdx = (heroCurIdx + 1) % HERO_VIDS.length;
  switchHeroVid(heroCurIdx);
}

function switchHeroVid(idx) {
  clearTimeout(heroTimer);
  heroCurIdx = idx;
  if (heroPlayer && heroPlayer.loadVideoById) {
    heroPlayer.loadVideoById(HERO_VIDS[idx]);
  }
  document.querySelectorAll('.vid-dot').forEach(function(d,i){
    d.style.background = i === idx ? '#ca8a04' : 'rgba(202,138,4,0.35)';
  });
  startHeroTimer();
}

// --- YOUTUBE API INIT ---
var tag = document.createElement('script');
tag.src = "https://www.youtube.com/iframe_api";
var firstScriptTag = document.getElementsByTagName('script')[0];
firstScriptTag.parentNode.insertBefore(tag, firstScriptTag);

var p1, p2;
function onYouTubeIframeAPIReady() {
    // 1. Init Hero Player
    var heroEl = document.getElementById('hero-player');
    if (heroEl) {
        heroPlayer = new YT.Player('hero-player', {
            videoId: HERO_VIDS[0],
            playerVars: { autoplay:1, mute:1, controls:0, loop:0, rel:0, modestbranding:1, showinfo:0, iv_load_policy:3, playsinline:1 },
            events: {
                'onReady': function(e){ e.target.playVideo(); startHeroTimer(); },
                'onStateChange': function(e){
                    if (e.data === YT.PlayerState.ENDED) { nextHeroVid(); }
                }
            }
        });
    }

    // 2. Init Video Grid Players
    var player1El = document.getElementById('player1');
    if (player1El) {
        p1 = new YT.Player('player1', {
            videoId: 'xDVx1Yb7sCQ',
            playerVars: { 'autoplay': 1, 'controls': 0, 'mute': 1, 'loop': 1, 'playlist': 'xDVx1Yb7sCQ', 'rel': 0, 'modestbranding': 1 },
            events: { 'onReady': function(e){e.target.playVideo()} }
        });
    }

    var player2El = document.getElementById('player2');
    if (player2El) {
        p2 = new YT.Player('player2', {
            videoId: 'GYaoqV-mCA4',
            playerVars: { 'autoplay': 1, 'controls': 0, 'mute': 1, 'loop': 1, 'playlist': 'GYaoqV-mCA4', 'rel': 0, 'modestbranding': 1 },
            events: { 'onReady': function(e){e.target.playVideo()} }
        });
    }
}

// --- GRID VIDEO CONTROLS ---
function toggleMute(n) {
    var p = n === 1 ? p1 : p2;
    var btn = document.getElementById('mute'+n);
    if (p.isMuted()) {
        p.unMute();
        btn.innerHTML = '<i class="fa-solid fa-volume-high"></i>';
        btn.style.background = 'var(--ac)';
    } else {
        p.mute();
        btn.innerHTML = '<i class="fa-solid fa-volume-xmark"></i>';
        btn.style.background = 'rgba(0,0,0,0.6)';
    }
}

var clickTimers = {1:null, 2:null};
function handleOverlayClick(n, ytId) {
    if (clickTimers[n]) {
        clearTimeout(clickTimers[n]);
        clickTimers[n] = null;
        window.open('https://youtube.com/watch?v=' + ytId, '_blank');
        return;
    }
    clickTimers[n] = setTimeout(function() {
        var p = n === 1 ? p1 : p2;
        if (p.getPlayerState() === YT.PlayerState.PLAYING) p.pauseVideo();
        else p.playVideo();
        clickTimers[n] = null;
    }, 250);
}
</script>
"""

html = html.replace('</body>', unified_script + '\n</body>')

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html)
