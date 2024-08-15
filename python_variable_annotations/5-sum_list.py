#!/usr/bin/env python3
"""
This module provides a T-A function to return the sum of a list of floats.
"""

from typing import List


def sum_list(input_list: List[float]) -> float:
    """
    Returns the sum of a list of floats.

    Parameters:
    input_list (List[float]): A list of float numbers.

    Returns:
    float: The sum of all numbers in `input_list`.
    """
    return sum(input_list)
