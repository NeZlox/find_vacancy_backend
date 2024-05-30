#!/bin/sh

# Wait for the dependencies to be ready
sleep 10

# Apply database migrations
alembic upgrade head

# Start Gunicorn server
gunicorn src.main:app --workers 4 --worker-class uvicorn.workers.UvicornWorker --bind=0.0.0.0:8000 &

# Start Celery worker
celery -A src.tasks.celery_app:celery worker --loglevel=INFO --pool=threads --concurrency=4 &

# Start Celery Flower
celery -A src.tasks.tasks:celery flower --url_prefix=/flower
