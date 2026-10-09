/* arkasystems.es · site.js
   Sin dependencias. Cada bloque es independiente y falla en silencio si su
   elemento no existe. Los textos de la demostración viven en window.DEMO_THREAD
   (index.html, <head>). */
(function () {
  'use strict';
  var d = document, w = window;
  var reduce = w.matchMedia('(prefers-reduced-motion: reduce)');
  var hoverable = w.matchMedia('(hover: hover)');
  function $(s, r) { return (r || d).querySelector(s); }
  function $$(s, r) { return Array.prototype.slice.call((r || d).querySelectorAll(s)); }
  function onChange(mq, fn) { if (mq.addEventListener) mq.addEventListener('change', fn); else mq.addListener(fn); }

  /* 1 · CTAs desde window.ARKA_LINKS */
  var L = w.ARKA_LINKS || {};
  $$('[data-arka-cta]').forEach(function (el) {
    var k = el.getAttribute('data-arka-cta');
    if (L[k]) el.setAttribute('href', L[k]);
    if (k === 'whatsapp' || k === 'calendly') { el.setAttribute('target', '_blank'); el.setAttribute('rel', 'noopener'); }
  });

  /* 2 · Nav: estado scrolled, menú móvil, sección activa */
  var nav = $('.nav');
  if (nav) {
    var onScroll = function () { nav.classList.toggle('scrolled', w.scrollY > 24); };
    onScroll();
    w.addEventListener('scroll', onScroll, { passive: true });

    var toggle = $('.nav-toggle', nav), panel = $('.nav-panel', nav);
    if (toggle && panel) {
      var setOpen = function (open) {
        nav.classList.toggle('is-open', open);
        toggle.setAttribute('aria-expanded', open ? 'true' : 'false');
      };
      toggle.addEventListener('click', function () { setOpen(!nav.classList.contains('is-open')); });
      $$('a', panel).forEach(function (a) { a.addEventListener('click', function () { setOpen(false); }); });
      d.addEventListener('keydown', function (e) { if (e.key === 'Escape' && nav.classList.contains('is-open')) { setOpen(false); toggle.focus(); } });
      d.addEventListener('click', function (e) { if (nav.classList.contains('is-open') && !nav.contains(e.target)) setOpen(false); });
    }

    var links = $$('.nav-links a[href^="#"]', nav);
    if (links.length && 'IntersectionObserver' in w) {
      var map = {};
      links.forEach(function (a) { var id = a.getAttribute('href').slice(1); var sec = d.getElementById(id); if (sec) map[id] = a; });
      var current = null;
      var ioNav = new IntersectionObserver(function (entries) {
        entries.forEach(function (e) {
          if (!e.isIntersecting) return;
          if (current) current.removeAttribute('aria-current');
          current = map[e.target.id];
          if (current) current.setAttribute('aria-current', 'true');
        });
      }, { rootMargin: '-35% 0px -55% 0px', threshold: 0 });
      Object.keys(map).forEach(function (id) { ioNav.observe(d.getElementById(id)); });
    }
  }

  /* 3 · Reveal jerárquico (solo añade la clase; el CSS decide cuánto se mueve) */
  var revealEls = $$('.reveal, .reveal-lead');
  if (revealEls.length) {
    if ('IntersectionObserver' in w) {
      var io = new IntersectionObserver(function (entries) {
        entries.forEach(function (e) {
          if (e.isIntersecting) { e.target.classList.add('in'); io.unobserve(e.target); }
        });
      }, { rootMargin: '0px 0px -8% 0px', threshold: 0.05 });
      revealEls.forEach(function (el) { io.observe(el); });
    } else {
      revealEls.forEach(function (el) { el.classList.add('in'); });
    }
  }

  /* 4 · Entrada del hero (una vez, al cargar) */
  var hero = $('.hero');
  if (hero) {
    w.requestAnimationFrame(function () { w.requestAnimationFrame(function () { hero.classList.add('is-in'); }); });
  }

  /* 5 · Vídeos del hero: uno activo, rotación solo visible, pausa real */
  var vids = $$('.hero-vid');
  if (hero && vids.length) {
    var vi = 0, rot = null, userPaused = reduce.matches, heroVisible = true;
    var pauseBtn = $('.hero-pause');
    var canPlay = function () { return !userPaused && !reduce.matches && heroVisible && !d.hidden; };
    var showVid = function (i) {
      vids.forEach(function (v, j) {
        if (j === i) {
          v.classList.add('active');
          if (canPlay()) {
            if (v.getAttribute('preload') === 'none') v.setAttribute('preload', 'auto');
            var p = v.play(); if (p && p.catch) p.catch(function () {});
          }
        } else {
          v.classList.remove('active');
          w.setTimeout(function () { v.pause(); }, 900);
        }
      });
    };
    var stopRot = function () { if (rot) w.clearInterval(rot); rot = null; };
    var startRot = function () {
      stopRot();
      if (vids.length < 2 || !canPlay()) return;
      rot = w.setInterval(function () { vi = (vi + 1) % vids.length; showVid(vi); }, 10000);
    };
    var sync = function () {
      if (canPlay()) { showVid(vi); startRot(); }
      else { stopRot(); vids.forEach(function (v) { v.pause(); }); vids[vi].classList.add('active'); }
    };
    if ('IntersectionObserver' in w) {
      new IntersectionObserver(function (entries) { heroVisible = entries[0].isIntersecting; sync(); }, { threshold: 0.1 }).observe(hero);
    }
    d.addEventListener('visibilitychange', sync);
    onChange(reduce, function () { userPaused = reduce.matches; if (pauseBtn) pauseBtn.setAttribute('aria-pressed', userPaused ? 'true' : 'false'); sync(); });
    if (pauseBtn) {
      pauseBtn.setAttribute('aria-pressed', userPaused ? 'true' : 'false');
      pauseBtn.addEventListener('click', function () {
        userPaused = !userPaused;
        pauseBtn.setAttribute('aria-pressed', userPaused ? 'true' : 'false');
        sync();
      });
    }
    sync();
  }

  /* 6 · Demostración del hero: la conversación que se resuelve sola */
  var thread = $('.device[data-demo="hero"] .chat-thread');
  var T = Array.isArray(w.DEMO_THREAD) ? w.DEMO_THREAD : [];
  if (thread && T.length) {
    var nodes = T.map(function (m) {
      var el = d.createElement('div');
      el.className = m.type === 'chip' ? 'chip' : 'bubble ' + (m.type === 'out' ? 'out' : 'in');
      el.textContent = m.text;
      thread.appendChild(el);
      return el;
    });
    var typing = d.createElement('div');
    typing.className = 'typing';
    typing.innerHTML = '<i></i><i></i><i></i>';
    thread.appendChild(typing);

    var step = 0, timer = null, playing = false, inView = false, ready = false;
    var wait = function (ms, fn) { timer = w.setTimeout(fn, ms); };
    var showAll = function () { nodes.forEach(function (n) { n.classList.add('is-shown'); }); typing.classList.remove('is-shown'); };
    var resetAll = function () { nodes.forEach(function (n) { n.classList.remove('is-shown'); }); typing.classList.remove('is-shown'); step = 0; };
    var next = function () {
      if (!playing) return;
      if (step >= nodes.length) {
        wait(4200, function () {
          thread.classList.add('is-resetting');
          wait(320, function () { resetAll(); thread.classList.remove('is-resetting'); wait(500, next); });
        });
        return;
      }
      var m = T[step];
      var go = function () {
        typing.classList.remove('is-shown');
        nodes[step].classList.add('is-shown');
        step++;
        wait(m.type === 'in' ? 750 : (m.type === 'chip' ? 650 : 950), next);
      };
      if (m.type === 'out') { typing.classList.add('is-shown'); wait(950, go); }
      else wait(m.type === 'chip' ? 250 : 150, go);
    };
    var play = function () { if (playing) return; playing = true; next(); };
    var pause = function () { playing = false; w.clearTimeout(timer); typing.classList.remove('is-shown'); };
    var syncDemo = function () {
      if (reduce.matches) { pause(); showAll(); return; }
      if (ready && inView && !d.hidden) play(); else pause();
    };
    if ('IntersectionObserver' in w) {
      new IntersectionObserver(function (entries) { inView = entries[0].isIntersecting; syncDemo(); }, { threshold: 0.35 }).observe(thread.closest('.device'));
    } else { inView = true; }
    d.addEventListener('visibilitychange', syncDemo);
    onChange(reduce, function () { if (!reduce.matches) resetAll(); syncDemo(); });
    w.setTimeout(function () { ready = true; syncDemo(); }, 800);
  }

  /* 7 · Servicios: el teléfono cambia de pantalla con la tarjeta que pasa */
  var stage = $('.svc-stage');
  var screens = $$('.svc-stage .screen');
  var svcCards = $$('.svc-card');
  if (stage && screens.length && svcCards.length) {
    var setActive = function (key) {
      screens.forEach(function (s) { s.classList.toggle('is-active', s.getAttribute('data-screen') === key); });
      svcCards.forEach(function (c) { c.classList.toggle('is-active', c.getAttribute('data-screen') === key); });
    };
    setActive(svcCards[0].getAttribute('data-screen'));
    if ('IntersectionObserver' in w) {
      var ioSvc = new IntersectionObserver(function (entries) {
        entries.forEach(function (e) { if (e.isIntersecting) setActive(e.target.getAttribute('data-screen')); });
      }, { rootMargin: '-42% 0px -42% 0px', threshold: 0 });
      svcCards.forEach(function (c) { ioSvc.observe(c); });
    }
    /* Móvil: cada tarjeta lleva su pantalla en miniatura (estática) */
    svcCards.forEach(function (c) {
      var slot = $('.svc-mini', c);
      var key = c.getAttribute('data-screen');
      var src = screens.filter(function (s) { return s.getAttribute('data-screen') === key; })[0];
      if (slot && src && !slot.children.length) {
        var clone = src.cloneNode(true);
        clone.classList.add('is-active');
        $$('[id]', clone).forEach(function (n) { n.removeAttribute('id'); });
        slot.appendChild(clone);
      }
    });
  }

  /* 8 · Luz que sigue al cursor en las tarjetas (solo con ratón) */
  if (hoverable.matches) {
    $$('.card').forEach(function (card) {
      var raf = null;
      card.addEventListener('pointermove', function (e) {
        if (raf) return;
        raf = w.requestAnimationFrame(function () {
          raf = null;
          var r = card.getBoundingClientRect();
          card.style.setProperty('--mx', ((e.clientX - r.left) / r.width * 100).toFixed(1) + '%');
          card.style.setProperty('--my', ((e.clientY - r.top) / r.height * 100).toFixed(1) + '%');
        });
      });
    });
  }

  /* 9 · Vídeo del caso: botón de play propio sobre el póster */
  var cv = $('.case-video');
  if (cv) {
    var v = $('video', cv), b = $('.play-overlay', cv);
    if (v && b) {
      b.addEventListener('click', function () { var p = v.play(); if (p && p.catch) p.catch(function () {}); });
      v.addEventListener('play', function () { cv.classList.add('is-playing'); });
      v.addEventListener('pause', function () { if (v.currentTime === 0 || v.ended) cv.classList.remove('is-playing'); });
      v.addEventListener('ended', function () { cv.classList.remove('is-playing'); });
    }
  }

  /* 10 · Arky (ElevenLabs): el widget se carga cuando la página ya está lista */
  var convai = $('elevenlabs-convai[data-widget-src]');
  if (convai) {
    var loadWidget = function () {
      if (d.querySelector('script[data-convai]')) return;
      var sc = d.createElement('script'); sc.src = convai.getAttribute('data-widget-src'); sc.async = true; sc.setAttribute('data-convai', ''); d.body.appendChild(sc);
    };
    var schedule = function () { if ('requestIdleCallback' in w) w.requestIdleCallback(loadWidget, { timeout: 4000 }); else w.setTimeout(loadWidget, 2500); };
    if (d.readyState === 'complete') schedule(); else w.addEventListener('load', schedule);
  }
})();
