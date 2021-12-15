#!/bin/bash
# add static files to server
python3 manage.py collectstatic --no-input
# migrate database
python3 manage.py makemigrations
python3 manage.py migrate --no-input
#host django on gunicorn server
gunicorn plantsproj.wsgi:application -c ./gunicorn.conf.py