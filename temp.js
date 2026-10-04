
import { db, auth, provider, ADMIN_EMAIL,
         collection, addDoc, getDocs, deleteDoc, doc, setDoc, getDoc, orderBy, query,
         onAuthStateChanged, signInWithPopup, signOut } from './firebase.js';

let currentUser = null;

// Compress image to base64
function compressImage(file) {
  return new Promise((resolve) => {
    const img = new Image();
    const url = URL.createObjectURL(file);
    img.onload = () => {
      const MAX = 900;
      let w = img.width, h = img.height;
      if (w > MAX || h > MAX) {
        const ratio = Math.min(MAX/w, MAX/h);
        w = Math.round(w * ratio);
        h = Math.round(h * ratio);
      }
      const canvas = document.createElement('canvas');
      canvas.width = w; canvas.height = h;
      canvas.getContext('2d').drawImage(img, 0, 0, w, h);
      URL.revokeObjectURL(url);
      resolve(canvas.toDataURL('image/jpeg', 0.72));
    };
    img.src = url;
  });
}

// Auth
onAuthStateChanged(auth, (user) => {
  if (user && user.email === ADMIN_EMAIL) {
    currentUser = user;
    document.getElementById('login-screen').style.display = 'none';
    document.getElementById('admin-panel').style.display = 'block';
    document.getElementById('user-email').textContent = user.email;
    document.getElementById('logout-btn').style.display = 'inline-block';
    loadPosts();
    
  } else {
    document.getElementById('login-screen').style.display = 'block';
    document.getElementById('admin-panel').style.display = 'none';
  }
});

document.getElementById('google-login-btn').onclick = async () => {
  document.getElementById('login-error').style.display = 'none';
  try {
    const result = await signInWithPopup(auth, provider);
    if (result.user.email !== ADMIN_EMAIL) {
      await signOut(auth);
      document.getElementById('login-error').style.display = 'block';
    }
  } catch(e) {
    document.getElementById('login-error').style.display = 'block';
    document.getElementById('login-error').textContent = 'Error: ' + e.message;
  }
};

document.getElementById('logout-btn').onclick = () => signOut(auth);

// Tab switch
window.showTab = (id, btn) => {
  document.querySelectorAll('.tab-panel').forEach(p => p.classList.remove('active'));
  document.querySelectorAll('.adm-tab').forEach(b => b.classList.remove('active'));
  document.getElementById(id).classList.add('active');
  btn.classList.add('active');
};


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

