#!/usr/bin/env python3
"""

This module contains a type-annotated function.

"""

from typing import List


def sum_list(input_list: List[float]) -> float:
    """

    Args:
        input_list: The list of floats.

    Returns:
        The sum of all floats contained in input_list.

    """
    res: float = 0
    for i in input_list:
        res += i

    return res
