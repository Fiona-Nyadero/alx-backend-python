#!/usr/bin/env python3
'''Module creates async comprehensions'''
import asyncio
from typing import List


async_generator = __import__('0-async_generator').async_generator


async def async_comprehension() -> List[float]:
    '''Function generate random numbers using an asnyc fx'''
    return [random async for random in async_generator()]
