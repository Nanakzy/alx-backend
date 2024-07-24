#!/usr/bin/env python3
""" MRU Caching module """

from collections import OrderedDict
from base_caching import BaseCaching


class MRUCache(BaseCaching):
    """ MRUCache defines a Most Recently Used (MRU) caching system """

    def __init__(self):
        """ Initialize MRUCache """
        super().__init__()
        self.cache_order = OrderedDict()

    def put(self, key, item):
        """ Add an item in the cache """
        if key is None or item is None:
            return

        if key in self.cache_data:
            self.cache_data[key] = item
            self.cache_order.move_to_end(key)
        else:
            if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
                self._evict()
            self.cache_data[key] = item
            self.cache_order[key] = item

    def get(self, key):
        """ Get an item by key """
        if key is None or key not in self.cache_data:
            return None

        self.cache_order.move_to_end(key)
        return self.cache_data[key]

    def _evict(self):
        """ Evict the most recently used item """
        key, _ = self.cache_order.popitem(last=True)
        del self.cache_data[key]
        print(f"DISCARD: {key}")

    def print_cache(self):
        """ Print the cache """
        print("Current cache:")
        for key in self.cache_data:
            print(f"{key}: {self.cache_data[key]}")
