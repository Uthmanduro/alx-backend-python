#!/usr/bin/env python3
"""async comperhensions"""
import asyncio
import random
from typing import List
async_generator = __import__('0-async_generator').async_generator


async def async_comprehension() -> Generator[float, None, None]:
    return [values async for values in async_generator()]
