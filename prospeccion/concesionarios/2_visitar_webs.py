#!/usr/bin/env python3
"""Paso 2 — Entra en la web de cada concesionario y saca WhatsApp, email y redes.

    python3 2_visitar_webs.py maps.json -o concesionarias.csv

Se visita con navegador real, no con curl, porque el boton de WhatsApp de la
mayoria de las webs lo inyecta un widget por JavaScript y en el HTML crudo no
aparece. Ademas de la home se prueba /contacto, que es donde suele estar el
numero bueno.

Cachea cada web en webs_cache.json: si se corta, al relanzar no repite.
"""
import argparse, csv, json, os, pathlib, random, sys, time
import comun as c

RUTAS = ["", "/contacto", "/contacto/", "/contactar", "/contact", "/es/contacto", "/quienes-somos"]
CHROMIUM = os.environ.get("CHROMIUM_PATH", "/opt/pw-browsers/chromium")


def lanzar(pw):
    if os.path.exists(CHROMIUM):
        try:
            return pw.chromium.launch(executable_path=CHROMIUM, headless=True)
        except Exception:
            pass
    return pw.chromium.launch(headless=True)


def raspar_web(page, web):
    """Devuelve el HTML de home + contacto concatenado. '' si no responde."""
    base = web.rstrip("/")
    trozos = []
    for ruta in RUTAS:
        try:
            r = page.goto(base + ruta, timeout=25000, wait_until="domcontentloaded")
            if not r or r.status >= 400:
                continue
            page.wait_for_timeout(1800)  # que arranquen los widgets
            trozos.append(page.content())
            # los href de los anchors, por si el widget usa atributos raros
            trozos.append(" ".join(page.eval_on_selector_all(
                "a", "els => els.map(e => e.href || '')")))
            if ruta and any(rx.search(trozos[-2]) for rx in c.RE_WA):
                break  # ya tenemos whatsapp, no hace falta seguir probando rutas
        except Exception:
            continue
        if ruta == "" and len(trozos) >= 2 and any(rx.search(trozos[0]) for rx in c.RE_WA):
            continue  # la home ya lo tiene, pero miramos contacto por email/redes
    return "\n".join(trozos)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("maps_json")
    ap.add_argument("-o", "--out", default="concesionarias.csv")
    ap.add_argument("--cache", default="webs_cache.json")
    ap.add_argument("--min", type=int, default=200)
    args = ap.parse_args()

    fichas = {k: v for k, v in json.loads(
        pathlib.Path(args.maps_json).read_text(encoding="utf-8")).items()
        if not k.startswith("_")}
    cache_p = pathlib.Path(args.cache)
    cache = json.loads(cache_p.read_text(encoding="utf-8")) if cache_p.exists() else {}

    con_web = [f for f in fichas.values() if f.get("web")]
    pendientes = [f for f in con_web if f["web"] not in cache]
    print(f"{len(fichas)} fichas de Maps · {len(con_web)} con web · "
          f"{len(cache)} ya visitadas · {len(pendientes)} por visitar")

    # Si no queda nada que visitar no se abre el navegador: asi el volcado a CSV
    # se puede relanzar sin red.
    if pendientes:
        from playwright.sync_api import sync_playwright
        with sync_playwright() as pw:
            nav = lanzar(pw)
            ctx = nav.new_context(locale="es-ES", ignore_https_errors=True,
                                  user_agent=("Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) "
                                              "AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0 Safari/537.36"))
            ctx.set_default_timeout(25000)
            page = ctx.new_page()
            # nada de imagenes ni fuentes: la mitad de tiempo por web
            page.route("**/*.{png,jpg,jpeg,webp,gif,svg,woff,woff2,ttf,mp4}", lambda r: r.abort())

            for i, f in enumerate(pendientes, 1):
                web = f["web"]
                if web in cache:
                    continue
                try:
                    html = raspar_web(page, web)
                except Exception as e:
                    print(f"  [{i}] {web} -> error: {e}", file=sys.stderr)
                    html = ""
                wa, origen = c.whatsapp_de_html(html)
                emails = c.emails_de_html(html)
                cache[web] = {
                    "whatsapp": wa, "whatsapp_origen": origen,
                    "email": emails[0] if emails else "",
                    "redes": c.redes_de_html(html),
                    "vende_online": c.vende_online(html, web),
                }
                print(f"  [{i}/{len(pendientes)}] {web} -> "
                      f"WA:{wa or '-'} mail:{cache[web]['email'] or '-'} "
                      f"redes:{','.join(cache[web]['redes']) or '-'}")
                if i % 10 == 0:
                    cache_p.write_text(json.dumps(cache, ensure_ascii=False, indent=1), encoding="utf-8")
                time.sleep(random.uniform(0.4, 1.2))

            cache_p.write_text(json.dumps(cache, ensure_ascii=False, indent=1), encoding="utf-8")
            nav.close()

    filas, vistos = [], set()
    for f in fichas.values():
        nombre, web = f.get("nombre", "").strip(), (f.get("web") or "").strip()
        if not nombre:
            continue
        clave = (c.norm(nombre), web.rstrip("/").lower() or f.get("direccion", ""))
        if clave in vistos:
            continue
        vistos.add(clave)

        w = cache.get(web, {})
        redes = w.get("redes", {})
        tel = c.e164(f.get("telefono"))
        wa = w.get("whatsapp") or (tel if c.es_movil(tel) else "")
        origen = w.get("whatsapp_origen") or ("maps-movil" if wa and not w.get("whatsapp") else "")
        dir_ = f.get("direccion", "")
        cp = ""
        for t in dir_.replace(",", " ").split():
            if t.isdigit() and len(t) == 5:
                cp = t
                break

        filas.append({
            "contactado": "FALSE",
            "nombre": nombre,
            "tipo": c.clasificar(nombre, f.get("categoria", "")),
            "vende_online": w.get("vende_online", "FALSE"),
            "categoria": f.get("categoria", ""),
            "direccion": dir_,
            "poblacion": (f.get("zona_busqueda", "").split()[-1] if f.get("zona_busqueda") else ""),
            "codigo_postal": cp,
            "provincia": "",
            "telefono": tel,
            "whatsapp": wa,
            "whatsapp_origen": origen,
            "web": web,
            "instagram": redes.get("instagram", ""),
            "facebook": redes.get("facebook", ""),
            "linkedin": redes.get("linkedin", ""),
            "tiktok": redes.get("tiktok", ""),
            "youtube": redes.get("youtube", ""),
            "email": w.get("email", ""),
            "rating": f.get("rating", ""),
            "num_resenas": f.get("num_resenas", ""),
            "es_cadena": c.es_cadena(nombre),
            "google_maps": f.get("google_maps", ""),
            "zona_busqueda": f.get("zona_busqueda", ""),
            "estado_crm": "", "aviso": "", "chip": "", "fecha_envio": "", "variante": "",
        })

    # Los que tienen WhatsApp arriba: son los que interesan de verdad.
    filas.sort(key=lambda r: (r["whatsapp"] == "", r["email"] == "", r["nombre"]))

    with open(args.out, "w", newline="", encoding="utf-8") as fh:
        w = csv.DictWriter(fh, fieldnames=c.COLUMNAS)
        w.writeheader()
        w.writerows(filas)

    con_wa = sum(1 for r in filas if r["whatsapp"])
    print(f"\n{len(filas)} concesionarios -> {args.out}")
    print(f"  con WhatsApp: {con_wa}  (de web: {sum(1 for r in filas if r['whatsapp_origen'].startswith('web'))})")
    print(f"  con email: {sum(1 for r in filas if r['email'])}")
    print(f"  con alguna red: {sum(1 for r in filas if r['instagram'] or r['facebook'] or r['tiktok'])}")
    print(f"  con venta online: {sum(1 for r in filas if r['vende_online'] == 'TRUE')}")
    if len(filas) < args.min:
        print(f"\nAVISO: por debajo de {args.min}. Añade ciudades a ciudades.txt y relanza "
              f"el paso 1 (no repite lo ya hecho).", file=sys.stderr)


if __name__ == "__main__":
    main()
