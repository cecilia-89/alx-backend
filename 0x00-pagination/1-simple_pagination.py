#!/usr/bin/env python3
"""Module: 0-simple_helper_func"""
from typing import Tuple, List
import csv
import math


def index_range(page: int, page_size: int) -> Tuple:
    """returns list paginator params"""
    end_index = page * page_size
    start_index = end_index - page_size

    return (start_index, end_index)


class Server:
    """Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        """instantiates an object"""
        self.__dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        """returns data set with appropriate page"""
        for item in [page, page_size]:
            assert isinstance(item, int) and item > 0
        self.dataset()
        index = index_range(page, page_size)
        return self.__dataset[index[0]: index[-1]]


server = Server()

try:
    should_err = server.get_page(-10, 2)
except AssertionError:
    print("AssertionError raised with negative values")

try:
    should_err = server.get_page(0, 0)
except AssertionError:
    print("AssertionError raised with 0")

try:
    should_err = server.get_page(2, 'Bob')
except AssertionError:
    print("AssertionError raised when page and/or page_size are not ints")

print(server.get_page(1, 3))
print(server.get_page(3, 2))
print(server.get_page(3000, 100))
