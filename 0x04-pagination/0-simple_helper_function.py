#!/usr/bin/python3
""" index_range module """

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
