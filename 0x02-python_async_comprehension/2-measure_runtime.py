#!/usr/bin/env python3
"""
module that measures run time for execution of async_comprehension four times
"""
import time
import asyncio
async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """ function that measures runtime """
    s = time.perf_counter()
    run = [async_comprehension() for _ in range(4)]
    await asyncio.gather(*run)

    elapsed = time.perf_counter() - s
    return elapsed
