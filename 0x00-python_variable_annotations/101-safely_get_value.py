#!/usr/bin/env python3
"""

This module contains a type-annotated function.

"""

from typing import Mapping, Any, Union, TypeVar

T = TypeVar("T")


def safely_get_value(dct: Mapping,
                     key: Any,
                     default: Union[T, None] = None) -> Union[Any, T]:
    """

    Args:
        dct: A dictionnary.
        key: The key to get the value of.
        default: The default return value if nothing is found.

    Returns:
        The value of the key or "default" if nothing is found.

    """

    if key in dct:
        return dct[key]
    else:
        return default
