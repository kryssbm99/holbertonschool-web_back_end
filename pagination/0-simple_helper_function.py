#!/usr/bin/env python3
"""Simple function for pagination."""
from typing import Tuple


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """
    Returns a tuple containing the start and end indexes
    for the given page and page size.
    """
    start = (page - 1) * page_size  # Calculate the starting index
    end = page * page_size  # Calculate the ending index
    return (start, end)  # Return the start and end indexes
