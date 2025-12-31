#!/usr/bin/env bash
# Arrêter le script si une erreur survient
set -o errexit

# 1. Installer les dépendances (Django, Gunicorn, etc.)
pip install -r requirements.txt

# 2. Rassembler les fichiers CSS/JS pour WhiteNoise
python manage.py collectstatic --no-input

# 3. Appliquer les migrations à la base de données (PostgreSQL sur Render)
python manage.py migrate