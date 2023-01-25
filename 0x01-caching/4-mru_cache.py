#!/usr/bin/python3
"""Module: 1-FIFOCache"""

from base_caching import BaseCaching


class MRUCache(BaseCaching):
    """basic caching system"""
    count = 0

    def __init__(self):
        """instantiates an object"""
        super().__init__()
        self.items = {}

    def put(self, key, item):
        """assigns item to the cache system"""
        if key is None or item is None:
            return
        MRUCache.count += 1
        self.items[key] = MRUCache.count
        self.cache_data[key] = item
        length = len(self.cache_data.keys())
        if length > BaseCaching.MAX_ITEMS:
            most = max(self.items.values())
            value = [k for k, v in self.items.items() if v == most]
            del self.cache_data[value[0]]
            del self.items[value[0]]
            print("DISCARD: {}".format(value[0]))

    def get(self, key):
        """returns a value"""
        if key in self.items.keys():
            MRUCache.count += 1
            self.items[key] = MRUCache.count
        value = self.cache_data.get(key)
        return value
