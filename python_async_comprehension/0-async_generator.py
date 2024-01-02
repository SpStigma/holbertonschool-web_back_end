#!/usr/bin/env python3
"""Asynchronous generator that yields random numbers between 0 and 10
with a 1-second interval."""
import asyncio
import random
from typing import AsyncGenerator


async def async_generator() -> AsyncGenerator:
    """Yields random numbers asynchronously."""
    for _ in range(10):
        await asyncio.sleep(1)
        yield random.uniform(0, 10)
