# script-unir-docx
Script en python para unir varios archivos de Microsoft Office Word en uno solo




me aparece esto en la terminal:

```
$ pip install PyODConverter
Collecting PyODConverter
  Downloading PyODConverter-1.8.tar.gz (5.7 kB)
  Preparing metadata (setup.py) ... done
Installing collected packages: PyODConverter
  DEPRECATION: PyODConverter is being installed using the legacy 'setup.py install' method, because it does not have a 'pyproject.toml' and the 'wheel' package is not installed. pip 23.1 will enforce this behaviour change. A possible replacement is to enable the '--use-pep517' option. Discussion can be found at https://github.com/pypa/pip/issues/8559
  Running setup.py install for PyODConverter ... done
Successfully installed PyODConverter-1.8
```

ese mensaje de advertencia está informando sobre un cambio en la forma en que pip instala paquetes en versiones futuras. Esto no afecta el funcionamiento del programa, pero es una buena práctica tener en cuenta estas actualizaciones.

Para evitar este mensaje de advertencia, puedes instalar `PyODConverter` utilizando el método recomendado `--use-pep517`:

```
pip install --use-pep517 PyODConverter
```

Esto le indica a pip que utilice el nuevo método de instalación basado en PEP 517, que es más moderno y recomendado.

Además, si quieres estar preparado para futuros cambios en pip, te recomiendo instalar el paquete `wheel`:

```
pip install wheel
```

De esta forma, pip podrá utilizar el formato de distribución de ruedas (wheels) para instalar paquetes, lo cual es más eficiente que el método antiguo de `setup.py install`.

Con estos cambios, deberías poder ejecutar tu programa sin recibir el mensaje de advertencia.
