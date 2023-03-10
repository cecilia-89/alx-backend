#!/usr/bin/env python3
"""Module: 0-simple_helper_func"""
from typing import Tuple, List, Dict
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

    def get_hyper(self, page: int = 1, page_size: int = 10) -> Dict:
        """returns a dictionary containing pages information"""
        prev, nxt = page - 1, page + 1

        page_data = self.get_page(page, page_size)
        total_pages = math.ceil(len(self.__dataset) / page_size)

        page_dict = {"page_size": len(page_data),
                     "page": page,
                     "data": page_data,
                     "next_page": nxt if nxt <= total_pages else None,
                     "prev_page": prev if prev > 0 else None,
                     "total_pages": total_pages}

        return page_dict
