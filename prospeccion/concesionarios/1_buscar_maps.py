#!/usr/bin/env python3
"""Paso 1 — Busca concesionarios en Google Maps y guarda ficha + web.

    python3 1_buscar_maps.py --ciudades ciudades.txt --out maps.json
    python3 1_buscar_maps.py --ciudades ciudades.txt --out maps.json --headful   # para depurar

Sin Apify y sin API de pago: conduce un Chromium real con Playwright.
Guarda despues de cada busqueda, asi que se puede cortar y reanudar: lo ya
scrapeado no se repite.
"""
import argparse, json, os, pathlib, random, re, sys, time

TERMINOS = [
    "concesionario de coches",
    "concesionario oficial",
    "venta de coches de ocasion",
    "concesionario de motos",
]
CHROMIUM = os.environ.get("CHROMIUM_PATH", "/opt/pw-browsers/chromium")


def lanzar(pw, headful):
    args = {"headless": not headful, "args": ["--disable-blink-features=AutomationControlled"]}
    if os.path.exists(CHROMIUM):
        try:
            return pw.chromium.launch(executable_path=CHROMIUM, **args)
        except Exception:
            pass
    return pw.chromium.launch(**args)


def aceptar_consentimiento(page):
    """El muro de cookies de Google, que cambia de idioma y de forma."""
    for sel in ['button:has-text("Aceptar todo")', 'button:has-text("Accept all")',
                'form[action*="consent"] button', '[aria-label*="Aceptar todo"]']:
        try:
            b = page.locator(sel).first
            if b.is_visible(timeout=1500):
                b.click()
                page.wait_for_timeout(1500)
                return
        except Exception:
            continue


def scroll_resultados(page, max_fichas):
    """Baja por el panel de resultados hasta que deja de crecer o se acaba."""
    panel = None
    for sel in ['div[role="feed"]', 'div[aria-label^="Resultados"]', 'div.m6QErb[aria-label]']:
        try:
            p = page.locator(sel).first
            if p.count():
                panel = p
                break
        except Exception:
            continue
    if panel is None:
        return
    previo, quieto = 0, 0
    while quieto < 3:
        try:
            panel.evaluate("el => el.scrollBy(0, el.scrollHeight)")
        except Exception:
            break
        page.wait_for_timeout(random.randint(1200, 2200))
        n = page.locator('a[href*="/maps/place/"]').count()
        if n >= max_fichas or "final de la lista" in page.content():
            break
        quieto = quieto + 1 if n == previo else 0
        previo = n


def txt(page, selectores, attr=None):
    for sel in selectores:
        try:
            el = page.locator(sel).first
            if el.count():
                v = el.get_attribute(attr) if attr else el.inner_text()
                if v and v.strip():
                    return v.strip()
        except Exception:
            continue
    return ""


def ficha(page, url, zona):
    page.goto(url, timeout=60000, wait_until="domcontentloaded")
    page.wait_for_timeout(random.randint(1800, 3000))
    nombre = txt(page, ["h1.DUwDvf", "h1"])
    if not nombre:
        return None
    direccion = txt(page, ['button[data-item-id="address"]', '[data-tooltip="Copiar dirección"]'])
    web = txt(page, ['a[data-item-id="authority"]', 'a[aria-label^="Sitio web"]'], attr="href")
    tel = txt(page, ['button[data-item-id^="phone:tel:"]', '[data-tooltip="Copiar número de teléfono"]'])
    if not tel:
        tel = txt(page, ['button[data-item-id^="phone:tel:"]'], attr="data-item-id").replace("phone:tel:", "")
    rating = txt(page, ['div.F7nice span[aria-hidden="true"]', 'span.ceNzKf'], attr=None)
    resenas = txt(page, ['div.F7nice span[aria-label*="reseña"]', 'button[aria-label*="reseña"]'])
    categoria = txt(page, ['button[jsaction*="category"]', 'button.DkEaL'])
    m = re.search(r"([\d.]+)", (resenas or "").replace(",", "."))
    return {
        "nombre": nombre,
        "categoria": categoria,
        "direccion": direccion,
        "telefono": tel,
        "web": web,
        "rating": (rating or "").replace(",", "."),
        "num_resenas": m.group(1).replace(".", "") if m else "",
        "google_maps": page.url,
        "zona_busqueda": zona,
    }


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--ciudades", default="ciudades.txt")
    ap.add_argument("--out", default="maps.json")
    ap.add_argument("--por-busqueda", type=int, default=40, help="fichas maximas por termino y ciudad")
    ap.add_argument("--headful", action="store_true")
    args = ap.parse_args()

    from playwright.sync_api import sync_playwright

    ciudades = [l.strip() for l in open(args.ciudades, encoding="utf-8")
                if l.strip() and not l.startswith("#")]
    salida = pathlib.Path(args.out)
    datos = json.loads(salida.read_text(encoding="utf-8")) if salida.exists() else {}
    hechas = {d.get("_busqueda") for d in datos.values()}
    print(f"{len(datos)} fichas ya guardadas de ejecuciones anteriores")

    with sync_playwright() as pw:
        navegador = lanzar(pw, args.headful)
        ctx = navegador.new_context(
            locale="es-ES", timezone_id="Europe/Madrid",
            viewport={"width": 1400, "height": 950},
            user_agent=("Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 "
                        "(KHTML, like Gecko) Chrome/124.0 Safari/537.36"))
        page = ctx.new_page()

        for ciudad in ciudades:
            for termino in TERMINOS:
                zona = f"{termino} {ciudad}"
                if zona in hechas:
                    print(f"  (ya hecha) {zona}")
                    continue
                print(f"\n>> {zona}")
                try:
                    page.goto("https://www.google.com/maps/search/" +
                              zona.replace(" ", "+") + "?hl=es", timeout=60000)
                    aceptar_consentimiento(page)
                    page.wait_for_timeout(2500)
                    scroll_resultados(page, args.por_busqueda)
                    enlaces = page.eval_on_selector_all(
                        'a[href*="/maps/place/"]', "els => [...new Set(els.map(e => e.href))]")
                except Exception as e:
                    print(f"   ERROR en la busqueda: {e}", file=sys.stderr)
                    continue
                print(f"   {len(enlaces)} fichas encontradas")

                for url in enlaces[:args.por_busqueda]:
                    clave = url.split("/place/")[-1].split("/data")[0]
                    if clave in datos:
                        continue
                    try:
                        f = ficha(page, url, zona)
                    except Exception as e:
                        print(f"   ficha fallida: {e}", file=sys.stderr)
                        continue
                    if not f:
                        continue
                    f["_busqueda"] = zona
                    datos[clave] = f
                    print(f"   + {f['nombre']} | {f['telefono'] or 's/tel'} | {f['web'] or 's/web'}")
                    time.sleep(random.uniform(0.8, 2.0))

                salida.write_text(json.dumps(datos, ensure_ascii=False, indent=1), encoding="utf-8")
                hechas.add(zona)
                print(f"   guardado: {len([k for k in datos if not k.startswith('_')])} fichas totales")

        navegador.close()
    print(f"\nListo -> {salida}")


if __name__ == "__main__":
    main()
