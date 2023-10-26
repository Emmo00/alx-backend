#!/usr/bin/env python3
"""
basic caching
"""
from base_caching import BaseCaching


class LIFOCache(BaseCaching):
    """
    LIFO impl. caching
    """
    def __init__(self):
        """initialize
        """
        super().__init__()
        self.last_in = None

    def put(self, key, item):
        """ Add an item in the cache
        """
        if key is None or item is None:
            return
        if len(self.cache_data) >= BaseCaching.MAX_ITEMS and key not in self.cache_data:
            print(f"DISCARD: {self.last_in}")
            del self.cache_data[self.last_in]
        self.cache_data[key] = item
        self.last_in = key

    def get(self, key):
        """ Get an item by key
        """
        if key is None:
            return None
        return self.cache_data.get(key)
