#!/usr/bin/env python3
"""
Module for a function that returns a multiplier function.
"""

from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """
    Returns a function that multiplies a float by the given multiplier.
    Parameters:
    multiplier (float): The multiplier value.
    Returns:
    Callable[[float], float]: A function that takes a float and returns a float
    """
    def multiply(n: float) -> float:
        return n * multiplier

    return multiply
