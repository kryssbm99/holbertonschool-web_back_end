#!/usr/bin/env python3
"""Async comprehension task 1"""
import asyncio
from typing import List

task_0_function = __import__('0-async_generator').async_generator


async def async_comprehension() -> List[float]:
    """Asynchronous function to collect and return
    10 random numbers from the async generator."""
    return [i async for i in task_0_function()]
