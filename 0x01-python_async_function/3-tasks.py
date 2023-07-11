#!/usr/bin/env python3
"""runs an asynchronous task"""
import asyncio
import random
from typing import Any
wait_random = __import__('0-basic_async_syntax').wait_random


def task_wait_random(max_delay: int) -> Any:
    """takes an int and returns an asyncio.TAsk"""
    return asyncio.create_task(wait_random(max_delay))
