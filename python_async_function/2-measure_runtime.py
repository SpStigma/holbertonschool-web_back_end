#!/usr/bin/env python3
"""asynchronous coroutine"""
import asyncio
import time

wait_random = __import__('0-basic_async_syntax').wait_random
wait_n = __import__('1-concurrent_coroutines').wait_n


def measure_time(n: int, max_delay: int) -> float:
    """Measure the average time it takes to execute n concurrent coroutines
    with a maximum delay."""

    async def async_measure():
        """Asynchronous coroutine to measure the time for concurrent
        coroutines."""
        start = time.time()
        await wait_n(n, max_delay)
        end = time.time()
        return (end - start) / n

    return asyncio.run(async_measure())
