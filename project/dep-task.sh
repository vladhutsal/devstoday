#!/bin/sh

echo " -------------- waiting for postgres to start"
while ! nc -z postgres://oljpcydxqkurqc:052d51200fd6eb339c7cc0603192e61a50329e2d07f48130de504b8aae8280f7@ec2-54-73-147-133.eu-west-1.compute.amazonaws.com 5432/dcmicb7atlirua; do
    sleep 0.1
done

echo " -------------- postgres started"

python3 manage.py makemigrations
python3 manage.py migrate

exec "$@"
