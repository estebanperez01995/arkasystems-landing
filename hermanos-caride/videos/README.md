# Vídeos

Copiar aquí el MP4 final del hero como `hero.mp4` (1920×1080, H.264, sin audio, ~10-15 s, < 8 MB).

Mientras no exista, `index.html` usa como fallback la URL del render de Higgsfield (CDN temporal).

## Optimizar para web (modo loop)

    ffmpeg -i original.mp4 -an -vf "scale=1920:-2" -c:v libx264 -profile:v high -crf 23 -preset slow -movflags +faststart hero.mp4

## Optimizar para modo "scrub" (el vídeo avanza con el scroll)

Para que el scrubbing sea fluido, cada frame debe ser keyframe:

    ffmpeg -i original.mp4 -an -vf "scale=1920:-2,fps=30" -c:v libx264 -g 1 -keyint_min 1 -crf 22 -preset slow -movflags +faststart hero.mp4

Luego en `index.html` cambiar `heroVideoMode: "loop"` por `"scrub"`.

## Poster

Extraer un frame para `img/hero-poster.jpg`:

    ffmpeg -ss 00:00:01 -i hero.mp4 -frames:v 1 -q:v 3 ../img/hero-poster.jpg
