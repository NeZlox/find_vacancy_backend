import asyncio

from src.tasks.celery_app import celery
from src.tasks.hh import main_page_async, sub_page_task

__all__ = ['parse_hh']


@celery.task
def parse_hh(country:str ='volgograd',name:str ='programmist', page_start:int=0, page_end:int=0) -> None:
    loop = asyncio.new_event_loop()
    try:
        asyncio.set_event_loop(loop)
        results = loop.run_until_complete(main_page_async(country, name, page_start, page_end))
        # logger.info(f"Функция sub_page_task {results}")
        for page, result in enumerate(results, start=page_start):
            # Передать в другую таску sub_page
            # logger.info(f"Page {result}")
            sub_page_task.delay(result)
    finally:
        loop.close()

