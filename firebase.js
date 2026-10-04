// Firebase Configuration - No Storage needed, images stored in Firestore as base64
import { initializeApp } from "https://www.gstatic.com/firebasejs/12.19.0/firebase-app.js";
import { getFirestore, collection, addDoc, getDocs, deleteDoc, doc, setDoc, getDoc, orderBy, query } from "https://www.gstatic.com/firebasejs/12.19.0/firebase-firestore.js";
import { getAuth, signInWithPopup, GoogleAuthProvider, onAuthStateChanged, signOut } from "https://www.gstatic.com/firebasejs/12.19.0/firebase-auth.js";

const firebaseConfig = {
  apiKey: "AIzaSyBKYaEWKKK_vBbvoucuhKfD23KRXF3rb6c",
  authDomain: "dustdamansikhsociety-ac302.firebaseapp.com",
  projectId: "dustdamansikhsociety-ac302",
  storageBucket: "dustdamansikhsociety-ac302.firebasestorage.app",
  messagingSenderId: "642118293846",
  appId: "1:642118293846:web:d31af6714cd70dcfdb9ef7"
};

const app = initializeApp(firebaseConfig);
const db = getFirestore(app);
const auth = getAuth(app);
const provider = new GoogleAuthProvider();

const ADMIN_EMAIL = "dustdamansikhsociety@gmail.com";

export { db, auth, provider, ADMIN_EMAIL, collection, addDoc, getDocs, deleteDoc, doc, setDoc, getDoc, orderBy, query, onAuthStateChanged, signInWithPopup, signOut };
