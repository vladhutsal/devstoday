#!/bin/sh

echo "Waiting for postgres to start"
while ! nc -z db 5432; do
    sleep 0.1
done

echo "postgres started"

python3 manage.py makemigrations
python3 manage.py migrate

exec "$@"
