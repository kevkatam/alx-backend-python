#!/usr/bin/env python3
"""
module that measures time of an asyncronous function
"""
import time
import asyncio
wait_n = __import__('1-concurrent_coroutines').wait_n


def measure_time(n: int, max_delay: int) -> float:
    """ function that measures total execution time for wait_n """
    s = time.perf_counter()
    asyncio.run(wait_n(n, max_delay))
    elapsed = time.perf_counter() -s
    return elapsed / n
