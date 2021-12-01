#!/bin/bash
python3 manage.py collectstatic --no-input
python3 manage.py makemigrations
python3 manage.py migrate --no-input
gunicorn plantsproj.wsgi -b 0.0.0.0:8000
