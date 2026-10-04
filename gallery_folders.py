import re

with open('gallery.html', 'r', encoding='utf-8') as f:
    html = f.read()

new_script = """
import { db, collection, getDocs, orderBy, query } from './firebase.js';

let allPosts = [];
let folders = {};

const categories = {
  "Nagar Kirtan": ["nagar", "parbhat", "pheri"],
  "Kirtan & Paath": ["kirtan", "paath", "path", "katha", "diwan", "smagam"],
  "Langar Seva": ["langar", "sewa", "seva"],
  "Gurbani Classes": ["punjabi", "tabla", "harmonium", "class", "gurbani", "santhiya"],
  "Special Events": ["gurpurab", "vaisakhi", "khalsa", "event", "camp"]
};

function getCategory(heading) {
  const h = (heading || '').toLowerCase();
  for (let cat in categories) {
    for (let keyword of categories[cat]) {
      if (h.includes(keyword)) return cat;
    }
  }
  return "Other Albums";
}

async function loadGallery() {
  const container = document.getElementById('gal-content');
  try {
    const q = query(collection(db, 'posts'), orderBy('createdAt', 'desc'));
    const snap = await getDocs(q);
    if (snap.empty) {
      container.innerHTML = '<p style="color:var(--mu); text-align:center; padding:40px 0;">No photos yet. Check back soon!</p>';
      return;
    }
    
    allPosts = [];
    folders = {};
    
    snap.forEach(d => {
      const p = { id: d.id, ...d.data() };
      allPosts.push(p);
      
      const cat = getCategory(p.heading);
      if (!folders[cat]) folders[cat] = [];
      folders[cat].push(p);
    });
    
    renderFolders();
  } catch(e) {
    container.innerHTML = '<p style="color:#ef4444;">Could not load gallery: ' + e.message + '</p>';
  }
}

window.renderFolders = () => {
  const container = document.getElementById('gal-content');
  let html = '<div class="album-grid">';
  
  Object.keys(folders).forEach((catName) => {
    const postsInFolder = folders[catName];
    let totalItems = 0;
    postsInFolder.forEach(p => { if (p.media) totalItems += p.media.length; });
    
    let thumb = 'logo.jpg';
    for (let p of postsInFolder) {
      if (p.media && p.media.length > 0) {
        const firstImg = p.media.find(m => m.type === 'image');
        if (firstImg) { thumb = firstImg.data; break; }
        else if (p.media[0].type === 'youtube') { thumb = 'https://img.youtube.com/vi/' + p.media[0].data + '/mqdefault.jpg'; break; }
      }
    }
    
    html += `
      <div class="album-card" onclick="openFolder('${catName}')">
        <div class="album-thumb" style="background-image: url('${thumb}');"></div>
        <div class="album-info">
          <div style="display:flex; align-items:center; gap:10px; margin-bottom:8px;">
            <i class="fa-solid fa-folder-open" style="color:var(--pr); font-size:1.4rem;"></i>
            <h3 style="margin:0;">${catName}</h3>
          </div>
          <span class="meta">${postsInFolder.length} Posts</span>
          <span class="count"><i class="fa-solid fa-images"></i> ${totalItems} items</span>
        </div>
      </div>
    `;
  });
  
  html += '</div>';
  container.innerHTML = html;
}

window.openFolder = (catName) => {
  const postsInFolder = folders[catName];
  const container = document.getElementById('gal-content');
  
  let html = `
    <button class="back-btn" onclick="renderFolders()"><i class="fa-solid fa-arrow-left"></i> Back to Folders</button>
    <div style="animation: fadeIn 0.3s;">
      <h2 style="color:var(--ac); margin-bottom: 25px; border-bottom: 3px solid var(--pr); padding-bottom:10px;">
        <i class="fa-regular fa-folder-open"></i> ${catName}
      </h2>
  `;
  
  postsInFolder.forEach(p => {
    const dateStr = p.date ? new Date(p.date).toLocaleDateString('en-GB',{day:'numeric',month:'long',year:'numeric'}) : '';
    let photoHTML = '';
    let ytHTML = '';
    
    (p.media || []).forEach(m => {
      if (m.type === 'youtube') ytHTML += `<div class="yt-thumb"><iframe src="https://www.youtube.com/embed/${m.data}?rel=0" allowfullscreen></iframe></div>`;
      else if (m.type === 'video') photoHTML += `<video src="${m.data}" controls style="width:100%; border-radius:10px;"></video>`;
      else photoHTML += `<img src="${m.data}" alt="${p.heading}" onclick="openLightbox('${m.data}')">`;
    });
    
    html += `
      <div class="gal-group" style="background:#fff; padding:20px; border-radius:16px; border:1px solid var(--bd); margin-bottom:25px; box-shadow:0 4px 10px rgba(0,0,0,0.03);">
        <h3 style="margin-top:0; color:#854d0e;">${p.heading}</h3>
        ${dateStr ? `<div class="meta"><i class="fa-regular fa-calendar"></i> ${dateStr}</div>` : ''}
        ${p.desc ? `<div class="desc">${p.desc}</div>` : ''}
        ${ytHTML ? `<h4 style="margin-top:15px; color:var(--ac); border-bottom: 2px solid var(--bd); padding-bottom:8px;"><i class="fa-brands fa-youtube" style="color:#ef4444;"></i> Videos</h4><div class="photo-grid" style="margin-bottom:15px;">${ytHTML}</div>` : ''}
        ${photoHTML ? `<h4 style="margin-top:15px; color:var(--ac); border-bottom: 2px solid var(--bd); padding-bottom:8px;"><i class="fa-solid fa-image"></i> Photos</h4><div class="photo-grid">${photoHTML}</div>` : ''}
      </div>
    `;
  });
  
  html += '</div>';
  container.innerHTML = html;
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

with open('gallery.html', 'w', encoding='utf-8') as f:
    f.write(html)
