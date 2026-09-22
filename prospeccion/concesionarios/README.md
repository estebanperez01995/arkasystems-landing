# Prospección de concesionarios (coches y motos) — España

Pipeline para sacar de Google Maps los concesionarios de toda España que **tienen web** y además
**email, WhatsApp o redes**, y cargarlos en `CRM PROSPECCION` en una pestaña nueva llamada
`consecionarias`.

> **Por qué no está ejecutado ya:** la sesión de Claude en la nube donde se escribió esto tiene la
> red de salida restringida por política del entorno (solo registros de paquetes y las APIs de
> Anthropic). `api.apify.com`, `google.com` y cualquier web devuelven 403 desde ahí. El scraping hay
> que lanzarlo desde un sitio con red: tu Mac, tu n8n o un entorno con la política de red abierta.

## Requisitos

- Cuenta de Apify con saldo (el actor `compass/crawler-google-places` es de pago por resultado).
- Python 3.9+.
- Para la subida a Sheets: `pip install gspread google-auth` y una service account con permiso de
  edición sobre la hoja (o `gspread.oauth()` con tu usuario).

## Paso 1 — Scraping

1. Abre el actor **Google Maps Scraper** (`compass/crawler-google-places`) en Apify.
2. Pega `apify_input.json` como input.
3. Lanza y espera. Descarga el dataset **en formato JSON** → `dataset.json`.

Claves del input, y por qué:

| Campo | Valor | Motivo |
|---|---|---|
| `website` | `withWebsite` | descarta de entrada los que no tienen web (requisito tuyo) |
| `scrapeContacts` | `true` | es lo que saca **emails y perfiles de redes** entrando en la web del negocio |
| `maxCrawledPlacesPerSearch` | `120` | 5 términos × 120 ≈ 600 sitios por zona antes de filtrar |
| `language` / `countryCode` | `es` | resultados y categorías en español |

**Cobertura de todo España.** Si `locationQuery: "Spain"` no da profundidad suficiente (Google
limita resultados por búsqueda), relanza por provincias. Lista lista para pegar en `locationQuery`,
una ejecución por bloque:

```
Madrid · Barcelona · Valencia · Sevilla · Zaragoza · Málaga · Murcia · Palma · Las Palmas ·
Bilbao · Alicante · Córdoba · Valladolid · Vigo · Gijón · Granada · A Coruña · Vitoria ·
Santa Cruz de Tenerife · Pamplona · Almería · San Sebastián · Santander · Castellón · Burgos ·
Albacete · Salamanca · Logroño · Badajoz · Huelva · Lleida · Tarragona · León · Cádiz · Jaén ·
Ourense · Girona · Lugo · Cáceres · Toledo · Ciudad Real · Guadalajara · Cuenca · Ávila ·
Segovia · Soria · Zamora · Palencia · Huesca · Teruel · Mérida · Melilla · Ceuta
```

Con las 10 primeras provincias suele bastar para pasar de 200 filas contactables. Empieza por ahí y
amplía solo si hace falta: cada resultado se paga.

## Paso 2 — Filtrado

```bash
python3 filtrar.py dataset.json -o concesionarias.csv
```

Qué hace:

- Descarta lo que no tiene web.
- Descarta lo que tiene web pero **ni email, ni WhatsApp, ni Instagram/Facebook**.
- Deduplica por nombre + dominio.
- Normaliza el teléfono a `+34XXXXXXXXX` y marca como `whatsapp` **solo los móviles** (6 y 7): un
  fijo en WhatsApp es un envío quemado.
- Clasifica `tipo` en `coches` / `motos` / `ambos`.
- Marca `vende_online` cuando la web enseña señales reales de venta o reserva online
  (`/stock`, "reserva online", "compra online", financiación online, carrito…).
- Marca `es_cadena` con una lista de grupos conocidos, para que puedas respetar el
  `solo_no_cadena: TRUE` que ya tienes en la configuración del CRM.
- Sale con error si no llega al mínimo de 200, para que te enteres antes de subir nada.

Imprime un resumen con cuántos descartó y por qué.

## Paso 3 — Carga en el CRM

```bash
export GOOGLE_APPLICATION_CREDENTIALS=/ruta/service-account.json
python3 subir_sheets.py concesionarias.csv
```

Crea la pestaña `consecionarias` en `CRM PROSPECCION` (ID ya puesto en el script), escribe las filas,
congela la cabecera y te devuelve el enlace directo. Si la pestaña ya existe, **aborta** en vez de
pisarla; para reemplazarla, `--reemplazar`.

**Plan B sin credenciales:** en la hoja, `Archivo → Importar → Subir → concesionarias.csv` y elige
*"Insertar hoja(s) nueva(s)"*. Luego renombra la pestaña a `consecionarias`.

## Paso 4 — Antes de disparar mensajes

La configuración actual del CRM apunta a otro sector y está en modo prueba:

- `pestana_leads: clinicas dentales` → cambiar a `consecionarias`.
- `modo_prueba: TRUE` y `numero_prueba: 34671286513` → así todo se envía a tu propio número.
- `solo_no_cadena: TRUE` → con la columna `es_cadena` que genera el filtro, esto ya funciona.
- La variante de mensaje `C1 / demo-carritos` es de e-commerce: para concesionarios hay que dar de
  alta una variante nueva con los textos de la sección 11 de `OFERTA-concesionarios.md`.

## Columnas que genera

`contactado · nombre · tipo · vende_online · categoria · direccion · poblacion · codigo_postal ·
provincia · telefono · whatsapp · whatsapp_origen · web · instagram · facebook · linkedin · tiktok ·
youtube · email · rating · num_resenas · es_cadena · google_maps · zona_busqueda · estado_crm ·
aviso · chip · fecha_envio · variante`

Las cuatro últimas van vacías: las rellena tu automatización, igual que en la pestaña de clínicas.

## Aviso sobre los nombres de campo de Apify

Los nombres de campo del input y del output (`scrapeContacts`, `socialProfiles`, `emails`,
`contactDetails`…) son los del actor en el momento de escribir esto, y **no se han podido verificar
contra la documentación en vivo** porque el entorno no tiene salida a internet. Si el actor cambió
algún nombre, `filtrar.py` devolverá menos filas de lo esperado: mira el resumen que imprime y
ajusta las claves en las funciones `main()` y `vende_online()`.
