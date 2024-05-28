import time
from contextlib import asynccontextmanager

from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware

from src.common import common_router
from src.logger import logger


@asynccontextmanager
async def lifespan(app: FastAPI):
    yield


app = FastAPI(
    title="Practice API",
    lifespan=lifespan,
    root_path='/api'
)


app.include_router(common_router)






origins = [
    "http://calendar_frontend:80",
    "http://localhost:3000"
]


app.add_middleware(
    CORSMiddleware,
    allow_origins=origins, # ["*"] origins
    allow_credentials=True,
    allow_methods=["GET", "POST", "DELETE", "PATCH", "OPTIONS"], # "OPTIONS","PUT",
    allow_headers=["Content-Type", "Set-Cookie", "Access-Control-Allow-Headers", "Access-Control-Allow-Origin",
                   "Authorization", "Access-Control-Allow-Credentials"]
)

@app.middleware("http")
async def add_process_time_header(request: Request, call_next):
    start_time = time.time()
    response = await call_next(request)
    process_time = time.time() - start_time
    # При подключении Prometheus + Grafana подобный лог не требуется
    logger.info("Request handling time", extra={
        "process_time": round(process_time, 4),
        "api_method": request.method,
        "api_request": request.url,
    })
    return response



# uvicorn main:app --reload

# ipconfig
# uvicorn main:app --host 127.0.0.1 --port 8000 --reload
# для продакшена и только на линуксе gunicorn main:app --workers 4 --worker-class uvicorn.workers.UvicornWorker --bind=0.0.0.0:8000

# celery -A src.tasks.tasks:celery worker --loglevel=INFO --pool=solo
# celery -A src.tasks.tasks:celery flower
# localhost:5555

# celery -A src.tasks.celery_app:celery worker --loglevel=INFO --concurrency=4 --pool=threads
# celery -A src.tasks.celery_app:celery worker --loglevel=INFO --concurrency=4 --pool=threads -n worker1@%h
# celery -A src.tasks.celery_app:celery worker --loglevel=INFO --concurrency=4 --pool=threads -n worker2@%h

