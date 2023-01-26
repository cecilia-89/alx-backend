#!/usr/bin/env python3
"""Module: 0-simple_helper_func"""
from typing import Tuple


def index_range(page: int, page_size: int) -> Tuple:
    """returns list paginator params"""
    end_index = page * page_size
    start_index = end_index - page_size

    return (start_index, end_index)
