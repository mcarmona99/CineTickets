# Desarrollo del hito 0

## Preparación del entorno

### Descarga de `git`

git instalado con éxito.

```
$ git --version
git version 2.25.1
```

### Creación del par clave pública/privada

Tras configurar la clave SSH, puedo hacer `git clone` sin que GitHub pida usuario y contraseña.

```
$ git clone git@github.com:mcarmona99/CineTickets.git
Clonando en 'CineTickets'...
remote: Enumerating objects: 5, done.
remote: Counting objects: 100% (5/5), done.
remote: Compressing objects: 100% (5/5), done.
remote: Total 5 (delta 0), reused 0 (delta 0), pack-reused 0
Recibiendo objetos: 100% (5/5), 13.21 KiB | 6.60 MiB/s, listo.
```


### Información personal en commits + firma

En mi caso, tengo correo de empresa y clave GPG para commits en repositorio de empresa.

Necesito por tanto una configuración local para el repo de la asignatura. Esta configuración añadirá tanto información de nombre y correo en commits como la firma de commits verificada, con la clave GPG.

```
$ git config user.name "Manuel Carmona Pérez"
$ git config user.email "e.manuelvillar@go.ugr.es"
$ cat .git/config 
[core]
	repositoryformatversion = 0
	filemode = true
	bare = false
	logallrefupdates = true
[remote "origin"]
	url = git@github.com:mcarmona99/CineTickets.git
	fetch = +refs/heads/*:refs/remotes/origin/*
[branch "master"]
	remote = origin
	merge = refs/heads/master
[user]
	name = Manuel Carmona Pérez
	email = e.manuelvillar@go.ugr.es
	signingkey = xxxxxxxxxxxxxxxx
```

Tras haber configurado la información del repositorio local, indico la clave GPG en GitHub. 

Finalmente, tengo los commits verificados y con mi información personal.


Ref.: 
- [Is it possible to have different Git configuration for different projects?](https://stackoverflow.com/questions/8801729/is-it-possible-to-have-different-git-configuration-for-different-projects)
- [Using GPG keys](https://confluence.atlassian.com/bitbucketserver/using-gpg-keys-913477014.html)
- [Telling Git about your signing key](https://docs.github.com/en/authentication/managing-commit-signature-verification/telling-git-about-your-signing-key)

### Incrementar la seguridad de nuestra cuenta en GitHub activando el segundo factor de autenticación

`Two-factor authentication` configurada con el método de **aplicación de autenticación**.

Ref.: [Configuring two-factor authentication](https://docs.github.com/en/authentication/securing-your-account-with-two-factor-authentication-2fa/configuring-two-factor-authentication)

## Tarea a realizar

Describir un problema a resolver con una lógica de negocio aceptable, cuya resolución esté en gran parte basada en un servidor y que se beneficie de su despligue en la nube, por los distintos casos de uso de datos a procesar y tratar en la misma.

La tarea realizada para este hito se encuentra en el archivo [README.md](https://github.com/mcarmona99/CineTickets/blob/master/README.md) del directorio principal.