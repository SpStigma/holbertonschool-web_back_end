#!/usr/bin/env python3
"""asynchronous coroutine"""
import asyncio
from typing import List


task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """Create a liste to launch n time wait  random and return a
    newlist sorted"""
    list_delay = []
    for _ in range(n):
        list_delay.append(task_wait_random(max_delay))
    result = await asyncio.gather(*list_delay)
    return sorted(result)
