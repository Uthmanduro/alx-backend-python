#!/usr/bin/env python3
"""async comperhensions"""
import asyncio
from typing import List
async_generator = __import__('0-async_generator').async_generator


async def async_comprehension() -> List[float]:
    """returns 10 random numbers"""
    return [values async for values in async_generator()]
