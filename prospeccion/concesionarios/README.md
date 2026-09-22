# Prospección de concesionarios (coches y motos) — España

Saca de **Google Maps** todos los concesionarios de las ciudades que le pongas, entra **una por una
en sus webs** para pescar el **WhatsApp**, el email y las redes, y lo carga en `CRM PROSPECCION` en
una pestaña nueva llamada `consecionarias`.

**Sin Apify y sin APIs de pago.** Conduce un Chromium real con Playwright.

> **Por qué no está ejecutado.** La sesión de Claude en la nube donde se escribió esto no tiene
> salida a internet: el proxy del entorno rechaza el CONNECT a cualquier host que no sea un registro
> de paquetes o la API de Anthropic. Chromium arranca perfectamente, pero al navegar devuelve
> `net::ERR_TUNNEL_CONNECTION_FAILED`. Comprobado con Google Maps, Bing y DuckDuckGo.
> **Todo lo que no es la red está escrito y probado** (ver `test_extraccion.py`).

## Ejecutar

```bash
pip install playwright && playwright install chromium   # solo la primera vez
python3 1_buscar_maps.py --ciudades ciudades.txt --out maps.json
python3 2_visitar_webs.py maps.json -o concesionarias.csv
python3 3_subir_sheets.py concesionarias.csv
```

Los tres pasos **se pueden cortar y reanudar**: el 1 guarda después de cada búsqueda y no repite las
ya hechas; el 2 cachea cada web visitada en `webs_cache.json`.

### Paso 1 — Google Maps (`1_buscar_maps.py`)

Por cada ciudad de `ciudades.txt` y cada uno de los 4 términos (`concesionario de coches`,
`concesionario oficial`, `venta de coches de ocasión`, `concesionario de motos`): abre la búsqueda,
acepta el muro de cookies, **baja por el panel de resultados** hasta que deja de crecer o llega al
final, y entra en cada ficha a sacar nombre, categoría, dirección, teléfono, web, rating y reseñas.

- `--por-busqueda 40` (por defecto): tope de fichas por término y ciudad. 25 ciudades × 4 términos ×
  40 ≈ 4.000 fichas como techo. Con las 10 primeras ciudades ya se pasa de 200 de sobra.
- `--headful` abre el navegador con ventana, para ver qué pasa si algo falla.

> **Este es el paso frágil.** Google cambia el DOM de Maps cada pocos meses. Los selectores llevan
> alternativas (`h1.DUwDvf` → `h1`, `button[data-item-id="address"]` → tooltip de copiar…), pero si
> un día devuelve fichas vacías, es aquí y se arregla mirando con `--headful`. Ve despacio a
> propósito (esperas aleatorias de 0,8–3 s): si aceleras, Google mete captcha.

### Paso 2 — Las webs (`2_visitar_webs.py`)

Esta es la parte que de verdad te interesa: **de dónde sale el WhatsApp**.

Se visita con navegador y no con `curl` porque **el botón de WhatsApp de la mayoría de las webs lo
inyecta un widget por JavaScript**: en el HTML crudo no existe. Por cada web se prueban la home y
luego `/contacto`, `/contactar`, `/contact`, `/es/contacto`, `/quienes-somos`, y se leen tanto el
HTML renderizado como los `href` de todos los enlaces.

Formatos de WhatsApp que reconoce, en orden de fiabilidad:

| Origen | Qué detecta |
|---|---|
| `web-enlace` | `wa.me/34…`, `api.whatsapp.com/send?phone=…`, `whatsapp://send?phone=…`, `web.whatsapp.com/send?phone=…` |
| `web-texto` | "WhatsApp: 611 22 33 44" en el texto, hasta 60 caracteres de distancia |
| `maps-movil` | sin nada en la web, pero el teléfono de Maps es móvil (6 o 7) |

Los fijos (9…) se guardan como `telefono` pero **no** como WhatsApp salvo que la web los publique
explícitamente como tal: un envío a un fijo es un envío quemado.

También saca email (priorizando `info@`, `contacto@`, `ventas@`, y descartando basura tipo
`@sentry`, `logo@2x`), Instagram, Facebook, LinkedIn, TikTok y YouTube (descartando enlaces de
compartir y de login), y marca `vende_online` cuando la web enseña señales reales de venta o reserva
online.

El CSV sale **ordenado con los que tienen WhatsApp primero**. Se cargan todos los encontrados, con
WhatsApp y sin él, como pediste.

### Paso 3 — El CRM (`3_subir_sheets.py`)

```bash
export GOOGLE_APPLICATION_CREDENTIALS=/ruta/service-account.json
python3 3_subir_sheets.py concesionarias.csv
```

Crea la pestaña `consecionarias` en `CRM PROSPECCION`, escribe las filas y congela la cabecera. Si
la pestaña existe, aborta en vez de pisarla (`--reemplazar` para forzar).

**Sin credenciales:** en la hoja, `Archivo → Importar → Subir → concesionarias.csv` →
*"Insertar hoja(s) nueva(s)"*, y renombrar la pestaña a `consecionarias`.

## Comprobar que la extracción funciona (sin red)

```bash
python3 test_extraccion.py
```

17 casos: los cuatro formatos de enlace de WhatsApp, el widget inyectado por JS, el número en texto
plano, el fijo, emails con basura mezclada, redes con enlaces de compartir, clasificación
coches/motos/ambos y normalización de teléfonos. Todos pasan.

## Columnas que genera

`contactado · nombre · tipo · vende_online · categoria · direccion · poblacion · codigo_postal ·
provincia · telefono · whatsapp · whatsapp_origen · web · instagram · facebook · linkedin · tiktok ·
youtube · email · rating · num_resenas · es_cadena · google_maps · zona_busqueda · estado_crm ·
aviso · chip · fecha_envio · variante`

Las cuatro últimas van vacías: las rellena tu automatización, igual que en la pestaña de clínicas.

## Antes de disparar mensajes

La configuración actual del CRM apunta a otro sector y está en modo prueba:

- `pestana_leads: clinicas dentales` → cambiar a `consecionarias`.
- `modo_prueba: TRUE` con `numero_prueba: 34671286513` → así todo va a tu propio número.
- `solo_no_cadena: TRUE` → funciona con la columna `es_cadena` que genera el paso 2.
- La variante `C1 / demo-carritos` es de e-commerce: alta una variante nueva con los textos de la
  sección 11 de `OFERTA-concesionarios.md`.
