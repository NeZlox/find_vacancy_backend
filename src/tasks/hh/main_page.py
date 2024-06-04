import asyncio
import threading
from concurrent.futures import ThreadPoolExecutor
from functools import partial
from typing import List

from src.logger import logger
from src.tasks.get_bs4 import get_content

__all__ = ['main_page_async']


async def main_page_process(country: str, name:str, page:int) -> List[str]:
    #thread_id = threading.get_ident()
    #logger.info(f"Thread {thread_id}: Processing page {page}")
    #url = f'https://{country}.hh.ru/vacancies/{name}?page={page}'
    url = f'https://{country}.hh.ru/search/vacancy?text={name}&page={page}'
    if country == 'moscow':
        url = f'https://hh.ru/search/vacancy?text={name}&page={page}'


    logger.info(f"\nUrl main_page  {url}\n")

    content_bs4 = await get_content(url)
    data = []
    if content_bs4:
        content_item_card = content_bs4.find_all('span', {'class': 'serp-item__title-link-wrapper'})
        for content in content_item_card:
            url_vacancies = content.find("a")
            if url_vacancies and 'href' in url_vacancies.attrs:
                # записывать в базу данных через алхимию АСИНХРОННО
                data.append(url_vacancies['href'])
    return data


async def main_page_async(country: str, name: str, page_start: int, page_end:int) -> List[List[str]]:
    loop = asyncio.get_running_loop()
    with ThreadPoolExecutor(max_workers=min(5,abs(page_end-page_start)+1)) as executor:
        tasks = [
            loop.run_in_executor(executor, partial(asyncio.run, main_page_process(country, name, page)))
            for page in range(page_start, page_end + 1)
        ]
        results = await asyncio.gather(*tasks)

        return results

