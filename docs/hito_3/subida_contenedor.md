# CineTickets

### Referencias:

- [Docker Hub](https://hub.docker.com/)
- [Crear repositorios de Docker Hub](https://docs.docker.com/docker-hub/repos/#:~:text=To%20push%20an%20image%20to,docs%2Fbase%3Atesting%20)
  .

### Subida del contenedor a Docker Hub

En primer lugar, creamos una cuenta de Docker Hub.

Los repos de Docker Hub te permiten compartir imagenes de contenedores. En nuestro caso, serán usadas para ser construidas automáticamente desde GitHub al encontrar cambios en el repo.

Para crear el repo, es importante tener en cuenta ciertas restricciones, una de ellas quizás la más importante, el nombre del repo debe de ser en minúscula. Ademas, la descripción debe tener hasta 100 caracteres.

Una vez se crea el repositorio, como vemos en la imagen,

![image](https://user-images.githubusercontent.com/57481331/142950574-22128032-f3e7-429a-a0f1-c0eb23c432af.png)

tenemos que subir la imagen de nuestro Dockerfile.

Seguimos ahora la sección llamada [Pushing a Docker container image to Docker Hub](https://docs.docker.com/docker-hub/repos/#pushing-a-docker-container-image-to-docker-hub).

Construcción de la imagen con tag:

```
$ docker build . -t mcarmona99/cinetickets:0.1
Sending build context to Docker daemon  885.2kB
Step 1/5 : FROM python:3.8-alpine3.13
 ---> f5b5076daaef
Step 2/5 : RUN apk add gcc libc-dev libffi-dev && pip install poetry pypyr
 ---> Using cache
 ---> 2ce49fbdd703
Step 3/5 : COPY . /app
 ---> Using cache
 ---> d31f33c75301
Step 4/5 : WORKDIR /app
 ---> Using cache
 ---> 423be4c206b7
Step 5/5 : CMD ["pypyr", "tests"]
 ---> Using cache
 ---> 76b8ccaac0e7
Successfully built 76b8ccaac0e7
Successfully tagged mcarmona99/cinetickets:0.1
```

Subida de la imagen: 

```
$ docker push mcarmona99/cinetickets:0.1
The push refers to repository [docker.io/mcarmona99/cinetickets]
72ba302ede9d: Preparing 
8ceaf09019de: Preparing 
a371e755efd7: Preparing 
72da5b12fa0b: Preparing 
db1287f7a640: Preparing 
71ae3b9da9b3: Waiting 
7fcb75871b21: Waiting 
denied: requested access to the resource is denied
```

Este error ocurre porque previo a la subida, tenemos que loguearnos en Docker con docker login (ref: https://stackoverflow.com/questions/41984399/denied-requested-access-to-the-resource-is-denied-docker):

```
$ docker login
Login with your Docker ID to push and pull images from Docker Hub. If you don't have a Docker ID, head over to https://hub.docker.com to create one.
Username: mcarmona99
Password: 
WARNING! Your password will be stored unencrypted in /home/manuel/.docker/config.json.
Configure a credential helper to remove this warning. See
https://docs.docker.com/engine/reference/commandline/login/#credentials-store

Login Succeeded
```

Tras esto, el push se realiza correctamente:

```
$ docker push mcarmona99/cinetickets:0.1
The push refers to repository [docker.io/mcarmona99/cinetickets]
72ba302ede9d: Pushed 
8ceaf09019de: Pushed 
a371e755efd7: Mounted from library/python 
72da5b12fa0b: Mounted from library/python 
db1287f7a640: Mounted from library/python 
71ae3b9da9b3: Mounted from library/python 
7fcb75871b21: Mounted from library/python 
0.1: digest: sha256:b609a9f6a53b6d37029a99ac2d2c15de1c69f3ad9b1fcd788f2143b7fc59cfe6 size: 1790
```

La imagen se ha subido correctamente a Docker Hub:

![image](https://user-images.githubusercontent.com/57481331/142951760-e7afe676-4dc0-4fab-8295-73c3fdcb05bd.png)