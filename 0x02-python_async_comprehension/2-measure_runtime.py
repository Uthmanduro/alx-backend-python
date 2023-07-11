#!/usr/bin/env python3
"""measures the runtime for four parallel comprehensions"""
import asyncio
import random
import time
async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """return the total runtime for the coroutime to run"""
    start = time.perf_counter()
    await asyncio.gather(*[async_comprehension() for _ in range(4)])
    end = time.perf_counter()
    return end - start
