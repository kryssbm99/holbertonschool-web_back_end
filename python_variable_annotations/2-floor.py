#!/usr/bin/env python3
"""
This module provides a type-annotated function to return the floor of a float.
"""
import math


def floor(n: float) -> int:
    """
    Returns the floor of a float.

    Parameters:
    n (float): The float number to floor.

    Returns:
    int: The floor of `n`.
    """
    return math.floor(n)
