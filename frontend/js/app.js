import { login, register } from './api.js';

console.log('🚀 Click&Clean frontend запущен');

const $ = s => document.querySelector(s);
const overlay = $('#auth-overlay');
const openBtns = ['#open-auth', '#open-auth-hero'].map(id => $(id)).filter(Boolean);
const closeBtn = $('#auth-close');
const loginTab = $('#tab-login');
const regTab = $('#tab-register');
const formLogin = $('#form-login');
const formRegister = $('#form-register');
const roleRadios = document.querySelectorAll('input[name="role"]');

// === Модалка ===
function openModal() {
  overlay.setAttribute('aria-hidden', 'false');
  document.body.style.overflow = 'hidden';
}
function closeModal() {
  overlay.setAttribute('aria-hidden', 'true');
  document.body.style.overflow = '';
}
openBtns.forEach(btn => btn?.addEventListener('click', openModal));
closeBtn?.addEventListener('click', closeModal);
overlay?.addEventListener('click', e => { if (e.target === overlay) closeModal(); });

// === Переключение вкладок ===
function switchTab(to) {
  const isLogin = to === 'login';
  loginTab.classList.toggle('active', isLogin);
  regTab.classList.toggle('active', !isLogin);
  formLogin.classList.toggle('active', isLogin);
  formRegister.classList.toggle('active', !isLogin);
}
loginTab?.addEventListener('click', () => switchTab('login'));
regTab?.addEventListener('click', () => switchTab('register'));

// === Логин ===
formLogin?.addEventListener('submit', async (e) => {
  e.preventDefault();
  const email = $('#login-email').value.trim();
  const password = $('#login-pass').value;

  const res = await login({ email, password });
  if (res.access) {
    alert('Вход выполнен');
    localStorage.setItem('token', res.access);
    localStorage.setItem('role', res.user?.role || 'client');
    closeModal();
    window.location.href = res.user?.role === 'courier' ? './courier.html' : './client.html';
  } else {
    alert(res.detail || 'Ошибка входа');
  }
});

// === Регистрация ===
formRegister?.addEventListener('submit', async (e) => {
  e.preventDefault();
  const name = $('#reg-name').value.trim();
  const email = $('#reg-email').value.trim();
  const password = $('#reg-pass').value;
  const role = Array.from(roleRadios).find(r => r.checked)?.value || 'client';

  if (!email || !password) return alert('Заполните все поля');

  const res = await register({ name, email, password, role });
  if (res.id || res.ok) {
    alert('Регистрация успешна! Теперь войдите.');
    switchTab('login');
  } else {
    alert(res.detail || JSON.stringify(res));
  }
});

// === Плавное появление ===
const fadeEls = document.querySelectorAll('.fade-in');
const reveal = () => fadeEls.forEach(el => {
  const r = el.getBoundingClientRect();
  if (r.top < innerHeight * 0.85) el.classList.add('visible');
});
window.addEventListener('scroll', reveal);
window.addEventListener('load', reveal);
