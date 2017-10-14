#!/usr/bin/env python3

import asyncio


async def task_f():
    print('in task()')


def example_1():
    ioloop = asyncio.get_event_loop()
    task = ioloop.create_task(task_f())
    ioloop.run_until_complete(task)
    ioloop.close()


example_1()
