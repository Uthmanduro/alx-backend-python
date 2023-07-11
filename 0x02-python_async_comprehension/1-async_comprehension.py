#!/usr/bin/env python3
"""async comperhensions"""
import asyncio
import random
async_generator = __import__('0-async_generator').async_generator


async def async_comprehension():
    return [values async for values in async_generator()]
