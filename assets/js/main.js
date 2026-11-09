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

  // hero video: autoplay muted + sound toggle
  var video = document.querySelector('.hero video'), sbtn = document.querySelector('.sound-btn');
  if (video) {
    video.muted = true;
    var p = video.play(); if (p && p.catch) p.catch(function () {});
  }
  if (video && sbtn) sbtn.addEventListener('click', function () {
    video.muted = !video.muted;
    if (!video.muted) { video.volume = 1; video.play(); }
    sbtn.classList.toggle('unmuted', !video.muted);
    sbtn.setAttribute('aria-pressed', String(!video.muted));
  });

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

  // reveal on scroll
  if ('IntersectionObserver' in window) {
    var io = new IntersectionObserver(function (es) {
      es.forEach(function (e) { if (e.isIntersecting) { e.target.classList.add('in'); io.unobserve(e.target); } });
    }, { threshold: .12 });
    document.querySelectorAll('.reveal').forEach(function (el) { io.observe(el); });
  } else document.querySelectorAll('.reveal').forEach(function (el) { el.classList.add('in'); });

  var y = document.getElementById('year'); if (y) y.textContent = new Date().getFullYear();
})();
