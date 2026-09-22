# Oferta Arka Systems — Variante para tiendas de ropa (España)

> **Para el agente que lee esto:** este documento es la fuente de verdad de la variante "tiendas de ropa".
> El repo ya tiene la variante de clínicas dentales implementada en `index-dental.html`.
> Tu trabajo es **añadir** la variante de ropa **sin tocar** la dental ni la genérica.
> Todo el copy de este documento está listo para pegar. No lo reescribas "mejorándolo": está calibrado
> con el método de venta que usa el negocio (ver sección 9).

---

## 1. Estado actual del repo

```
arkasystems-landing/
├── index.html              ← landing genérica (todos los sectores)
├── index-dental.html       ← variante clínicas dentales  ← MOLDE A COPIAR
├── aviso-legal.html
├── privacidad.html
├── sitemap.xml · robots.txt · og.png · apple-touch-icon.png
├── assets/                 ← logos, founders/, voraldent-logo.jpg
├── videos/                 ← hero-1..3.mp4 (+posters), caso-voraldent.mp4
├── ARKA-base-conocimiento.md      ← knowledge base del agente de voz Arky
└── AGENTE-ARKY-elevenlabs.md
```

Sin build, sin frameworks. HTML + CSS + JS vanilla, todo inline en cada página.

### Lo que hay que crear

| Archivo | Acción |
|---|---|
| `index-ropa.html` | **Crear.** Clon de `index-dental.html` con el contenido de este documento. |
| `sitemap.xml` | Añadir la URL nueva. `index-dental.html` tampoco está listada: añadir las dos. |
| `ARKA-base-conocimiento.md` | Añadir el bloque del sector ropa (ver sección 10). |

---

## 2. La decisión de precios (leer antes de tocar la sección de planes)

Hay **dos capas de precio** y no son la misma cosa. No las mezcles.

**Capa pública (la landing):** se muestra la **mensualidad** y la implementación queda como
"implementación única a medida", exactamente igual que en `index-dental.html`.

**Capa de la llamada de venta (NO va en la web):** el pago único es 1.000 € / 1.500 € / 2.000 €
según el nivel, con estructura 50/50.

**Por qué el pago único no se publica:** el método de venta depende de decir el número grande
(lo que la tienda pierde al mes) **antes** del número chico (la inversión), y eso solo funciona en
la llamada, después de la demo. Si el pago único está en la web, el cliente llega con el número
en la cabeza y la secuencia se rompe. Es una decisión comercial, no un olvido: **no añadas el
pago único a la landing** aunque lo veas en este documento.

---

## 3. La oferta: los 3 niveles

Cada nivel **incluye todo el anterior**. Son un menú interno: en la llamada se recomienda UNO.
En la landing se muestran los tres, como en la dental, con el 02 marcado como recomendado.

### Nivel 1 — Vendedor 24/7
**Mensualidad: 200 €/mes · Pago único (solo llamada): 1.000 €**

WhatsApp e Instagram atendidos las 24 horas con el catálogo cargado: prendas, tallas, colores,
precios, envíos y cambios. Entiende fotos y audios. Hace seguimiento automático a quien no compra.
Si hay tienda online, recupera carritos. Cuando alguien quiere reservar o comprar, avisa a la dueña
y cierra ella.

*Resultado que vende:* no se escapa ninguna venta por no llegar a contestar, y los "me lo pienso"
vuelven solos.

### Nivel 2 — Clientela (= Nivel 1 + esto)
**Mensualidad: 300 €/mes · Pago único (solo llamada): 1.500 €**

Base de clientas ordenada (quién compró qué, qué talla, cuándo) y difusiones por la API oficial de
WhatsApp: colección nueva, rebajas, "volvió tu talla".

*Resultado que vende:* vender a quien ya compró, sin pagar publicidad. Una difusión y se vende en
un día lo de una semana.

### Nivel 3 — Sistema Pro (= Nivel 2 + esto)
**Mensualidad: 400 €/mes · Pago único (solo llamada): 2.000 €**

Stock en tiempo real conectado a la tienda online o al TPV, y panel en vivo: ventas recuperadas,
consultas atendidas, prendas más preguntadas, tallas que piden y no hay.

*Resultado que vende:* ver cuánta plata genera el sistema y qué comprar la próxima temporada, sin
adivinar.

### Escalera de entrada (solo llamada, nunca en la web)

Sin testimonios del sector todavía, el pago único arranca abajo y sube con cada cliente:
500 € → 700 € → 850 € → 1.000 €. **La mensualidad no baja nunca**: es el piso del negocio.

---

## 4. El resultado que se vende (la línea que abre todo)

> Recuperás las ventas que hoy se te escapan por Instagram y WhatsApp — las consultas que nadie
> contesta, los "me lo pienso" que no vuelven y los carritos que se quedan a mitad — sin sumar una
> persona ni estar pegado al móvil.

### Tabla de traducción obligatoria: feature → resultado

Al dueño de tienda no le importa la feature. Le importa el resultado de la feature. **Todo el copy
de la landing usa la columna derecha.**

| Nunca escribas esto | Escribe esto |
|---|---|
| Responde 24/7 | No se te escapa una venta por no contestar a tiempo: el domingo por la noche, en pleno cambio de temporada, cuando estás atendiendo en tienda |
| Entiende imágenes y audios | Te mandan una captura de Instagram o un audio preguntando si hay la 40, y el sistema entiende y vende igual |
| Seguimientos automáticos | Las que dijeron "me lo pienso" vuelven a comprar sin que las persigas |
| Recuperación de carritos | La venta del carrito que se queda a medias, vuelve |
| Derivación con pausa | El sistema atiende y filtra; cuando alguien quiere reservar, te avisa y cierras tú |
| Catálogo y stock conectados | Nunca más vendes una talla que no tienes ni dices "déjame mirar y te digo" |
| CRM | Todas tus clientas ordenadas: quién compró qué, qué talla usa, a quién avisar cuando entra lo nuevo |
| Difusiones / API oficial | Avisas a toda tu base de que llegó la colección nueva y vendes en un día lo de una semana |
| Dashboard | Ves cuántas ventas te generó el sistema este mes, sin adivinar |
| IA, prompt, n8n, API, multimodal, agente, flujo, automatización | **No aparecen en la página.** Al dueño no le importa cómo está hecho |

**Regla léxica:** en toda la página se dice **inversión**, nunca "precio". Precio es un gasto que
duele; inversión es plata que vuelve.

---

## 5. Los 4 dolores del sector (base de la sección `#para-quien`)

1. Mensajes de Instagram y WhatsApp sin contestar o contestados tarde, sobre todo fuera de horario,
   los domingos y mientras se atiende en tienda.
2. Las que preguntan talla, precio o stock y desaparecen: los "me lo pienso" que nunca vuelven.
3. Carritos abandonados en la tienda online, o ventas perdidas por contestar "déjame ver si queda"
   y no volver.
4. Cero base de clientas: no saben a quién avisar cuando entra la colección nueva o empiezan las
   rebajas. Publican y rezan.

---

## 6. La cuenta de ROI (va en la landing y en la llamada)

Se hace con los números del cliente, **nunca inventados**. En la landing va como ejemplo ilustrativo,
etiquetado como tal.

**Parte 1 — consultas sin contestar / fuera de horario**

```
Consultas sin respuesta a tiempo al mes × % que compraría × Ticket medio
Ejemplo: 80 × 25 % × 45 € = 900 €/mes que se dejan de ganar
```

**Parte 2 — carritos abandonados (solo si hay tienda online)**

```
Carritos abandonados al mes × Ticket medio = venta que se va sola
Ejemplo: 50 × 45 € = 2.250 €/mes
Recuperable con WhatsApp + seguimiento, ~30 % → ~675 €/mes
```

**Total del ejemplo: ~1.575 €/mes sobre la mesa.** Con eso, el sistema se paga el primer mes.

Reglas: usar siempre el porcentaje de recuperación bajo (conservador); si un dato falta, se pregunta,
no se inventa; y toda cifra publicada va marcada como estimación.

---

## 7. Estructura de pago (llamada, no landing)

50 % para arrancar (flexible en el cómo, no en el cuánto) → entrega en **15 días desde que el cliente
entrega TODOS los datos** (catálogo con fotos, tallas y precios, políticas de envío y cambios,
horarios, acceso a la tienda online) → lo prueba y da el OK → 50 % restante → **primer mes de
mantenimiento gratis** → desde el segundo, la mensualidad del nivel.

**La mensualidad incluye:** mantenimiento, ajustes y corrección de errores, cambios en cómo habla el
sistema, carga de colección nueva, rebajas y promos de temporada, actualización de tallas y precios.

**No incluye:** rehacer la estructura, funcionalidades nuevas grandes (subir de nivel), integraciones
nuevas desde cero (otra tienda online, otro TPV). Se cotizan aparte.

**Ojo con la incoherencia de plazos:** la landing dental dice "2–4 semanas" y la garantía de 30 días.
La oferta de llamada dice 15 días y 50 % al OK. Para la landing de ropa **usa el plazo de la landing
(2–4 semanas) y la garantía de 30 días**, que es el estándar de la marca. El 50/50 y los 15 días son
de la llamada.

---

## 8. Implementación: `index-ropa.html`

### Método

1. Copia `index-dental.html` → `index-ropa.html`.
2. **No toques el CSS.** Todo el sistema de diseño (tokens oklch, tipografías Geist e Instrument
   Serif, componentes) se hereda tal cual.
3. Mantén `<body data-accent="amber" data-serif="on" data-density="comfortable">` salvo que se pida
   otro acento. Los valores válidos de `data-accent` son `amber`, `olive`, `terracotta`, `mono`.
4. Sustituye **solo el contenido de sector**, sección por sección, según el mapa de abajo.

### Cabeza del documento

- `<title>`: `Arka Systems · Sistemas de IA para tiendas de ropa en España`
- `meta description`: habla de ventas recuperadas por WhatsApp e Instagram, no de features.
- `link rel="canonical"` y todos los `og:url` → `https://www.arkasystems.es/index-ropa.html`
  (ajusta si el deploy usa una ruta limpia tipo `/tiendas-de-ropa`).
- Bloque `window.ARKA_LINKS`: cambia el texto del WhatsApp. Debe decir tienda, no clínica:
  ```
  https://wa.me/34671286513?text=Hola%20Esteban%2C%20vengo%20de%20arkasystems.es%20y%20tengo%20una%20tienda%20de%20ropa.
  ```
  El `calendly` y el `webhook` **no se tocan**.
- JSON-LD: mantén el `ProfessionalService`. **Elimina el `VideoObject` del caso Voraldent** de esta
  página si no se reutiliza ese vídeo, para no declarar un vídeo que no está en la página.

### Mapa sección por sección

Los `id` de sección se conservan todos, para no romper anclas ni JS.

#### `.hero`

Eyebrow, H1 con `<span class="em">` en las palabras destacadas, subtítulo, dos CTA y las dos píldoras
de abajo (`Sin permanencia` · `30 días o no pagas`) se mantienen igual en estructura.

H1 (sustituye el de la clínica):

> Recuperamos las **ventas** que tu tienda pierde cada semana en Instagram y WhatsApp, y te
> devolvemos **las noches** sin el móvil en la mano.

Subtítulo:

> Un sistema que atiende tus privados 24 horas con tu catálogo, resuelve tallas, colores y envíos,
> y persigue por ti a las que dicen "me lo pienso". Tú solo cierras la venta.

#### `#para-quien` — tres resultados en 30 días

Tres `.icp-card` con el mismo formato (`num` + h3 + línea + 3 bullets de métrica). Contenido:

**01 / Más ventas — Dejas de perder las consultas que no llegas a contestar**
- Hasta un 25 % de los mensajes fuera de horario convertidos en venta
- Respuesta en menos de 3 segundos, 24/7, también domingos
- Recuperación de carritos abandonados desde el primer mes

**02 / Menos móvil — Recuperas tus noches y tus domingos**
- Las consultas repetidas de talla, color y envío, resueltas sin ti
- Cero mensajes contestados a las once de la noche desde el sofá
- El sistema filtra y te avisa solo cuando hay una venta que cerrar

**03 / Más recurrencia — Vendes a quien ya te compró**
- Tu base de clientas ordenada por talla y última compra
- Difusiones de colección nueva y rebajas a toda tu base en un clic
- Seguimiento automático a quien preguntó y no compró

> Todas las cifras van etiquetadas como estimaciones, igual que en la dental. Nota al pie obligatoria:
> *"Cifras estimadas según el diseño del sistema. Cada tienda es distinta — en tu diagnóstico
> calculamos rangos para tu caso."*

#### `#caso` — **AQUÍ NO INVENTES NADA**

No hay ningún cliente del sector ropa en producción todavía. **Prohibido fabricar un caso, un
testimonio, un logo o unas métricas de una tienda que no existe.** Dos salidas válidas:

- **Opción A (recomendada):** reemplaza la sección por una titulada *"Cómo se ve en una tienda"*
  con la conversación de ejemplo (clienta pregunta por una talla → el sistema responde con foto y
  precio → no contesta en 3 minutos → mensaje de recuperación → quiere reservar → avisa a la dueña).
  Etiquétala explícitamente como **demostración**, no como caso real.
- **Opción B:** conserva el caso Voraldent tal cual, con su vídeo y su logo, bajo un titular honesto
  del tipo *"Un sistema ya en producción, en otro sector"*, y explica en una línea que el mismo
  enfoque se aplica a una tienda.

Cuando haya una tienda real en producción, esta sección pasa a ser un caso de verdad con sus cifras.

#### `#como` — tres pasos

Se mantiene el molde (Diagnóstico 30 min gratis → Implementación 2–4 semanas → Validación 30 días).
Solo cambian los ejemplos: en el paso 01, "vemos el día a día de tu tienda e identificamos cuántas
consultas se quedan sin contestar y cuánto se te va en carritos"; en el 02, "montamos el sistema
sobre lo que ya usas: tu Instagram, tu WhatsApp y tu tienda online (Shopify, WooCommerce) o tu TPV";
en el 03, "medimos ventas recuperadas, consultas atendidas y tiempo liberado".

#### `#servicios` — cuatro frentes, un solo sistema

1. **Agente de ventas 24/7 en WhatsApp e Instagram** — resuelve tallas, colores, precios, stock,
   envíos y cambios con tu catálogo real. Entiende fotos y audios.
2. **Seguimiento y recuperación** — persigue a quien preguntó y no compró, y recupera los carritos
   que se quedan a medias.
3. **Base de clientas y difusiones** — quién compró qué y qué talla usa, con envíos a toda tu base
   para colección nueva y rebajas por la API oficial de WhatsApp.
4. **Stock y panel en tiempo real** — conectado a tu tienda online o tu TPV: ventas recuperadas,
   prendas más preguntadas y las tallas que te piden y no tienes.

#### `#paquetes` — los tres planes

Mismo componente que la dental: eyebrow "Inversión transparente", H2 "Tres formas de empezar.
**Riesgo cero**.", las dos notas laterales (garantía 30 días, capacidad limitada a 2 implementaciones
al mes) y las tres tarjetas con `desde` + importe + `/mes` + "+ implementación única a medida".
El plan 02 lleva la cinta `★ Recomendado`.

| Tarjeta | Título | Blurb | Desde |
|---|---|---|---|
| 01 — Vendedor 24/7 | Atención que no se escapa | Para tiendas con Instagram activo que pierden ventas por no llegar a contestar. | **200 €/mes** |
| 02 — Clientela | El sistema completo | Atención, seguimiento y tu base de clientas trabajando. Para tiendas que quieren vender más a quien ya les compró. | **300 €/mes** |
| 03 — Sistema Pro | Varias tiendas y stock en vivo | Para tiendas con volumen, tienda online o más de un local. | **400 €/mes** |

Bullets de cada tarjeta: los del nivel correspondiente en la sección 3, escritos en resultado
(columna derecha de la tabla de traducción). El 02 y el 03 empiezan con "Todo lo del plan anterior,
más:". Cada tarjeta cierra con la línea de garantía, igual que la dental.

Pie: `IVA no incluido. Cupos limitados a 2 implementaciones/mes para garantizar calidad de entrega.`

#### `#contacto` y `#faq`

`#contacto` se mantiene igual (diagnóstico de 30 minutos, sin guion comercial), cambiando "qué tarea
te está comiendo el tiempo" por "cuántas consultas se te quedan sin contestar".

FAQ, seis preguntas. Las dos primeras y las dos últimas se adaptan; el RGPD se mantiene:

1. **¿Cuánto tarda en estar funcionando?** Una primera automatización, 2 semanas. Sistema completo,
   3–4 semanas. Varias tiendas, 6–8 semanas.
2. **¿Funciona con mi tienda online?** Sí. Shopify, WooCommerce, PrestaShop o un TPV. El sistema
   funciona como capa externa: no te obligamos a migrar nada.
3. **¿Y si contesta mal a una clienta?** El sistema responde solo lo que tiene cargado de tu
   catálogo y tus políticas. Lo que no sabe, lo deriva a una persona al instante. Nunca improvisa
   un precio ni un plazo de envío.
4. **¿Esto no quita el trato cercano?** Al revés. Lo repetitivo (talla, color, horario, envío) lo
   resuelve el sistema. Tú te quedas con la conversación que vende y con la clienta que tienes
   delante.
5. **¿Cómo gestionáis los datos de mis clientas (RGPD)?** Servidores europeos, RGPD por defecto,
   contrato de tratamiento de datos, sin compartir con terceros. *(Igual que la dental, sin la parte
   de AEPD ni consentimientos clínicos.)*
6. **¿Y si no funciona en mi tienda?** Medimos el impacto 30 días tras el go-live. Si no hay impacto
   medible, no pagas la implementación. Y si antes de empezar vemos que no encaja, te lo decimos.

#### `#founder`

No se toca. Es contenido de marca, igual en las tres variantes. Respeta el atributo
`data-show-section="showFounder"`.

---

## 9. Tono e identidad (esto es lo que hay que respetar de verdad)

- **Español de España, de tú.** La landing habla a una dueña de tienda en España: "tienes",
  "tu tienda", "vosotros" solo si se refiere al equipo. *(Los documentos internos de método están
  en rioplatense; la web, no.)*
- **Cero jerga técnica.** Ni IA, ni API, ni prompt, ni n8n, ni flujo, ni automatización en el copy
  de cara al cliente. El stack puede aparecer en una ficha técnica discreta, como en la dental.
- **Resultado antes que feature**, siempre. Si una frase describe lo que el sistema *hace*,
  reescríbela para que describa lo que el dueño *gana*.
- **"Inversión", nunca "precio".**
- **Sin humo y sin exagerar.** Toda cifra va como estimación. Si un dato no se tiene, no se publica.
- **Nada de casos, testimonios, logos ni resultados inventados.** Es la regla que no se negocia.
- Frases cortas. Sin signos de exclamación en el copy de la página. Sin emojis.

---

## 10. Bloque para `ARKA-base-conocimiento.md`

Añadir al documento de la base de conocimiento del agente de voz, respetando su formato de secciones
en mayúsculas, un bloque de sector:

```markdown
## SECTOR TIENDAS DE ROPA (ESPAÑA)
Qué implementamos: atención de WhatsApp e Instagram 24/7 con el catálogo real de la tienda (tallas,
colores, precios, envíos, cambios), seguimiento automático a quien pregunta y no compra,
recuperación de carritos, base de clientas con difusiones de colección nueva y rebajas por la API
oficial, y stock y panel en tiempo real conectados a la tienda online o al TPV.
Dolores típicos: privados sin contestar fuera de horario y en domingo; los "me lo pienso" que no
vuelven; carritos abandonados; y no tener a quién avisar cuando entra la colección nueva.
Resultado que se promete: ventas recuperadas y dejar de contestar mensajes de noche. NO dar cifras
de euros recuperados: dependen del ticket medio y del volumen de cada tienda. Si preguntan por el
retorno, redirigir al diagnóstico gratuito para estimarlo con sus números.
Herramientas que solemos conectar: Shopify, WooCommerce, PrestaShop, TPV, Instagram, WhatsApp.
Casos en producción en este sector: NINGUNO todavía. No inventar ni insinuar uno. El caso real
disponible es Voraldent, clínica dental en Barcelona, y se puede mencionar como cliente en
producción de otro sector.
Precio: no se publican tarifas. Se cierra en el diagnóstico. Nunca dar una cifra.
```

---

## 11. Mensajes de captación en frío (no van en la web)

Para Instagram DM y WhatsApp. Requisito previo: la demo de **esa** tienda ya montada, porque el
mensaje afirma que existe.

**Base:**

> Hola, muy buenas! Acabo de crear un clon con IA de tu tienda: responde exactamente igual que
> vosotros. Está creado para responder fuera de horario, resolver dudas de tallas y stock, y hacer
> seguimiento de las que dicen "me lo pienso" en automático, y tienes estadísticas en tiempo real.
> Si te gustaría verlo, responde VER y te lo envío en menos de un minuto!

**Con tienda online:** cambia el tercer punto por "recuperar los carritos que se quedan a medias".

**Solo local físico:** abre con "contesta los privados de Instagram exactamente igual que vosotros"
y usa "responder de noche y los domingos".

**Seguimiento a 48 h:**

> Hola! Te escribí el otro día, te dejé montado el clon de tu tienda. Sigue ahí guardado. Respondes
> VER y te lo mando, son 30 segundos de mirarlo.

**Cuando responde VER:** se manda el vídeo y se cierra pidiendo la llamada, no se deja en "qué guay".

Reglas: la palabra clave es de una sílaba (VER); cero links en el primer mensaje, que Instagram y
WhatsApp castigan los enlaces a desconocidos; y la promesa de "menos de un minuto" se cumple.

---

## 12. Checklist de aceptación

- [ ] `index-ropa.html` creado a partir de `index-dental.html`, con el CSS intacto.
- [ ] `index.html` e `index-dental.html` sin un solo cambio.
- [ ] Ni una palabra técnica (IA, API, prompt, n8n, flujo, automatización, agente) en el copy visible.
- [ ] "Inversión" en lugar de "precio" en toda la página.
- [ ] Los tres planes muestran mensualidad + "implementación única a medida". **El pago único
      (1.000/1.500/2.000 €) no aparece en ningún sitio de la web.**
- [ ] Ningún caso, testimonio, logo ni métrica de una tienda inventada.
- [ ] Toda cifra de resultado etiquetada como estimación.
- [ ] `canonical`, `og:url` y `twitter:*` apuntan a la URL de la página nueva, no a la raíz.
- [ ] El texto del WhatsApp de `ARKA_LINKS` dice tienda, no clínica. `calendly` y `webhook` intactos.
- [ ] `VideoObject` del JSON-LD eliminado si el vídeo del caso no está en la página.
- [ ] `sitemap.xml` con la URL nueva (y la dental, que falta).
- [ ] Responsive verificado a 400 px de ancho: sin scroll horizontal.
- [ ] Los dos CTA abren WhatsApp y el calendario correctamente.

## 13. Pendientes que necesitan material que no existe todavía

Estos no los puede resolver el agente solo. Dejarlos anotados, no inventarlos:

- Vídeo de demo con una tienda de ropa (el equivalente a `videos/caso-voraldent.mp4`).
- Imagen OG propia de la variante ropa (1200×630).
- Primer cliente del sector en producción, para convertir `#caso` en un caso real.
- Decidir la URL final de deploy: `index-ropa.html` o una ruta limpia tipo `/tiendas-de-ropa`.
