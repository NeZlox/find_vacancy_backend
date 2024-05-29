import asyncio
import traceback

import aiohttp
from bs4 import BeautifulSoup
from fake_useragent import UserAgent
from src.logger import logger


async def get_content(url, proxy=None) -> BeautifulSoup | None:
    error = 429
    cnt = 0

    while error == 429 and cnt < 5:
        cnt += 1
        headers = {
            "User-Agent": UserAgent().random
        }

        try:
            async with aiohttp.ClientSession() as session:
                async with session.get(url, headers=headers, proxy=proxy if proxy else None,timeout=30) as response:
                    error = response.status
                    if response.status == 200:
                        html = await response.text()
                        soup = BeautifulSoup(html, 'lxml')
                        return soup
            await asyncio.sleep(10)

        except Exception as e:
            logger.error(f"traceback.format_exc()\n\n{e}\n")
            #print(traceback.format_exc())
            #print(e)
            #print(proxy)
            return None

    return None