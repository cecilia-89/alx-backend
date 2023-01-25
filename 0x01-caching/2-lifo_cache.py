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
        length = len(self.cache_data.keys()) + 1
        if length > BaseCaching.MAX_ITEMS:
            keylist = list(self.cache_data.keys())
            if key in keylist:
                del self.cache_data[key]
            else:
                value = keylist[-1]
                del self.cache_data[value]
                print("DISCARD: {}\n".format(value))
        self.cache_data[key] = item


    def get(self, key):
        """returns a value"""
        value = self.cache_data.get(key)
        return value

my_cache = LIFOCache()
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
my_cache.put("G", "San Francisco")
my_cache.print_cache()