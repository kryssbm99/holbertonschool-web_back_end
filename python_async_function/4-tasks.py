#!/usr/bin/env python3
"""Module to create a new async function
that spawns tasks using task_wait_random."""

import asyncio
from typing import List
import importlib.util

spec = importlib.util.spec_from_file_location(
    "task_wait_random", "./3-tasks.py"
)
module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)
task_wait_random = module.task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """Spawns task_wait_random n times and returns a sorted list of delays."""
    tasks = [task_wait_random(max_delay) for _ in range(n)]
    delays = await asyncio.gather(*tasks)
    return sorted(delays)
