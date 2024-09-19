#!/usr/bin/env python3
"""Async generator task 0"""
import asyncio
import random
from typing import Generator


async def async_generator() -> Generator[float, None, None]:
    """Asynchronous generator that waits for 1 second
    and yields a random float between 0 and 10."""
    for _ in range(10):
        await asyncio.sleep(1)  # Pause execution for 1 second
        yield random.uniform(0, 10)
