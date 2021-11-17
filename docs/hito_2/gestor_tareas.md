# CineTickets

Analizo los siguientes tasks runner:

#### pypyr

Este task runner o gestor de tareas se usa para automatización y funciona con el lenguaje de marcas `yaml`. Como se
comenta en su [web oficial](https://pypyr.io/), este task runner se usa para cuando los scripts shell se vuelven algo
complejos. Más sencillo que un Makefile.

Con este gestor, se puede automatizar todo combinando comandos; y sobre todo y algo que lo hace muy versátil es que
podemos usar scripts escritos en distintos lenguajes de programación en un mismo pipeline.

Ejemplo: archivo `tests.yaml`

```yaml
# To execute this pipeline, shell something like:
# pypyr tests
steps:
  - name: pypyr.steps.cmd
    comment: Run the project tests using pytest.
    in:
      cmd: pytest
```

#### taskipy

Usado para tareas de pipeline de desarrollos, como pueden ser test, lint or publish.

Como ventaja, tiene la posibilidad de ser integrado con poetry, de forma que se puede añadir lo siguiente a poetry:

```toml
[tool.taskipy.tasks]
test = "python -m unittest tests/test_*.py"
lint = "pylint tests taskipy"
```

y también documentar cada task:

```toml
[tool.taskipy.tasks]
test = { cmd = "python -m unittest tests/test_*.py", help = "runs all unit tests" }
lint = { cmd = "pylint tests taskipy", help = "confirms code style using pylint" } 
```

para después lanzar cada task desde poetry con `poetry run task test`

Como desventaja, depende mucho de poetry, ya que su uso fuera de poetry está poco documentado. Otra desventaja es que
tasks con muchos commandos se pueden volver complejas, ya que estaríamos incluyéndolas en el `pyproject.toml` de poetry.

Fuertemente inspirado en el task runner de npm: [npm-run-script](https://docs.npmjs.com/cli/v8/commands/npm-run-script)

#### poethepoet

Muy similar a `taskipy`.

En este caso, tenemos completa dependencia de poetry.

```toml
[tool.poe.tasks]
  test       = "pytest --cov=poethepoet"                                # simple command based task
  mksandwich = { script = "my_package.sandwich:build" }                 # python script based task
  tunnel     = { shell = "ssh -N -L 0.0.0.0:8080:$PROD:8080 $PROD &" }  # shell script based task
```

En `poethepoet`, tenemos una de las ventajas de pypyr, podemos usar varios lenguajes y en este caso, especificar si es
lenguaje o apuntar a un script de otro directorio, ejemplo task `mksandwich`.

De nuevo como desventaja, complejidad si tenemos muchos comandos para una misma task.

#### invoke

Provee una API de alto nivel para lanzar comandos de shell.

Las tasks en invoke están escritas en python y agrupadas en forma de funciones en un archivo `tasks.py`, con lo que su
estructuración es limpia en cuanto a archivos. Se usa el decorador @task para indicar que una función representa una
tarea para el task runner.

Permite pasar parámetros a cada una de las tareas por medio de flags, lo que lo hace versátil:

```python
from invoke import task


@task
def clean(c, docs=False, bytecode=False, extra=''):
    patterns = ['build']
    if docs:
        patterns.append('docs/_build')
    if bytecode:
        patterns.append('**/*.pyc')
    if extra:
        patterns.append(extra)
    for pattern in patterns:
        c.run("rm -rf {}".format(pattern))
```

Uso:

```bash
$ invoke clean --docs --bytecode build --docs --extra='**/*.pyo'
$ invoke clean -d -b build --docs -e '**/*.pyo'
$ invoke clean -db build -de '**/*.pyo'
```

#### Conclusión

Como conclusión, debato entre usar `pypyr` o `invoke`.

Descarto `taskipy` y `poethepoet` por su alta dependencia de `poetry` y porque al realizar tareas más complejas, se
pierde la facilidad de uso, ya que tendríamos que incorporar al `pyproject.toml` varias líneas para ejecución de una
misma tarea, lo que ensuciaría bastante el archivo.

Entre `pypyr` e `invoke`, decido usar `pypyr` por la modularización que propone. En este task runner, a diferencia
de `invoke`, podemos dividir cada tarea en un archivo distinto, lo que mejora la legibilidad de cada tarea a costa de
tener comandos y archivos distintos para cada tarea. Además de esto, tenemos la oportunidad de usar más lenguajes, cosa
que también aporta `invoke` pero con alguna limitación, ya que parte de un script de `python`.

Este task runner o gestor de tareas se usa para automatización y funciona con el lenguaje de marcas yaml. Como se
comenta en su web oficial, este task runner se usa para cuando los scripts shell se vuelven algo complejos.

Con este gestor, se puede automatizar todo combinando comandos; y sobre todo y algo que lo hace muy versátil es que
podemos usar scripts escritos en distintos lenguajes de programación en un mismo pipeline.

Siguiendo la guía encontrada en https://pypyr.io/docs/getting-started/run-your-first-pipeline/, creo
`my-first-pipeline.yaml` como archivo gestor de tareas base. Este primer pipeline se lanza de la siguiente forma:

```shell
$ pypyr my-first-pipeline
this is step 1
this is step 2
```

Este pipeline se ha adaptado para generar el archivo referente a la orden `installdeps` del proyecto:

```shell
$ pypyr installdeps
Installing dependencies from lock file

No dependencies to install or update
```
