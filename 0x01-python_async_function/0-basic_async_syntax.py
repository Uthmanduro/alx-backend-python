#!/usr/bin/env python3
"""a coroutine to show the basics of async"""
import asyncio
import random


async def wait_random(max_delay=10):
    """waits for a random delay and returns a random int btw 0 and max_dely"""
    time = random.uniform(0, max_delay)
    await asyncio.sleep(time)
    return time
