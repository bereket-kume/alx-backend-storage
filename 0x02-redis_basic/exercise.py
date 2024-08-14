#!/usr/bin/env python3
"""
redis module
"""
import redis
import uuid
from typing import Union


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
