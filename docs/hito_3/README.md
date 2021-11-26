# CineTickets

## Infraestructura: despliegue de la aplicación para pruebas

En esta parte del desarrollo de la aplicación, se realiza el despliegue de la aplicación para poder lanzar los tests
unitarios de manera automática en futuros apartados. Esto lo queremos conseguir con el uso de contenedores de Docker,
herramienta útil para despliegues repetibles de cualquier aplicación.

Se ha creado y conseguido completar el
milestone [Interno 3 - Contenedores para pruebas](https://github.com/mcarmona99/CineTickets/milestone/7).

En este milestone, se han creado y completado las siguientes issues:

- https://github.com/mcarmona99/CineTickets/issues/42: para actualización de documentación referente a este producto
  mínimamente viable. Cerrada por PR [#56](https://github.com/mcarmona99/CineTickets/pull/56).
- https://github.com/mcarmona99/CineTickets/issues/44: para automatizar el despliegue de la APP para pruebas. Cerrada
  por PR [#45](https://github.com/mcarmona99/CineTickets/pull/45).
- https://github.com/mcarmona99/CineTickets/issues/46: para añadir buenas prácticas al contenedor creado en la
  issue [#44](https://github.com/mcarmona99/CineTickets/issues/44) y otras mejoras. Cerrada por
  PR [#50](https://github.com/mcarmona99/CineTickets/pull/50).
- https://github.com/mcarmona99/CineTickets/issues/47: para añadir documentación sobre la subida del contenedor a Docker
  Hub y la actualización automática. Cerrada por PR [#48](https://github.com/mcarmona99/CineTickets/pull/48).
- https://github.com/mcarmona99/CineTickets/issues/49: para corregir la tarea tests.yaml y cambios necesarios al
  Dockerfile. Cerrada por PR [#53](https://github.com/mcarmona99/CineTickets/pull/53).
- https://github.com/mcarmona99/CineTickets/issues/51: para investigar la necesariedad de algunas dependencias
  instaladas en el contenedor. Cerrada por PR [#52](https://github.com/mcarmona99/CineTickets/pull/52).
- https://github.com/mcarmona99/CineTickets/issues/54: para subir el contenedor a registros alternativos y públicos de
  contenedores. Cerrada por PR [#55](https://github.com/mcarmona99/CineTickets/pull/55).

Además, se ha creado la issue https://github.com/mcarmona99/CineTickets/issues/43 para añadir documentación referente al
control de versiones (tags de la aplicación). Esta issue no ha sido añadida al PMV.

#### Con respecto a cada una de las rúbricas del apartado:

1.- Elección correcta y justificada del contenedor base.

Podemos ver la documentación relativa a la elección de
base [aquí](https://github.com/mcarmona99/CineTickets/blob/master/docs/hito_3/eleccion_base_dockerfile.md). Issue
relativa a la investigación: [#44](https://github.com/mcarmona99/CineTickets/issues/44). PR que lo
cierra: [#45](https://github.com/mcarmona99/CineTickets/pull/45).

2.- Dockerfile correcto, buenas prácticas, optimización, etc.

Podemos ver la documentación relativa a la mejora del
Dockerfile [aquí](https://github.com/mcarmona99/CineTickets/blob/master/docs/hito_3/mejora_dockerfile.md). Resuelta
issue [#46](https://github.com/mcarmona99/CineTickets/issues/46) para añadir buenas prácticas al contenedor creado en la
issue [#44](https://github.com/mcarmona99/CineTickets/issues/44) y otras mejoras. Cerrada por
PR [#50](https://github.com/mcarmona99/CineTickets/pull/50). También
resueltas [#49](https://github.com/mcarmona99/CineTickets/issues/49) (por
PR [#53](https://github.com/mcarmona99/CineTickets/pull/53))
y [#51](https://github.com/mcarmona99/CineTickets/issues/51) (por
PR [#52](https://github.com/mcarmona99/CineTickets/pull/52)).

3.- Contenedor subido correctamente a Docker Hub y documentación de la actualización automática.

Podemos ver la documentación relativa a la subida del contenedor a Docker Hub y actualización
automática, [aquí](https://github.com/mcarmona99/CineTickets/blob/master/docs/hito_3/subida_contenedor.md)
y [aquí](https://github.com/mcarmona99/CineTickets/blob/master/docs/hito_3/actualizacion_automatica.md),
respectivamente. Para la actualización automática, se ha hecho uso de una GitHub Action. Issue relativa a este
desarrollo: [#47](https://github.com/mcarmona99/CineTickets/issues/47). PR que la
resuelve: [#48](https://github.com/mcarmona99/CineTickets/pull/48).

4.- Uso de registros alternativos y públicos de contenedores (como GitHub Container Registry)

Podemos ver la documentación referente al uso de registros alternativos y públicos de contenedores, en este caso GitHub
Container
Registry, [en este link](https://github.com/mcarmona99/CineTickets/blob/master/docs/hito_3/github_container_registry.md)
. Issue relativa a esta investigación: [#54](https://github.com/mcarmona99/CineTickets/issues/54). PR que la
resuelve: [#55](https://github.com/mcarmona99/CineTickets/pull/55).