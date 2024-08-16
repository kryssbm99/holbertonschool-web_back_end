#!/usr/bin/env python3
"""Module to create an asyncio.Task from the wait_random coroutine."""

import asyncio
import importlib.util

spec = importlib.util.spec_from_file_location(
    "wait_random", "./0-basic_async_syntax.py"
)
module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)
wait_random = module.wait_random


def task_wait_random(max_delay: int) -> asyncio.Task:
    """Returns an asyncio.Task that waits for a random delay."""
    return asyncio.create_task(wait_random(max_delay))
