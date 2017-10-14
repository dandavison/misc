#!/usr/bin/env python3

import asyncio


async def make_coro(i):
    print('in make_coro %d' % i)


class C:
    async def make_coro(self, i):
        print('in make_coro method %d' % i)


def example_1():
    ioloop = asyncio.get_event_loop()
    ioloop.run_until_complete(C().make_coro(1))
    ioloop.close()



def example_2():
    ioloop = asyncio.get_event_loop()
    coros = [make_coro(i) for i in [1, 2]]
    ioloop.run_until_complete(asyncio.wait(coros))
    ioloop.close()


example_2()
