(function () {
  var header = document.querySelector('.site-header');
  function onScroll() { header && header.classList.toggle('scrolled', window.scrollY > 30); }
  window.addEventListener('scroll', onScroll, { passive: true }); onScroll();

  // mobile menu
  var burger = document.querySelector('.burger'), links = document.querySelector('.nav-links');
  if (burger && links) burger.addEventListener('click', function () {
    var open = links.classList.toggle('open');
    burger.setAttribute('aria-expanded', open);
  });

  // home video: autoplay muted + sound toggle
  var video = document.querySelector('.phone video'), sbtn = document.querySelector('.sound-btn');
  if (video) {
    video.muted = true;
    var p = video.play(); if (p && p.catch) p.catch(function () {});
  }
  if (video && sbtn) {
    var setUI = function () {
      sbtn.classList.toggle('unmuted', !video.muted);
      sbtn.setAttribute('aria-pressed', String(!video.muted));
    };
    sbtn.addEventListener('click', function (e) {
      e.preventDefault(); e.stopPropagation();
      var wantSound = video.muted;
      video.muted = !wantSound;
      if (wantSound) {
        video.removeAttribute('muted');
        try { video.volume = 1; } catch (err) {}
        var pr = video.play();
        if (pr && pr.catch) pr.catch(function () {
          // iOS sometimes refuses: restart the video with sound inside the tap
          video.pause(); video.muted = false;
          video.play().catch(function () { video.muted = true; setUI(); });
        });
      } else {
        video.setAttribute('muted', '');
      }
      setUI();
    });
    video.addEventListener('volumechange', setUI);
  }

  // today (JS: 0=Sun..6=Sat)
  var keys = ['sun', 'mon', 'tue', 'wed', 'thu', 'fri', 'sat'];
  var today = keys[new Date().getDay()];

  document.querySelectorAll('[data-col="' + today + '"]').forEach(function (el) { el.classList.add('today'); });

  // schedule day tabs (mobile)
  document.querySelectorAll('.sched-days').forEach(function (wrap) {
    var btns = wrap.querySelectorAll('.day-tabs button'), lists = wrap.querySelectorAll('[data-day]');
    function show(day) {
      btns.forEach(function (b) { b.classList.toggle('active', b.dataset.target === day); });
      lists.forEach(function (l) { l.hidden = l.dataset.day !== day; });
    }
    btns.forEach(function (b) { b.addEventListener('click', function () { show(b.dataset.target); }); });
    show(today === 'fri' ? 'sat' : today);
  });

  // home "today" box
  document.querySelectorAll('.today-box').forEach(function (box) {
    var lists = box.querySelectorAll('[data-day]');
    lists.forEach(function (l) { l.hidden = l.dataset.day !== today; });
    var label = box.querySelector('[data-day-label="' + today + '"]');
    if (label) label.hidden = false;
  });

  var reduce = window.matchMedia('(prefers-reduced-motion: reduce)').matches;

  // scroll progress bar + hero parallax
  var bar = document.querySelector('.progress'), heroBg = document.querySelector('.hero-bg'),
      pageHero = document.querySelector('.page-hero'), ticking = false;
  function onMove() {
    var y = window.scrollY, h = document.documentElement.scrollHeight - window.innerHeight;
    if (bar) bar.style.transform = 'scaleX(' + (h > 0 ? Math.min(1, y / h) : 0) + ')';
    if (!reduce && y < window.innerHeight * 1.2) {
      if (heroBg) heroBg.style.transform = 'translate3d(0,' + (y * 0.3) + 'px,0)';
      if (pageHero && window.innerWidth > 860) pageHero.style.backgroundPosition = 'center calc(50% + ' + (y * 0.35) + 'px)';
    }
    ticking = false;
  }
  window.addEventListener('scroll', function () { if (!ticking) { ticking = true; requestAnimationFrame(onMove); } }, { passive: true });
  onMove();

  // stagger cards inside grids
  document.querySelectorAll('.grid, .features, .gallery').forEach(function (g) {
    var i = 0;
    Array.prototype.forEach.call(g.children, function (c) {
      if (c.classList.contains('reveal') || g.classList.contains('features')) {
        c.classList.add('reveal'); c.style.transitionDelay = (i++ % 8) * 90 + 'ms';
      }
    });
  });

  // count-up numbers
  function countUp(el) {
    var end = parseInt(el.dataset.count, 10), start = null, dur = 1400;
    if (reduce || !end) { el.textContent = end; return; }
    function step(ts) {
      if (!start) start = ts;
      var p = Math.min(1, (ts - start) / dur), e = 1 - Math.pow(1 - p, 3);
      el.textContent = Math.round(end * e);
      if (p < 1) requestAnimationFrame(step);
    }
    el.textContent = '0'; setTimeout(function () { requestAnimationFrame(step); }, 1100);
  }
  document.querySelectorAll('[data-count]').forEach(countUp);

  // smooth page transitions (fallback for browsers without view transitions)
  if (!reduce && !('onpagereveal' in window)) {
    document.addEventListener('click', function (e) {
      var a = e.target.closest('a');
      if (!a || a.target || e.metaKey || e.ctrlKey || e.shiftKey || a.hasAttribute('download')) return;
      var url = new URL(a.href, location.href);
      if (url.origin !== location.origin || (url.pathname === location.pathname && url.hash)) return;
      e.preventDefault();
      document.body.classList.add('leaving');
      setTimeout(function () { location.href = a.href; }, 230);
    });
    window.addEventListener('pageshow', function () { document.body.classList.remove('leaving'); });
  }

  // reveal on scroll
  if ('IntersectionObserver' in window) {
    var io = new IntersectionObserver(function (es) {
      es.forEach(function (e) { if (e.isIntersecting) { var t = e.target; t.classList.add('in'); io.unobserve(t); setTimeout(function () { t.style.transitionDelay = ''; }, 1600); } });
    }, { threshold: .12 });
    document.querySelectorAll('.reveal').forEach(function (el) { io.observe(el); });
  } else document.querySelectorAll('.reveal').forEach(function (el) { el.classList.add('in'); });

  var y = document.getElementById('year'); if (y) y.textContent = new Date().getFullYear();
})();
