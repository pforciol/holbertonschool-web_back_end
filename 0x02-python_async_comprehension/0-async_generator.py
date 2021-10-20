#!/usr/bin/env python3
"""

This module contains an asynchronous coroutine.

"""
import asyncio
import random


async def async_generator() -> float:
    """

    Loop 10 times, each time asynchronously wait 1 second,
    and generates a random number between 0 and 10.

    Return: 10 random generated numbers.

    """
    for _ in range(10):
        await asyncio.sleep(1)
        yield random.uniform(0, 10)
