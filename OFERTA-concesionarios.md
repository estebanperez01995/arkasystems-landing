# Oferta Arka Systems — Variante para concesionarios de coches y motos (España)

> **Para el agente que lee esto:** este documento es la fuente de verdad de la variante
> "concesionarios". Es la adaptación directa de `OFERTA-tiendas-de-ropa.md` al sector de la
> automoción (coches y motos, oficial y multimarca, venta y taller).
> El repo ya tiene la variante de clínicas dentales implementada en `index-dental.html`.
> Tu trabajo es **añadir** la variante de concesionarios **sin tocar** la dental, la de ropa ni la
> genérica. Todo el copy está listo para pegar. No lo reescribas "mejorándolo": está calibrado con
> el método de venta del negocio (ver sección 9).

---

## 0. Qué cambia respecto a la variante de tiendas de ropa

Se conserva intacto el esqueleto: tres niveles acumulativos, dos capas de precio, tabla de
traducción feature → resultado, cuenta de ROI con los números del cliente, prohibición de inventar
casos, y el mismo tono. Lo que cambia es la física del negocio:

| | Tienda de ropa | Concesionario |
|---|---|---|
| Ticket medio | 40–60 € | 12.000–30.000 € (coche) · 4.000–9.000 € (moto) |
| Qué se pierde | Una venta pequeña | **Una venta de 1.500–3.000 € de margen** |
| De dónde entra la demanda | Instagram y WhatsApp | **Portales** (coches.net, Milanuncios, AutoScout24, Wallapop, Motos.net), formularios web, WhatsApp, llamadas |
| Ciclo de compra | Minutos u horas | **30–90 días**, con varias visitas y comparación entre concesionarios |
| Qué decide la venta | Tener la talla | **Ser el primero en contestar**, con el coche y el precio en la mano |
| Segunda pata de negocio | Recurrencia de temporada | **Taller y postventa**: revisión, ITV, garantía, neumáticos, renovación |
| Sistema interno que ya tienen | Ninguno o un Excel | **DMS y CRM de marca** (a veces impuesto por el fabricante) |

Las dos consecuencias que hay que tener presentes al escribir: aquí **el número grande es enorme**
(una sola venta perdida al mes son miles de euros), y **el sistema nunca sustituye al comercial ni
al CRM de marca**: cualifica, agenda y avisa. Cerrar lo sigue cerrando una persona.

---

## 1. Estado del repo y lo que hay que crear

```
arkasystems-landing/
├── index.html                    ← landing genérica (todos los sectores)
├── index-dental.html             ← variante clínicas dentales  ← MOLDE A COPIAR
├── OFERTA-tiendas-de-ropa.md     ← brief de la variante ropa
├── OFERTA-concesionarios.md      ← este documento
├── aviso-legal.html · privacidad.html
├── sitemap.xml · robots.txt · og.png · apple-touch-icon.png
├── assets/                       ← logos, founders/, voraldent-logo.jpg
├── videos/                       ← hero-1..3.mp4 (+posters), caso-voraldent.mp4
├── ARKA-base-conocimiento.md     ← knowledge base del agente de voz Arky
└── AGENTE-ARKY-elevenlabs.md
```

Sin build, sin frameworks. HTML + CSS + JS vanilla, todo inline en cada página.

| Archivo | Acción |
|---|---|
| `index-concesionarios.html` | **Crear.** Clon de `index-dental.html` con el contenido de este documento. |
| `sitemap.xml` | Añadir la URL nueva (y la dental y la de ropa, que siguen sin listarse). |
| `ARKA-base-conocimiento.md` | Añadir el bloque del sector automoción (sección 10). |

---

## 2. La decisión de precios (leer antes de tocar la sección de planes)

Hay **dos capas de precio** y no son la misma cosa. No las mezcles.

**Capa pública (la landing):** se muestra la **mensualidad** y la implementación queda como
"implementación única a medida", exactamente igual que en `index-dental.html` y en la variante ropa.

**Capa de la llamada de venta (NO va en la web):** el pago único, con estructura 50/50.

**Por qué el pago único no se publica:** el método depende de decir el número grande (lo que el
concesionario pierde al mes en ventas no atendidas) **antes** del número chico (la inversión), y eso
solo funciona en la llamada, después de la demo.

### Los números — DECIDIDOS, no se tocan

**Son los mismos que en tiendas de ropa. Ese es el arma, no un descuido.**

| Nivel | Mensualidad (web) | Pago único (solo llamada) |
|---|---|---|
| 01 — Comercial 24/7 | **200 €/mes** | 1.000 € |
| 02 — Cartera | **300 €/mes** | 1.500 € |
| 03 — Sistema Pro | **400 €/mes** | 2.000 € |

**Escalera de entrada (solo llamada, nunca en la web):** 500 € → 700 € → 850 € → 1.000 €, igual que
en ropa. **La mensualidad no baja nunca**: es el piso del negocio.

**Por qué este sector con este precio.** El mismo importe que en una tienda de ropa, puesto delante
de un negocio cuyo margen por unidad es de 1.500–3.000 €, deja de ser una inversión y pasa a ser una
obviedad. Las cuentas exactas, para decirlas sin exagerar ni quedarse corto:

| | Nivel 01 | Nivel 02 | Nivel 03 |
|---|---|---|---|
| Implementación | 1.000 € | 1.500 € | 2.000 € |
| Año 1 completo (implementación + 11 meses, el primero va gratis) | 3.200 € | 4.800 € | 6.400 € |
| Ventas recuperadas que hacen falta al año (margen 1.800 €) | **2** | **3** | **4** |

Dicho con precisión, que es como aguanta una objeción: **la primera venta que recupere el sistema
paga la implementación entera** — 1.800 € de margen contra 1.500 € de implementación — y deja de
sobra para los primeros meses de mantenimiento. El año completo se cubre con dos o tres ventas. En
un concesionario que hace decenas de operaciones al mes, eso no es una apuesta: es aritmética.

No hace falta inflarlo. Redondear "una venta al año" a "una venta y ya está todo pagado para
siempre" es justo el tipo de frase que un gerente desmonta en diez segundos y te tira la llamada.

**Las dos frases exactas para la llamada** (la segunda solo después de haber dicho el número grande):

> Con que el sistema te recupere **una sola venta**, ya está pagado.

> Tu margen por coche es de unos X €. El sistema completo son 1.500 € y 300 € al mes. Recupera una
> venta al año y sales ganando; nosotros esperamos que te recupere una al mes.

**Si te dicen que es barato** — pasa en este sector, no en ropa —: no subas el precio en la llamada.
La respuesta es que el precio es bajo porque el sistema es el mismo que ya está funcionando en otros
negocios, no porque sea menos sistema; y que los cupos son dos implementaciones al mes. El precio
bajo con cupo limitado se lee como oportunidad. El precio bajo sin cupo se lee como barato.

---

## 3. La oferta: los 3 niveles

Cada nivel **incluye todo el anterior**. Son un menú interno: en la llamada se recomienda UNO.
En la landing se muestran los tres, con el 02 marcado como recomendado.

### Nivel 1 — Comercial 24/7
**Mensualidad: 200 €/mes · Pago único (solo llamada): 1.000 €**

Atiende en menos de un minuto todo lo que entra: leads de los portales, formularios de la web,
WhatsApp y los mensajes de redes. Responde con el stock real — modelo, año, kilómetros, precio,
cuota estimada, si está disponible —, cualifica al comprador (forma de pago, si entrega coche a
cambio, cuándo lo necesita), agenda la prueba de conducción o la visita en la agenda del comercial,
y le pasa la ficha ya hecha. Entiende fotos y audios: si mandan la captura de un anuncio o la foto
de su coche, lo entiende igual.

*Resultado que vende:* el lead que entra a las once de la noche de un domingo se contesta a las once
de la noche de un domingo, no el lunes a las diez cuando ya ha pedido precio en otros tres sitios.

### Nivel 2 — Cartera (= Nivel 1 + esto)
**Mensualidad: 300 €/mes · Pago único (solo llamada): 1.500 €**

Seguimiento automático del comprador que preguntó y no compró, durante las semanas que dura de
verdad la decisión: cuando baja de precio el modelo que miró, cuando entra uno igual con menos
kilómetros, cuando cambia la campaña de financiación. Tasación de su coche actual para arrancar la
conversación. Base de compradores ordenada (qué miró, qué presupuesto, qué coche tiene ahora) y
difusiones por la API oficial de WhatsApp: km 0, campañas de marca, liquidación de stock.

*Resultado que vende:* dejar de perder al que dijo "me lo tengo que pensar", que es la mitad de los
que entran por la puerta.

### Nivel 3 — Sistema Pro (= Nivel 2 + esto)
**Mensualidad: 400 €/mes · Pago único (solo llamada): 2.000 €**

Taller y postventa trabajando solos: avisos de revisión, de ITV, de fin de garantía y de cambio de
neumáticos, con la cita agendada directamente en la agenda del taller. Stock en tiempo real
conectado a la web o al DMS. Panel en vivo: leads atendidos, tiempo real de primera respuesta,
pruebas de conducción agendadas, citas de taller, y a qué modelo y a qué portal corresponde cada
venta.

*Resultado que vende:* llenar el taller sin llamar uno por uno, y saber qué portal trae ventas y
cuál solo trae ruido.

---

## 4. El resultado que se vende (la línea que abre todo)

> Contestamos en menos de un minuto todos los leads que entran en tu concesionario — de los
> portales, de la web y de WhatsApp, también de noche y en fin de semana —, te los dejamos
> cualificados y con la prueba de conducción agendada. Tus comerciales solo cierran.

### Tabla de traducción obligatoria: feature → resultado

Al gerente no le importa la feature. Le importa el resultado. **Todo el copy de la landing usa la
columna derecha.**

| Nunca escribas esto | Escribe esto |
|---|---|
| Responde 24/7 | El lead que entra el domingo por la noche se contesta el domingo por la noche, no el lunes cuando ya está pidiendo precio en otros tres concesionarios |
| Integración con portales | Todo lo que entra de coches.net, Milanuncios, AutoScout24 o Wallapop se contesta igual de rápido que si llamaran por teléfono |
| Cualificación automática de leads | Tu comercial deja de perder la mañana con quien mira por mirar y llama al que tiene el dinero y la fecha |
| Agendado en calendario | La prueba de conducción queda puesta en la agenda sin que nadie cruce tres mensajes |
| Entiende imágenes y audios | Te mandan la captura de un anuncio o la foto de su coche y el sistema lo entiende y sigue la conversación |
| Seguimientos automáticos | Los "me lo tengo que pensar" vuelven solos cuando baja el precio o entra uno igual con menos kilómetros |
| Módulo de tasación | Empiezas la conversación por lo que a él le importa: cuánto le das por el suyo |
| CRM / base de datos | Sabes qué coche tiene cada cliente, cuándo se le acaba la garantía y cuándo le toca cambiar |
| Recordatorios de postventa | El taller se llena solo: revisión, ITV y garantía avisadas a tiempo |
| Stock conectado al DMS | Nunca más ofreces un coche que ya se vendió ni dices "déjame que lo mire y te digo" |
| Dashboard | Ves qué portal te trae ventas y cuál solo te trae ruido, y cuánto tardáis de verdad en contestar |
| IA, prompt, n8n, API, multimodal, agente, flujo, automatización | **No aparecen en la página.** Al gerente no le importa cómo está hecho |

**Regla léxica:** en toda la página se dice **inversión**, nunca "precio". Y se dice **comprador** o
**cliente**, nunca "usuario" ni "lead" en el copy visible (dentro, entre nosotros, sí).

---

## 5. Los 4 dolores del sector (base de la sección `#para-quien`)

1. **Leads que se enfrían.** Los portales y los formularios de la web entran a cualquier hora y se
   contestan cuando hay un comercial libre. El comprador ha pedido precio en tres sitios a la vez:
   se lo lleva el que contesta primero, no el que tiene mejor coche.
2. **Fuera de horario y fin de semana.** La gente mira coches por la noche, los sábados por la tarde
   y los domingos, justo cuando el concesionario está cerrado.
3. **El que no compra hoy.** La decisión tarda semanas. Sin seguimiento, el 90 % de los que
   preguntaron desaparecen y acaban comprando en otro sitio.
4. **La postventa dormida.** Clientes que no vuelven a la revisión, garantías que se acaban sin que
   nadie avise, ITV que caducan, coches de hace cuatro años listos para renovar. Nadie está avisando
   porque nadie tiene tiempo de llamar uno por uno.

---

## 6. La cuenta de ROI (va en la landing y en la llamada)

Se hace con los números del cliente, **nunca inventados**. En la landing va como ejemplo
ilustrativo, etiquetado como tal.

**Parte 1 — leads que no se contestan a tiempo**

```
Leads al mes × % sin respuesta rápida o fuera de horario × % que acabaría comprando × Margen medio por unidad
Ejemplo: 150 × 30 % × 3 % ≈ 1,35 ventas × 1.800 € = ~2.400 €/mes que se dejan de ganar
```

**Parte 2 — el seguimiento que no se hace**

```
Compradores que preguntan y no cierran al mes × % recuperable con seguimiento × Margen medio
Ejemplo: 60 × 2 % ≈ 1,2 ventas × 1.800 € = ~2.100 €/mes
```

**Parte 3 — taller y postventa (solo si tienen taller)**

```
Clientes con revisión, ITV o garantía vencida al mes × % que vuelve si se le avisa × Ticket medio de taller
Ejemplo: 80 × 20 % × 280 € = ~4.480 €/mes
```

**Total del ejemplo: entre 4.500 y 9.000 €/mes sobre la mesa.** Con recuperar **una sola venta al
mes**, el sistema está pagado varias veces.

Reglas, iguales que en ropa: porcentajes siempre conservadores; si falta un dato se pregunta, no se
inventa; y toda cifra publicada va marcada como estimación. En la landing se publica **solo la
Parte 1** con la nota al pie; las tres partes completas son material de llamada.

---

## 7. Estructura de pago (llamada, no landing)

50 % para arrancar (flexible en el cómo, no en el cuánto) → entrega en **21 días desde que el
cliente entrega TODOS los datos** (acceso al stock o feed de la web, credenciales de los portales o
el correo donde caen los leads, política de financiación y tasación, horarios de sala y de taller,
agenda de comerciales) → lo prueba y da el OK → 50 % restante → **primer mes de mantenimiento
gratis** → desde el segundo, la mensualidad del nivel.

> Son 21 días y no 15 como en ropa: el stock y los portales llevan más trabajo de conexión que un
> catálogo de prendas.

**La mensualidad incluye:** mantenimiento, ajustes y corrección de errores, cambios en cómo habla el
sistema, actualización de stock y de campañas de financiación, alta de modelos y promociones nuevas,
y ajustes de horarios y agendas.

**No incluye:** rehacer la estructura, funcionalidades nuevas grandes (subir de nivel), sedes
adicionales, ni integraciones nuevas desde cero (otro DMS, otro portal, otra marca). Se cotizan
aparte.

**Plazos en la landing:** usa el estándar de la marca — **2–4 semanas** y garantía de 30 días. Los
21 días y el 50/50 son de la llamada.

---

## 8. Implementación: `index-concesionarios.html`

### Método

1. Copia `index-dental.html` → `index-concesionarios.html`.
2. **No toques el CSS.** Todo el sistema de diseño (tokens oklch, tipografías Geist e Instrument
   Serif, componentes) se hereda tal cual.
3. Mantén `<body data-accent="amber" data-serif="on" data-density="comfortable">` salvo que se pida
   otro acento. Valores válidos de `data-accent`: `amber`, `olive`, `terracotta`, `mono`.
4. Sustituye **solo el contenido de sector**, sección por sección, según el mapa de abajo.

### Cabeza del documento

- `<title>`: `Arka Systems · Sistemas de IA para concesionarios de coches y motos en España`
- `meta description`: habla de leads contestados en menos de un minuto y de ventas recuperadas, no
  de features.
- `link rel="canonical"` y todos los `og:url` → `https://www.arkasystems.es/index-concesionarios.html`
  (ajusta si el deploy usa una ruta limpia tipo `/concesionarios`).
- Bloque `window.ARKA_LINKS`: cambia el texto del WhatsApp. Debe decir concesionario:
  ```
  https://wa.me/34671286513?text=Hola%20Esteban%2C%20vengo%20de%20arkasystems.es%20y%20tengo%20un%20concesionario.
  ```
  El `calendly` y el `webhook` **no se tocan**.
- JSON-LD: mantén el `ProfessionalService`. **Elimina el `VideoObject` del caso Voraldent** si ese
  vídeo no se reutiliza en esta página.

### Mapa sección por sección

Los `id` de sección se conservan todos, para no romper anclas ni JS.

#### `.hero`

Estructura idéntica (eyebrow, H1 con `<span class="em">`, subtítulo, dos CTA, dos píldoras
`Sin permanencia` · `30 días o no pagas`).

H1:

> Contestamos tus **leads** en menos de un minuto, también a las once de la noche, y te los dejamos
> con la **prueba de conducción** agendada.

Subtítulo:

> Un sistema que atiende los portales, la web y el WhatsApp de tu concesionario con tu stock real,
> cualifica al comprador y lo pone en la agenda de tu comercial. Tus vendedores solo cierran.

#### `#para-quien` — tres resultados en 30 días

Tres `.icp-card` con el mismo formato (`num` + h3 + línea + 3 bullets). Contenido:

**01 / Más ventas — Dejas de perder el lead por llegar tarde**
- Primera respuesta en menos de 1 minuto, 24/7, también sábado por la tarde y domingo
- Leads de portales, web y WhatsApp atendidos por el mismo sitio
- El comprador llega al comercial ya cualificado y con la visita puesta

**02 / Más cierre — El que dijo "me lo pienso" vuelve**
- Seguimiento durante las semanas que dura de verdad la decisión
- Aviso automático cuando entra o baja de precio el coche que miró
- Tasación de su coche actual para reabrir la conversación

**03 / Taller lleno — La postventa deja de depender de que alguien llame**
- Revisión, ITV, fin de garantía y neumáticos avisados a tiempo
- Cita puesta directamente en la agenda del taller
- Tu cartera ordenada: qué coche tiene cada cliente y cuándo le toca cambiar

Nota al pie obligatoria:
*"Cifras estimadas según el diseño del sistema. Cada concesionario es distinto — en tu diagnóstico
calculamos rangos con tus números."*

#### `#caso` — **AQUÍ NO INVENTES NADA**

No hay ningún concesionario en producción todavía. **Prohibido fabricar un caso, un testimonio, un
logo o unas métricas de un concesionario que no existe.** Dos salidas válidas:

- **Opción A (recomendada):** sección *"Cómo se ve en un concesionario"* con una conversación de
  ejemplo (entra un lead de coches.net a las 23:40 preguntando por un Golf de 2021 → el sistema
  responde con kilómetros, precio y cuota estimada → pregunta forma de pago y si entrega coche →
  ofrece dos huecos para la prueba → agenda y avisa al comercial con la ficha). Etiquétala
  explícitamente como **demostración**.
- **Opción B:** conserva el caso Voraldent con su vídeo y su logo, bajo un titular honesto tipo
  *"Un sistema ya en producción, en otro sector"*.

#### `#como` — tres pasos

Se mantiene el molde (Diagnóstico 30 min gratis → Implementación 2–4 semanas → Validación 30 días).
Cambian los ejemplos: en el 01, "medimos cuánto tardáis de verdad en dar la primera respuesta y
cuántos leads se quedan sin contestar"; en el 02, "montamos el sistema sobre lo que ya usáis:
vuestros portales, vuestra web, vuestro WhatsApp y vuestro stock"; en el 03, "medimos tiempo de
primera respuesta, pruebas agendadas y ventas atribuidas".

#### `#servicios` — cuatro frentes, un solo sistema

1. **Atención de leads 24/7** — portales, formularios de la web, WhatsApp y redes, contestados en
   menos de un minuto con el stock real: modelo, año, kilómetros, precio y cuota estimada.
2. **Cualificación y agenda** — forma de pago, si entrega coche a cambio y plazo; prueba de
   conducción o visita puesta en la agenda del comercial, con la ficha hecha.
3. **Seguimiento y cartera** — recuperación del comprador que no cerró, tasación de su coche actual,
   y difusiones de campañas y km 0 por la API oficial de WhatsApp.
4. **Taller y panel en tiempo real** — revisión, ITV y garantía avisadas con cita automática, stock
   conectado a la web o al DMS, y panel con tiempo de respuesta, pruebas agendadas y ventas por
   portal.

#### `#paquetes` — los tres planes

Mismo componente que la dental: eyebrow "Inversión transparente", H2 "Tres formas de empezar.
**Riesgo cero**.", las dos notas laterales (garantía 30 días, capacidad limitada a 2
implementaciones al mes) y las tres tarjetas con `desde` + importe + `/mes` + "+ implementación
única a medida". El plan 02 lleva la cinta `★ Recomendado`.

| Tarjeta | Título | Blurb | Desde |
|---|---|---|---|
| 01 — Comercial 24/7 | Ningún lead sin contestar | Para concesionarios que reciben leads de portales y web y no llegan a contestarlos a tiempo. | **200 €/mes** |
| 02 — Cartera | El sistema completo | Atención, seguimiento y tu cartera de compradores trabajando. Para los que pierden ventas en el "me lo pienso". | **300 €/mes** |
| 03 — Sistema Pro | Venta, taller y stock en vivo | Para concesionarios con taller, varias marcas o más de una sede. | **400 €/mes** |

Bullets de cada tarjeta: los del nivel correspondiente en la sección 3, escritos en resultado. El 02
y el 03 empiezan con "Todo lo del plan anterior, más:". Cada tarjeta cierra con la línea de
garantía.

Pie: `IVA no incluido. Cupos limitados a 2 implementaciones/mes para garantizar calidad de entrega.`

#### `#contacto` y `#faq`

`#contacto` se mantiene (diagnóstico de 30 minutos, sin guion comercial), cambiando la pregunta de
entrada por "cuánto tardáis de verdad en contestar un lead de portal".

FAQ, seis preguntas:

1. **¿Cuánto tarda en estar funcionando?** Una primera automatización, 2 semanas. Sistema completo,
   3–4 semanas. Varias sedes o varias marcas, 6–8 semanas.
2. **¿Funciona con mi DMS y con el CRM de la marca?** Sí, y no los sustituye. El sistema funciona
   como capa externa: atiende, cualifica y vuelca la ficha donde ya trabajáis. No os obligamos a
   migrar nada ni a pelearos con el fabricante.
3. **¿Y los leads de los portales?** Entran igual que los de la web: da igual que lleguen por
   coches.net, Milanuncios, AutoScout24 o Wallapop. Todo se contesta por el mismo sitio y queda
   registrado.
4. **¿Esto no espanta al comprador, que quiere hablar con una persona?** Al revés. Lo repetitivo
   (si está disponible, kilómetros, precio, cuota, horarios) lo resuelve el sistema al instante. La
   prueba de conducción y el cierre los hace tu comercial, con el cliente ya caliente. El sistema
   nunca improvisa un precio, un descuento ni una condición de financiación: solo dice lo que tiene
   cargado, y lo que no sabe lo deriva a una persona al momento.
5. **¿Cómo gestionáis los datos de mis clientes (RGPD)?** Servidores europeos, RGPD por defecto,
   contrato de tratamiento de datos, sin compartir con terceros.
6. **¿Y si no funciona en mi concesionario?** Medimos el impacto 30 días tras el go-live: tiempo de
   primera respuesta, leads atendidos y pruebas agendadas. Si no hay impacto medible, no pagas la
   implementación. Y si antes de empezar vemos que no encaja, te lo decimos.

#### `#founder`

No se toca. Es contenido de marca, igual en todas las variantes. Respeta el atributo
`data-show-section="showFounder"`.

---

## 9. Tono e identidad (esto es lo que hay que respetar de verdad)

- **Español de España, de tú.** La landing habla a un gerente o a un jefe de ventas en España.
- **Cero jerga técnica.** Ni IA, ni API, ni prompt, ni n8n, ni flujo, ni automatización en el copy
  visible. El stack puede ir en una ficha técnica discreta, como en la dental.
- **Resultado antes que feature**, siempre.
- **"Inversión", nunca "precio".**
- **El sistema no vende coches: los comerciales venden coches.** Nunca escribas nada que suene a
  sustituir al equipo de ventas. Esa es la objeción número uno del sector y la página no debe
  alimentarla.
- **Sin humo.** Toda cifra va como estimación. Si un dato no se tiene, no se publica.
- **Nada de casos, testimonios, logos ni resultados inventados.** Regla no negociable.
- Frases cortas. Sin exclamaciones en el copy de la página. Sin emojis.

### Objeciones típicas del sector y cómo se responden (material de llamada)

| Objeción | Respuesta |
|---|---|
| "Ya tengo el CRM de la marca / el DMS" | No lo tocamos. El sistema atiende y cualifica, y deja la ficha dentro de lo que ya usáis. |
| "Mis comerciales ya contestan los leads" | ¿En cuánto? Medimos vuestro tiempo real de primera respuesta en el diagnóstico. Casi siempre sorprende. |
| "El cliente de coche quiere hablar con una persona" | Y va a hablar con una persona: con tu comercial, cuando ya tiene la visita puesta. Lo que resuelve el sistema es el "¿sigue disponible?" de las 23:40. |
| "Los leads de portales ya me entran en el CRM" | Entrar no es contestar. El problema no es que no lleguen, es cuánto tardan en tener respuesta. |
| "Tengo el volumen cubierto" | Entonces el dinero está en el taller y en la renovación de tu cartera, no en vender más. Nivel 3. |

---

## 10. Bloque para `ARKA-base-conocimiento.md`

Añadir al documento de la base de conocimiento del agente de voz, respetando su formato de secciones
en mayúsculas:

```markdown
## SECTOR CONCESIONARIOS DE COCHES Y MOTOS (ESPAÑA)
Qué implementamos: atención en menos de un minuto de los leads que entran por portales
(coches.net, Milanuncios, AutoScout24, Wallapop, Motos.net), formularios de la web, WhatsApp y
redes, con el stock real cargado (modelo, año, kilómetros, precio, cuota estimada); cualificación
del comprador (forma de pago, si entrega coche a cambio, plazo) y agendado de la prueba de
conducción en la agenda del comercial; seguimiento automático del comprador que no cerró; tasación
del coche usado; difusiones de campañas y km 0 por la API oficial; y avisos de revisión, ITV, fin de
garantía y neumáticos con cita automática de taller, con stock y panel conectados a la web o al DMS.
Dolores típicos: leads que se contestan tarde y se los lleva el concesionario que contesta primero;
consultas fuera de horario, sábado por la tarde y domingo; el "me lo tengo que pensar" que no vuelve
porque nadie le hace seguimiento; y la postventa dormida (revisiones, ITV y garantías que caducan
sin que nadie avise).
Resultado que se promete: ningún lead sin contestar y pruebas de conducción agendadas. NO dar cifras
de euros recuperados: dependen del margen por unidad y del volumen de cada concesionario. Si
preguntan por el retorno, redirigir al diagnóstico gratuito.
Qué NO hacemos: no sustituimos al comercial ni al CRM/DMS de la marca. El sistema atiende, cualifica
y agenda; el cierre lo hace siempre una persona. Nunca damos un precio, un descuento ni una
condición de financiación que no esté cargada.
Herramientas que solemos conectar: portales de anuncios, formularios web, WhatsApp, Instagram,
agenda de comerciales y de taller, y el DMS o el feed de stock de la web.
Casos en producción en este sector: NINGUNO todavía. No inventar ni insinuar uno. El caso real
disponible es Voraldent, clínica dental en Barcelona, y se puede mencionar como cliente en
producción de otro sector.
Precio: no se publican tarifas. Se cierra en el diagnóstico. Nunca dar una cifra.
```

---

## 11. Mensajes de captación en frío (no van en la web)

Para WhatsApp e Instagram DM. Requisito previo: la demo de **ese** concesionario ya montada, porque
el mensaje afirma que existe.

**Base:**

> Hola, muy buenas! Acabo de montar un clon con IA de vuestro concesionario: contesta los leads
> igual que vosotros, con vuestro stock, en menos de un minuto y a cualquier hora. Cualifica al
> comprador y deja la prueba de conducción agendada. Si quieres verlo, responde VER y te lo mando
> en menos de un minuto!

**Variante para el que vende mucho online / tiene stock publicado:** cambia el segundo punto por
"y hace seguimiento solo a los que piden precio y no vuelven".

**Variante moto:** "contesta los mensajes de Wallapop y Motos.net igual que vosotros" y usa
"responder de noche y los domingos, que es cuando se miran las motos".

**Seguimiento a 48 h:**

> Hola! Te escribí el otro día, te dejé montado el clon de tu concesionario. Sigue ahí guardado.
> Respondes VER y te lo mando, son 30 segundos de mirarlo.

**Cuando responde VER:** se manda el vídeo y se cierra pidiendo la llamada.

Reglas: palabra clave de una sílaba (VER); cero links en el primer mensaje; y la promesa de "menos
de un minuto" se cumple.

> **Ojo con el destinatario:** en un concesionario el número público suele ser el de recepción o el
> de un comercial, no el del gerente. El mensaje tiene que funcionar también cuando lo lee alguien
> que no decide: por eso habla de "vuestro concesionario" y pide ver una demo, no una reunión.

---

## 12. Checklist de aceptación

- [ ] `index-concesionarios.html` creado a partir de `index-dental.html`, con el CSS intacto.
- [ ] `index.html` e `index-dental.html` sin un solo cambio.
- [ ] Ni una palabra técnica (IA, API, prompt, n8n, flujo, automatización, agente) en el copy visible.
- [ ] "Inversión" en lugar de "precio" en toda la página.
- [ ] Ninguna frase que insinúe que el sistema sustituye a los comerciales.
- [ ] Los tres planes muestran mensualidad + "implementación única a medida". **El pago único
      (1.000/1.500/2.000 €) no aparece en ningún sitio de la web.**
- [ ] Ningún caso, testimonio, logo ni métrica de un concesionario inventado.
- [ ] Toda cifra de resultado etiquetada como estimación.
- [ ] `canonical`, `og:url` y `twitter:*` apuntan a la URL de la página nueva.
- [ ] El texto del WhatsApp de `ARKA_LINKS` dice concesionario. `calendly` y `webhook` intactos.
- [ ] `VideoObject` del JSON-LD eliminado si el vídeo del caso no está en la página.
- [ ] `sitemap.xml` con la URL nueva (y las que faltan).
- [ ] Responsive verificado a 400 px de ancho: sin scroll horizontal.
- [ ] Los dos CTA abren WhatsApp y el calendario correctamente.

## 13. Pendientes que necesitan material que no existe todavía

- Vídeo de demo con un concesionario (el equivalente a `videos/caso-voraldent.mp4`).
- Imagen OG propia de la variante (1200×630).
- Primer cliente del sector en producción, para convertir `#caso` en un caso real.
- Decidir la URL final de deploy: `index-concesionarios.html` o ruta limpia `/concesionarios`.
- Decidir si coches y motos comparten landing (este documento asume que sí, con el copy de coche
  como principal y la moto nombrada) o si la moto merece su propia variante más adelante.
