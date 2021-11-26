## Infraestructura y tests del proyecto

Para correcciones de la entrega del proyecto, se crean las siguientes issues:

- [Redistribuir directorios del proyecto para seguir formato estándar](https://github.com/mcarmona99/CineTickets/issues/30)
  . Cerrado por PR 31
- [No se están usando excepciones propias para el proyecto, se usa una sola con códigos](https://github.com/mcarmona99/CineTickets/issues/33)
  . Cerrado por PR 35
- [El diseño de clases Sala y Pelicula no son adecuados para la lógica de negocio](https://github.com/mcarmona99/CineTickets/issues/34)
  . Cerrado por PR 36
- [Actualizar README y archivos de documentación referentes a Interno 1 e Interno 2](https://github.com/mcarmona99/CineTickets/issues/38)
  . Cerrado por PR 41

Se crea además la nueva historia de
usuario: [HU6 - Asistente al cine - Obtener alternativas a las acciones solicitadas](https://github.com/mcarmona99/CineTickets/issues/32)
.

Además, se avanza también con la
issue [Diagrama de clases del proyecto](https://github.com/mcarmona99/CineTickets/issues/10).

Todos los anteriores relativos al comentario:
> los issues que llevan a cabo los tests no están asociados a ninguna HU. Los mensajes de commit no siguen buenas prácticas. Las aserciones usan códigos en vez de tipos propios. ¿Para qué haces una excepción con tipo si luego usas códigos en vez de tipos para las excepciones? Si las películas tienen una fecha determinada, ¿por qué se usa la misma clase para la asignación de asientos, en vez de uno por sala? ¿Por qué no es la fecha un atributo de la sala? ¿Cómo distingues una sala asignada en una fecha de otra asignada en otra fecha? El argumento p ni siquiera lo usas. Debes usar una distribución estándar para el proyecto, y no la de Django. Las excepciones son parte del modelo, y no algo extraordinario. No testeas ninguna excepción como parte del modelo.

Se han reabierto las siguientes issues para profundizar en investigaciones:

- [#21](https://github.com/mcarmona99/CineTickets/issues/21): Cerrada por PR 39. Relativo al comentario:

> pytest es compatible con cualquier biblioteca, como cualquier marco de pruebas. No examinas ningún otro. Te has limitado a copiar, en el mismo orden, el primer resultado que aparece en Google (que indica erróneamente que UnitTest es un marco de test)

- [#20](https://github.com/mcarmona99/CineTickets/issues/20): Cerrada por PR 40. Relativo al comentario:

> enumear marcos de pruebas y bibliotecas de aserciones no es tomar una decisión informada. Y más cuando algunos (unittest) ni siquiera están clasificados correctamente. Primero dices que usas assertpy, y luego a continuación dices que pytest es la biblioteca de seciones. Por favor, aclárate sobre lo que es o no es una biblioteca de aserciones (pytest sólo modifica assert e introduce la aserción raises https://docs.pytest.org/en/6.2.x/assert.html#assert

- [#19](https://github.com/mcarmona99/CineTickets/issues/19): Cerrada por PR 37. Relativo al comentario:

> decir el gestor de tareas que se ha elegido sin compararlo con ningún otro no es documentar una elección. Tampoco usas el gestor de tareas correctamente, sino que lo usas desde poetry.
