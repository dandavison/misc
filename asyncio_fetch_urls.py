#!/usr/bin/env python3

import asyncio

from aiohttp import ClientSession


async def fetch(url):
    async with ClientSession() as session:
        async with session.get(url) as response:
            return await response.read()


loop = asyncio.get_event_loop()
urls = ['http://www.gov.uk', 'http://www.theguardian.com']

coros_1 = [fetch(urls[0])]
coros_2 = [fetch(urls[1])]
coros = coros_1 + coros_2
import ipdb ; ipdb.set_trace()
future = asyncio.gather(*coros)
try:
    loop.run_until_complete(future)
finally:
    loop.close()


for res in future.result():
    print(res[:1000], '\n')
