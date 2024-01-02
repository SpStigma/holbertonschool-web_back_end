#!/usr/bin/env python3
"""Async comprehension using an async generator."""
import asyncio
from typing import List


async_generator = __import__('0-async_generator').async_generator


async def async_comprehension() -> List[float]:
    """Return: A list of randomly generated floating-point numbers."""
    random_numbers = [_ async for _ in async_generator()]
    return random_numbers
