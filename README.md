# CineTickets

## Hito 0 - Descripción de la aplicación a desarrollar

### Descripción 

**CineTickets** es una aplicación para compra de entradas de cine. El cliente del cine usará la aplicación para comprar entradas, a su vez cada una de las cadenas de cines que estén disponibles en la aplicación podrán usar información recogida a partir de los datos que tenemos de las compras de los clientes. Entre esta información disponible destacan perfiles de clientes, gustos de cada uno de ellos, etc.

#### Implicados

Encontramos dos implicados o principales interesados en usar la aplicación, como se ha mencionado en la descripción.

Por una parte, el **cliente que pretende realizar la compra de entradas**. Este usuario o implicado podrá comprar una o más de una entradas de cine para una o más películas específicas.

Por otra parte, la **cadena de cines que se oferta** para vender entradas. La empresa ofertará las entradas para cada una de las películas que tenga disponibles. La empresa, al usar la aplicación, podrá obtener información de cada uno de sus clientes. Entre esta información destacarían posibles perfiles de cada cliente. Los clientes podrían tener perfiles tales como perfil familiar, si el cliente suele comprar entradas para un número exacto de personas; perfil de pareja, si el cliente suele comprar entradas para dos personas; entre otros. Otra información disponible para la empresa serían los gustos de cada uno de los clientes, o posibles películas que podría gustarle a cada uno realizando agrupaciones. Se podrá obtener también información compleja tal como días de la semana que suele acudir un cliente, actores más vistos, etc.

#### Ejemplo

- Uso de la aplicación por parte del cliente Manuel: compra de 5 entradas para la película Dune para el sábado 09 de octubre de 2021.

- Uso de la aplicación por parte de la empresa Kinépolis: obtención del perfil de Manuel.
    - Perfil: grupo de amigos. Posible beneficio interno, realizar oferta para grupo de amigos.
    - Gusto: ciencia ficción.
    - Agrupación: los que vieron Dune también vieron Mad Max. Posible beneficio interno, recomendación.

Manuel obtendría las entradas y su beneficio sería ver la película. 

La empresa que oferta la película, Kinépolis, tendría información sobre Manuel. Una posible acción para obtener beneficios para la empresa sería recomendar a Manuel la película Mad Max y ofrecerle un descuento si compra más de 5 entradas para dicha película.

### Lógica de negocio

La lógica de negocio subyacente de la aplicación reside en el cálculo de información a utilizar por la empresa que oferta las películas de cine. 

En este apartado, la aplicación deberá asignar para cada cliente un posible perfil. Este perfil será asignado teniendo en cuenta cada una de las compras que ha hecho dicho usuario en la APP.

En segundo lugar, la aplicación asignará a cada cliente gustos específicos. Para este apartado, la APP conectará con APIs de cines y/u obtendrá información de cada una de las películas ofertadas en internet. Entre esta información tomaremos el género de la película, actores, etc.

Por otra parte, la aplicación podrá realizar agrupaciones (clustering) de películas para las cuáles se comparten los mismos clientes.

Aparte de la posible información a obtener ya detallada, se estudiará qué otro tipo de datos se podrán obtener de los clientes.


### Despliegue en la nube

La aplicación será viable de cara a un despliegue en la nube. La APP consistirá en un servidor al que los usuarios, ya sean clientes o cines, podrán hacer peticiones para comprar entradas u obtener información de clientes, respectivamente. El cálculo de la información mencionada será realizada en este servidor, siendo ésta la parte más importante del proyecto. 