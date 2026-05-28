# proyecto_unittest_python
Proyecto de creación de unidades de test con python y unittest
<hr>
<h3>🔹 Pruebas y depuración</h3>
<ul>
  <li><b>pytest</b> → Para pruebas unitarias.
    <pre><code>pip install pytest</code></pre>
  </li>
  <li><b>pylint</b> / <b>flake8</b> → Análisis estático y buenas prácticas de código.
    <pre><code>pip install pylint flake8</code></pre>
  </li>
</ul>

<p>
Para que unittest reconozca los archivos y funciones de prueba, asegúrate de que los archivos comiencen con la palabra test_ (ej. test_funciones.py) y que los métodos dentro de tus clases de prueba también comiencen con test.
</p>

<p>
Para ejecutar todos los archivos de prueba (test) en un módulo o proyecto de Python utilizando unittest, puedes usar la terminal. El comando principal te permite descubrir y ejecutar automáticamente todas las pruebas.
</p>
<code>python -m unittest discover</code>

<p>
Una vez descubiertas las pruebas, se pueden ejecutar con el comando:
</p>
<code>pytest</code>

<h4>Ejecutar un archivo de test específico</h4>
<p>
Para ejecutar un archivo de prueba (test) específico, puedes usar la terminal y ejecutar el siguiente comando:
</p>
<code>python -m unittest test_nombre_archivo</code>

<h4>Ejecutar una clase de test específica</h4>
<p>
Si tienes múltiples clases dentro de un mismo archivo de pruebas, puedes filtrar por la clase, mediante el terminal ejecutando el siguiente comando:
</p>
<code>python -m unittest test_nombre_archivo.NombreDeLaClase</code>

<hr>
<h3>📂 Instalación mediante <code>requirements.txt</code></h3>

<p>
Un archivo <code>requirements.txt</code>,  permite simplificar la instalación de dependencias, especificando librerías y versiones a utilizar en cada proyecto.
</p>

<p>
Para crear un archivo <code>requirements.txt</code>,  teniendo las dependencias YA instaladas, mediante el terminal, ejecutar el siguiente comando:
  <pre><code>pip freeze > requirements.txt</code></pre>
</p>

<p>
Para ejecutar la instalación de todas las dependencias definidas previamente para cada proyecto, debemos crear un archivo <code>requirements.txt</code>,  y luego, mediante el terminal, navegar hasta la ubicación del archivo, para ejecutar el siguiente comando:
  <pre><code>pip install -r requirements.txt</code></pre>
</p>
