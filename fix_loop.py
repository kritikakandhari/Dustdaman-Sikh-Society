import re

with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

# Fix playerVars
html = re.sub(
    r'playerVars:\s*\{\s*start:10,\s*end:30,',
    'playerVars: {',
    html
)

# Fix switchHeroVid
html = re.sub(
    r'heroPlayer\.loadVideoById\(\{videoId:\s*HERO_VIDS\[idx\],\s*startSeconds:\s*10,\s*endSeconds:\s*30\}\);',
    'heroPlayer.loadVideoById({videoId: HERO_VIDS[idx], startSeconds: 10});',
    html
)

# Replace the entire onReady and onStateChange for heroPlayer
replacement = """'onReady': function(e){ 
                    e.target.seekTo(10, true); 
                    e.target.playVideo(); 
                    setInterval(function() {
                        if (e.target.getCurrentTime && e.target.getCurrentTime() >= 30) {
                            e.target.seekTo(10, true);
                        }
                    }, 500);
                },
                'onStateChange': function(e){ }"""

html = re.sub(
    r'\'onReady\': function\(e\)\{ e\.target\.playVideo\(\); \},\s*\'onStateChange\': function\(e\)\{\s*if \(e\.data === YT\.PlayerState\.ENDED\) \{ e\.target\.seekTo\(10\); e\.target\.playVideo\(\); \}\s*\}',
    replacement,
    html,
    flags=re.DOTALL
)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html)
