from bs4 import BeautifulSoup


import asyncio
from concurrent.futures import ThreadPoolExecutor
from functools import partial

import requests
from fake_useragent import UserAgent
from bs4 import BeautifulSoup
import traceback
import time


def get_content(url, proxy=None) -> BeautifulSoup | None:
    error = 429
    cnt = 0
    temp = open("test.txt", 'r', encoding='utf-8')
    soup = BeautifulSoup(temp, 'lxml')
    #return soup
    while error == 429 and cnt < 5:
        try:
            cnt += 1
            headers = {
                "User-Agent": UserAgent().random
            }

            if proxy != None:
                response = requests.get(url=url, headers=headers, proxies=proxy, timeout=30)
            else:
                response = requests.get(url=url, headers=headers, timeout=30)



            error = response.status_code
            if response.status_code == 200:
                html = response.text
                soup = BeautifulSoup(html, 'lxml')
                return soup


            time.sleep(10)


        except Exception as e:
            print(traceback.print_exc())
            print(e)
            print(proxy)
            return None


URL = "https://volgograd.hh.ru/vacancies"
"https://volgograd.hh.ru/vacancies/programmist?page=0"


def main_page(name):
    url = f"{URL}/{name}"



    #content_bs4 = await get_content(url)
    temp = open("test.txt", "r", encoding="utf-8")
    content_bs4 = BeautifulSoup(temp, 'lxml')
    content_item_card = content_bs4.find_all("span", {"class": "serp-item__title-link-wrapper"})
    data = []
    for content in content_item_card:
        name_vacancies = content.find("span")
        url_vacancies = content.find("a")
        if name_vacancies:
            pass
            #print(name_vacancies.text)
        if url_vacancies and 'href' in url_vacancies.attrs:
            pass
            data.append(url_vacancies['href'])
            #print(url_vacancies['href'])

    return data
def sub_page(url,c):
    content_bs4 = get_content(url)
    open(f'vacancies_{c}.txt', 'w', encoding='utf-8').write(str(content_bs4))


def main():
    vacancie = "programmist"
    data = main_page(vacancie)

    with ThreadPoolExecutor(max_workers=5) as executor:
        executor.map(sub_page, data, range(1, len(data) + 1))


if __name__ == "__main__":
    import time

    start_time = time.time()
    main()
    end_time = time.time()
    print(end_time - start_time)



# 50 данных
# 5 потоков и синхронный requests VS 5 потоков и асинхронный aiohttp

# 11.220036506652832
# 9.793546438217163

# 12.561756372451782
# 9.94325590133667