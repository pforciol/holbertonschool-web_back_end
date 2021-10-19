#!/usr/bin/env python3
"""

This module contains a function.

"""

from asyncio import Task, create_task

wait_random = __import__('0-basic_async_syntax').wait_random


def task_wait_random(max_delay: int) -> Task:
    """

    Args:
        max_delay: The maximum random time generated.

    Returns:
        An asyncio.Task element.

    """

    return create_task(wait_random(max_delay))
