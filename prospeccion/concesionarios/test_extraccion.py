#!/usr/bin/env python3
"""Pruebas de la extraccion contra HTML de ejemplo. Se ejecuta sin red:
    python3 test_extraccion.py
"""
import comun as c

CASOS = [
    ("enlace wa.me clasico",
     '<a href="https://wa.me/34611223344" class="wsp">Escríbenos</a>',
     ("+34611223344", "web-enlace")),
    ("api.whatsapp con %2B",
     '<a href="https://api.whatsapp.com/send?phone=%2B34622334455&text=Hola">WhatsApp</a>',
     ("+34622334455", "web-enlace")),
    ("widget inyectado por JS",
     '<div data-url="whatsapp://send?phone=34733445566&amp;text=Hola"></div>',
     ("+34733445566", "web-enlace")),
    ("solo texto: WhatsApp 611 22 33 44",
     '<p>Llámanos o escríbenos por WhatsApp: 611 22 33 44</p>',
     ("+34611223344", "web-texto")),
    ("fijo en wa.me se descarta como movil pero se captura",
     '<a href="https://wa.me/34932170070">chat</a>',
     ("+34932170070", "web-enlace")),
    ("sin whatsapp",
     '<a href="tel:+34932170070">Llamar</a>',
     ("", "")),
]

fallos = 0
for nombre, html, esperado in CASOS:
    got = c.whatsapp_de_html(html)
    ok = got == esperado
    fallos += not ok
    print(f"[{'OK ' if ok else 'FALLO'}] {nombre}: {got}")

HTML = """
<html><body>
<a href="mailto:info@concesionariolopez.es">Escríbenos</a>
<span>ventas@concesionariolopez.es</span>
<img src="logo@2x.png"><script>Sentry.init({dsn:'x@sentry.io/1'})</script>
<a href="https://www.instagram.com/concelopez/">IG</a>
<a href="https://www.facebook.com/sharer/sharer.php?u=x">compartir</a>
<a href="https://es-es.facebook.com/concelopez">FB</a>
<a href="https://www.tiktok.com/@concelopez">TT</a>
<a href="/nuestro-stock">Reserva online tu coche</a>
</body></html>
"""
pruebas = [
    ("emails, genericos primero", c.emails_de_html(HTML)[:2],
     ["info@concesionariolopez.es", "ventas@concesionariolopez.es"]),
    ("instagram", c.redes_de_html(HTML).get("instagram"), "https://www.instagram.com/concelopez"),
    ("facebook sin sharer", c.redes_de_html(HTML).get("facebook"), "https://es-es.facebook.com/concelopez"),
    ("tiktok", c.redes_de_html(HTML).get("tiktok"), "https://www.tiktok.com/@concelopez"),
    ("vende online", c.vende_online(HTML, ""), "TRUE"),
    ("tipo motos", c.clasificar("Motos Sevilla Sur", "Concesionario de motos"), "motos"),
    ("tipo coches", c.clasificar("Auto Vallès", "Concesionario de coches"), "coches"),
    ("tipo ambos", c.clasificar("Auto y Moto Pérez", "Concesionario de coches y motos"), "ambos"),
    ("movil si", c.es_movil("+34611223344"), True),
    ("fijo no", c.es_movil("+34932170070"), False),
    ("e164 desde 0034", c.e164("0034 611 22 33 44"), "+34611223344"),
]
for nombre, got, esperado in pruebas:
    ok = got == esperado
    fallos += not ok
    print(f"[{'OK ' if ok else 'FALLO'}] {nombre}: {got!r}")

print("\nTODO OK" if not fallos else f"\n{fallos} FALLOS")
raise SystemExit(1 if fallos else 0)
