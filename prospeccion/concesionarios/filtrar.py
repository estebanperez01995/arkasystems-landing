#!/usr/bin/env python3
"""Filtra el export de Apify (Google Maps) y deja solo concesionarios contactables.

Uso:
    python3 filtrar.py dataset.json -o concesionarias.csv

Entrada: el JSON que descargas del dataset del actor (formato lista de objetos).
Salida: CSV con las columnas del CRM, listo para subir a Sheets.

Criterio de corte (lo que pidio Esteban): web SI o SI, y ademas al menos uno de
email / whatsapp / redes sociales. Los que no lo cumplen se descartan y se
cuentan en el resumen final.
"""
import argparse, csv, json, re, sys
from collections import Counter

COLUMNAS = [
    "contactado", "nombre", "tipo", "vende_online", "categoria", "direccion",
    "poblacion", "codigo_postal", "provincia", "telefono", "whatsapp",
    "whatsapp_origen", "web", "instagram", "facebook", "linkedin", "tiktok",
    "youtube", "email", "rating", "num_resenas", "es_cadena", "google_maps",
    "zona_busqueda", "estado_crm", "aviso", "chip", "fecha_envio", "variante",
]

# Señales de venta online en la web del negocio (texto o URLs capturadas por el actor).
SENALES_ONLINE = [
    "reserva online", "reservar online", "compra online", "comprar online",
    "compra 100% online", "financia online", "financiacion online",
    "tienda online", "carrito", "add to cart", "/stock", "/vehiculos",
    "/coches-ocasion", "/vehiculos-ocasion", "/km0", "/nuestro-stock",
    "reserva tu coche", "reserva tu moto", "reservalo online",
]

CADENAS = [
    "quadis", "grupo mocauto", "caetano", "astara", "pons", "aurgi", "nuba",
    "grupo dalmau", "movilnorte", "autolica", "grupo julia", "vehiculos de ocasion sl",
    "carplus", "clicars", "flexicar", "ocasionplus", "wallapop", "autocasion",
    "grupo ibericar", "ibericar", "grupo rio", "lesseps", "grupo marcos",
]

MOTO = ["moto", "motocicleta", "scooter", "ciclomotor", "harley", "ducati", "kawasaki",
        "yamaha", "honda moto", "ktm", "vespa", "piaggio", "bmw motorrad"]
# OJO: "concesionario" a secas NO va aqui: aparece tambien en los de motos y los marcaria todos como "ambos".
COCHE = ["coche", "automovil", "turismo", "vehiculo", "car dealer", "automocion"]


def norm(txt):
    return (txt or "").lower()


def e164(tel):
    """Normaliza un telefono espanol a +34XXXXXXXXX. Devuelve '' si no es movil valido."""
    if not tel:
        return ""
    d = re.sub(r"\D", "", str(tel))
    if d.startswith("0034"):
        d = d[4:]
    elif d.startswith("34") and len(d) > 9:
        d = d[2:]
    if len(d) != 9:
        return ""
    return "+34" + d


def es_movil(tel_e164):
    """Solo 6 y 7 aceptan WhatsApp de forma fiable en Espana."""
    return bool(tel_e164) and tel_e164[3] in "67"


def red(perfiles, dominio):
    for u in perfiles or []:
        if dominio in norm(u):
            return u
    return ""


def clasificar(p):
    blob = " ".join([norm(p.get("title")), norm(p.get("categoryName")),
                     " ".join(norm(c) for c in p.get("categories") or [])])
    hay_moto = any(k in blob for k in MOTO)
    hay_coche = any(k in blob for k in COCHE)
    if hay_moto and hay_coche:
        return "ambos"
    if hay_moto:
        return "motos"
    return "coches"


def vende_online(p):
    blob = " ".join([
        norm(p.get("website")),
        norm(p.get("description")),
        " ".join(norm(x) for x in (p.get("additionalInfo") or {}).get("Service options", []) if isinstance(x, str)),
        " ".join(norm(u) for u in (p.get("contactDetails") or {}).get("links", []) or []),
        norm(json_str(p.get("contactDetails"))),
    ])
    return "TRUE" if any(s in blob for s in SENALES_ONLINE) else "FALSE"


def json_str(o):
    try:
        return json.dumps(o, ensure_ascii=False)
    except Exception:
        return ""


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("dataset")
    ap.add_argument("-o", "--out", default="concesionarias.csv")
    ap.add_argument("--min", type=int, default=200, help="minimo de filas esperado")
    args = ap.parse_args()

    with open(args.dataset, encoding="utf-8") as f:
        datos = json.load(f)

    vistos, filas = set(), []
    motivos = Counter()

    for p in datos:
        nombre = (p.get("title") or "").strip()
        web = (p.get("website") or "").strip()
        if not nombre:
            motivos["sin nombre"] += 1
            continue
        if not web:
            motivos["sin web"] += 1
            continue

        contacto = p.get("contactDetails") or {}
        emails = p.get("emails") or contacto.get("emails") or []
        perfiles = (p.get("socialProfiles") or contacto.get("links") or [])
        if isinstance(perfiles, dict):
            perfiles = list(perfiles.values())

        tel = e164(p.get("phone") or p.get("phoneUnformatted"))
        wa = tel if es_movil(tel) else ""
        ig = red(perfiles, "instagram.com")
        fb = red(perfiles, "facebook.com")
        li = red(perfiles, "linkedin.com")
        tk = red(perfiles, "tiktok.com")
        yt = red(perfiles, "youtube.com")
        email = emails[0] if emails else ""

        if not (email or wa or ig or fb):
            motivos["web pero sin email/whatsapp/redes"] += 1
            continue

        clave = (norm(nombre), web.rstrip("/").lower())
        if clave in vistos:
            motivos["duplicado"] += 1
            continue
        vistos.add(clave)

        filas.append({
            "contactado": "FALSE",
            "nombre": nombre,
            "tipo": clasificar(p),
            "vende_online": vende_online(p),
            "categoria": p.get("categoryName") or "",
            "direccion": p.get("address") or "",
            "poblacion": p.get("city") or "",
            "codigo_postal": p.get("postalCode") or "",
            "provincia": p.get("state") or p.get("countyCode") or "",
            "telefono": tel,
            "whatsapp": wa,
            "whatsapp_origen": "maps-movil" if wa else "",
            "web": web,
            "instagram": ig, "facebook": fb, "linkedin": li, "tiktok": tk, "youtube": yt,
            "email": email,
            "rating": p.get("totalScore") or "",
            "num_resenas": p.get("reviewsCount") or "",
            "es_cadena": "TRUE" if any(c in norm(nombre) for c in CADENAS) else "FALSE",
            "google_maps": p.get("url") or "",
            "zona_busqueda": p.get("searchString") or p.get("searchPageUrl") or "",
            "estado_crm": "", "aviso": "", "chip": "", "fecha_envio": "", "variante": "",
        })

    with open(args.out, "w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=COLUMNAS)
        w.writeheader()
        w.writerows(filas)

    print(f"Entrada: {len(datos)} sitios")
    for m, n in motivos.most_common():
        print(f"  descartados por {m}: {n}")
    print(f"Salida: {len(filas)} concesionarios contactables -> {args.out}")
    con_online = sum(1 for r in filas if r["vende_online"] == "TRUE")
    print(f"  con senales de venta online: {con_online}")
    print(f"  con email: {sum(1 for r in filas if r['email'])} | "
          f"con whatsapp: {sum(1 for r in filas if r['whatsapp'])} | "
          f"con instagram: {sum(1 for r in filas if r['instagram'])}")
    if len(filas) < args.min:
        print(f"\nAVISO: por debajo del minimo de {args.min}. Amplia provincias o terminos "
              f"en apify_input.json y vuelve a lanzar.", file=sys.stderr)
        sys.exit(1)


if __name__ == "__main__":
    main()
