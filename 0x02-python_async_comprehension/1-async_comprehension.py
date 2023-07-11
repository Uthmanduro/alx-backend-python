#!/usr/bin/env python3
"""async comperhensions"""
import asyncio
import random
from typing import Iterator
async_generator = __import__('0-async_generator').async_generator


async def async_comprehension() -> Iterator[float]:
    return [values async for values in async_generator()]
