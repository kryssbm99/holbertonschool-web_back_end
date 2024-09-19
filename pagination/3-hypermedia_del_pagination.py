#!/usr/bin/env python3
"""
Deletion-aware hypermedia pagination
"""

import csv
import math
from typing import List, Dict, Any


class Server:
    """Server class to paginate a database of popular baby names."""
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        """Initialize the server with empty dataset and indexed dataset."""
        self.__dataset = None
        self.__indexed_dataset = None

    def dataset(self) -> List[List]:
        """Return the cached dataset or load it from the CSV file."""
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]  # Skip the header row

        return self.__dataset

    def indexed_dataset(self) -> Dict[int, List]:
        """Return the dataset indexed by its position starting from 0."""
        if self.__indexed_dataset is None:
            dataset = self.dataset()
            truncated_dataset = dataset[:1000]  # Limit to first 1000 entries
            self.__indexed_dataset = {
                i: dataset[i] for i in range(len(truncated_dataset))
            }
        return self.__indexed_dataset

    def get_hyper_index(
        self, index: int = None, page_size: int = 10
    ) -> Dict[str, Any]:
        """
        Provide deletion-aware pagination metadata.
        Ensures that if rows are deleted, the next index is adjusted.
        """
        assert (
            isinstance(index, int) and 0 <= index < len(self.indexed_dataset())
        ), "Index out of range"

        indexed_data = self.indexed_dataset()
        data = []
        next_index = index

        while len(data) < page_size and next_index < len(indexed_data):
            if next_index in indexed_data:  # Skip any missing entries
                data.append(indexed_data[next_index])
            next_index += 1

        return {
            "index": index,  # Current index
            "next_index": next_index,  # Next index to paginate from
            "page_size": len(data),  # Size of the current page
            "data": data  # Data for the current page
        }
