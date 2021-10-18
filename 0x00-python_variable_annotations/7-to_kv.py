#!/usr/bin/env python3
"""

This module contains a type-annotated function.

"""

from typing import Union, Tuple


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """

    Args:
        k: The key of the tuple.
        v: The value of the tuple.

    Returns:
        The tuple of both with squared value.

    """

    return (k, v ** 2)
