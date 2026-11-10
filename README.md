# proyecto_unittest_python
Proyecto de creación de unidades de test con python y unittest

---

### 🔹 Pruebas y depuración

- **pytest** → Para pruebas unitarias.

  ```bash
  pip install pytest
  ```

- **pylint** / **flake8** → Análisis estático y buenas prácticas de código.

  ```bash
  pip install pylint flake8
  ```

Para que unittest reconozca los archivos y funciones de prueba, asegúrate de que
los archivos comiencen con la palabra `test_` (ej. `test_validaciones.py`) y
que los métodos dentro de tus clases de prueba también comiencen con `test`.

Para ejecutar todos los archivos de prueba (test) en un módulo o proyecto de
Python utilizando unittest, puedes usar la terminal. El comando principal te
permite descubrir automáticamente todas las pruebas.

```bash
python -m unittest discover
```

Una vez descubiertas las pruebas, se pueden ejecutar con el comando:

```bash
pytest
```

#### Ejecutar un archivo de test específico

Para ejecutar un archivo de prueba (test) específico, puedes usar la terminal y
ejecutar el siguiente comando:

```bash
python -m unittest test_nombre_archivo
```

#### Ejecutar una clase de test específica

Si tienes múltiples clases dentro de un mismo archivo de pruebas, puedes filtrar
por la clase, mediante el terminal ejecutando el siguiente comando:

```bash
python -m unittest test_nombre_archivo.NombreDeLaClase
```

---

### 📂 Instalación mediante `requirements.txt`

Un archivo `requirements.txt` permite simplificar la instalación de
dependencias, especificando librerías y versiones a utilizar en cada proyecto.

Para crear un archivo `requirements.txt`, teniendo las dependencias YA
instaladas, mediante el terminal, ejecutar el siguiente comando:

```bash
pip freeze > requirements.txt
```

Para ejecutar la instalación de todas las dependencias definidas previamente
para cada proyecto, debemos crear un archivo `requirements.txt`, y luego,
mediante el terminal, navegar hasta la ubicación del archivo, para ejecutar el
siguiente comando:

```bash
pip install -r requirements.txt
```
