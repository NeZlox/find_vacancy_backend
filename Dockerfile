FROM python:3.12-alpine

WORKDIR /vacancy

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY . .
# запускается в докер компосе
# RUN alembic upgrade head
# CMD ["gunicorn", "src.main:app", "--workers", "4", "--worker-class", "uvicorn.workers.UvicornWorker", "--bind=0.0.0.0:8000"]


