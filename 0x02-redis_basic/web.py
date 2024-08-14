#!/usr/bin/env python3
"""
Implementing an expiring web cache and tracker
"""
import requests
import redis
from typing import Callable


redis_client = redis.Redis()


def count_requests(method: Callable) -> Callable:
    """
    decorator to count how many times a url is accessed
    """
    def wrapper(url: str) -> str:
        redis_client.incr(f'count:{url}')
        cached_content = redis_client.get(f'cache:{url}')
        if cached_content:
            return cached_content.decode('utf-8')
        content = method(url)
        redis_client.setex(f'cache:{url}', 10, content)
        return content
    return wrapper


@count_requests
def get_page(url: str) -> str:
    """
    fetch the html content of a url and return it
    """
    response = requests.get(url)
    return response.text
