#!/usr/bin/env python3
'''Module for creating tasks'''
import asyncio
import random
from typing import List

task_wait_random = __import__("3-tasks").task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    '''A function like wait_n'''
    delaylist = []
    for _ in range(n):
        delaylist.append(task_wait_random(max_delay))
    return sorted(await asyncio.gather(*delaylist))
