#!/usr/bin/env python3
"""

This module contains a type-annotated function.

"""

from typing import Union, List


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """

    Args:
        mxd_lst: The list of int and floats.

    Returns:
        The sum of all items contained in mxd_lst.

    """
    res: float = 0
    for i in mxd_lst:
        res += i

    return res
