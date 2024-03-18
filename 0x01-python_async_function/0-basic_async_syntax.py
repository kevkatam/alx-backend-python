#!/usr/bin/env python3
"""
module containing an asynchronous coroutine that takes in an integer
argumentnamed wait_random that waits for a random delay between 0 and
max_delay seconds and eventually returns it.
"""
import asyncio
import time
import random


async def wait_random(max_delay: int = 10) -> float:
    """ corouting that awaits for a random delay btwn 0 and max_delay seconds
       and returns it
    """
    i: float = random.uniform(0, max_delay)
    await asyncio.sleep(i)

    return i
