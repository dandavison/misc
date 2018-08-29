#!/usr/bin/env python3

import asyncio

from aiohttp import ClientSession


async def fetch(url):
    async with ClientSession() as session:
        async with session.get(url) as response:
            return await response.read()


def got_result(future):
    print(future.result()[:100])
    loop.stop()


loop = asyncio.get_event_loop()
task = asyncio.ensure_future(fetch('http://www.theguardian.com'))
task.add_done_callback(got_result)
try:
    loop.run_forever()
finally:
    loop.close()


1
