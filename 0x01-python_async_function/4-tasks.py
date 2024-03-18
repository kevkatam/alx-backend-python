#!/usr/bin/env python3
"""
module that executes multiple coroutines at the same time with async
"""
import asyncio
from typing import List
task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """ function that returns a list of all the delays """
    mylist: List[float] = []
    for _ in range(n):
        i = await task_wait_random(max_delay)
        mylist.append(i)
    mylist = sorted(mylist)
    return mylist
