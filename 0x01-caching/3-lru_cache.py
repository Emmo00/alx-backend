#!/usr/bin/env python3
"""
basic caching
"""
import math
from datetime import datetime
from base_caching import BaseCaching


class LRUCache(BaseCaching):
    """
    LIFO impl. caching
    """
    def __init__(self):
        """initialize
        """
        super().__init__()
        self.used = {}

    def put(self, key, item):
        """ Add an item in the cache
        """
        if key is None or item is None:
            return
        if len(self.cache_data) >= BaseCaching.MAX_ITEMS and key not in self.cache_data:
            lru = self.get_lru()
            print(f"DISCARD: {lru}")
            del self.cache_data[lru]
            del self.used[lru]
        self.cache_data[key] = item
        self.used[key] = datetime.now()

    def get(self, key):
        """ Get an item by key
        """
        if key is None:
            return None
        if key in self.cache_data:
            self.used[key] = datetime.now()
        return self.cache_data.get(key)
    
    def get_lru(self):
        """
        get LRU item on the cache"""
        min = list(self.used.values())[0]
        min_key = list(self.used.keys())[0]
        for key in self.used:
            if self.used[key] < min:
                min_key = key
        return min_key
