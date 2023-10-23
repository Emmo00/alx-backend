#!/usr/bin/env python3
"""
Simple pagination
"""
import csv
import math
from typing import List, Tuple, Dict


def index_range(page: int, page_size: int) -> Tuple:
    """
    page index
    """
    return (page - 1) * page_size, page * page_size


class Server:
    """Server class to paginate a database of popular baby names.
    """
    DATA_FILE: str = "Popular_Baby_Names.csv"

    def __init__(self):
        """
        initialize class
        """
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
        """
        get page from page number and size
        """
        assert type(page) is int and type(page_size) is int
        assert page > 0 and page_size > 0
        start_index, end_index = index_range(page, page_size)
        return self.dataset()[start_index:end_index]

    def get_hyper(self, page: int = 1, page_size: int = 10) -> Dict:
        """
        get page with hypermedia information
        """
        dataset = self.dataset()
        data = self.get_page(page, page_size)
        next_page = None if page * page_size >= len(dataset) else page + 1
        prev_page = None if (page - 1) * page_size <= 0 else page - 1
        hyper = {"page_size": len(data),
                 "page": page,
                 "data": data,
                 "next_page": next_page,
                 "prev_page": prev_page,
                 "total_pages": math.ceil(len(dataset) / page_size)}
        return hyper
