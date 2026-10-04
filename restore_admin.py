import re

with open('admin.html', 'r', encoding='utf-8') as f:
    html = f.read()

missing_js = """
// Status
function showStatus(msg, isErr) {
  const el = document.getElementById('status-bar');
  el.textContent = msg;
  el.className = 'status-bar ' + (isErr ? 'err' : 'ok');
  window.scrollTo(0, 0);
  setTimeout(() => { el.style.display = 'none'; }, 5000);
}

document.getElementById('pf').onchange = (e) => {
  const c = document.getElementById('img-preview');
  c.innerHTML = '';
  Array.from(e.target.files).forEach(f => {
    const r = new FileReader();
    r.onload = ev => c.innerHTML += `<img src="${ev.target.result}">`;
    r.readAsDataURL(f);
  });
};

document.getElementById('py').oninput = (e) => {
  const val = e.target.value.trim();
  const c = document.getElementById('yt-preview');
  if (!val) { c.style.display = 'none'; return; }
  let ytId = '';
  const match = val.match(/[?&]v=([^&]+)/);
  if (match) ytId = match[1];
  else ytId = val.split('/').pop().split('?')[0];
  if (ytId) {
    c.style.display = 'flex';
    c.innerHTML = `<img src="https://img.youtube.com/vi/${ytId}/mqdefault.jpg" style="height:60px; border-radius:8px;"> YouTube Video added.`;
  }
};

window.addPost = async () => {
  const heading = document.getElementById('ph').value.trim();
  const desc = document.getElementById('pd').value.trim();
  const files = document.getElementById('pf').files;
  const ytLink = document.getElementById('py').value.trim();

  if (!heading) { showStatus('Please enter a heading.', true); return; }
  if (files.length === 0 && !ytLink) { showStatus('Please add at least one photo or YouTube link.', true); return; }

  const prog = document.getElementById('upload-progress');
  const fill = document.getElementById('progress-fill');
  const statusTxt = document.getElementById('upload-status');
  const addBtn = document.getElementById('add-btn');
  prog.style.display = 'block';
  addBtn.disabled = true;

  try {
    const media = [];
    let done = 0;
    const total = files.length;

    for (let file of files) {
      statusTxt.textContent = `Compressing image ${done+1} of ${total}...`;
      const b64 = await compressImage(file);
      media.push({ type: 'image', data: b64 });
      done++;
      fill.style.width = Math.round((done / Math.max(total,1)) * 90) + '%';
    }

    if (ytLink) {
      let ytId = '';
      const match = ytLink.match(/[?&]v=([^&]+)/);
      if (match) ytId = match[1];
      else ytId = ytLink.split('/').pop().split('?')[0];
      media.push({ type: 'youtube', data: ytId });
    }

    statusTxt.textContent = 'Saving to database...';
    fill.style.width = '95%';

    await addDoc(collection(db, 'posts'), {
      heading, desc, media,
      createdAt: Date.now()
    });

    fill.style.width = '100%';
    prog.style.display = 'none';
    addBtn.disabled = false;

    document.getElementById('ph').value = '';
    document.getElementById('pd').value = '';
    document.getElementById('pf').value = '';
    document.getElementById('py').value = '';
    document.getElementById('img-preview').innerHTML = '';
    document.getElementById('yt-preview').style.display = 'none';

    showStatus('Post successfully added.');
    loadPosts();
  } catch(e) {
    prog.style.display = 'none';
    addBtn.disabled = false;
    showStatus('Error: ' + e.message, true);
  }
};

async function loadPosts() {
  const ls = document.getElementById('post-list');
  ls.innerHTML = '<p>Loading posts...</p>';
  try {
    const q = query(collection(db, 'posts'), orderBy('createdAt', 'desc'));
    const snap = await getDocs(q);
    if (snap.empty) { ls.innerHTML = '<p>No posts yet.</p>'; return; }
    ls.innerHTML = '';
    snap.forEach(d => {
      const p = d.data();
      const thumbs = (p.media || []).map(m => {
        if (m.type === 'youtube') return `<div style="background:#fee2e2; border-radius:8px; padding:6px 12px; font-size:.85rem; color:#991b1b; display:inline-flex; align-items:center; gap:6px;"><i class="fa-brands fa-youtube"></i> YouTube Video</div>`;
        return `<img src="${m.data}" style="width:90px; height:70px; object-fit:cover; border-radius:8px; border:2px solid var(--bd);">`;
      }).join('');

      const card = document.createElement('div');
      card.className = 'post-card';
      card.innerHTML = `
        <button class="del-btn" onclick="deletePost('${d.id}')"><i class="fa-solid fa-trash"></i> Delete</button>
        <h3>${p.heading}</h3>
        <p style="color:#666; font-size:0.9rem;">${p.desc}</p>
        <div class="img-preview">${thumbs}</div>
      `;
      ls.appendChild(card);
    });
  } catch(e) {
    ls.innerHTML = '<p style="color:red;">Error loading posts: ' + e.message + '</p>';
  }
}

window.deletePost = async (id) => {
  if (!confirm('Are you sure you want to delete this post? All associated media will be removed.')) return;
  try {
    await deleteDoc(doc(db, 'posts', id));
    showStatus('Post deleted successfully.');
    loadPosts();
  } catch(e) {
    showStatus('Delete error: ' + e.message, true);
  }
};

async function loadTextFields() {
  try {
    const docRef = await getDoc(doc(db, 'siteText', 'main'));
    if (docRef.exists()) {
      const data = docRef.data();
      const fields = ['welcomeT', 'welcomeP', 'aboutT', 'aboutP', 's1', 's1d', 's2', 's2d', 's3', 's3d', 'tag', 'cta', 'vtxt'];
      fields.forEach(f => {
        if (data[f]) {
          const el = document.getElementById('t_' + f);
          if (el) el.value = data[f];
        }
      });
    }
  } catch(e) {
    console.error("Could not load texts", e);
  }
}

window.saveText = async (field, elId) => {
  const val = document.getElementById(elId).value.trim();
  if (!val) { showStatus('Field cannot be empty.', true); return; }
  try {
    await setDoc(doc(db, 'siteText', 'main'), { [field]: val }, { merge: true });
    showStatus('Successfully saved and updated.');
  } catch(e) {
    showStatus('Save error: ' + e.message, true);
  }
};
"""

html = re.sub(r'// Status\s*function showStatus.*?\}\s*;\s*', missing_js, html, flags=re.DOTALL)

with open('admin.html', 'w', encoding='utf-8') as f:
    f.write(html)
