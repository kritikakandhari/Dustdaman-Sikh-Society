import urllib.request
import re

url = 'https://www.youtube.com/watch?v=xDVx1Yb7sCQ'
req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
try:
    html = urllib.request.urlopen(req).read().decode('utf-8')
    match = re.search(r'"channelId":"(UC[a-zA-Z0-9_-]+)"', html)
    if match:
        print('Channel ID:', match.group(1))
    else:
        print('Not found')
except Exception as e:
    print(e)
