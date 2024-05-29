FROM python:3.12-alpine

WORKDIR /vacancy

COPY requirements.txt .

RUN pip install -r requirements.txt && python -c "from transformers import BertTokenizer, BertModel; BertTokenizer.from_pretrained('ai-forever/ruBert-large'); BertModel.from_pretrained('ai-forever/ruBert-large')"

COPY . .





