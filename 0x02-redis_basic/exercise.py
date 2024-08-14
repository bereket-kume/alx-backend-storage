#!/usr/bin/env python3
"""
redis module
"""
import redis
import uuid
from typing import Union, Callable, Optional, Any


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
