#!/bin/bash

python3 -m venv django_venv

source django_venv/bin/activate

pip install django
pip install psycopg2-binary

pip freeze > requirements.txt

pip install -r requirements.txt

# START PROJECT;; START APP
django-admin startproject fitly

cd fitly

python3 manage.py startapp web


# Deactivate the virtual environment
deactivate
