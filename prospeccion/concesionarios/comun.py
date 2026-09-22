"""Utilidades compartidas: normalizacion, extraccion de contacto y clasificacion."""
import re

COLUMNAS = [
    "contactado", "nombre", "tipo", "vende_online", "categoria", "direccion",
    "poblacion", "codigo_postal", "provincia", "telefono", "whatsapp",
    "whatsapp_origen", "web", "instagram", "facebook", "linkedin", "tiktok",
    "youtube", "email", "rating", "num_resenas", "es_cadena", "google_maps",
    "zona_busqueda", "estado_crm", "aviso", "chip", "fecha_envio", "variante",
]

# --- WhatsApp -------------------------------------------------------------
# Los tres formatos que usan de verdad las webs, mas el widget flotante que
# inyectan por JS (por eso visitamos con navegador y no con curl).
RE_WA = [
    re.compile(r"(?:https?://)?(?:api\.)?wa\.me/(?:\+?)(\d{9,15})", re.I),
    re.compile(r"api\.whatsapp\.com/send/?\?[^\"'\s]*phone=(?:%2B|\+)?(\d{9,15})", re.I),
    re.compile(r"whatsapp://send\?[^\"'\s]*phone=(?:%2B|\+)?(\d{9,15})", re.I),
    re.compile(r"web\.whatsapp\.com/send\?[^\"'\s]*phone=(?:%2B|\+)?(\d{9,15})", re.I),
]
# "WhatsApp: 611 22 33 44" en texto plano, hasta 60 caracteres de distancia.
RE_WA_TEXTO = re.compile(
    r"whats\s?app[^0-9+]{0,60}((?:\+?34[\s.-]?)?[67](?:[\s.-]?\d){8})", re.I)

RE_EMAIL = re.compile(r"[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}")
EMAIL_BASURA = ("@sentry", "@example", "@2x", "@domain", "wixpress", "@sitename",
                "@email.com", "@tudominio", "noreply@", "no-reply@")

REDES = {
    "instagram": re.compile(r"https?://(?:www\.)?instagram\.com/([A-Za-z0-9_.]+)", re.I),
    "facebook": re.compile(r"https?://(?:www\.|es-es\.)?facebook\.com/([A-Za-z0-9_.\-]+)", re.I),
    "linkedin": re.compile(r"https?://(?:[a-z]{2}\.)?linkedin\.com/(?:company|in)/([A-Za-z0-9_.\-]+)", re.I),
    "tiktok": re.compile(r"https?://(?:www\.)?tiktok\.com/@([A-Za-z0-9_.]+)", re.I),
    "youtube": re.compile(r"https?://(?:www\.)?youtube\.com/(?:c/|channel/|user/|@)([A-Za-z0-9_.\-]+)", re.I),
}
REDES_BASURA = ("sharer", "share.php", "intent", "plugins", "dialog", "login",
                "policy", "privacy", "help", "developers", "watch?v=", "embed")

SENALES_ONLINE = [
    "reserva online", "reservar online", "resérvalo online", "compra online",
    "comprar online", "compra 100% online", "financia online", "financiación online",
    "tienda online", "añadir al carrito", "add to cart", "reserva tu coche",
    "reserva tu moto", "/stock", "/vehiculos-ocasion", "/coches-ocasion",
    "/nuestro-stock", "/km0", "reservar ahora", "comprar ahora", "paga y reserva",
]

CADENAS = ["quadis", "caetano", "astara", "pons", "autolica", "ibericar", "clicars",
           "flexicar", "ocasionplus", "carplus", "grupo mocauto", "movilnorte",
           "grupo julia", "grupo dalmau", "aurgi", "grupo marcos", "lesseps"]

MOTO = ["moto", "motocicleta", "scooter", "ciclomotor", "harley", "ducati",
        "kawasaki", "ktm", "vespa", "piaggio", "motorrad", "motos"]
# OJO: "concesionario" a secas NO va aqui: sale tambien en los de motos.
COCHE = ["coche", "automovil", "automóvil", "turismo", "vehiculo", "vehículo",
         "car dealer", "automocion", "automoción"]


def norm(t):
    return (t or "").lower()


def e164(tel):
    """Normaliza un telefono espanol a +34XXXXXXXXX. '' si no es valido."""
    if not tel:
        return ""
    d = re.sub(r"\D", "", str(tel))
    if d.startswith("0034"):
        d = d[4:]
    elif d.startswith("34") and len(d) > 9:
        d = d[2:]
    return "+34" + d if len(d) == 9 else ""


def es_movil(t):
    """Solo 6 y 7 aceptan WhatsApp de forma fiable en Espana."""
    return bool(t) and t[3] in "67"


def whatsapp_de_html(html):
    """Devuelve (numero_e164, origen) o ('', ''). Prioriza el enlace explicito."""
    for rx in RE_WA:
        for m in rx.finditer(html or ""):
            n = e164(m.group(1))
            if n:
                return n, "web-enlace"
    m = RE_WA_TEXTO.search(html or "")
    if m:
        n = e164(m.group(1))
        if n:
            return n, "web-texto"
    return "", ""


def emails_de_html(html):
    vistos = []
    for m in RE_EMAIL.finditer(html or ""):
        e = m.group(0).lower().rstrip(".")
        if any(b in e for b in EMAIL_BASURA) or e.endswith((".png", ".jpg", ".webp", ".svg")):
            continue
        if e not in vistos:
            vistos.append(e)
    # Los buzones genericos de contacto van primero: son los que se leen.
    vistos.sort(key=lambda e: 0 if e.split("@")[0] in
                ("info", "contacto", "ventas", "comercial", "hola", "recepcion") else 1)
    return vistos


def redes_de_html(html):
    out = {}
    for red, rx in REDES.items():
        for m in rx.finditer(html or ""):
            url = m.group(0)
            if any(b in url.lower() for b in REDES_BASURA):
                continue
            out[red] = url
            break
    return out


def vende_online(html, web):
    blob = norm(html) + " " + norm(web)
    return "TRUE" if any(s in blob for s in SENALES_ONLINE) else "FALSE"


def clasificar(nombre, categoria):
    blob = norm(nombre) + " " + norm(categoria)
    moto = any(k in blob for k in MOTO)
    coche = any(k in blob for k in COCHE)
    if moto and coche:
        return "ambos"
    return "motos" if moto else "coches"


def es_cadena(nombre):
    return "TRUE" if any(c in norm(nombre) for c in CADENAS) else "FALSE"
