#!/usr/bin/env python3
"""
Module for an asynchronous routine that spawns multiple wait_random coroutines.
"""

import asyncio
from typing import List
import importlib.util

spec = importlib.util.spec_from_file_location(
    "wait_random", "./0-basic_async_syntax.py"
)
module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)
wait_random = module.wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """
    Spawns wait_random n times with the specified max_delay
    and returns a list of delays.

    Parameters:
    n (int): The number of times to spawn wait_random.
    max_delay (int): The maximum delay for each wait_random call.

    Returns:
    List[float]: A list of all the delays in ascending order.
    """
    delays = []
    for _ in range(n):
        delays.append(asyncio.create_task(wait_random(max_delay)))

    completed_delays = []
    for task in asyncio.as_completed(delays):
        completed_delays.append(await task)

    return completed_delays
