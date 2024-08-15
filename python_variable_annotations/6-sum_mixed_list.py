#!/usr/bin/env python3
"""
Module provides a T-A function to return the sum of a list of ints and floats.
"""

from typing import List, Union


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """
    Returns the sum of a list containing integers and floats.

    Parameters:
    mxd_lst (List[Union[int, float]]): A list of integers and floats.

    Returns:
    float: The sum of all numbers in `mxd_lst`.
    """
    return sum(mxd_lst)
