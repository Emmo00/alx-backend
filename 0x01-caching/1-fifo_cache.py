#!/usr/bin/env python3
"""
basic caching
"""
from base_caching import BaseCaching


class FIFOCache(BaseCaching):
    """
    FIFO impl. caching
    """
    def __init__(self):
        """
        initialize
        """
        super().__init__()
        self.queue = {}
        self.history_in = 0

    def put(self, key, item):
        """ Add an item in the cache
        """
        if key is None or item is None:
            return
        if len(self.cache_data) > BaseCaching.MAX_ITEMSi:
            del self.cache_data[self.first_in]
        self.cache_data[key] = item
        self.queue[self.history_index] = key
        self.history_index += 1

    def get(self, key):
        """ Get an item by key
        """
        if key is None:
            return None
        return self.cache_data.get(key)
