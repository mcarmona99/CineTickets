# CineTickets

## Descripción de la aplicación a desarrollar

La documentación referente al desarrollo de este hito puede encontrarse en
[documentacion/hito_0/desarrollo_hito_0.md](https://github.com/mcarmona99/CineTickets/blob/master/documentacion/hito_0/desarrollo_hito_0.md)

### Problema a resolver

#### Contexto

Con la ya vivida situación epidemiológica relativa a la enfermedad del Covid-19, el sector del espectáculo en vivo se ha
visto fuertemente influenciado por los cambios de medidas de seguridad tales como distanciamiento, que da lugar a una
limitación de aforo; y la restricción de horarios. A diferencia de la televisión y otros canales de distribución en
línea (Netflix, HBO, etc.), este sector del espectáculo, donde destacamos cines, teatros, etc. es más afectado debido a
que propone actividades únicamente en directo, por lo que la asistencia del público es crucial para que este negocio se
lleve a cabo.

Con esta introducción se plantea un claro problema a resolver por las empresas dedicadas al espectáculo en directo,
concretamente los cines.

#### Problema

Teniendo en cuenta unas restricciones específicas de distanciamiento de seguridad para asegurar las condiciones
sanitarias de los asistentes, se quiere maximizar la asistencia del mayor número de personas a una sala de cine,
agrupando, sin guardar distancia de seguridad, a personas que van juntas a ver la película.

### Descripción de la aplicación

**CineTickets** es una aplicación para compra de entradas de cine. Cuando un usuario de la aplicación interesado en
comprar entradas para una película realiza una compra, estará haciendo una reserva de butacas para el número de entradas
que ha comprado, teniendo en cuenta que dichas butacas serán siempre colindantes, es decir, el grupo de personas para el
que se ha hecho la compra irá sentado junto.

Internamente, para cada compra, la aplicación calculará si ese número de personas cabe en la sala de cine respetando las
restricciones, teniendo ya una sala de cine con alguna butaca cubierta o totalmente vacía si es la primera compra. En el
caso de que no haya disponibilidad de asientos, se procederá a una optimización de manera que se resituarán algunos de
los grupos que ya tienen sus entradas compradas para maximizar el número de asistentes al cine y de esta forma, el
beneficio económico.

Para cada compra de cada cliente se repetirá este proceso, de forma que llegará un punto en el que no se encontrará una
solución para la distribución de asientos respetando las restricciones de distanciamiento, con lo que no se podrá
realizar la venta de dichas entradas a ese cliente.

#### Ejemplo

Supongamos el siguiente ejemplo, tenemos que situar a grupos de personas en una sala respectando una distancia de
seguridad equivalente a una butaca a la derecha, izquierda, delante y detrás de cada persona:

Tenemos una sala de cine con aforo (sin contar restricciones), para 24 personas, 8 personas por fila.

|   |   |   |   |   |   |   |   |
|---|---|---|---|---|---|---|---|
|   |   |   |   |   |   |   |   |
|   |   |   |   |   |   |   |   |

Suponemos que cierta persona A, compra entradas para un grupo de 3 asistentes a dicha película, en dicha sala (
asignación de sala según horario). La aplicación comprueba que el grupo de personas cabe en el cine respetando las
restricciones y asigna butacas para dicho grupo:

| A  | A  |  A |   |   |   |   |   |
|---|---|---|---|---|---|---|---|
|   |   |   |   |   |   |   |   |
|   |   |   |   |   |   |   |   |

Suponemos ahora que una persona B, compra entradas para otro grupo de 2 asistentes. La aplicación comprueba que el grupo
de personas cabe en el cine respetando las restricciones y asigna butacas para dicho grupo:

| A  | A  |  A |   |  B  | B  |   |   |
|---|---|---|---|---|---|---|---|
|   |   |   |   |   |   |   |   |
|   |   |   |   |   |   |   |   |

Ahora tenemos que una persona C, compra entradas para otro grupo de 2 asistentes. La aplicación comprueba que el grupo
de personas cabe en el cine respetando las restricciones y asigna butacas para dicho grupo:

| A  | A  |  A |   |  B  | B  |   |   |
|---|---|---|---|---|---|---|---|
|   |   |   |   |   |   |  C | C  |
|   |   |   |   |   |   |   |   |

Persona D, 4 entradas, mismo proceso:

| A  | A  |  A |   |  B  | B  |   |   |
|---|---|---|---|---|---|---|---|
|   |   |   |   |   |   |  C | C  |
|  D |  D |  D |  D |   |   |   |   |

Persona E, compra 2 entradas. En este caso, no tenemos butacas disponibles para este grupo de personas. La aplicación
entonces aplica el algoritmo de optimización y comprueba si podríamos meter a dos personas más respetando restricciones,
con lo que buscamos maximizar el aforo y por tanto, beneficios. Se redistribuyen las butacas de B y C.

| A  | A  |  A |   |    |   | B  |  B |
|---|---|---|---|---|---|---|---|
|   |   |   |   |  C |  C |   |   |
|  D |  D |  D |  D |   |   |  E | E  |

Persona F, quiere comprar otras 2 entradas. Ocurre como en el caso anterior, no hay butacas disponibles. La aplicación
ejecuta el algoritmo, pero en este caso, no se llega a una solución factible respetando las restricciones, entonces, no
se pueden vender las entradas a F.

Con este ejemplo vemos que la aplicación resuelve el problema planteado, hemos situado a grupos de personas en la sala
respetando que cada persona de un mismo grupo está junto a otra del mismo grupo y se respeta la distancia de seguridad
con otro grupo, todo esto, maximizando el número de ventas de entradas (si no hubiésemos recalculado posiciones con la
compra de C, estaríamos perdiendo dos entradas).

En el ejemplo solo se ha aplicado el algoritmo de redistribución una vez. En ejemplos con salas de mayor tamaño se darán
muchas más redistribuciones para vender más entradas, con lo que este algoritmo será clave para maximizar beneficios en
las ventas de un cine.

#### Implicados

Encontramos dos implicados o principales interesados en usar la aplicación:

- Por una parte, el **cliente que pretende realizar la compra de entradas**:

  Este usuario o implicado podrá comprar una o más de una entrada de cine para una o más películas específicas.


- Por otra parte, la **cadena de cines que se oferta para vender entradas**:

  La empresa ofertará las entradas para cada una de las películas que tenga disponibles. Dicha empresa actúa como un
  implicado pasivo, ya que realmente no participa directamente en el uso de la aplicación. La aplicación realiza la
  distribución de butacas en una sala de cine y manda dicha distribución al cine una vez se ha completado aforo u horas
  antes de empezar la película en caso de no completar aforo.

### Lógica de negocio

La lógica de negocio subyacente de la aplicación reside en la distribución de butacas para cada uno de los grupos de
personas que han comprado entradas. Esto se realizará implementando y evaluando distintos algoritmos basados en
heurísticas.

### Despliegue en la nube

La aplicación será viable de cara a un despliegue en la nube. La APP consistirá en un servidor al que los usuarios,
clientes, podrán hacer peticiones para comprar entradas para una película.

El servidor realizará para cada compra, las evaluaciones y redistribuciones de salas necesarias. De esta forma, el
servidor deberá aplicar el algoritmo de distribución a la vez para distintas compras de distintas películas; y también
de distintas horas, ya que entendemos que una película podrá estar disponible en distintos horarios y por tanto, usando
distintas salas.
