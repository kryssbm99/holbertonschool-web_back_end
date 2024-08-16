#!/usr/bin/env python3
"""
Module to measure the runtime of the wait_n function.
"""

import time
import asyncio
from typing import Union
import importlib.util

spec = importlib.util.spec_from_file_location(
    "wait_n", "./1-concurrent_coroutines.py"
)
module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)
wait_n = module.wait_n


def measure_time(n: int, max_delay: int) -> float:
    """
    Measures the total execution time for wait_n(n, max_delay)
    and returns the average time per call.

    Parameters:
    n (int): The number of wait_n calls.
    max_delay (int): The maximum delay for each wait_n call.

    Returns:
    float: The average time per call.
    """
    start_time = time.perf_counter()
    asyncio.run(wait_n(n, max_delay))
    end_time = time.perf_counter()
    total_time = end_time - start_time
    return total_time / n
