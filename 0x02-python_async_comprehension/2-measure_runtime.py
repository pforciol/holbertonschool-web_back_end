#!/usr/bin/env python3
"""

This module contains an asynchronous coroutine.

"""

import asyncio
from time import time

async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime():
    """

    Return

    """
    start: float = time()
    await asyncio.gather(*[async_comprehension() for _ in range(4)])
    end: float = time()

    return (end - start)
