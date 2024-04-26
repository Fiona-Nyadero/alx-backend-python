#!/usr/bin/env python3
'''Module executes multiple coroutines'''
import asyncio
import random
from typing import List


wait_random = __import__("0-basic_async_syntax").wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    '''function returns a sorted list of all delays'''
    delaylist = []
    for _ in range(n):
        delaylist.append(asyncio.create_task(wait_random(max_delay)))
    return sorted(await asyncio.gather(*delaylist))
