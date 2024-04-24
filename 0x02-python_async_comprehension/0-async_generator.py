#!/usr/bin/env python3
'''Module generates random numbers'''
import asyncio
import random
from typing import Generator


async def async_generator() -> Generator[float, None, None]:
    '''Function yields a random float between 0-10'''
    delays = []
    for _ in range(10):
        await asyncio.sleep(1)
        yield random.uniform(0, 10)
