import torch
import numpy as np
import re

from transformers import BertTokenizer, BertModel
from typing import List
from sklearn.metrics.pairwise import cosine_similarity

from src.common.schemas import Vacancy_DTO

tokenizer = BertTokenizer.from_pretrained('ai-forever/ruBert-large')
model = BertModel.from_pretrained('ai-forever/ruBert-large')


async def find_matching_jobs(data: List[Vacancy_DTO], search_line: str, n_top: int=10) -> List[Vacancy_DTO]:
    search_line_vector = await get_bert_embedding(search_line.lower())
    similarities = []
    for vacancy in data:
        if vacancy.vacancy_vector is None:
            continue
        vacancy_vector = np.frombuffer(eval(vacancy.vacancy_vector), dtype=search_line_vector.dtype)
        similarity = cosine_similarity([vacancy_vector], [search_line_vector])[0][0]
        similarities.append((vacancy, similarity / (10 if vacancy.description is None else 1)))
    similarities.sort(key=lambda x: x[1], reverse=True)
    result = []
    for vacancy, similarity in similarities[:n_top]:
        print(similarity, vacancy.title)
        result.append(vacancy)

    return result


async def get_bert_embedding(text):
    text = re.sub(r'[^\w\s]', ' ', text)
    inputs = tokenizer(text, return_tensors='pt', truncation=True, padding=True, max_length=512)
    with torch.no_grad():
        outputs = model(**inputs)
    return outputs.last_hidden_state[:, 0, :].squeeze().detach().numpy()