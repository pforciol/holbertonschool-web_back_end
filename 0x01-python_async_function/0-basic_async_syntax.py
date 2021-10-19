#!/usr/bin/env python3
"""

This module contains an asynchronous coroutine.

"""

import asyncio
import random


async def wait_random(max_delay: int = 10) -> float:
    """

    Args:
        max_delay: The maximum random time generated.

    Returns:
        The random generated value between 0 and max_delay.

    """
    rand: float = random.uniform(0, max_delay)
    await asyncio.sleep(rand)

    return rand
