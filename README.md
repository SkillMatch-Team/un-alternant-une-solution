# un-alternant-une-solution (develop branch)

## Introduction

Dans le cadre du cours de Web full stack à Ynov Nantes, il nous a été demandé, à nous étudiant en Mastère développemnt Web, de répondre à un appel à projets étudiants, en proposant un projet innovant.  
Notre solution consiste donc à créer un pont entre les écoles, les étudiants, et les entreprises à travers une plateforme web. Des informations telles que les profils d’étudiants, des offres d’alternances ou de formation y seront accessibles.  
Pour répondre à cet appel, nous avons mis sur pied une équipe que nous avons appelée [SkillMatch](https://github.com/SkillMatch-Team). SkillMatch est constituée de quatre étudiants alternants développeurs Web :

[Yann Kotto](https://github.com/prynge) en tant que Product Owner,  
[Kassai Kaym](https://github.com/TheYMK) en tant que Scrum Master,  
[Tom Leveque](https://github.com/tleveke) et [Lilian Ouvrard](https://github.com/Lilian-MMI) en tant que développeurs.

Le cours a été dispensé par [Antoine NGUYEN](https://github.com/tonioo).

---

## Initialisation

### Pre-requis

- Python 3.9 ou ultérieur

- Docker : 
  - [Postgres Database](https://hub.docker.com/_/postgres)
  - [Python](https://hub.docker.com/_/python)
  - [Redis](https://hub.docker.com/_/redis)

- [Make](https://community.chocolatey.org/packages/make) (facultatif)


### Installations

1. Installer les dépendences
  ```sh
    pip install -r requirements.txt
  ```

2. Ajouter les variables d'environnement dans un fichier .env à la racine du projet

  ```bin
    DATABASE_PASSWORD=
    DATABASE_NAME=
    DATABASE_USER=
    DATABASE_HOST=
    DATABASE_PORT=
    DATABASE_URL=
  ```
  
  Les variables d'environnement permettront par la suite d'initier votre container Docker avec ces variables. Votre base de données POSTGRES tournera alors aux valeurs assignées, ce qui signifie que le fichier docker-compose n'a pas à être modifié.

3. Lancer une migration la base de données

  ```sh
    python manager.py migrate
  ```
  
4. Récupération des données initiales

  Si vous n'avez pas la dépendance Make d'installer, il vous faudrat lancer les fixtures unes à unes.
  
  ```sh
    python	.\manage.py loaddata .\authentication\fixtures\schools.json
    python	.\manage.py loaddata .\job\fixtures\jobCodes.json
    python	.\manage.py loaddata .\course\fixtures\courses.json
    python	.\manage.py loaddata .\course\fixtures\refCourseJobCodes.json
    python	.\manage.py loaddata .\course\fixtures\refSchoolCourses.json
   ```
 
  Cependant, si vous possedez Make, vous pouvez simplement lancer la commande :
 
  ```sh
  make loaddata
  ```
  
  L'opération peut durée une petit moment.
 
5. Lancer l'application

  L'application est prête à être lancer localement ! Il vous suffit d'exécuter la commande :
  
  ```sh
    python manager.py runserver
  ```
  
  L'application tourne maintenant à l'adresse `localhost:8000` ou `127.0.0.1:8000`

---

## À des fins de développement

### Pour l'utilisation de sass

```sh
  python manage.py sass authentication/static/styles/scss/ authentication/static/styles/css/ --watch
```

**Remplacer le chemin de votre dossier de styles !**

### Pour l'utilisation de vue

Regarder l'exemple au niveau de `authentication/templates/sign_in.html` et de `app/templates/base.html`

### Pour l'utilisation de Docker

```sh
  docker-compose up
```


### Maquette

[Maquette sur Figma](https://www.figma.com/file/TsQhezJSfolIuSrQkSEEzp/1Alternant1Solution?node-id=0%3A1)


