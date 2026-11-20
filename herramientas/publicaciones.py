"""python herramientas/publicaciones.py
   -> recorta publicaciones reales de las capturas de perfil de Marcas (public/assets/ig/<cuenta>.webp, las que deja
      perfiles.py) y las guarda en duotono cobalto, de la noche al hielo pasando por #1e55e0, en
      public/assets/redes/<cuenta>-<n>.webp, para las historias de Redes. n es la casilla de la cuadrícula del perfil, de
      izquierda a derecha y de arriba abajo. Las que se usan están en USADAS y redes.astro las pide con el mismo nombre.
      Si se vuelven a tomar las capturas, se corre otra vez y las historias muestran lo que haya entonces en esas casillas."""
from pathlib import Path
import numpy as np
from PIL import Image, ImageOps

RAIZ = Path(__file__).resolve().parents[1]
CAPTURAS = RAIZ / 'public' / 'assets' / 'ig'
SALIDA = RAIZ / 'public' / 'assets' / 'redes'
# (la historia "Contenido con IA" ya no usa publicaciones reales: sus piezas se dibujan, porque esas publicaciones no se hicieron con IA)
USADAS = ['oneillcolombia-1', 'oneillcolombia-4', 'oneillcolombia-8', 'speedocolombia-1', 'speedocolombia-8',
          'weedhoney-3', 'graduadoseafit-1', 'lamigueria-2', 'agilcash-3']
# el duotono: cada gris va a un azul, de la noche (#02071a) al hielo (#eef3ff)
TONOS = [(0, (2, 7, 23)), (.34, (12, 42, 122)), (.6, (30, 85, 224)), (.84, (143, 176, 255)), (1, (238, 243, 255))]


def cuadricula(a):
    """las filas de la cuadrícula: tramos altos de filas casi sin blanco, debajo de la cabecera del perfil"""
    blanco = (a > 245).mean(axis=1)
    filas, desde = [], None
    for y in range(350, a.shape[0]):
        if blanco[y] < .5 and desde is None: desde = y
        if blanco[y] >= .5 and desde is not None:
            if y - desde > 120: filas.append(desde)
            desde = None
    if desde is not None and a.shape[0] - desde > 300: filas.append(desde)
    return filas


def duotono(im):
    g = np.asarray(ImageOps.autocontrast(im.convert('L'), cutoff=1)).astype(float) / 255
    xs = np.array([t[0] for t in TONOS]); cs = np.array([t[1] for t in TONOS], float)
    return Image.fromarray(np.stack([np.interp(g, xs, cs[:, c]) for c in range(3)], -1).astype('uint8'))


def main():
    SALIDA.mkdir(parents=True, exist_ok=True)
    for nombre in USADAS:
        cuenta, n = nombre.rsplit('-', 1); n = int(n) - 1
        # la captura en español a 780 (no la de inglés ni la de 480, que perfiles.py deja al lado)
        grandes = [f for f in CAPTURAS.glob(f'{cuenta}*.webp') if not f.stem.endswith('-480')]
        archivo = next((f for f in grandes if not f.stem.endswith('-en')), next(iter(grandes), None))
        if not archivo: print(f'{nombre}: no hay captura de {cuenta}'); continue
        im = Image.open(archivo).convert('RGB'); a = np.asarray(im.convert('L')).astype(int)
        filas = cuadricula(a); w = im.width
        if n // 3 >= len(filas): print(f'{nombre}: la captura no llega a esa casilla'); continue
        # las casillas van separadas por una raya blanca de dos píxeles; se deja fuera
        x0 = round((n % 3) * w / 3) + (2 if n % 3 else 0); x1 = round((n % 3 + 1) * w / 3) - (2 if n % 3 < 2 else 0)
        y0 = filas[n // 3]; alto = round((x1 - x0) * 4 / 3)
        duotono(im.crop((x0, y0, x1, min(im.height, y0 + alto)))).save(SALIDA / f'{nombre}.webp', quality=82)
        print(f'{nombre}: {archivo.name} casilla {n + 1}')


if __name__ == '__main__':
    main()
