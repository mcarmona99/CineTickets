# CineTickets

### Uso de registros alternativos y públicos, GitHub Container Registry

Para la resolución de esta issue, sigo
la [documentación oficial de GitHub](https://docs.github.com/en/packages/working-with-a-github-packages-registry/working-with-the-container-registry)
.

Siguiendo los pasos de la documentación, concretamente la parte de autenticar al Container Registry, empezamos creando
un nuevo token PAT (personal access token).

Para crear el PAT,
seguimos [esta guía](https://docs.github.com/en/authentication/keeping-your-account-and-data-secure/creating-a-personal-access-token)
. Básicamente, accedemos a la parte de `settings` de nuestra cuenta de GitHub, luego `developer settings` y finalmente
en` Personal access tokens` para crear el nuevo.

Con respecto a los scopes a elegir (o permisos), elegimos `repo` ya que queremos usar el token para acceder a
repositorios desde la command line.

![image](https://user-images.githubusercontent.com/57481331/143505563-299bde44-a1d7-4eda-9c41-a31a1ba78a82.png)

Una vez tenemos el Token,

![image](https://user-images.githubusercontent.com/57481331/143505618-c230f6bb-4cb2-4a0e-99b1-9cd7517a111c.png)

lo guardamos en una variable de entorno:

```bash
$ export CR_PAT=YOUR_TOKEN
```

Y lo usamos para hacer login al servicio de GitHub Container Registry:

```bash
$ echo $CR_PAT | docker login ghcr.io -u mcarmona99 --password-stdin
```

Finalmente, hacemos push de la imagen a GHCR de la siguiente forma (antes hay que construir la imagen y aplicar el tag
correspondiente):

```bash
$ docker build . -t ghcr.io/mcarmona99/cinetickets
...
$ docker push ghcr.io/mcarmona99/cinetickets:latest
```

Esto no me está funcionando, ya que no he dado permisos de escritura al Token. Por esto, tenía el siguiente error:

```bash
The push refers to repository [ghcr.io/mcarmona99/cinetickets]
a8e62bc67ae9: Preparing 
28c08b1adaeb: Preparing 
de4d2f684298: Preparing 
be32542139d7: Preparing 
a371e755efd7: Preparing 
72da5b12fa0b: Waiting 
db1287f7a640: Waiting 
71ae3b9da9b3: Waiting 
7fcb75871b21: Waiting 
denied: permission_denied: The token provided does not match expected scopes.
```

Con los nuevos permisos añadidos al PAT, `write:packages`, ahora sí se sube correctamente el contenedor a GHCR:

```bash
$ docker build . -t ghcr.io/mcarmona99/cinetickets
...
$ docker push ghcr.io/mcarmona99/cinetickets:latest
The push refers to repository [ghcr.io/mcarmona99/cinetickets]
a8e62bc67ae9: Pushed 
28c08b1adaeb: Pushed 
de4d2f684298: Pushed 
be32542139d7: Pushed 
a371e755efd7: Pushed 
72da5b12fa0b: Pushed 
db1287f7a640: Pushed 
71ae3b9da9b3: Pushed 
7fcb75871b21: Pushed 
latest: digest: sha256:baf1ca02b1925b36b7da35435d0741679551667824b1c4a753a2a95dbc5ae5eb size: 2207
```

Con esto tendríamos el contenedor subido. El problema que nos queda es que la visibilidad es privada por defecto. Para
cambiar esta visibilidad,
seguimos [esta guía](https://docs.github.com/en/packages/learn-github-packages/configuring-a-packages-access-control-and-visibility)
.

Your profile > Packages > cinetickets > Package settings > Change visibility (in the Danger Zone)

Con este cambio, vemos que el contenedor subido es público (se ha quitado el tag de su derecha en el que ponía pr`i`
vate):

![image](https://user-images.githubusercontent.com/57481331/143506432-404191f0-01e7-41d1-aeba-dba775ffe42e.png)

Para bajarlo:

![image](https://user-images.githubusercontent.com/57481331/143506456-90eedaff-d4f9-4cdb-94c3-a18cc258ed0d.png)
