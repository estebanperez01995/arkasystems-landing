# BRIEF · Arka Systems · consola

**Origen:** entrevista parcial. Las respuestas 1, 6, 7 y 8 vienen del usuario
(Esteban) en la sesión; el resto está autoescrito a partir de la copy real de
arkasystems.es, de `ARKY-base-conocimiento.md` y de `AGENTE-ARKY-elevenlabs.md`.
Marcado como **parcialmente autoescrito**, no entrevistado en su totalidad.

---

## Las ocho respuestas

**1. Vibe en tres a cinco palabras, más referencias.**
Del usuario: "algo muy profesional". Identidad existente: ámbar tierra sobre
fondo cálido oscuro, Geist + Instrument Serif italic, sobrio, sin ruido.
Referencias implícitas en la web actual: consola de operaciones, panel de
control, no folleto de agencia.

**2. El recorrido de scroll, sección a sección.**
Autoescrito desde la estructura real de index.html: reconocimiento del problema
(atención al cliente, trabajo manual, información dispersa) → caso real →
cómo trabajamos → qué implementamos → llamada.

**3. La curva de energía.**
Empieza en calma (una mañana cualquiera), se tensa (la cola crece y nadie
responde), estalla en alivio (el agente entra), baja a técnica sobria (cómo lo
hace), y cierra tranquila (un campo donde escribir).

**4. Cómo debería sentirse, y el ÚNICO momento a recordar.**
Ver abajo, "Curva de sentimiento". El momento: **el instante en que el agente
toma la conversación y la cola empieza a vaciarse bajo tu propio scroll.**

**5. Una cosa que este sitio haga que ningún otro haga.**
La traza. Ver "Movimiento firma".

**6. Cuán lejos del premium-minimal.**
Del usuario: profesional. Se queda en editorial/técnico. Nada de brutalismo,
nada de maximalismo. La identidad ámbar sobre oscuro no se toca.

**7. ¿Un mundo continuo o escenas distintas?**
Del usuario, indirectamente, al elegir **Live surface**: ni lo uno ni lo otro.
La página no es un viaje ni una serie de escenas: es **una superficie única
operando**. Los actos son estados de esa superficie, no lugares.

**8. ¿Qué assets ya tiene?**
`videos/hero-1..3.mp4` (3,6–5,5 MB), `videos/caso-voraldent.mp4` (31 MB),
pósters, `assets/logo.png`, `assets/logo.svg`, `assets/founders/*`,
`assets/voraldent-logo.jpg`. Autorizó reencodearlos todos.

---

## Gramática: Live surface

**Por qué perdieron las otras siete:**

- **Filmic one-shot** — es hacia donde ya apunta la web actual (vídeo en bucle
  a sangre + fade-ups) y carga con la carga de la prueba en el skill. Arka no
  vende una sensación, vende un sistema que funciona sin mirarlo.
- **Chaptered editorial** — su prueba es operativa, no narrativa. Nadie lee la
  automatización de una clínica dental como un reportaje impreso.
- **Continuous world** — no hay geografía real, y es la más cara y frágil.
  Nada en el brief la justifica.
- **Typographic poster** — tiran a la basura su activo más fuerte: la cosa
  funcionando de verdad.
- **Gallery / catalog** — tienen cinco servicios, pero la pregunta real del
  visitante es "¿funcionará en mi negocio?", no "¿qué opciones hay?".
- **Split stage** — segunda opción real (manual vs. automatizado). Pierde
  porque obliga a un compromiso simétrico de dos columnas durante toda la
  página, y el argumento de Arka no es binario: es "el sistema trabaja mientras
  tú no miras".
- **Rhythmic cutlist** — registro equivocado. El comprador es un dueño de PyME
  al que le vas a pedir su CRM y su WhatsApp.

**Por qué gana Live surface:** el pitch honesto de Arka es literalmente
"mira lo que hace". Su producto ya es una consola — hilos de WhatsApp,
llamadas a herramientas, traza de auditoría, paneles en tiempo real. La página
puede *ser* esa consola en lugar de enseñar capturas de ella.

**Regla de honestidad (uniqueness.md §2.3):** todos los paneles son markup real
computando su estado desde arrays en la página. El chrome declara en su cara
`ENTORNO DE DEMOSTRACIÓN · datos de ejemplo` de forma permanente, y las cifras
de Voraldent conservan su descargo original.

---

## Movimiento firma: la traza

Un raíl de auditoría persistente, parte del chrome de la consola, que registra
cada acción que el sistema ejecuta a medida que el visitante hace scroll.

Empieza vacío. Al llegar al cierre acumula ~30 líneas con marca de tiempo que
el visitante ha generado con su propio scroll, y el cierre se las lee de vuelta:
*"En tu visita el sistema ejecutó N acciones."*

Está atado a su reclamo real de producto ("trazabilidad absoluta"), no existe
en ningún otro sitio, y es el único elemento que persiste de punta a punta de
la página. No es un parámetro de un dispositivo del kit: es JS propio en la
página, alimentado por `--sc-p` y por eventos de acto.

---

## Curva de sentimiento

| Acto | Emoción | Qué la causa en pantalla |
|---|---|---|
| 1 · Estado | Reconocimiento | La consola en marcha a las 07:58, tranquila. Es un lunes cualquiera. |
| 2 · La bandeja | Tensión → **alivio (PICO)** | La cola se llena bajo tu scroll, los contadores envejecen, el estado se pone rojo. A mitad de acto el agente entra, responde turno a turno y la cola se vacía. |
| 3 · Bajo el capó | Confianza | El raíl de llamadas reales: `buscar_disponibilidad()`, `crear_cita()`. No es magia, es una tubería. |
| 4 · Módulos | Reconocimiento propio | El visitante elige el panel que aplica a su negocio. Clic real, cambio real. |
| 5 · En producción | Prueba | Voraldent: cliente real, stack real, cifras que cuentan, vídeo en su propio panel. |
| 6 · Puesta en marcha | Compromiso tranquilo | El asistente de primer arranque. Paso 01 es un campo donde escribir. |

Ningún par de actos adyacentes comparte sentimiento. La tensión y el alivio
viven dentro del mismo acto porque son el mismo gesto: es el giro, no dos
secciones.

---

## El pico

**"Es la web donde la IA fue contestando los mensajes mientras yo hacía scroll."**

Vive en el acto 2. Tiene el span más grande de la página por margen visible
(4.2 vh contra 2.0 del siguiente). El acto anterior (Estado, 0.9 vh) es el más
callado de todos: el silencio delante del pico es deliberado.

## La frase de contárselo a alguien

*Es la web donde la bandeja de entrada se vacía sola mientras bajas, y al final
te enseña el registro de todo lo que hizo mientras la leías.*

---

## Silencio autorizado

- **Acto 1, p 0.00–0.35.** La consola está quieta a propósito. Nada se mueve
  salvo el reloj. Es reconocimiento, no scroll muerto: el visitante tiene que
  creer que es una mañana normal antes de que deje de serlo.
- **Acto 2, p 0.42–0.48.** La pausa entre el último mensaje sin responder y la
  primera respuesta del agente. Es el respiro antes del giro.

## Tabla de dispositivos

| Acto | Dispositivo | Span | Por qué este |
|---|---|---|---|
| 1 Estado | `flow` + `in` | 0.9 | La superficie ya está en un estado. No es un título. |
| 2 La bandeja | `pin` + `--sc-p` + un salto de `drift` | 4.2 | Una superficie que aguanta mientras el estado avanza: la definición de la gramática. El giro cae donde `dwell` asienta. |
| 3 Bajo el capó | `pan` | 2.0 | El viaje lateral se lee como "tubería"; el vertical se lee como "argumento". |
| 4 Módulos | `flow` + puntero | 1.1 | Una tira de pestañas real. El visitante opera, no lee. |
| 5 En producción | `pin` + `count` | 1.6 | `count` solo sobre cifras reales, ya publicadas y con descargo. |
| 6 Puesta en marcha | `flow` + input real | 1.2 | El cierre de Live surface es una entrada de verdad, no un botón magnético. |

Familias distintas: flow, pin, pan, puntero, count. Cinco. Ninguna dos veces
seguidas. `drift` se usa en dos paradas, no más. Prohibidos por la gramática y
respetados: `scrub`, `kinetic`, `spotlight`, `magnet`.

---

## Verificación

Harness propio en `shoot.mjs` y `reduced.mjs`. Camina la página posición a
posición, con el scroll suave desactivado (medir a mitad de una animación de
scroll da falsos positivos en todo), y reporta scroll muerto, cues que nunca
llegan a opacidad plena, y el recuento final de la traza.

**Resultado, escritorio 1440×900, 40 posiciones**
- Longitud: 9911 px, 11.0 alturas de viewport. Dentro del presupuesto 8–14, y
  fuera de la banda 13.6–13.8 que el skill marca como huella.
- Scroll muerto: ninguno.
- Cues que nunca llegan a opacidad plena: ninguno.
- Traza al final: 18 acciones.

**Resultado, móvil 390×844, 30 posiciones**
- Longitud: 10439 px, 12.4 alturas de viewport.
- Scroll muerto: ninguno. Cues incompletos: ninguno. Traza: 18 acciones.

**Movimiento reducido**
La historia se cuenta entera: 18 acciones en la traza y los 7 mensajes del hilo
pintados, sin depender de la posición de scroll.

### Lo que la verificación encontró y se corrigió

1. **Los contadores de Voraldent desaparecían.** Llevaban un `data-sc-cue` con
   `to=1.00`, así que se desvanecían justo cuando el panel estaba entero en
   pantalla. Los números pasaron a `data-sc-count-at`, que es su ventana propia,
   sin cue que los apague.
2. **El raíl lateral del acto 3 se metía por debajo del raíl de traza.** Se
   añadió una ventana con `overflow: hidden` a la anchura de la columna.
3. **En móvil desaparecían la traza y la navegación enteras.** La traza es el
   movimiento firma: si no sobrevive al teléfono, la página no lo tiene. Ahora
   es un ticker de una línea desplegable sobre la barra de estado, y el raíl de
   módulos es una tira de pestañas bajo la cabecera.
4. **El hilo se veía vacío en móvil.** Los mensajes ocultos con `opacity: 0`
   seguían maquetando, así que en un panel de altura fija el contenedor
   recortaba por el extremo equivocado. Pasaron a `display: none` con una
   animación de entrada.
5. **Dos líneas del acto 2 se solapaban de forma ilegible.** Se acortó el cruce
   al 3% del acto y se aceleraron las rampas, para que en todo momento una
   domine. La última línea, que es la resolución del pico, pasó a cue de un solo
   valor: entra y se queda.
6. **La barra de estado se contradecía**: decía "cola acumulándose" y
   "latencia —" mientras el agente respondía en el hilo. La alarma quedó
   confinada a la primera mitad del acto.
7. **El ticker de móvil quedaba tapado** por una barra de estado que envolvía a
   dos filas. La barra pasó a una sola fila de la altura que declara.

### Feel check

Recorrido en frío, una palabra por acto, comparado después contra la curva:

| Acto | Curva pretendida | Sentido al recorrerlo | Diff |
|---|---|---|---|
| 1 Estado | Reconocimiento | Reconocimiento | — |
| 2 Bandeja | Tensión → alivio | Tensión → alivio | — |
| 3 Bajo el capó | Confianza | Confianza | — |
| 4 Módulos | Reconocimiento propio | Curiosidad | Cerca. El clic real es lo que lo salva; sin él sería un catálogo. |
| 5 En producción | Prueba | Prueba | — |
| 6 Puesta en marcha | Compromiso tranquilo | Compromiso | — |

El pico es el mayor cambio visual de la página y tiene el mayor espacio de
scroll por margen visible. El cierre resuelve: no se desvanece ni se convierte
en un pie de página, y el recuento de la traza cierra el arco que abrió el
acto 1.

### Lo que NO está verificado

- **Un teléfono de verdad.** Chromium sin cabeza no reproduce el decodificador
  de vídeo de un iPhone, su política de autoplay, el modo de bajo consumo ni el
  scroll táctil. La página no depende de vídeo con scrub, así que el riesgo es
  bajo, pero el vídeo del caso Voraldent hay que verlo en un iPhone real.
- **Las fuentes.** Google Fonts está bloqueado en el entorno de construcción, así
  que las capturas salen con las fuentes de reserva. Geist e Instrument Serif
  cargan igual que en la web actual.
- **El widget de voz de ElevenLabs.** Bloqueado también aquí. Se le reservó
  hueco sobre la barra de estado, pero hay que comprobarlo en producción.
- **Contraste medido sobre la página compuesta.** El harness no lo mide todavía;
  se comprobó a ojo sobre las capturas. La paleta es la misma que la web actual,
  que ya está en producción.
