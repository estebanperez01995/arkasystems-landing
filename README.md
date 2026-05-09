# Arka Systems — Landing Page

Landing page de [arkasystems.es](https://www.arkasystems.es). Una sola página, HTML + CSS + JS vanilla, sin build, sin frameworks.

## Estructura

```
arkasystems-landing/
├── index.html      ← landing completa (todo inline: CSS + JS)
└── README.md
```

## Conectar las URLs reales (1 sola edición)

Todos los CTAs (`data-arka-cta="whatsapp"`, `data-arka-cta="calendly"`) leen sus URLs de un único bloque al inicio del `<head>`:

```html
<script>
window.ARKA_LINKS = {
  whatsapp: "https://wa.me/34TUNUMERO?text=Hola%20Esteban...",
  calendly: "https://calendar.app.google/TU-ID-DE-RESERVA",
  webhook:  "https://tasty-n8n.2pebut.easypanel.host/webhook/arka-leads"
};
</script>
```

Edita estas 3 URLs y todos los botones de la página apuntan a lo correcto. **No hace falta tocar nada más en el HTML.**

### WhatsApp

Formato: `https://wa.me/<código de país sin +><número>?text=<mensaje URL-encoded>`

Ejemplo:
```
https://wa.me/34631980043?text=Hola%20Esteban%2C%20vengo%20de%20arkasystems.es%20y%20quiero%20automatizar%20%5BX%5D%20en%20mi%20negocio.
```

### Calendly / Google Appointment Schedule

Pega la URL pública de tu evento de reserva (calendar.app.google/... o calendly.com/...).

### Webhook del formulario

El form del drawer postea aquí en JSON. Por defecto apunta al webhook actual de n8n. Si lo cambias, asegúrate de que acepta `POST` con `Content-Type: application/json`.

Payload de ejemplo:

```json
{
  "name": "Carlos",
  "contact": "+34 600 000 000",
  "task": "Confirmación de citas por WhatsApp",
  "_source": "arkasystems.es",
  "_ts": "2026-05-09T12:00:00.000Z"
}
```

## Pendientes para producción

- [ ] Reemplazar `https://www.arkasystems.es/og.png` por imagen OG real (1200×630, fondo cálido oscuro, logo + tagline)
- [ ] Sustituir `wa.me/34000000000` por el número de WhatsApp real
- [ ] Sustituir `calendar.app.google/REEMPLAZAR` por la URL de reserva real
- [ ] Reemplazar la foto del founder (sección "Quién está detrás" — el `.founder-photo` placeholder)
- [ ] Crear las páginas `/aviso-legal` y `/privacidad` (links del footer)

## Deploy

### Cloudflare Pages (recomendado, gratis)

1. Conecta este repo a Cloudflare Pages.
2. Build command: *(ninguno)*
3. Build output directory: `/` (la raíz)
4. Deploy.

Domain custom → arkasystems.es desde Cloudflare DNS (en menos de 1 min si el dominio ya está en Cloudflare).

### Vercel

Mismo flow: importar repo, framework "Other", build command vacío, output `/`.

## Stack

- HTML5 + CSS (oklch + custom properties + container queries)
- JS vanilla (IntersectionObserver para reveal, fetch API para form)
- Google Fonts: Geist + Geist Mono + Instrument Serif
- Sin React, sin build, sin npm, sin nada
- Pesa ~60 KB total, carga en <1s

## Cómo está hecha

Esta landing salió de una iteración con Claude Design + retoques manuales. El copy, ICP, posicionamiento y pricing están alineados con el Business Plan v3.0 de Arka Systems. La presentación de Voraldent es como **caso real + patrón replicable** para no nichar la web a clínicas.
