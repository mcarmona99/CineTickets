# CineTickets

### Referencias:

- [Docker Hub](https://hub.docker.com/)
- [Para configurar construcciones de contenedores automáticas desde GitHub](https://docs.docker.com/docker-hub/builds/link-source/)
  .

### Actualizaciones automáticas

Docker Hub permite configurar construcciones automáticas desde GitHub y BitBucket. Ref: https://docs.docker.com/docker-hub/builds/link-source/

Sin embargo, esto sólo es posible con la versión Pro, que es de pago:

![image](https://user-images.githubusercontent.com/57481331/142952461-127267af-1495-4fc5-a598-7c6cce597279.png)

Mi cuenta fue creada en Julio de 2020, es decir, antes que esta feature fuese de pago, pero no hicé el link entonces.

Tenemos varias alternativas para hacer frente a este problema y conseguir la actualización automática. En clase hemos hablado de las GitHub actions, que será lo que utilicemos. Ref: https://github.com/features/actions

Seguimos [esta guía](https://docs.github.com/en/actions/quickstart#creating-your-first-workflow) para aprender a diseñar nuestro workflow. Estos workflow son básicos, necesitamos construir una GitHub Action que actualice el contenedor de Docker en Docker Hub, con lo que necesitamos profundizar en el tema.

En [este enlace](https://github.com/marketplace/actions/build-and-push-docker-images), se explica cómo construir y subir imágenes de Docker desde una GitHub Action.

Esta acción usa el contexto de Git, con lo que no es necesario usar la Action actions/checkout. Si el repositorio fuese privado, necesitaríamos un Token en la Action.

La Action ejemplo es la siguiente:

```
name: ci

on:
  push:
    branches:
      - 'master'

jobs:
  docker:
    runs-on: ubuntu-latest
    steps:
      -
        name: Set up QEMU
        uses: docker/setup-qemu-action@v1
      -
        name: Set up Docker Buildx
        uses: docker/setup-buildx-action@v1
      -
        name: Login to DockerHub
        uses: docker/login-action@v1 
        with:
          username: ${{ secrets.DOCKERHUB_USERNAME }}
          password: ${{ secrets.DOCKERHUB_TOKEN }}
      -
        name: Build and push
        id: docker_build
        uses: docker/build-push-action@v2
        with:
          push: true
          tags: user/app:latest
```

A continuación, realizo algunos cambios para adaptarla a mi caso de uso.

En primer lugar, como mi proyecto está basado en issues y pull requests, no quiero actualizar la imagen al pushear en master, que es lo que tenemos por defecto. En mi caso quiero actualizarla para todas las ramas en su respectivo pull request.
Para ello, cambio la etiqueta `on` por `on: [pull_request]`. Ref: https://futurestud.io/tutorials/github-actions-run-on-pull-request

Como vemos en los steps, se usa el TOKEN y USERNAME de DockerHub en dos variables, dentro de secrets. Sigo [esta guía](https://docs.github.com/en/actions/security-guides/encrypted-secrets) para configurar esos dos secretos. Concretamente, [este link](https://docs.github.com/en/actions/security-guides/encrypted-secrets#creating-encrypted-secrets-for-a-repository).

![image](https://user-images.githubusercontent.com/57481331/142954086-16d97ef4-df1f-4911-ad78-a91e7ed3ee4e.png)

Con respecto al Token de Docker Hub, se refiere justamente a la contraseña de la cuenta. Con esto, ya tenemos los dos secretos:

![image](https://user-images.githubusercontent.com/57481331/142954376-4ef6c490-cffd-4070-a4fb-c25cfc79eaf2.png)

Este sería el workflow final:

```
name: Update Docker image

on: [pull_request]

jobs:
  docker:
    runs-on: ubuntu-latest
    steps:
      -
        name: Login to DockerHub
        uses: docker/login-action@v1
        with:
          username: ${{ secrets.DOCKERHUB_USERNAME }}
          password: ${{ secrets.DOCKERHUB_TOKEN }}
      -
        name: Build and push
        id: docker_build
        uses: docker/build-push-action@v2
        with:
          push: true
          tags: mcarmona99/cinetickets:latest
```
