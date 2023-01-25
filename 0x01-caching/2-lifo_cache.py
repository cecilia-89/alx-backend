#!/usr/bin/python3
"""Module: 1-FIFOCache"""

from base_caching import BaseCaching


class LIFOCache(BaseCaching):
    """basic caching system"""

    def __init__(self):
        """instantiates an object"""
        super().__init__()

    def put(self, key, item):
        """assigns item to the cache system"""
        if key is None or item is None:
            return
        self.cache_data[key] = item
        length = len(self.cache_data.keys())
        if length > BaseCaching.MAX_ITEMS:
            discard = list(self.cache_data.keys())[-1]
            del self.cache_data[discard]
            print("DISCARD: {}\n".format(discard))

    def get(self, key):
        """returns a value"""
        value = self.cache_data.get(key)
        return value
