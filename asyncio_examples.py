#!/usr/bin/env python3

import asyncio


async def make_coro(i):
    print('in make_coro %d' % i)


class C:
    async def make_coro(self, i):
        print('in make_coro method %d' % i)


def example_1():
    event_loop = asyncio.get_event_loop()
    event_loop.run_until_complete(C().make_coro(1))
    event_loop.close()



def example_2():
    event_loop = asyncio.get_event_loop()
    coros = [make_coro(i) for i in [1, 2]]
    event_loop.run_until_complete(asyncio.wait(coros))
    event_loop.close()


example_2()
