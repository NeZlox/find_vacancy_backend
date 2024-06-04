# find_vacancy_backend

## Клонирование проекта

```sh
git clone https://github.com/NeZlox/find_vacancy_backend.git
```

## Переход в рабочую папку проекта

```sh
cd find_vacancy_backend
```

### Скачивание модели

Скачайте предварительно обученную модель и поместите её в папку `src/models/ai-forever_ruBert-large/`. Ссылка на скачивание и список файлов модели доступны по следующей ссылке:

- `pytorch_model.bin`: [Ссылка на скачивание](https://huggingface.co/ai-forever/ruBert-large/tree/main)


## Запуск проекта локально

### Необходимые зависимости

Для запуска проекта на локальной машине необходимы следующие компоненты:
- Python
- PostgreSQL
- Redis
- Node.js (npm)

### Настройка окружения

Настройте файл `.env` под свои нужды и установите `mode=DEV`.

### Установка зависимостей

```sh
pip install -r requirements.txt
```

### Миграция базы данных

```sh
alembic upgrade head
```

### Запуск Redis и остальных компонентов бэкенда

Запустите Redis самостоятельно, затем выполните следующие команды для запуска Celery и Uvicorn:

```sh
celery -A src.tasks.tasks:celery flower


# Выберите один из вариантов 1 или 2:
# 1
celery -A src.tasks.celery_app:celery worker --loglevel=INFO --pool=solo
# 2
celery -A src.tasks.celery_app:celery worker --loglevel=INFO --concurrency=4 --pool=threads


uvicorn src.main:app --host 127.0.0.1 --port 8000 --reload
```

### Запуск фронтенда

Отредактируйте файл `frontend/src/api/config.js`, чтобы установить URL API:

```javascript
const api_url = "http://127.0.0.1:8000";
```

Запустите фронтенд:

```sh
cd frontend
npm start
```

## Запуск в Docker контейнерах

Для запуска проекта в Docker требуется 12-16 гигабайт оперативной памяти.

### Сборка контейнеров

В корневой папке выполните команду для сборки бэкенда:

```sh
docker build -t vacancy_backend:latest .
```

В папке `frontend/` выполните команду для сборки фронтенда:

```sh
cd frontend
docker build -t vacancy_frontend:latest .
```

### Запуск контейнеров

```sh
docker compose up -d
```



```

Этот файл содержит все необходимые инструкции для клонирования, настройки и запуска вашего проекта как локально, так и в Docker контейнерах.