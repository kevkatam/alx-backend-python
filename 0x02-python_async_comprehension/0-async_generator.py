#!/usr/bin/env python3
"""
module containing a coroutine that takes no arguments and yields random nums
"""
import asyncio
from typing import Generator
import random


async def async_generator() -> Generator[float, None, None]:
    """ a coroutine that yielsd random numbers between 0 and 10 """
    for _ in range(10):
        await asyncio.sleep(1)
        yield random.uniform(0, 10)
