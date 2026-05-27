/* ── main.js — Consolidated frontend logic ────────────────
   Theme toggle, toast notifications, navigation, auth helpers.
   ─────────────────────────────────────────────────────────── */

document.addEventListener('DOMContentLoaded', function () {

  /* ── Theme toggle ───────────────────────── */
  const toggle = document.getElementById('themeToggle');
  const metaTheme = document.querySelector('meta[name="theme-color"]');

  function toggleTheme() {
    const isDark = !document.documentElement.classList.contains('dark');

    document.documentElement.classList.add('theme-transitioning');
    document.documentElement.classList.toggle('dark', isDark);
    localStorage.setItem('theme', isDark ? 'dark' : 'light');

    if (metaTheme) {
      metaTheme.content = isDark ? '#0b1220' : '#2563eb';
    }

    setTimeout(function () {
      document.documentElement.classList.remove('theme-transitioning');
    }, 300);
  }

  if (toggle) {
    toggle.addEventListener('click', toggleTheme);
    toggle.addEventListener('touchend', function (e) {
      e.preventDefault();
      toggleTheme();
    });
  }

  /* ── Mobile nav hamburger ───────────────── */
  const hamburger = document.getElementById('hamburger');
  const navMenu = document.getElementById('navMenu');

  if (hamburger && navMenu) {
    hamburger.addEventListener('click', function () {
      const expanded = hamburger.getAttribute('aria-expanded') === 'true';
      hamburger.setAttribute('aria-expanded', !expanded);
      navMenu.classList.toggle('nav-open');
    });

    navMenu.querySelectorAll('a, button').forEach(function (el) {
      el.addEventListener('click', function () {
        hamburger.setAttribute('aria-expanded', 'false');
        navMenu.classList.remove('nav-open');
      });
    });
  }

  /* ── Toast notification system ──────────── */
  window.toast = function (message, type) {
    type = type || 'success';
    var container = document.getElementById('toastContainer');
    if (!container) return;

    var icons = {
      success: '<svg class="toast-icon" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M22 11.08V12a10 10 0 1 1-5.93-9.14"/><polyline points="22 4 12 14.01 9 11.01"/></svg>',
      error: '<svg class="toast-icon" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><circle cx="12" cy="12" r="10"/><line x1="15" y1="9" x2="9" y2="15"/><line x1="9" y1="9" x2="15" y2="15"/></svg>',
      warning: '<svg class="toast-icon" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M10.29 3.86L1.82 18a2 2 0 0 0 1.71 3h16.94a2 2 0 0 0 1.71-3L13.71 3.86a2 2 0 0 0-3.42 0z"/><line x1="12" y1="9" x2="12" y2="13"/><line x1="12" y1="17" x2="12.01" y2="17"/></svg>'
    };

    var toast = document.createElement('div');
    toast.className = 'toast toast-' + type;
    toast.innerHTML = (icons[type] || icons.success) + '<span>' + message + '</span><button class="toast-close" aria-label="Dismiss">&times;</button>';

    var closeBtn = toast.querySelector('.toast-close');
    closeBtn.addEventListener('click', function () { dismiss(toast); });

    container.appendChild(toast);

    var timeout = setTimeout(function () { dismiss(toast); }, 5000);

    function dismiss(el) {
      clearTimeout(timeout);
      el.classList.add('toast-out');
      setTimeout(function () { el.remove(); }, 300);
    }
  };

  /* ── Convert Django messages to toasts ──── */
  var alerts = document.querySelectorAll('.alert');
  alerts.forEach(function (alert) {
    var cls = alert.className;
    var type = 'success';
    if (cls.indexOf('alert-error') !== -1 || cls.indexOf('alert-danger') !== -1) type = 'error';
    else if (cls.indexOf('alert-warning') !== -1) type = 'warning';
    window.toast(alert.textContent.trim(), type);
    alert.remove();
  });

  /* ── Password toggle ────────────────────── */
  var eyeOpen = '<svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M1 12s4-8 11-8 11 8 11 8-4 8-11 8-11-8-11-8z"/><circle cx="12" cy="12" r="3"/></svg>';
  var eyeClosed = '<svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M17.94 17.94A10.07 10.07 0 0 1 12 20c-7 0-11-8-11-8a18.45 18.45 0 0 1 5.06-5.94"/><path d="M9.9 4.24A9.12 9.12 0 0 1 12 4c7 0 11 8 11 8a18.5 18.5 0 0 1-2.16 3.19"/><line x1="1" y1="1" x2="23" y2="23"/></svg>';

  document.querySelectorAll('input[type="password"]').forEach(function (input) {
    var wrap = input.parentNode;
    if (wrap && wrap.classList.contains('pw-wrap')) return;

    wrap = document.createElement('div');
    wrap.className = 'pw-wrap';
    wrap.style.cssText = 'position:relative;display:grid;';
    input.parentNode.insertBefore(wrap, input);
    wrap.appendChild(input);
    input.style.paddingRight = '46px';

    var btn = document.createElement('button');
    btn.type = 'button';
    btn.className = 'pw-eye';
    btn.setAttribute('aria-label', 'Toggle password visibility');
    btn.innerHTML = eyeOpen;

    btn.addEventListener('click', function () {
      var hidden = input.type === 'password';
      input.type = hidden ? 'text' : 'password';
      btn.innerHTML = hidden ? eyeClosed : eyeOpen;
    });

    wrap.appendChild(btn);
  });

  /* ── Form submit loading ────────────────── */
  var authForms = document.querySelectorAll('.auth-card form');
  authForms.forEach(function (form) {
    form.addEventListener('submit', function () {
      var btn = form.querySelector('.btn');
      if (btn && !btn.classList.contains('btn-loading')) {
        btn.classList.add('btn-loading');
        var spinner = document.createElement('span');
        spinner.className = 'btn-spinner';
        btn.appendChild(spinner);
      }
    });
  });

  /* ── Password strength (register) ───────── */
  var pwField = document.getElementById('id_password1');
  if (pwField) {
    var container = document.createElement('div');
    container.className = 'pw-strength';
    for (var i = 0; i < 4; i++) {
      var bar = document.createElement('div');
      bar.className = 'pw-strength-bar';
      container.appendChild(bar);
    }
    pwField.parentNode.appendChild(container);

    var textEl = document.createElement('div');
    textEl.className = 'pw-strength-text';
    pwField.parentNode.appendChild(textEl);

    var bars = container.querySelectorAll('.pw-strength-bar');

    pwField.addEventListener('input', function () {
      var val = pwField.value;
      var score = 0;
      if (val.length >= 8) score++;
      if (val.length >= 12) score++;
      if (/[A-Z]/.test(val) && /[a-z]/.test(val)) score++;
      if (/\d/.test(val)) score++;
      if (/[^A-Za-z0-9]/.test(val)) score++;

      var level = Math.min(4, Math.max(0, score));
      var colors = ['var(--border)', 'var(--danger)', 'var(--warning)', '#3b82f6', 'var(--success)'];
      var labels = ['', 'Weak', 'Fair', 'Good', 'Strong'];

      bars.forEach(function (bar, idx) {
        bar.style.background = idx < level ? colors[level] : 'var(--border)';
      });
      textEl.textContent = level > 0 ? 'Password strength: ' + labels[level] : '';
    });
  }

  /* ── Floating label support ─────────────── */
  document.querySelectorAll('.floating-wrap input, .floating-wrap select').forEach(function (el) {
    var wrap = el.closest('.floating-wrap');
    if (!wrap) return;

    if (el.value) wrap.classList.add('has-value');

    el.addEventListener('input', function () {
      wrap.classList.toggle('has-value', !!el.value);
    });

    el.addEventListener('blur', function () {
      wrap.classList.toggle('has-value', !!el.value);
    });
  });

  /* ── Page transition: fade in main content ── */
  var page = document.querySelector('main.page');
  if (page) {
    page.style.opacity = '0';
    requestAnimationFrame(function () {
      page.style.transition = 'opacity 0.3s ease';
      page.style.opacity = '1';
    });
  }

});
