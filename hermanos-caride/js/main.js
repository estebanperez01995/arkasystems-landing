/* ═══════════════════════════════════════════════════════════════
   Hermanos Caride · Trabajos Verticales — scroll & interacción
   GSAP 3 + ScrollTrigger + Lenis (todo vendorizado en js/vendor)
   ═══════════════════════════════════════════════════════════════ */
(function () {
  "use strict";

  const CFG = window.CARIDE || {};
  const reduce = window.matchMedia("(prefers-reduced-motion: reduce)").matches;
  const isMobile = () => window.matchMedia("(max-width: 760px)").matches;

  gsap.registerPlugin(ScrollTrigger);

  /* ─── CTAs desde la configuración ─── */
  document.querySelectorAll("[data-cta]").forEach((a) => {
    const k = a.dataset.cta;
    if (k === "whatsapp" && CFG.whatsapp) { a.href = CFG.whatsapp; a.target = "_blank"; a.rel = "noopener"; }
    if (k === "tel" && CFG.phone) a.href = "tel:" + CFG.phone;
    if (k === "mail" && CFG.email) a.href = "mailto:" + CFG.email;
  });
  document.querySelectorAll("[data-email]").forEach((el) => { if (CFG.email) el.textContent = CFG.email; });
  document.getElementById("year").textContent = new Date().getFullYear();
  document.querySelectorAll("[data-legal]").forEach((a) => a.addEventListener("click", (e) => { e.preventDefault(); alert("Página legal pendiente de redactar con los datos del cliente."); }));

  /* ─── Smooth scroll (Lenis) ─── */
  let lenis = null;
  if (!reduce && window.Lenis) {
    lenis = new Lenis({ lerp: 0.1, smoothWheel: true });
    lenis.on("scroll", ScrollTrigger.update);
    gsap.ticker.add((t) => lenis.raf(t * 1000));
    gsap.ticker.lagSmoothing(0);
  }
  const scrollTo = (target) => {
    if (lenis) lenis.scrollTo(target, { offset: -70, duration: 1.4 });
    else target.scrollIntoView({ behavior: "smooth" });
  };
  document.querySelectorAll('a[href^="#"]').forEach((a) => {
    a.addEventListener("click", (e) => {
      const id = a.getAttribute("href");
      if (id.length < 2) return;
      const t = document.querySelector(id);
      if (!t) return;
      e.preventDefault();
      closeMenu();
      scrollTo(t);
    });
  });

  /* ─── Nav ─── */
  const nav = document.getElementById("nav");
  ScrollTrigger.create({ start: 80, onUpdate: (s) => nav.classList.toggle("is-solid", s.scroll() > 80) });

  const burger = document.getElementById("burger");
  const menu = document.getElementById("menu");
  function closeMenu() {
    menu.classList.remove("is-open"); menu.setAttribute("aria-hidden", "true");
    burger.setAttribute("aria-expanded", "false"); document.body.classList.remove("is-locked");
    lenis && lenis.start();
  }
  burger.addEventListener("click", () => {
    const open = !menu.classList.contains("is-open");
    if (!open) return closeMenu();
    menu.classList.add("is-open"); menu.setAttribute("aria-hidden", "false");
    burger.setAttribute("aria-expanded", "true"); document.body.classList.add("is-locked");
    lenis && lenis.stop();
  });

  /* ─── Preloader + intro hero ─── */
  const loader = document.getElementById("loader");
  const heroVideo = document.getElementById("heroVideo");

  function intro() {
    const tl = gsap.timeline({ defaults: { ease: "power4.out" } });
    tl.to(loader, { yPercent: -100, duration: 0.9, ease: "power4.inOut", onComplete: () => loader.remove() })
      .from(".hero__video", { scale: 1.18, duration: 2.2, ease: "power2.out" }, "<0.1")
      .to(".hero__title .line > span", { y: 0, duration: 1.1, stagger: 0.09 }, "<0.25")
      .to(".hero__sub", { opacity: 1, y: 0, duration: 0.9 }, "-=0.6")
      .to(".hero__actions", { opacity: 1, y: 0, duration: 0.9 }, "-=0.7")
      .to(".hero__meta", { opacity: 1, duration: 0.9 }, "-=0.6")
      .from(".nav", { y: -30, opacity: 0, duration: 0.8 }, "-=0.9");
  }
  if (reduce) { loader.remove(); gsap.set([".hero__title .line > span"], { y: 0 }); gsap.set([".hero__sub", ".hero__actions", ".hero__meta"], { opacity: 1, y: 0 }); }
  else window.addEventListener("load", () => setTimeout(intro, 500));

  /* ─── Hero scroll: parallax/zoom en modo loop, o scrub del vídeo ─── */
  if (!reduce) {
    if (CFG.heroVideoMode === "scrub") {
      // El vídeo avanza con el scroll. Hero queda fijado durante 250vh.
      heroVideo.removeAttribute("autoplay"); heroVideo.removeAttribute("loop"); heroVideo.pause();
      // Versión con keyframe en cada frame para que el scrubbing sea fluido.
      const scrubSrc = heroVideo.querySelector("source"); if (scrubSrc && !scrubSrc.src.startsWith("data:")) { scrubSrc.src = "videos/hero-scrub.mp4"; heroVideo.load(); }
      const setTime = (p) => { if (heroVideo.duration) heroVideo.currentTime = heroVideo.duration * p; };
      ScrollTrigger.create({
        trigger: ".hero", start: "top top", end: "+=250%", pin: true, scrub: 0.6,
        onUpdate: (s) => setTime(s.progress)
      });
      gsap.to(".hero__content", { yPercent: -30, opacity: 0, ease: "none", scrollTrigger: { trigger: ".hero", start: "top top", end: "+=120%", scrub: true } });
    } else {
      gsap.to(".hero__video", { scale: 1.15, yPercent: 8, ease: "none", scrollTrigger: { trigger: ".hero", start: "top top", end: "bottom top", scrub: true } });
      gsap.to(".hero__content", { yPercent: -25, opacity: 0, ease: "none", scrollTrigger: { trigger: ".hero", start: "top top", end: "70% top", scrub: true } });
      gsap.to(".hero__shade", { opacity: 1.6, ease: "none", scrollTrigger: { trigger: ".hero", start: "top top", end: "bottom top", scrub: true } });
    }
  }

  /* ─── Marquee infinito ─── */
  const track = document.querySelector(".marquee__track");
  if (track && !reduce) {
    const half = track.scrollWidth / 2;
    const mq = gsap.to(track, { x: -half, duration: 28, ease: "none", repeat: -1 });
    ScrollTrigger.create({ onUpdate: (s) => { mq.timeScale(1 + Math.min(Math.abs(s.getVelocity()) / 800, 3)); }, onScrubComplete: () => mq.timeScale(1) });
    gsap.ticker.add(() => { if (mq.timeScale() > 1) mq.timeScale(gsap.utils.interpolate(mq.timeScale(), 1, 0.05)); });
  }

  /* ─── Texto palabra a palabra (manifiesto y zona) ─── */
  document.querySelectorAll("[data-words]").forEach((el) => {
    const words = el.textContent.trim().split(/\s+/);
    el.innerHTML = words.map((w) => `<span class="w">${w}</span>`).join(" ");
    const spans = el.querySelectorAll(".w");
    if (reduce) return spans.forEach((s) => s.classList.add("is-on"));
    ScrollTrigger.create({
      trigger: el, start: "top 80%", end: "bottom 45%", scrub: true,
      onUpdate: (s) => {
        const n = Math.round(s.progress * spans.length);
        spans.forEach((sp, i) => sp.classList.toggle("is-on", i < n));
      }
    });
  });

  /* ─── Servicios: scroll horizontal fijado (solo escritorio/tablet) ─── */
  const svcTrack = document.getElementById("servicesTrack");
  const svcBar = document.getElementById("servicesBar");
  ScrollTrigger.matchMedia({
    "(min-width: 761px)": function () {
      if (reduce) return;
      const dist = () => svcTrack.scrollWidth - window.innerWidth;
      gsap.to(svcTrack, {
        x: () => -dist(), ease: "none",
        scrollTrigger: {
          trigger: ".services", start: "top top", end: () => "+=" + dist(), pin: ".services__pin", scrub: 0.8,
          invalidateOnRefresh: true, anticipatePin: 1,
          onUpdate: (s) => { svcBar.style.width = (s.progress * 100) + "%"; }
        }
      });
      gsap.from(".services__head", { y: 40, opacity: 0, duration: 1, scrollTrigger: { trigger: ".services", start: "top 70%" } });
    }
  });

  /* ─── Contadores ─── */
  document.querySelectorAll("[data-count]").forEach((el) => {
    const end = +el.dataset.count, pre = el.dataset.prefix || "", suf = el.dataset.suffix || "";
    const obj = { v: 0 };
    const render = () => { el.textContent = pre + Math.round(obj.v) + suf; };
    if (reduce) { obj.v = end; return render(); }
    gsap.to(obj, { v: end, duration: 1.8, ease: "power3.out", onUpdate: render, scrollTrigger: { trigger: el, start: "top 85%", once: true } });
  });

  /* ─── Parallax en medios (proyectos, seguridad) ─── */
  if (!reduce) {
    document.querySelectorAll("[data-speed]").forEach((el) => {
      const sp = parseFloat(el.dataset.speed) || 1;
      // Se escala ligeramente el medio para que el desplazamiento nunca deje bordes visibles.
      gsap.set(el, { scale: 1.12 });
      gsap.fromTo(el, { yPercent: (1 - sp) * 40 }, { yPercent: (sp - 1) * 40, ease: "none", scrollTrigger: { trigger: el, start: "top bottom", end: "bottom top", scrub: true } });
    });
    gsap.utils.toArray(".proj").forEach((p, i) => {
      gsap.from(p, { y: 60, opacity: 0, duration: 1, ease: "power3.out", delay: (i % 2) * 0.1, scrollTrigger: { trigger: p, start: "top 88%" } });
    });
  }

  /* ─── Proceso: pasos que se encienden ─── */
  document.querySelectorAll(".step").forEach((st) => {
    ScrollTrigger.create({ trigger: st, start: "top 65%", end: "bottom 35%", onToggle: (s) => st.classList.toggle("is-on", s.isActive) });
    if (!reduce) gsap.from(st, { x: 40, opacity: 0, duration: 0.9, ease: "power3.out", scrollTrigger: { trigger: st, start: "top 85%" } });
  });

  /* ─── Reveal de cabeceras ─── */
  if (!reduce) {
    gsap.utils.toArray(".projects__head, .safety__body, .contact__copy, .form, .stats__grid, .area__cols").forEach((el) => {
      gsap.from(el, { y: 50, opacity: 0, duration: 1.1, ease: "power3.out", scrollTrigger: { trigger: el, start: "top 82%" } });
    });
  }

  /* ─── Formulario ─── */
  const form = document.getElementById("form");
  const msg = document.getElementById("formMsg");
  form.addEventListener("submit", async (e) => {
    e.preventDefault();
    if (!form.checkValidity()) { msg.className = "form__msg err"; msg.textContent = "Revisa los campos obligatorios."; return; }
    const data = Object.fromEntries(new FormData(form).entries());
    data._source = location.hostname; data._ts = new Date().toISOString();
    if (CFG.webhook) {
      try {
        msg.className = "form__msg"; msg.textContent = "Enviando…";
        const r = await fetch(CFG.webhook, { method: "POST", headers: { "Content-Type": "application/json" }, body: JSON.stringify(data) });
        if (!r.ok) throw new Error(r.status);
        msg.className = "form__msg ok"; msg.textContent = "Recibido. Te llamamos en menos de 24 h."; form.reset();
      } catch (err) {
        msg.className = "form__msg err"; msg.textContent = "No se pudo enviar. Llámanos al " + (CFG.phonePretty || "") + ".";
      }
    } else {
      const body = `Nombre: ${data.name}\nTeléfono: ${data.phone}\nTipo: ${data.type}\n\n${data.message || ""}`;
      location.href = `mailto:${CFG.email}?subject=${encodeURIComponent("Solicitud de presupuesto · " + data.type)}&body=${encodeURIComponent(body)}`;
      msg.className = "form__msg ok"; msg.textContent = "Se abre tu correo con la solicitud preparada.";
    }
  });

  /* ─── Imágenes reales: si existe img/<nombre>.jpg se carga; si no, queda el placeholder ─── */
  document.querySelectorAll("[data-img]").forEach((box) => {
    const name = box.dataset.img;
    const img = new Image();
    img.alt = ""; img.loading = "lazy"; img.decoding = "async";
    img.onload = () => { box.appendChild(img); box.classList.add("has-img"); ScrollTrigger.refresh(); };
    img.src = `img/${name}.jpg`;
  });

  window.addEventListener("load", () => ScrollTrigger.refresh());
})();
