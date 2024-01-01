#!/usr/bin/env python3
"""asynchronous coroutine"""
import asyncio
from typing import List


wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """Create a liste to launch n time wait  random and return a
    newlist sorted"""
    tasks = []
    for _ in range(n):
        tasks.append(wait_random(max_delay))

    delays = await asyncio.gather(*tasks)

    return sorted(delays)
