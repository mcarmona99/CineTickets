# CineTickets

## Hito 0 - Descripción de la aplicación a desarrollar

La documentación referente al desarrollo de este hito puede encontrarse en
[documentacion/desarrollo_hito_0.md](https://github.com/mcarmona99/CineTickets/blob/master/documentacion/desarrollo_hito_0.md)

### Descripción

**CineTickets** es una aplicación para compra de entradas de cine. El cliente del cine usará la aplicación para comprar
entradas. A su vez cada una de las cadenas de cine que estén disponibles en la aplicación podrán ver información
recogida a partir de los datos que tenemos de las compras de los clientes y que la APP usa para recomendaciones
personalizadas. Entre esta información disponible destacan perfiles de clientes, gustos de cada uno de ellos, etc.

La aplicación utiliza esta información de forma interna para mandar correos electrónicos automáticos a los clientes
recomendando nuevas películas a ver una vez se tiene un perfil concreto para un cliente en cuestión. La creación de este
perfil forma parte de la lógica de negocio del proyecto. Cuando se consigue un perfil definido, se realiza esta
recomendación.

#### Implicados

Encontramos dos implicados o principales interesados en usar la aplicación, como se ha mencionado en la descripción.

- Por una parte, el **cliente que pretende realizar la compra de entradas**:

  Este usuario o implicado podrá comprar una o más de una entrada de cine para una o más películas específicas.


- Por otra parte, la **cadena de cines que se oferta** para vender entradas:

  La empresa ofertará las entradas para cada una de las películas que tenga disponibles. La empresa, al usar la
  aplicación, podrá ver información de cada uno de sus clientes previamente calculada por la aplicación. Entre esta
  información destacarían posibles perfiles de cada cliente. Los clientes podrían tener perfiles tales como perfil
  familiar, si el cliente suele comprar entradas para un número exacto de personas; perfil de pareja, si el cliente
  suele comprar entradas para dos personas; entre otros. Otra información disponible para la empresa serían los gustos
  de cada uno de los clientes, o posibles películas que podría gustarle a cada uno realizando agrupaciones. Se podrá
  obtener también información compleja tal como días de la semana que suele acudir un cliente, actores más vistos, etc.

La información mencionada que la empresa puede consultar relativa a cada cliente, es procesada para realizar
recomendaciones automáticas de películas, una vez se obtiene una cantidad de información adecuada para realizar dicha
recomendación.

#### Ejemplo

- Uso de la aplicación por parte del cliente Manuel: compra de 5 entradas para la película Dune para el sábado 09 de
  octubre de 2021.


- Uso de la aplicación por parte de la empresa Kinépolis: obtención de información de Manuel. Consulta de perfil y
  gustos.


- Uso automático para beneficio de la empresa: tras procesar la información que tenemos de Manuel, la aplicación
  recomienda por medio de un correo electrónico ver Mad Max con una oferta para 5 personas, ya que con su última compra
  cumple las condiciones para dicha recomendación.

Manuel obtendría las entradas y su beneficio sería ver la película.

La empresa que oferta la película, Kinépolis, tendría como beneficio tener a Manuel con descuentos y ofertas
personalizadas, de manera automática.

### Lógica de negocio

La lógica de negocio subyacente de la aplicación reside en el cálculo y procesamiento de información obtenida con cada
compra de entradas de los clientes para realizar recomendaciones personalizadas.

En este apartado, la aplicación deberá asignar para cada cliente un posible perfil. Este perfil será asignado teniendo
en cuenta cada una de las compras que ha hecho dicho usuario en la APP.

En segundo lugar, la aplicación asignará a cada cliente gustos específicos. Para estos gustos, la APP conectará con API
de cines y/u obtendrá información de cada una de las películas ofertadas en internet. Entre esta información tomaremos
el género de la película, actores, etc.

Por otra parte, la aplicación podrá realizar agrupaciones (clustering) de películas para las cuales se comparten los
mismos clientes.

Cuando tenemos toda esta información obtenida, procedemos a su procesamiento. Si se cumplen los `x` criterios
establecidos para poder realizar una recomendación, la aplicación creará una recomendación personalizada para un cliente
específico. Esta recomendación será mandada por correo electrónico al cliente.

Aparte de la posible información a obtener ya detallada, se estudiará qué otro tipo de datos se podrán obtener de los
clientes y sus respectivas compras.

### Despliegue en la nube

La aplicación será viable de cara a un despliegue en la nube. La APP consistirá en un servidor al que los usuarios, ya
sean clientes o cines, podrán hacer peticiones para comprar entradas u obtener información de clientes, respectivamente.
El cálculo de la información mencionada y su procesamiento para la realización de la recomendación personalizada
automática será realizada en este servidor, siendo esta la parte más importante del proyecto.
