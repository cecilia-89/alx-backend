#!/usr/bin/python3
"""Module: 1-FIFOCache"""

from base_caching import BaseCaching


class LRUCache(BaseCaching):
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
        LRUCache.count += 1
        self.items[key] = LRUCache.count
        self.cache_data[key] = item
        length = len(self.cache_data.keys())
        if length > BaseCaching.MAX_ITEMS:
            least = min(self.items.values())
            value = [k for k, v in self.items.items() if v == least]
            del self.cache_data[value[0]]
            del self.items[value[0]]
            print("DISCARD: {}".format(value[0]))

    def get(self, key):
        """returns a value"""
        if key in self.items.keys():
            LRUCache.count += 1
            self.items[key] = LRUCache.count
        value = self.cache_data.get(key)
        return value
