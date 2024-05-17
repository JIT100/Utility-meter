#!/bin/sh
set -o errexit
set -o pipefail
set -o nounset

# migrate
python manage.py migrate

echo "Populating local test data..."
python manage.py runscript seed_data

# collect static files
python manage.py collectstatic --no-input

# run app
python manage.py runserver 0.0.0.0:8000

