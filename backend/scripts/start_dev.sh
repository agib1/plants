#!/bin/bash

# migrate database
python3 manage.py makemigrations
python3 manage.py migrate --no-input
# run django in development mode
python3 manage.py runserver 0.0.0.0:8000
