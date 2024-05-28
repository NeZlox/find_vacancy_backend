
import asyncio
import threading
from concurrent.futures import ThreadPoolExecutor
from functools import partial

from src.tasks.get_bs4 import get_content

URL = "https://volgograd.hh.ru/vacancies"
URL = 'https://volgograd.hh.ru/vacancies/programmist?page=0'



async def main_page(country:str ='volgograd',name:str ='programmist', page_start:int=0, page_end:int=0):

    url = f'https://{country}.hh.ru/vacancies/{name}?page={page_start}'


    content_bs4 = await get_content(url)


    #temp = open("test.txt", "r", encoding="utf-8")
    #content_bs4 = BeautifulSoup(temp, 'lxml')


    content_item_card = content_bs4.find_all('span', {'class': 'serp-item__title-link-wrapper'})
    data = []
    for content in content_item_card:
        url_vacancies = content.find("a")
        if url_vacancies and 'href' in url_vacancies.attrs:
            data.append(url_vacancies['href'])

    return data
async def sub_page(url):

    print(threading.get_ident())
    content_bs4 = await get_content(url)
    #temp = open(f'vacancies_{3}.txt', "r", encoding="utf-8")
    #content_bs4 = BeautifulSoup(temp, 'lxml')


    attributes = {
        'Название': {'tag': 'h1', 'params':{'class': 'bloko-header-section-1', 'data-qa':'vacancy-title'}},
        'Зарплата': {'tag': 'span', 'params': {'class': 'magritte-text___pbpft_3-0-4 magritte-text_style-primary___AQ7MW_3-0-4 magritte-text_typography-label-1-regular___pi3R-_3-0-4'}},
        'Опыт работы': {'tag': 'span', 'params': {'data-qa': 'vacancy-experience'}},
        'Формат работы': {'tag': 'p', 'params': {'class': 'vacancy-description-list-item',
                          'data-qa': 'vacancy-view-employment-mode'}},
        'Описание': {'tag': 'div', 'params': {'class': 'g-user-content', 'data-qa': 'vacancy-description'}},
        'Скиллы': {'tag': 'li', 'params': {'data-qa': 'skills-element'}}
    }

    for name, attr in attributes.items():
        text = ""
        if name == 'Скиллы':
            items = content_bs4.find_all(attr['tag'], attr['params'])
            if items:
                skills = [item.text.strip() for item in items]
                text = ' '.join(skills)
        else:
            item = content_bs4.find(attr['tag'], attr['params'])
            if item:
                text = item.text.strip()

        #print(f"{name}: {text}")
    #print("-------------------------------------------------------------")

async def main():
    vacancy = "programmist"
    data_vacancies = await main_page(name=vacancy)




    loop = asyncio.get_running_loop()
    with ThreadPoolExecutor(max_workers=min(5,len(data_vacancies))) as executor:
        tasks = [
            loop.run_in_executor(executor, partial(asyncio.run, sub_page(url)))
            for url in data_vacancies
        ]


        await asyncio.gather(*tasks)


if __name__ == "__main__":
    import time
    time_start = time.time()
    asyncio.run(main())
    time_end = time.time()
    print(time_end - time_start)