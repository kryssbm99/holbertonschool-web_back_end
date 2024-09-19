#!/usr/bin/env python3
"""Simple function and class for pagination."""
from typing import Tuple, List
import csv
import math


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """
    Returns a tuple containing the start and end indexes
    based on the page number and page size.
    """
    start = (page - 1) * page_size  # Calculate start index
    end = page * page_size  # Calculate end index
    return (start, end)  # Return tuple (start, end)


class Server:
    """Server class to paginate a database of popular baby names."""
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        """Initialize the server with an empty dataset cache."""
        self.__dataset = None

    def dataset(self) -> List[List]:
        """
        Return the cached dataset or load it from the CSV file.
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]  # Skip header row

        return self.__dataset

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        """
        Retrieve a page of data from the dataset based on the page number
        and page size.
        """
        assert isinstance(page, int) and page > 0, \
            "Page must be a positive integer."
        assert isinstance(page_size, int) and page_size > 0, \
            "Page size must be a positive integer."

        start, end = index_range(page, page_size)  # Get index range

        dataset = self.dataset()  # Load dataset

        return dataset[start:end]  # Return the requested page
