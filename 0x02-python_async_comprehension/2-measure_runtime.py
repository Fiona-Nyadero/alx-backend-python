#!/usr/bin/env python3
'''Module checks the runtime of parallel async comprehensn'''
import time
import asyncio


async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    '''Function returns the runtime of || comprehensions'''
    before = time.perf_counter()
    await asyncio.gather(async_comprehension(),
                         async_comprehension(),
                         async_comprehension(),
                         async_comprehension())
    after = time.perf_counter()
    return after - before
