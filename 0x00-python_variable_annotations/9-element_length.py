#!/usr/bin/env python3
"""

This module contains a type-annotated function.

"""

from typing import Iterable, Sequence, Tuple, List


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """

    Args:
        lst: A list of elements.

    Returns:
        The elements length.
    """

    return [(i, len(i)) for i in lst]
