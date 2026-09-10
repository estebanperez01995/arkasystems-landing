# Hermanos Caride · Trabajos Verticales — web con efecto scroll

Web de una sola página para **Hermanos Caride Fernández Trabajos Verticales S.L.** (Coles, Ourense).
HTML + CSS + JS vanilla, sin build. Efectos de scroll con **GSAP ScrollTrigger** y scroll suave con **Lenis**, ambos vendorizados en `js/vendor/` (no dependen de ningún CDN).

```
hermanos-caride/
├── index.html        ← contenido + bloque de configuración (teléfono, WhatsApp, email, webhook, modo del vídeo)
├── css/style.css     ← estilos (tema oscuro industrial, naranja seguridad)
├── js/main.js        ← animaciones y formulario
├── js/vendor/        ← gsap.min.js, ScrollTrigger.min.js, lenis.min.js
├── img/              ← favicon, poster del vídeo y fotos/renders (ver PROMPTS.md)
├── videos/           ← hero.mp4 (no se sube a git; ver videos/README.md)
└── PROMPTS.md        ← prompts de imagen/vídeo para Higgsfield
```

## Efectos de scroll incluidos

| Sección | Efecto |
|---|---|
| Hero | Vídeo a pantalla completa con zoom + parallax al hacer scroll. Titular con entrada línea a línea. Modo alternativo **scrub** (el vídeo avanza con el scroll). |
| Marquee | Cinta infinita que acelera con la velocidad del scroll. |
| Manifiesto / Zona | Texto que se "enciende" palabra a palabra según avanzas. |
| Servicios | Sección fijada con desplazamiento horizontal de tarjetas y barra de progreso (en móvil se apila en vertical). |
| Números | Contadores animados. |
| Proyectos | Parallax por tarjeta con velocidades distintas + reveal. |
| Proceso | Columna izquierda pegajosa, pasos que se activan al pasar por el centro. |
| Seguridad | Imagen con parallax + reveal del texto. |
| Footer | Palabra gigante de fondo. |

Respeta `prefers-reduced-motion`: sin animaciones para quien lo tenga activado.

## Puesta en marcha (paso a paso)

1. **Vídeo del hero** → copiar el MP4 final como `videos/hero.mp4` (instrucciones de compresión en `videos/README.md`). Mientras tanto se usa la URL temporal de Higgsfield como fallback.
2. **Poster** → extraer un frame del vídeo a `img/hero-poster.jpg` (comando en `videos/README.md`).
3. **Imágenes** → generar con los prompts de `PROMPTS.md` y guardar con estos nombres exactos en `img/` (JPG, 1600 px de ancho aprox.):
   `ferroviario.jpg`, `puentes.jpg`, `fachadas.jpg`, `cubiertas.jpg`, `limpieza.jpg`, `viaducto.jpg`, `talud.jpg`, `fachada-ourense.jpg`, `arco.jpg`, `seguridad.jpg`.
   La web las detecta sola: si el archivo existe, sustituye el placeholder gris.
4. **Datos** → editar el bloque `window.CARIDE` al inicio de `index.html`: teléfono, WhatsApp, email y webhook del formulario.
5. **Logo** → sustituir el símbolo `#logo-mark` (SVG al final de `index.html`) por el logo real del cliente, y `img/favicon.svg`.
6. **Confirmar con el cliente** los textos marcados como *CONFIRMAR* (certificaciones en Seguridad, email) y las estadísticas de la sección Números.
7. **Legal** → redactar aviso legal y privacidad (ahora los enlaces muestran un aviso).
8. **Deploy** → ver sección "Publicar en Vercel" más abajo.

## Modo "scrub" del vídeo

En `index.html`, `heroVideoMode` controla el hero. Por defecto `"loop"`: el vídeo se reproduce en bucle con zoom y parallax al hacer scroll (`videos/hero.mp4`). Con `"scrub"` el vídeo no se reproduce solo: el hero se fija 3 pantallas (`heroScrubScreens`) y avanza con el scroll usando `videos/hero-scrub.mp4` (keyframe en cada frame).

## Ver en local

```
npx http-server -p 8080 .
# abrir http://localhost:8080/hermanos-caride/
```

## Publicar en Vercel (gratis)

1. Entra en [vercel.com/new](https://vercel.com/new) con la cuenta de GitHub e importa el repositorio `arkasystems-landing`.
2. En la pantalla de configuración:
   - **Framework Preset**: Other
   - **Root Directory**: `hermanos-caride`  (pulsar *Edit* y elegir la carpeta)
   - Build Command y Output Directory: vacíos
3. Deploy. Vercel devuelve una URL tipo `https://hermanos-caride.vercel.app`.
4. Como la web está en la rama `claude/vertical-work-company-website-u4j4ua`, en *Settings → Git → Production Branch* poner esa rama (o hacer merge a `main`).
5. Dominio propio: *Settings → Domains* → añadir `hermanoscaridefernandez.com` y seguir las instrucciones de DNS.

`vercel.json` ya incluye caché larga para vídeos e imágenes y URLs limpias.
