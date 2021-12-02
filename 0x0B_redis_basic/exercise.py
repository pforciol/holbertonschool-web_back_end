#!/usr/bin/env python3
""" Exercise module. """
from typing import Callable, Optional, Union
from functools import wraps
import redis
import uuid


def count_calls(method: Callable) -> Callable:
    """ count_calls decorator. """
    @wraps(method)
    def count_calls_wrapper(self, *args, **kwargs) -> bytes:
        """ count_calls wrapper. """
        self._redis.incr(method.__qualname__)
        return method(self, *args, **kwargs)

    return count_calls_wrapper


def call_history(method: Callable) -> Callable:
    """ call_history decorator. """
    inputs = f"{method.__qualname__}:inputs"
    outputs = f"{method.__qualname__}:outputs"

    @wraps(method)
    def call_history_wrapper(self, *args, **kwargs) -> bytes:
        """ call_history wrapper. """
        self._redis.rpush(inputs, str(args))
        output = method(self, *args, **kwargs)
        self._redis.rpush(outputs, output)

        return output

    return call_history_wrapper


def replay(method: Callable):
    """ Replay the calls of a specific method """
    m_name = method.__qualname__
    inputs = f"{m_name}:inputs"
    outputs = f"{m_name}:outputs"
    r = redis.Redis()

    data = r.get(m_name).decode("utf-8")
    inputs_list = r.lrange(inputs, 0, -1)
    outputs_list = r.lrange(outputs, 0, -1)

    print(f"{m_name} was called {data} times:")

    for k, v in zip(inputs_list, outputs_list):
        print(f"{m_name}(*{k.decode('utf-8')}) -> {v.decode('utf-8')}")


class Cache():
    """ Cache class. """

    def __init__(self) -> None:
        self._redis = redis.Redis()
        self._redis.flushdb()

    @count_calls
    @call_history
    def store(self, data: Union[str, bytes, int, float]) -> str:
        """ Store the input data and return the random key. """
        key = str(uuid.uuid4())
        self._redis.set(key, data)

        return key

    def get(self, key: str, *fn: Optional[Callable]) -> Union[str, bytes, int, float]:
        """ Convert the data back to the desired format. """
        if fn:
            data = self._redis.get(key)
            return fn(data)

        return self._redis.get(key)

    def get_str(self, key: str) -> str:
        """ Converts the key to a str. """
        return self.get(key, str)

    def get_int(self, key: str) -> int:
        """ Converts the key to an int. """
        return self.get(key, int)
