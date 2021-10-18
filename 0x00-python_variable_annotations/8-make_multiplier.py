#!/usr/bin/env python3
"""

This module contains a type-annotated function.

"""

from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """

    Args:
        multiplier: The multiplier to use.

    Returns:
        A function that multiplies the multiplier by a float.

    """

    return lambda x: multiplier * x
