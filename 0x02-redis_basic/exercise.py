#!/usr/bin/env python3
"""
redis module
"""
import redis
import uuid
from functools import wraps
from typing import Union, Callable, Optional, Any


def count_calls(method: Callable) -> Callable:
    """
    decorator that counts the number of times method is called
    """
    @wraps(method)
    def wrapper(self, *args, **kwargs):
        """
        increment the count for the method
        """
        key = method.__qualname__
        self._redis.incr(key)
        return method(self, *args, **kwargs)

    return wrapper


def call_history(method: Callable) -> Callable:
    """
    Decorator for cache class method to track args
    """
    @wraps(method)
    def wrapper(self: Any, *args) -> str:
        """
        tracks its passed argument by storing them in redis
        """
        self._redis.rpush(f'{method.__qualname__}:inputs', str(args))
        output = method(self, *args)
        self._redis.rpush(f'{method.__qualname__}:outputs', output)
        return output
    return wrapper


def replay(fn: Callable) -> None:
    """
    check how many times i was called
    """
    client = redis.Redis()
    calls = client.get(fn.__qualname__).decode('utf-8')
    inputs = [input.decode('utf-8') for input in
              client.lrange(f'{fn.__qualname__}:inputs', 0, -1)]
    outputs = [output.decode('utf-8') for output in
               client.lrange(f'{fn.__qualname__}:outputs', 0, -1)]
    print(f'{fn.__qualname__} was called {calls} times')
    for input, output in zip(inputs, outputs):
        print(f'{fn.__qualname__}(*{input}) -> {output}')


class Cache:
    """
    caching class
    """
    def __init__(self):
        """
        initalize new cache object
        """
        self._redis = redis.Redis()
        self._redis.flushdb()

    @call_history
    @count_calls
    def store(self, data: Union[str, bytes, int, float]) -> str:
        """
        stores data in redis with randomly generated key
        """
        key = str(uuid.uuid4())
        self._redis.set(key, data)
        return key

    def get(self, key: str, fn: Optional[Callable] = None) -> Any:
        """
        convert the result byte into correct data type
        """
        data = self._redis.get(key)
        if data is None:
            return None
        if fn is int:
            return self.get_int(data)
        if fn is str:
            return self.get_str(data)
        if callable(fn):
            return fn(data)
        return data

    def get_str(self, value: bytes) -> str:
        """
        convert bytes to string
        """
        return value.decode('utf-8')

    def get_int(self, value: bytes) -> int:
        """
        convert bytes to string
        """
        return int(value)
