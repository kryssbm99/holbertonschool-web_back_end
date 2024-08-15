#!/usr/bin/env python3
"""
Module for a function that returns a tuple
with a string and the square of an int/float.
"""

from typing import Union, Tuple


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """
    Returns a tuple with the string `k` and the square of `v` as a float.
    """
    return (k, float(v ** 2))
