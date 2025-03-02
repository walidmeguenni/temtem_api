#!/bin/bash

# Wait for Postgres to be ready
echo "Waiting for Postgres..."
sleep 10

# Create migrations
echo "Create migrations"
python manage.py makemigrations
echo "=================================="


# Run migrations
echo "Migrate"
python manage.py migrate
echo "=================================="

# Seed the database
echo "Seed the database"
python manage.py seed_data
echo "=================================="

# Start the application in production mode
echo "Start server"
python manage.py runserver 0.0.0.0:8000