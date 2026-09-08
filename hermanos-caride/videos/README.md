# Vídeos del hero

| Archivo | Uso | Formato |
|---|---|---|
| `hero.mp4` | Modo `loop` (por defecto) | 1920×1080, H.264, CRF 24, sin audio, ~5 MB |
| `hero-scrub.mp4` | Modo `scrub` (opcional: avanza con el scroll) | 1280×720, H.264, keyframe en cada frame, ~10 MB |

Origen: render 4K del viaducto generado en Higgsfield (job `dbedd9e0…`, 10 s). El modo se elige en `index.html` → `heroVideoMode`.

## Regenerar desde un máster nuevo

    # loop
    ffmpeg -i master.mp4 -an -vf "scale=1920:-2" -c:v libx264 -profile:v high -pix_fmt yuv420p -crf 24 -preset slow -movflags +faststart hero.mp4
    # scrub (cada frame es keyframe)
    ffmpeg -i master.mp4 -an -vf "scale=1280:-2,fps=30" -c:v libx264 -profile:v high -pix_fmt yuv420p -g 1 -keyint_min 1 -crf 26 -preset slow -movflags +faststart hero-scrub.mp4
    # poster
    ffmpeg -ss 00:00:01 -i master.mp4 -frames:v 1 -vf "scale=1920:-2" -q:v 4 ../img/hero-poster.jpg
