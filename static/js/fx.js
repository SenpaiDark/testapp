/* -----------------------------------------------------------
   mayor4code - FX v1 "Terminal"
   Particles, 3D tilt, scroll reveals
   ----------------------------------------------------------- */
(function () {
  'use strict';

  var reduced = window.matchMedia('(prefers-reduced-motion: reduce)').matches;

  /* -------------------------------------------------------
     PARTICLES — drifting nodes + connecting lines
     Attach: <canvas class="fx-particles" data-particles></canvas>
     ------------------------------------------------------- */
  function initParticles(canvas) {
    var ctx = canvas.getContext('2d');
    var dpr = Math.min(window.devicePixelRatio || 1, 2);
    var host = canvas.parentElement;
    var W = 0, H = 0, dots = [], raf = null;

    function isDark() { return document.documentElement.classList.contains('dark'); }

    function resize() {
      W = host.clientWidth;
      H = host.clientHeight;
      canvas.width = W * dpr;
      canvas.height = H * dpr;
      canvas.style.width = W + 'px';
      canvas.style.height = H + 'px';
      ctx.setTransform(dpr, 0, 0, dpr, 0, 0);
      var count = Math.min(70, Math.floor(W * H / 16000));
      dots = [];
      for (var i = 0; i < count; i++) {
        dots.push({
          x: Math.random() * W,
          y: Math.random() * H,
          vx: (Math.random() - 0.5) * 0.35,
          vy: (Math.random() - 0.5) * 0.35,
          r: Math.random() * 1.6 + 0.6
        });
      }
    }

    function tick() {
      ctx.clearRect(0, 0, W, H);
      var col = isDark() ? '0,255,135' : '0,135,90';
      var i, j, d;
      for (i = 0; i < dots.length; i++) {
        d = dots[i];
        d.x += d.vx; d.y += d.vy;
        if (d.x < 0 || d.x > W) d.vx *= -1;
        if (d.y < 0 || d.y > H) d.vy *= -1;
        ctx.beginPath();
        ctx.arc(d.x, d.y, d.r, 0, Math.PI * 2);
        ctx.fillStyle = 'rgba(' + col + ',' + (isDark() ? 0.55 : 0.35) + ')';
        ctx.fill();
      }
      for (i = 0; i < dots.length; i++) {
        for (j = i + 1; j < dots.length; j++) {
          var dx = dots[i].x - dots[j].x;
          var dy = dots[i].y - dots[j].y;
          var dist = dx * dx + dy * dy;
          if (dist < 110 * 110) {
            ctx.beginPath();
            ctx.moveTo(dots[i].x, dots[i].y);
            ctx.lineTo(dots[j].x, dots[j].y);
            ctx.strokeStyle = 'rgba(' + col + ',' + (0.10 * (1 - dist / (110 * 110))).toFixed(3) + ')';
            ctx.lineWidth = 1;
            ctx.stroke();
          }
        }
      }
      raf = requestAnimationFrame(tick);
    }

    function start() { if (!raf) raf = requestAnimationFrame(tick); }
    function stop()  { if (raf) { cancelAnimationFrame(raf); raf = null; } }

    resize();
    start();
    window.addEventListener('resize', resize, { passive: true });
    document.addEventListener('visibilitychange', function () {
      document.hidden ? stop() : start();
    });
  }

  /* -------------------------------------------------------
     3D TILT — cards lean toward the cursor
     Attach: data-tilt (optional data-tilt-max="8")
     ------------------------------------------------------- */
  function initTilt(el) {
    var max = parseFloat(el.getAttribute('data-tilt-max')) || 7;
    el.addEventListener('pointermove', function (e) {
      if (e.pointerType !== 'mouse') return;
      var r = el.getBoundingClientRect();
      var px = (e.clientX - r.left) / r.width - 0.5;
      var py = (e.clientY - r.top) / r.height - 0.5;
      el.style.setProperty('--tilt-x', (-py * max).toFixed(2) + 'deg');
      el.style.setProperty('--tilt-y', (px * max).toFixed(2) + 'deg');
    });
    el.addEventListener('pointerleave', function () {
      el.style.setProperty('--tilt-x', '0deg');
      el.style.setProperty('--tilt-y', '0deg');
    });
  }

  /* -------------------------------------------------------
     SCROLL REVEAL — stagger siblings 60ms apart
     Attach: data-reveal
     ------------------------------------------------------- */
  function initReveals(els) {
    if (!('IntersectionObserver' in window)) {
      els.forEach(function (el) { el.classList.add('revealed'); });
      return;
    }
    var seen = 0;
    var io = new IntersectionObserver(function (entries) {
      entries.forEach(function (entry) {
        if (!entry.isIntersecting) return;
        var el = entry.target;
        el.style.setProperty('--reveal-delay', (seen % 6) * 60 + 'ms');
        seen++;
        el.classList.add('revealed');
        io.unobserve(el);
      });
    }, { threshold: 0.12, rootMargin: '0px 0px -8% 0px' });
    els.forEach(function (el) { io.observe(el); });
  }

  /* -------------------------------------------------------
     BOOT
     ------------------------------------------------------- */
  function boot() {
    var reveals = Array.prototype.slice.call(document.querySelectorAll('[data-reveal]'));
    if (reduced) {
      reveals.forEach(function (el) { el.classList.add('revealed'); });
      return; // no particles, no tilt
    }
    document.querySelectorAll('canvas[data-particles]').forEach(initParticles);
    document.querySelectorAll('[data-tilt]').forEach(initTilt);
    initReveals(reveals);
  }

  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', boot);
  } else {
    boot();
  }
})();
