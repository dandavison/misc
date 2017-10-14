#!/usr/bin/env python3

import asyncio


async def task_f():
    print('in task()')


def example_1():
    ioloop = asyncio.get_event_loop()
    ioloop.run_until_complete(task_f())
    ioloop.close()


example_1()
