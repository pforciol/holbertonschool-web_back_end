#!/usr/bin/env python3
"""

This module contains an asynchronous coroutine.

"""

from typing import List
from asyncio import gather

wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """

    Args:
        n: The number of times to generate a random value.
        max_delay: The maximum random time generated.

    Returns:
        The random generated values list.

    """

    return sorted(await gather(*[wait_random(max_delay) for i in range(n)]))
