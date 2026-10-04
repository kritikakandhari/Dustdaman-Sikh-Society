import glob, re

# A broad regex to match emojis but keep Punjabi text and FontAwesome safe
# Emojis are typically in higher unicode planes
emoji_pattern = re.compile(r'[\U00010000-\U0010ffff]', flags=re.UNICODE)

for f in glob.glob('*.html'):
    with open(f, 'r', encoding='utf-8') as file:
        content = file.read()
    
    # Remove emojis
    content = emoji_pattern.sub('', content)
    
    # Replace hindi/hinglish phrases with more professional english ones if they exist
    content = content.replace('Bina coding ke apni website manage karo.', 'Manage your website content seamlessly.')
    content = content.replace('Post Add karo', 'Publish Post')
    content = content.replace('Website Text Edit karo', 'Edit Website Text')
    content = content.replace('Kya aap sach mein yeh post delete karna chahte ho? Saari photos bhi hat jayengi.', 'Are you sure you want to delete this post? All associated media will be removed.')
    
    with open(f, 'w', encoding='utf-8') as file:
        file.write(content)
