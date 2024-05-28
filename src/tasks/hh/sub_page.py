import asyncio
import re
import threading
from concurrent.futures import ThreadPoolExecutor
from functools import partial
from typing import Any, Dict, List

from src.logger import logger
from src.tasks.celery_app import celery
from src.tasks.get_bs4 import get_content
from src.tasks.hh.add import insert_db_task

__all__ = ['sub_page_task']

async def sub_page_process(url:str) -> None:

    #thread_id = threading.get_ident()
    #logger.info(f"Функция sub_page_process {thread_id}")
    content_bs4 = await get_content(url)
    attributes = {
        'title': {'tag': 'h1', 'params':{'class': 'bloko-header-section-1', 'data-qa':'vacancy-title'}},
        'salary': {'tag': 'span', 'params': {'class': 'magritte-text___pbpft_3-0-4 magritte-text_style-primary___AQ7MW_3-0-4 magritte-text_typography-label-1-regular___pi3R-_3-0-4'}},
        'experience': {'tag': 'span', 'params': {'data-qa': 'vacancy-experience'}},
        'work_format': {'tag': 'p', 'params': {'class': 'vacancy-description-list-item',
                          'data-qa': 'vacancy-view-employment-mode'}},
        'description': {'tag': 'div', 'params': {'class': 'g-user-content', 'data-qa': 'vacancy-description'}},
        'skills': {'tag': 'li', 'params': {'data-qa': 'skills-element'}}
    }
    info_data = {'url': url}
    for name, attr in attributes.items():
        info_data[name] = None
        if name == 'skills':
            items = content_bs4.find_all(attr['tag'], attr['params'])
            if items:
                skills = [item.text.strip() for item in items]
                info_data[name] = skills
        else:
            item = content_bs4.find(attr['tag'], attr['params'])
            if item:
                text = item.text.strip()
                clean_text = re.sub(r'[\n\xa0\t]', '', text)
                info_data[name] = clean_text
        # записывать в базу данных через алхимию АСИНХРОННО
        #logger.info(f"Функция sub_page_process {name}:{text}")
    #logger.info(f"-------------------------------------------------------------\n")
    insert_db_task.delay(info_data)


async def sub_page_async(data_url_vacancies: List[str]) -> None:
    if len(data_url_vacancies) < 1:
        return None
    loop = asyncio.get_running_loop()
    with ThreadPoolExecutor(max_workers=min(5,len(data_url_vacancies))) as executor:
        tasks = [
            loop.run_in_executor(executor, partial(asyncio.run, sub_page_process(url)))
            for url in data_url_vacancies
        ]

        await asyncio.gather(*tasks)




@celery.task
def sub_page_task(data_url_vacancies: List[str]) -> None:
    #logger.info(f"Функция sub_page_task {data_url_vacancies}")
    loop = asyncio.new_event_loop()
    try:
        asyncio.set_event_loop(loop)
        loop.run_until_complete(sub_page_async(data_url_vacancies))
    finally:
        loop.close()