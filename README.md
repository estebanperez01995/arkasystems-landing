# Arka Systems — Landing Page

Landing de [arkasystems.es](https://www.arkasystems.es). HTML + CSS + JS vanilla, sin build,
sin frameworks. Servida por nginx (Dockerfile) en Easypanel desde la rama `main`.

Rediseño del 9-oct-2026: "Golden Arka nocturno, con materia y una demostración real".

## Estructura

```
arkasystems-landing/
├── index.html            ← la landing (solo HTML; el copy vive aquí)
├── assets/site.css       ← todo el estilo: tokens, materia, motion, reduced-motion
├── assets/site.js        ← CTAs, nav, reveals, vídeos, demostración, servicios, widget
├── assets/mark-64.png    ← marca para la nav (mark-256.png para 2x y favicon)
├── assets/founders/      ← foto de fundadores en WebP (440 y 880)
├── videos/               ← 3 renders del hero (mp4 + póster webp) y testimonio Voraldent
├── aviso-legal.html · privacidad.html   ← heredan site.css
├── index-dental.html     ← versión antigua, huérfana (nadie la enlaza)
└── _sin-usar/            ← material descartado, fuera de git
```

## Lo que se edita sin tocar nada más

Las cosas que cambian con frecuencia están en el `<head>` de `index.html`:

1. **`window.ARKA_LINKS`**: WhatsApp, enlace de reserva y webhook. Todos los botones
   `data-arka-cta="whatsapp|calendly"` leen de aquí.
2. **`window.DEMO_THREAD`**: los mensajes del teléfono del hero (la conversación que se
   resuelve sola). `type: "in"` escribe el cliente, `"out"` responde el sistema, `"chip"`
   es un estado. Se reproduce en bucle, se pausa fuera de pantalla y con
   `prefers-reduced-motion` se muestra en estado final.
3. Las pantallas del teléfono de Servicios están en el HTML bajo el comentario
   `Demostración: pantallas del teléfono`. Cada tarjeta `.svc-card[data-screen]` activa la
   pantalla `.screen[data-screen]` del mismo nombre al pasar por el centro del viewport.

Los textos de la página están tal cual se aprobaron; el rediseño del 9-oct no cambió copy.

## Sistema de diseño (resumen de site.css)

- Tokens: neutros cálidos en oklch (`--bg`, `--surface-1/2/3`, `--ink`…), acento ámbar
  `--accent`, materia (`--edge`, `--shadow-1/2`, `--glow`), motion (`--ease-out`, `--dur-1..4`).
- Tarjetas `.card`: superficie con borde-luz, sombra con desplazamiento y luz que sigue al
  cursor (`--mx/--my`, solo con ratón).
- Motion: una coreografía de entrada en el hero (≤ 1 s), `reveal-lead` (blur-materialize)
  solo en el elemento principal de cada sección, `stagger` en una lista por vista,
  pulsación `scale(.98)` en botones, `:focus-visible` ámbar, FAQ animado con
  `::details-content` donde el navegador lo soporta.
- `prefers-reduced-motion`: sin desplazamientos ni blur, vídeos en póster, demo en estado final.
- Vídeos del hero: uno activo, rotación cada 10 s solo con la pestaña visible, botón de pausa.
- Arky (ElevenLabs) se carga después de `load`, en idle, para no bloquear el primer render.
- Fuentes autohospedadas en `assets/fonts/` (`fonts.css`), sin llamadas a Google Fonts.

## SEO

- Título con la keyword primero (`Automatización con IA para empresas en Barcelona | Arka Systems`),
  meta description sin condiciones comerciales, canonical, hreflang, Open Graph y Twitter.
- JSON-LD: ProfessionalService, FAQPage (generado desde el FAQ visible: si cambias una
  pregunta en el HTML, cambia también el bloque) y VideoObject.
- `index-dental.html` lleva `noindex`; las legales `noindex, follow`; `sitemap.xml` con las tres
  URLs indexables.
- Lo que falta para posicionar de verdad son páginas por nicho y un perfil de Google Business;
  esta página sola compite poco.

## Analítica

Umami (sin cookies) en `stats.arkasystems.es`. Los CTAs llevan `data-umami-event`
(`cta-whatsapp-nav`, `cta-whatsapp-hero`, `cta-diagnostico-hero`, `cta-whatsapp-final`,
`cta-diagnostico-final`, `cta-whatsapp-footer`).

## Deploy

Push a `main` → Easypanel reconstruye la imagen nginx. Si producción no cambia tras el push,
hay que lanzar el deploy a mano desde el panel (en oct-2026 el autodeploy no se disparó
con dos commits seguidos).

## Pendientes (decisión del CEO, fuera del rediseño)

- Cifras del caso Voraldent: usar las medidas de la ficha (85 % confirmación, 2 % ausencias
  sobre 2.250 citas, 30 de 200 recalls) y etiquetar "más de 15 h" como estimación.
- Handle de Instagram (`esteban.arkasystems` → verificar `estebanperez.ia`), "bot" en el FAQ,
  "Casos reales" en plural con un caso, mayúsculas del párrafo de fundadores.
- `index-dental.html`: borrar o redirigir.
- Regenerar los renders del hero sin cifras inventadas.
