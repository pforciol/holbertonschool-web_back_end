#!/usr/bin/env python3
"""

This module contains a function.

"""

import time
from asyncio import run

wait_n = __import__('1-concurrent_coroutines').wait_n


def measure_time(n: int, max_delay: int) -> float:
    """

    Args:
        n: The number of times to generate a random value.
        max_delay: The maximum random time generated.

    Returns:
        The average time to make a generated values list.

    """

    start: float = time.time()
    run(wait_n(n, max_delay))
    end: float = time.time()

    return (end - start) / n
