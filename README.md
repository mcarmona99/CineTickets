# CineTickets

## Descripción de la aplicación a desarrollar

La documentación referente al desarrollo de esta parte puede encontrarse en el directorio
[docs/hito_0](https://github.com/mcarmona99/CineTickets/blob/master/docs/hito_0).

En este directorio podemos encontrar un archivo `desarrollo_hito_0.md` que describe los pasos seguidos para la
realización del hito 0. A su vez, podemos encontrar un archivo `descripcion_problema.md` que incluye el desarrollo o MVP
del hito. En este caso se trata de la descripción de la aplicación a desarrollar.

## Concretando y planificando el proyecto

La documentación referente al desarrollo de esta parte puede encontrarse en el directorio
[docs/hito_1](https://github.com/mcarmona99/CineTickets/blob/master/docs/hito_1).

En este directorio podemos encontrar un archivo `planificacion.md` que describe los pasos seguidos para realizar la
primera de planificación del proyecto, donde concretamos hitos e historias de usuario.

## Infraestructura y tests del proyecto

La documentación referente al desarrollo de esta parte puede encontrarse en el directorio
[docs/hito_2](https://github.com/mcarmona99/CineTickets/blob/master/docs/hito_2).

En este apartado añadimos tests y una descripción inicial del entorno o infraestructura de la aplicación, donde se
concretan los gestores de dependencias y tareas. Para la adición de tests, se necesita una biblioteca de aserciones y
marco de pruebas, ambos añadidos también en este apartado.

Cabe mencionar que esta parte del proyecto se divide en la entrega de dos productos mínimamente viables o hitos; en este
caso internos:

- [Interno 1 - Preparación del entorno del proyecto](https://github.com/mcarmona99/CineTickets/milestone/6): en este
  hito interno, se avanza con respecto al hito anterior y se incluyen los gestores de tareas y dependencias y la
  biblioteca de aserciones y marco de pruebas. Más información
  en [docs/hito_2/pmv_interno_1.md](https://github.com/mcarmona99/CineTickets/blob/master/docs/hito_2/pmv_interno_1.md).

- [Interno 2 - Algoritmo básico de asignación de butacas en sala de cine](https://github.com/mcarmona99/CineTickets/milestone/3):
  este hito interno consiste en un producto mínimamente viable que incluye al anterior y que realiza la implementación
  de la función que corresponde con el algoritmo básico de asignación de butacas en una sala de cine. Usamos en este PMV
  el entorno de tests definido en el anterior hito para realizar los tests de la función implementada. Más información
  en [docs/hito_2/pmv_interno_2.md](https://github.com/mcarmona99/CineTickets/blob/master/docs/hito_2/pmv_interno_2.md).

Para correcciones de la entrega del proyecto, se crean las siguientes issues:

- [Redistribuir directorios del proyecto para seguir formato estándar](https://github.com/mcarmona99/CineTickets/issues/30)
- [No se están usando excepciones propias para el proyecto, se usa una sola con códigos](https://github.com/mcarmona99/CineTickets/issues/33)
- [El diseño de clases Sala y Pelicula no son adecuados para la lógica de negocio](https://github.com/mcarmona99/CineTickets/issues/34)
- [Actualizar README y archivos de documentación referentes a Interno 1 e Interno 2](https://github.com/mcarmona99/CineTickets/issues/38)

Se crea además la nueva historia de
usuario: [HU6 - Asistente al cine - Obtener alternativas a las acciones solicitadas](https://github.com/mcarmona99/CineTickets/issues/32)
.

Además, se avanza también con la
issue [Diagrama de clases del proyecto](https://github.com/mcarmona99/CineTickets/issues/10).

Se han reabierto las siguientes issues para profundizar en
investigaciones: [#21](https://github.com/mcarmona99/CineTickets/issues/21)
, [#20](https://github.com/mcarmona99/CineTickets/issues/20), [#19](https://github.com/mcarmona99/CineTickets/issues/19)
.

## Infraestructura: despliegue de la aplicación y tests automáticos

La documentación referente al desarrollo de esta parte puede encontrarse en el directorio
[docs/hito_3](https://github.com/mcarmona99/CineTickets/blob/master/docs/hito_3).

En esta parte del desarrollo de la aplicación, se realiza el despliegue de la aplicación para poder lanzar los tests
unitarios de manera automática. Esto lo queremos conseguir con el uso de contenedores de Docker, herramienta útil para
despliegues repetibles de cualquier aplicación.

Podemos ver la documentación relativa a la subida del contenedor a Docker Hub y actualización
automática, [aquí]((https://github.com/mcarmona99/CineTickets/blob/master/docs/hito_3/subida_contenedor.md))
y [aquí]((https://github.com/mcarmona99/CineTickets/blob/master/docs/hito_3/actualizacion_automatica.md)),
respectivamente. Para la actualización automática, se ha hecho uso de una GitHub Actio. Issue relativa a este
desarrollo: [#47](https://github.com/mcarmona99/CineTickets/issues/47). PR que la
resuelve: [#48](https://github.com/mcarmona99/CineTickets/pull/48).
