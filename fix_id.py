with open('admin.html', 'r', encoding='utf-8') as f:
    html = f.read()

html = html.replace("getElementById('post-list')", "getElementById('posts-list')")

with open('admin.html', 'w', encoding='utf-8') as f:
    f.write(html)
