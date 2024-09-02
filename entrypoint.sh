#!/bin/sh
# Wait for PostgreSQL to be available
echo "Waiting for PostgreSQL to be available..."
while ! nc -z db 5432; do
  sleep 0.1
done
echo "PostgreSQL is up and running."

# Apply SQLAlchemy database initialization
echo "Initializing SQLAlchemy database..."
python init_db.py

# Apply database migrations
python manage.py migrate

# Collect static files
python manage.py collectstatic --noinput

# Start the Gunicorn server
exec gunicorn --bind 0.0.0.0:8001 pr_academy360.wsgi:application
