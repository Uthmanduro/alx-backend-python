#!/usr/bin/env python3
"""alters the function"""
import asyncio
import random
from typing import List
wait_n = __import__('1-concurrent_coroutines').wait_n


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """alters a new function and creates the task"""
    return await wait_n(n, max_delay)
