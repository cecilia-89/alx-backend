#!/usr/bin/python3
"""Module: 1-FIFOCache"""

from base_caching import BaseCaching


class FIFOCache(BaseCaching):
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
            firstIn = list(self.cache_data.keys())[0]
            del self.cache_data[firstIn]
            print("DISCARD: {}".format(firstIn))

    def get(self, key):
        """returns a value"""
        value = self.cache_data.get(key)
        return value

my_cache = FIFOCache()
my_cache.put("A", "Hello")
my_cache.put("B", "World")
my_cache.put("C", "Holberton")
my_cache.put("D", "School")
my_cache.print_cache()
my_cache.put("E", "Battery")
my_cache.print_cache()
my_cache.put("C", "Street")
my_cache.print_cache()
my_cache.put("F", "Mission")
my_cache.print_cache()