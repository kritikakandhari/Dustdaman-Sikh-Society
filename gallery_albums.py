import re

with open('gallery.html', 'r', encoding='utf-8') as f:
    html = f.read()

new_script = """
import { db, collection, getDocs, orderBy, query } from './firebase.js';

let allPosts = [];

async function loadGallery() {
  const container = document.getElementById('gal-content');
  try {
    const q = query(collection(db, 'posts'), orderBy('createdAt', 'desc'));
    const snap = await getDocs(q);
    if (snap.empty) {
      container.innerHTML = '<p style="color:var(--mu); text-align:center; padding:40px 0;">No albums yet. Check back soon!</p>';
      return;
    }
    allPosts = [];
    snap.forEach(d => {
      allPosts.push({ id: d.id, ...d.data() });
    });
    renderAlbums();
  } catch(e) {
    container.innerHTML = '<p style="color:#ef4444;">Could not load gallery: ' + e.message + '</p>';
  }
}

window.renderAlbums = () => {
  const container = document.getElementById('gal-content');
  
  let html = '<div class="album-grid">';
  
  allPosts.forEach((p, idx) => {
    let thumb = 'logo.jpg'; 
    if (p.media && p.media.length > 0) {
      const firstImg = p.media.find(m => m.type === 'image');
      if (firstImg) thumb = firstImg.data;
      else if (p.media[0].type === 'youtube') thumb = 'https://img.youtube.com/vi/' + p.media[0].data + '/mqdefault.jpg';
    }
    
    const dateStr = p.date ? new Date(p.date).toLocaleDateString('en-GB',{day:'numeric',month:'long',year:'numeric'}) : '';
    
    html += `
      <div class="album-card" onclick="openAlbum(${idx})">
        <div class="album-thumb" style="background-image: url('${thumb}');"></div>
        <div class="album-info">
          <h3>${p.heading}</h3>
          ${dateStr ? `<span class="meta"><i class="fa-regular fa-calendar"></i> ${dateStr}</span>` : ''}
          <span class="count"><i class="fa-solid fa-images"></i> ${p.media ? p.media.length : 0} items</span>
        </div>
      </div>
    `;
  });
  
  html += '</div>';
  container.innerHTML = html;
}

window.openAlbum = (idx) => {
  const p = allPosts[idx];
  const container = document.getElementById('gal-content');
  
  const dateStr = p.date ? new Date(p.date).toLocaleDateString('en-GB',{day:'numeric',month:'long',year:'numeric'}) : '';
  
  let photoHTML = '';
  let ytHTML = '';
  
  (p.media || []).forEach(m => {
    if (m.type === 'youtube') {
      ytHTML += `<div class="yt-thumb"><iframe src="https://www.youtube.com/embed/${m.data}?rel=0" allowfullscreen></iframe></div>`;
    }
    else if (m.type === 'video') {
      photoHTML += `<video src="${m.data}" controls style="width:100%; border-radius:10px;"></video>`;
    }
    else {
      photoHTML += `<img src="${m.data}" alt="${p.heading}" onclick="openLightbox('${m.data}')">`;
    }
  });

  container.innerHTML = `
    <button class="back-btn" onclick="renderAlbums()"><i class="fa-solid fa-arrow-left"></i> Back to Albums</button>
    <div class="gal-group" style="animation: fadeIn 0.3s;">
      <h3>${p.heading}</h3>
      ${dateStr ? `<div class="meta"><i class="fa-regular fa-calendar"></i> ${dateStr}</div>` : ''}
      ${p.desc ? `<div class="desc">${p.desc}</div>` : ''}
      
      ${ytHTML ? `<h4 style="margin-top:20px; color:var(--ac); border-bottom: 2px solid var(--bd); padding-bottom:8px;"><i class="fa-brands fa-youtube" style="color:#ef4444;"></i> Videos</h4><div class="photo-grid" style="margin-bottom:30px;">${ytHTML}</div>` : ''}
      
      ${photoHTML ? `<h4 style="margin-top:20px; color:var(--ac); border-bottom: 2px solid var(--bd); padding-bottom:8px;"><i class="fa-solid fa-image"></i> Photos</h4><div class="photo-grid">${photoHTML}</div>` : ''}
    </div>
  `;
  window.scrollTo({ top: 0, behavior: 'smooth' });
};

window.openLightbox = (url) => {
  document.getElementById('lightbox-img').src = url;
  document.getElementById('lightbox').classList.add('on');
};

loadGallery();

const L = localStorage.getItem('lang') || 'en';
document.getElementById('lang').onclick = function() {
  const nl = L === 'en' ? 'pa' : 'en';
  localStorage.setItem('lang', nl);
  location.reload();
};
"""

html = re.sub(r'import \{ db.*?(?=<\/script>)', new_script, html, flags=re.DOTALL)

new_css = """
  .album-grid { display: grid; grid-template-columns: repeat(auto-fill, minmax(260px, 1fr)); gap: 24px; margin-top: 20px; }
  .album-card { background: #fff; border: 1px solid var(--bd); border-radius: 16px; overflow: hidden; cursor: pointer; transition: .2s; box-shadow: 0 4px 10px rgba(0,0,0,0.05); }
  .album-card:hover { transform: translateY(-4px); box-shadow: 0 10px 25px rgba(0,0,0,0.1); border-color: var(--pr); }
  .album-thumb { width: 100%; aspect-ratio: 4/3; background-size: cover; background-position: center; background-color: #eee; border-bottom: 3px solid var(--pr); }
  .album-info { padding: 18px; }
  .album-info h3 { margin: 0 0 8px; color: var(--ac); font-size: 1.3rem; }
  .album-info .meta { color: var(--mu); font-size: 0.9rem; display: block; margin-bottom: 8px; }
  .album-info .count { display: inline-block; background: #fef08a; color: #854d0e; font-size: 0.8rem; padding: 4px 10px; border-radius: 20px; font-weight: 600; }
  .back-btn { background: #fffbeb; color: #854d0e; border: 1px solid #fde047; padding: 10px 20px; border-radius: 10px; cursor: pointer; font-weight: 600; margin-bottom: 25px; font-family: inherit; font-size: 1rem; display: inline-flex; align-items: center; gap: 8px; transition: .2s; }
  .back-btn:hover { background: #fef08a; transform: translateX(-2px); }
  @keyframes fadeIn { from { opacity: 0; transform: translateY(10px); } to { opacity: 1; transform: translateY(0); } }
"""
html = html.replace('</style>', new_css + '\n</style>')

with open('gallery.html', 'w', encoding='utf-8') as f:
    f.write(html)
