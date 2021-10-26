#!/usr/bin/python3
""" simple_pagination module """

import csv
from typing import List
from typing import Tuple


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """

        Args:
            page: the number of the page
            page_size: the size of the page

        Returns:
            A tuple of size two containing a start index and an end index
            corresponding to the range of indexes to return in a list for those
            particular pagination parameters.

    """

    return (page_size * (page - 1), page_size * page)


class Server:
    """Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
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

            Args:
                page: the number of the page
                page_size: the size of the page

            Returns:
                The appropriate page of the dataset.

        """
        assert type(page) is int and type(
            page_size) is int and page > 0 and page_size > 0

        return self.dataset()[slice(*index_range(page, page_size))]
