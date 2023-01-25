#!/usr/bin/python3
"""Module: 0-basic_cache"""

from base_caching import BaseCaching


class BasicCache(BaseCaching):
    """basic caching system"""

    def __init__(self):
        """instantiates an object"""
        super().__init__()

    def put(self, key, item):
        """assigns item to the cache system"""
        if key is None or item is None:
            pass
        else:
            self.cache_data[key] = item

    def get(self, key):
        """returns a value"""
        value = self.cache_data.get(key)
        return value
