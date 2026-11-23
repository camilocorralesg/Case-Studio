"""python herramientas/revisar.py [--sin-armar]
   -> la revisión completa antes de dar un cambio por terminado: arma el sitio (npm run build)
      y corre a la vez auditar, lineas, bajo_menu, ida_y_vuelta, idioma y contenido (que la copia de los textos del sitio,
      de la que salen el texto sin JavaScript, los datos estructurados y llms.txt, esté al día). Imprime la salida de cada una y un resumen.
   Termina con código 1 si alguna falla. Tarda entre uno y tres minutos."""
import os, subprocess, sys, time
import comun  # deja el sitio servido mientras corren las pruebas

PY = sys.executable
PRUEBAS = ["auditar", "lineas", "bajo_menu", "ida_y_vuelta", "idioma", "contenido"]
CON = {"contenido": ["--comprobar"]}
ENTORNO = dict(os.environ, PYTHONIOENCODING="utf-8", PYTHONUTF8="1", PYTHONDONTWRITEBYTECODE="1")


def armar():
    r = subprocess.run("npm run build --silent", shell=True, cwd=str(comun.RAIZ), capture_output=True, text=True, encoding="utf-8", errors="replace", env=ENTORNO)
    salida = (r.stdout + r.stderr).strip().splitlines()
    print(*salida[-3:], sep="\n")
    if r.returncode:
        print(*salida, sep="\n")
        sys.exit("No se pudo armar el sitio.")


def main():
    if "--sin-armar" not in sys.argv:
        armar()
    t = time.time()
    procs = {n: subprocess.Popen([PY, os.path.join(comun.AQUI, n + ".py")] + CON.get(n, []), stdout=subprocess.PIPE, stderr=subprocess.STDOUT, text=True, encoding="utf-8", errors="replace", env=ENTORNO) for n in PRUEBAS}
    res = {}
    for n, p in procs.items():
        out, _ = p.communicate()
        res[n] = p.returncode
        print(f"\n===== {n} =====\n{out.strip()}")
    print(f"\n===== resumen ({time.time() - t:.0f} s) =====")
    for n in PRUEBAS:
        print(f"  {'bien ' if res[n] == 0 else 'FALLA'}  {n}")
    sys.exit(1 if any(res.values()) else 0)


if __name__ == "__main__":
    main()
