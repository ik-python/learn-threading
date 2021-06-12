#!/usr/bin/env python3

# https://docs.aiohttp.org/en/stable/
# https://github.com/realpython/materials/blob/master/concurrency-overview/io_asyncio.py

import asyncio
import time
import aiohttp

async def download_site(session, url):
    async with session.get(url) as response:
        print(f"status: {response.status}, content: {response.content_length}")

async def download_all_sites(sites):
    async with aiohttp.ClientSession() as session:
        tasks = []
        for url in sites:
            task = asyncio.ensure_future(download_site(session, url))
            tasks.append(task)
        await asyncio.gather(*tasks, return_exceptions=True)

if __name__ == "__main__":
    sites = [
        "https://www.jython.org",
        "http://olympus.realpython.org/dice",
    ] * 80
    start_time = time.time()
    asyncio.run(download_all_sites(sites))
    asyncio.gather()
    duration = time.time() - start_time
    print(f"Downloaded {len(sites)} in {duration} seconds")
