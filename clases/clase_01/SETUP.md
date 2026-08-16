# Guía de instalación — MASDFR

**Matemáticas Actuariales para Seguro de Daños, Fianzas y Reaseguro**
Facultad de Ciencias, UNAM

Esta guía deja tu computadora lista para todo el curso: editor, Python, el repositorio de trabajo y el ambiente `MASDFR` con las librerías. La haremos juntos en la Sesión 1; te queda como referencia.

---

## Paso 1 — VS Code

1. Descarga e instala **VS Code** desde <https://code.visualstudio.com>.
2. Ábrelo y ve a la pestaña **Extensiones** (`Ctrl/Cmd + Shift + X`).
3. Instala estas extensiones de Microsoft:
   - **Python**
   - **Jupyter**  (nos deja correr notebooks dentro de VS Code)
   - *(opcional)* **Pylance**

## Paso 2 — Python con Anaconda

1. Descarga **Anaconda** desde <https://www.anaconda.com/download> e instálalo con las opciones por defecto.
2. Abre el **Anaconda Prompt** (Windows) o la **Terminal** (macOS/Linux).
3. Comprueba que responde:

   ```bash
   conda --version
   python --version
   ```

## Paso 3 — Git y el repositorio

1. Instala **Git** desde <https://git-scm.com> si aún no lo tienes.
2. En el **Anaconda Prompt**, colócate donde quieras guardar el curso (en este caso yo quiero la capreta documents\Ciencias Cursos\Daños\2027-1, en lugar de cd documents, pondria cd documents\Ciencias Cursos\Daños\2027-1 ) y clona el repositorio:

   ```bash
   cd Documentos
   git clone https://github.com/Ericdaniel78/MASDFR_20271.git
   cd MASDFR_20271
   ```

   > Si Git te pide contraseña al clonar o al subir cambios, usa un **Personal Access Token** de GitHub (GitHub → *Settings → Developer settings → Personal access tokens*), **no** tu contraseña de la cuenta.

## Paso 4 — El ambiente `MASDFR`

El repositorio incluye el archivo `environment.yml` con todas las librerías. Desde la carpeta `MASDFR_20271`:

```bash
conda env create -f environment.yml
conda activate MASDFR
python -m ipykernel install --user --name MASDFR
```

Cuando el ambiente esté activo verás `(MASDFR)` al inicio de la línea.

## Paso 5 — Verificar

1. En VS Code: **File → Open Folder** y abre la carpeta `MASDFR_20271`.
2. Abre el notebook **`00_verificacion.ipynb`**.
3. Arriba a la derecha, elige el kernel **MASDFR**.
4. Corre todas las celdas (**Run All**). Deben salir puras ✓ y una gráfica de prueba.

Si todo está en verde, tu entorno quedó listo para la Sesión 2.

---

## Problemas frecuentes

- **`conda` no se reconoce** → abre específicamente el *Anaconda Prompt* (no la terminal común), o reinstala Anaconda marcando la opción de agregarlo al PATH.
- **El kernel `MASDFR` no aparece en VS Code** → confirma que corriste el `ipykernel install` con el ambiente activado; reinicia VS Code.
- **`git` no se reconoce** → instala Git y reinicia el Anaconda Prompt.
- **Falla la clonación por permisos** → genera y usa un Personal Access Token de GitHub.
- **`conda env create` muy lento** → es normal la primera vez (descarga varias librerías); déjalo terminar.

## Trabajo diario con el repositorio

```bash
git pull                      # traer lo último antes de empezar
# ...trabajas en tus notebooks...
git add .
git commit -m "describe tu cambio"
git push                      # subir tu trabajo
```
