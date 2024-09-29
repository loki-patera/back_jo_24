
# back_jo_24

Ce projet étudiant comprend une version de back-end pour l'administration de la billetterie des Jeux olympiques 2024.
  

## Pré-requis

- [Python 3.12.6](https://www.python.org/downloads/)

- [PostgreSQL 16.3](https://www.postgresql.org/download/)


## Installation

Pour une installation en locale avec docker, suivre les étapes suivantes :


  1. À la racine du projet, entrer dans le premier dossier core :
      `cd core`

  2. Créer un environnement virtuel :
      `python -m venv venv`

  3. Activer l'environnement virtuel (commande Windows) :
      `venv\Scripts\activate`

  4. Compléter le fichier env.example avec vos données

  5. Créer une image Docker :
      `docker-compose build`

  6. Démarrer Docker :
      `docker-compose up -d`

  7. Créer un super user pour vous connecter à l'interface admin en fournissant un nom d'utilisateur et un mot de passe :
      `docker-compose exec web python manage.py createsuperuser`
    

## Utilisation

Pour utiliser l'application en locale, suivre les étapes :

 
 1. Ouvrir le serveur à l'adresse [http://127.0.0.1:8000/admin](http://127.0.0.1:8000/admin)

 2. Entrer le nom d'utilisateur et le mot de passe que vous avez créés précédemment