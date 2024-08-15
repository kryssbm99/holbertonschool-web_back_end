#!/usr/bin/env python3
"""
Module for a function that returns a list of
tuples containing elements and their lengths.
"""

from typing import Iterable, Sequence, List, Tuple


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """
    Returns a list of tuples with each element and its length.

    Parameters:
    lst (Iterable[Sequence]): An iterable of sequences.

    Returns:
    List[Tuple[Sequence, int]]: A list of tuples
    containing the sequence and its length.
    """
    return [(i, len(i)) for i in lst]
