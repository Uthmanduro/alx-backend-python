#!/usr/bin/env python3
"""executes multiole coroutine at the same time"""
import asyncio
import random
wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n, max_delay):
    """returns a list of all the delays"""
    return_list = []
    for i in range(n):
        result = wait_random(max_delay)
        return_list.append(result)
    new = asyncio.as_completed(return_list)
    return [await items for items in new]
