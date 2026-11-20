"""python herramientas/cobalto.py ORIGEN NOMBRE
   -> lleva el azul de fondo de una ilustración (las que el usuario genera con Nano Banana) al cobalto de la marca, #1e55e0,
      sin tocar lo que no es azul (el pan, la madera, el vapor), y la guarda para el sitio en public/assets/NOMBRE-640.webp y
      public/assets/NOMBRE-1024.webp. El original se guarda en src/assets/.
      Ejemplo: python herramientas/cobalto.py src/assets/rd-pan.jpg rd-pan"""
import sys
from pathlib import Path
import numpy as np
from PIL import Image

RAIZ = Path(__file__).resolve().parents[1]
COBALTO = (30, 85, 224)
TAMANOS = (640, 1024)


def a_hsv(a):
    r, g, b = a[..., 0], a[..., 1], a[..., 2]
    mx, mn = a.max(-1), a.min(-1); d = mx - mn; dd = np.maximum(d, 1e-6)
    s = np.where(mx > 0, d / np.maximum(mx, 1e-6), 0)
    rc, gc, bc = (mx - r) / dd, (mx - g) / dd, (mx - b) / dd
    h = np.where(r == mx, bc - gc, np.where(g == mx, 2 + rc - bc, 4 + gc - rc))
    return np.where(d > 1e-6, (h / 6) % 1, 0), s, mx


def a_rgb(h, s, v):
    i = np.floor(h * 6).astype(int) % 6; f = h * 6 - np.floor(h * 6)
    p, q, t = v * (1 - s), v * (1 - s * f), v * (1 - s * (1 - f))
    return np.stack([np.choose(i, [v, q, p, p, t, v]), np.choose(i, [t, v, v, q, p, p]), np.choose(i, [p, p, t, v, v, q])], -1)


def suave(e0, e1, x):
    t = np.clip((x - e0) / (e1 - e0), 0, 1); return t * t * (3 - 2 * t)


def main(origen, nombre):
    im = Image.open(origen).convert('RGB'); a = np.asarray(im).astype(np.float32) / 255
    h, s, v = a_hsv(a); grados = h * 360
    # el azul de fondo de esta imagen: la mediana de sus píxeles azules y saturados
    fondo = (grados > 190) & (grados < 250) & (s > .35)
    if fondo.mean() < .05: sys.exit('la imagen casi no tiene fondo azul; no se toca')
    h0, s0, v0 = (float(np.median(x[fondo])) for x in (h, s, v))
    h1, s1, v1 = (x.item() for x in a_hsv(np.array([[c / 255 for c in COBALTO]], dtype=np.float32)))
    # cuánto es azul cada píxel: por su tono y por su saturación; la luz clara y lo cálido casi no se mueven
    peso = suave(0, 1, np.clip(1 - np.abs(grados - h0 * 360) / 34, 0, 1)) * suave(.12, .42, s)
    h2 = (h + peso * (h1 - h0)) % 1
    s2 = np.clip(s * (1 + peso * (s1 / s0 - 1)), 0, 1)
    v2 = np.clip(v * (1 + peso * (v1 / v0 - 1) * (1 - suave(.8, 1, v))), 0, 1)
    nuevo = Image.fromarray((np.clip(a_rgb(h2, s2, v2), 0, 1) * 255 + .5).astype(np.uint8))
    destino = RAIZ / 'public' / 'assets'
    for t in TAMANOS:
        if t > max(nuevo.size): continue
        k = t / max(nuevo.size)
        nuevo.resize((round(nuevo.width * k), round(nuevo.height * k)), Image.LANCZOS).save(destino / f'{nombre}-{t}.webp', 'WEBP', quality=84, method=6)
        print(destino / f'{nombre}-{t}.webp', (destino / f'{nombre}-{t}.webp').stat().st_size // 1024, 'KB')
    print('azul de fondo #%02x%02x%02x -> #%02x%02x%02x' % (*(round(c * 255) for c in a_rgb(np.array(h0), np.array(s0), np.array(v0))), *COBALTO))


if __name__ == '__main__':
    if len(sys.argv) != 3: sys.exit(__doc__)
    main(sys.argv[1], sys.argv[2])
