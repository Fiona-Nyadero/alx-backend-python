#!/usr/bin/env python3
'''Module creates an async function'''
import asyncio
import random


async def wait_random(max_delay: int = 10) -> float:
    '''Function prints the delay time on an async fx'''
    delay_wait = random.uniform(0, max_delay)
    await asyncio.sleep(delay_wait)
    return delay_wait
