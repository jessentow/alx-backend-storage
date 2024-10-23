#!/usr/bin/env python3

'''
This method that implements an
expiring web cache and tracker
'''

from typing import Callable
from functools import wraps
import redis
import requests


def requests_counter(method: Callable) -> Callable:
    """This  counts how many times a request has been made
    """
    r = redis.Redis()

    @wraps(method)
    def wrapper(url):
        """
        This wrapper fxn that counts
        actual no of requests made
        """
        r.incr(f"count:{url}")
        cached_ = r.get(f"cached:{url}")
        if cached:
            return cached.decode('utf-8')

        html = method(url)
        r.setex(f"cached:{url}", 10, html)
        return html

    return wrapper


@requests_counter
def get_page(url: str) -> str:
    """ This obtains html content for a given
    site url and returns it.
    """
    resp = requests.get(url)
    return resp.text
