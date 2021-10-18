#!/usr/bin/env python3
"""

This module contains a type-annotated function.

"""

from typing import Sequence, Any, Union


def safe_first_element(lst: Sequence[Any]) -> Union[Any, None]:
    """

    Args:
        lst: A sequence of elements.

    Returns:
        The first element or nothing if None.

    """

    if lst:
        return lst[0]
    else:
        return None
