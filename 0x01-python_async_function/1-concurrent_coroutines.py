#!/usr/bin/env python3
"""
module that executes multiple coroutines at the same time with async
"""
import asyncio
from typing import List
wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """ function that returns a list of all the delays """
    mylist: List[float] = []
    for _ in range(n):
        i = await wait_random(max_delay)
        mylist.append(i)
    mylist = sorted(mylist)
    return mylist
