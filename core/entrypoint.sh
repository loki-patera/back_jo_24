#!/bin/sh

# Contrôle la connection avec la base de données
if [ "$DATABASE" = "postgres" ]
then
  echo "Vérifie si la base de données est en cours d’exécution ..."

  while ! nc -z "$POSTGRES_HOST" "$POSTGRES_PORT"
  do
    sleep 0.1
  done

  echo "La base de données est opérationnelle"
fi

# Crée les migrations
python manage.py makemigrations
# Applique les migrations
python manage.py migrate

exec "$@"