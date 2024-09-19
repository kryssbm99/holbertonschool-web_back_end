#!/usr/bin/env python3
"""Four parallel task execution - task 2"""
import asyncio
import time
from typing import List

task_1_async = __import__('1-async_comprehension').async_comprehension

async def measure_runtime() -> float:
    """Measures the total runtime of executing async_comprehension
    four times in parallel."""
    start_time = time.time()  # Record the start time
    tasks = [task_1_async() for _ in range(4)]  # Create a list of 4 tasks
    await asyncio.gather(*tasks)  # Run tasks concurrently
    end_time = time.time()  # Record the end time
    return end_time - start_time  # Calculate and return the total runtime
