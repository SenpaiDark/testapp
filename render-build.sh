#!/bin/bash
# Render build script for Django deployment

echo "Starting Render build process..."

# Install dependencies
echo "Installing Python dependencies..."
pip install -r requirements.txt

# Collect static files
echo "Collecting static files..."
python manage.py collectstatic --noinput

# Apply database migrations
echo "Applying database migrations..."
python manage.py migrate

# Seed initial data if needed
echo "Seeding initial data..."
python manage.py seed_lessons

echo "Build process completed successfully!"