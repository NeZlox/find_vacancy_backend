FROM python:3.12-slim

WORKDIR /vacancy

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY . .





