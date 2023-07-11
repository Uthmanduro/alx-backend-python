#!/usr/bin/env python3
""" measures the runtime"""
import asyncio
import random
import time
wait_n = __import__('1-concurrent_coroutines').wait_n


def measure_time(n: int, max_delay: int) -> float:
    """measure the total runtine and returns total time / n"""
    start = time.perf_counter()
    asyncio.run(wait_n(n, max_delay))
    finish = time.perf_counter()
    total = finish - start
    return total / n
